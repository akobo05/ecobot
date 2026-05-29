# EcoBot — Specs · 01 Contratos congelados

> Estos son los puntos donde el trabajo de un rol **depende** del de otro. Se
> congelan en la Semana 1. **Cambiar un contrato después obliga a avisar a todo el
> equipo** y actualizar este documento. Derivado de `ECOBOT_PLAN_TRABAJO.md` §3.

Índice: [§1 Nivel JSON](#1-esquema-canónico-de-nivel) ·
[§2 Instrucciones](#2-instrucciones-y-semántica-de-repeat--función) ·
[§3 Estados](#3-estados-del-juego) ·
[§4 Filtros](#4-contrato-de-filtros-surface--ndarray) ·
[§5 Guardado](#5-formato-de-guardado) ·
[§6 Coordenadas homogéneas](#6-coordenadas-homogéneas)

---

## 1. Esquema canónico de nivel

Formato definitivo (validado por `data/levels/level_schema.json`). Tokens en ASCII;
los emojis quedan solo para la UI, nunca en los datos.

```json
{
  "world": 1,
  "level": 1,
  "name": "Primer Árbol",
  "intro_text": "Texto narrativo con un dato ambiental real.",
  "grid_size": [6, 6],
  "max_slots": 6,
  "star_thresholds": [6, 4, 3],
  "robot_start": { "col": 0, "row": 5, "direction": "RIGHT" },
  "available_instructions": ["MOVE", "TURN_L", "TURN_R", "ACTION"],
  "grid": [ ["GROUND", "..."], "..." ],
  "tasks": [{ "type": "PLANT", "col": 2, "row": 5 }]
}
```

**Reglas:**
- `grid_size` es `[columnas, filas]`. `grid` se indexa como `grid[row][col]`.
- La posición del robot está **solo** en `robot_start`, nunca como token dentro de `grid`.
- `star_thresholds` es `[slots para 1★, para 2★, para 3★]` (descendente).
- Tokens de celda válidos: `GROUND` (transitable), `DIRTY` (contaminada, **intransitable**: peligro, pisarla = derrota), `WALL` (inaccesible), `GOAL` (meta), `DEAD_TREE` (tarea `PLANT`), `TRASH` (tarea `COLLECT`), `SPILL` (tarea `NEUTRALIZE`), `HIDDEN` (oculta hasta aplicar un filtro). Las celdas-tarea son transitables; ver §3.
- Direcciones válidas: `UP`, `DOWN`, `LEFT`, `RIGHT`.
- Tipos de tarea: `PLANT`, `COLLECT`, `NEUTRALIZE`.

---

## 2. Instrucciones y semántica de REPEAT / función

Tokens de instrucción (contrato entre `interpreter.py`, `ui/panel.py` y `filters/`):

`MOVE`, `TURN_L`, `TURN_R`, `ACTION`, `JUMP`, `REPEAT`, `CALL_F1`, `CALL_F2`,
`FILTER_EDGES`, `FILTER_EQ`, `FILTER_THRESH`.

El programa del jugador es una **lista**. `REPEAT` no es un token plano: es un objeto
con su propio cuerpo. Las funciones se definen aparte:

```json
{
  "main": [
    { "op": "MOVE" },
    { "op": "REPEAT", "n": 3, "body": [ { "op": "MOVE" }, { "op": "ACTION" } ] },
    { "op": "CALL_F1" }
  ],
  "functions": {
    "F1": [ { "op": "TURN_R" }, { "op": "MOVE" } ],
    "F2": []
  }
}
```

- `Interpreter._expand()` aplana esta estructura: `REPEAT` se repite `n` veces y
  `CALL_F1`/`CALL_F2` se sustituyen por el cuerpo de la función.
- `ACTION` sobre una celda sin tarea es un **no-op**: no hace fallar el nivel, pero
  gasta un slot.

**Decisiones congeladas (Semana 1, 2026-05-29):**
- [x] **(a)** Un bloque `REPEAT` cuesta **1 slot por el token `REPEAT` + 1 slot por
  cada instrucción de su `body`**, **independiente de `n`**. Ejemplo: `REPEAT(5){MOVE,
  ACTION}` = 1 + 2 = **3 slots**. Esto premia comprimir secuencias largas en bucles
  (más estrellas con menos slots).
- [x] **(b)** **No** se permite `REPEAT` anidado dentro de otro `REPEAT` (un solo
  nivel de anidamiento). Una función no contiene bloques.
- [x] **(c)** Condiciones de derrota: ver §3 de esta spec y `collision.py`.

---

## 3. Estados del juego

`core/game.py` maneja una máquina de estados con estos valores fijos (definidos en
`settings.py`):

`MENU`, `MAP`, `LEVEL`, `FILTER_EFFECT`, `VICTORY`, `FAILURE`.

Cualquier pantalla nueva se agrega aquí y se avisa al equipo.

**Celdas-tarea vs celdas-peligro (modelo congelado):**
- `DEAD_TREE` (PLANT), `TRASH` (COLLECT) y `SPILL` (NEUTRALIZE) son **transitables**:
  el robot se para encima y `ACTION` completa la tarea. **Pisarlas NO es derrota.**
- `WALL` y `DIRTY` son **intransitables (peligro)**: pisarlas = derrota inmediata.
  `DIRTY` no tiene mecánica de limpieza (es un peligro a esquivar, como `WALL` pero
  temático). Si más adelante se quiere "limpiar suelo", sería un cambio de contrato
  (nuevo tipo de tarea), no la regla actual.

**Condiciones de derrota (decisión (c), congelada 2026-05-29):** se dispara `FAILURE`
si ocurre **cualquiera**:
1. Moverse fuera de la grilla: coordenadas fuera de `[0, cols-1] × [0, rows-1]`.
2. Pisar una celda `WALL`.
3. Pisar una celda `DIRTY`.
4. Agotar la cola de instrucciones (queue vacía) con tareas pendientes
   (`tasks_remaining() > 0`).

**`ACTION`:** sobre una celda-tarea completa su tarea; sobre cualquier otra celda es un
no-op (no falla, pero gasta el slot).

**Condición de victoria:** todas las tareas completas **y** el robot en una celda `GOAL`.

---

## 4. Contrato de filtros (Surface ↔ ndarray)

- `utils/pygame_cv_bridge.py` expone dos funciones:
  - `pygame_to_numpy(surface, rect) -> ndarray` (formato **BGR** de OpenCV),
  - `numpy_to_pygame(array) -> pygame.Surface`.
- `filters.filter_engine.FilterEngine` recibe siempre una `pygame.Surface` y un
  `pygame.Rect`, y devuelve una `pygame.Surface` con el filtro aplicado:
  - `apply_sobel(surface, rect) -> Surface`
  - `apply_equalization(surface, rect) -> Surface`
  - `apply_threshold(surface, rect) -> Surface`
- El **Rol A** entrega al **Rol B** la superficie del nivel ya renderizada; el Rol B
  no necesita saber cómo se dibujó la grilla.

---

## 5. Formato de guardado

`data/save/progress.json` (lo escribe `Game`, Rol A; lo lee `MapScreen`, Rol C):

```json
{
  "levels": {
    "1-1": { "completed": true, "stars": 3, "best_slots": 3 },
    "1-2": { "completed": true, "stars": 2, "best_slots": 8 }
  },
  "unlocked": ["1-1", "1-2", "1-3"]
}
```

No se versiona (está en `.gitignore`).

---

## 6. Coordenadas homogéneas

**El gancho más fuerte con la Unidad 4.** El movimiento del robot **no se hace
sumando enteros**: se hace con matrices 3×3 y coordenadas homogéneas (NumPy). Se debe
poder señalar en la sustentación. Implementación en `core/robot.py` y `core/camera.py`.

- Un punto de la grilla es el vector columna `[col, row, 1]ᵀ`.
- `MOVE` multiplica por la matriz de traslación
  `T(dc, dr) = [[1,0,dc],[0,1,dr],[0,0,1]]`, donde `(dc, dr)` es el vector de la
  dirección actual: `RIGHT=(1,0)`, `LEFT=(-1,0)`, `UP=(0,-1)`, `DOWN=(0,1)`
  (row crece hacia abajo).
- `TURN_L` / `TURN_R` rotan el vector de dirección 90° con una matriz de rotación.
- **Mundo → pantalla:** se concatena una matriz de escala (tamaño del tile) con una
  de traslación (desplazamiento de la cámara). Esa concatenación es, literalmente, el
  tema "concatenación de transformaciones" del sílabo (`core/camera.py`).
