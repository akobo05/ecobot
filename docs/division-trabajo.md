# División de trabajo — EcoBot

**Curso:** CC431 — Computación Gráfica · UNI · 2026-I
**Proyecto:** EcoBot — juego de pensamiento computacional (PyGame + OpenCV)
**Equipo:** Aaron Dávila Santos (AD) · Max Serrano Aróstegui (MS) · Walter Poma Navarro (WP)
**Repositorio:** https://github.com/akobo05/ecobot · **Tablero:** GitHub Project "EcoBot"
**Ventana:** 6 semanas (ver cronograma en [`../CONTRIBUTING.md`](../CONTRIBUTING.md))

> Mismo equipo y misma metodología que el proyecto de IHC (Gem de specs + Gem de
> review, specs por feature, ramas + PR revisado, code-review por PR).

---

## Mapeo persona ↔ rol

Se mantiene la afinidad demostrada en el proyecto de IHC.

| Persona | Rol en EcoBot | Por qué él (continuidad con IHC) |
|---------|---------------|----------------------------------|
| **Aaron (AD)** | **Rol A — Motor y lógica** | Lideró el repositorio y el backend/LLM en IHC; aquí toma el núcleo algorítmico (intérprete, colisiones, movimiento). |
| **Walter (WP)** | **Rol B — Gráficos, filtros y visión** | En IHC hizo el pipeline multimodal (STT/TTS/MediaPipe) y el análisis técnico; aquí la parte de OpenCV, matrices y cámara es su continuación natural. |
| **Max (MS)** | **Rol C — UI, niveles y contenido** | Diseñó el prototipo en Figma y la sala virtual en IHC; aquí lleva el panel drag&drop, menús, diseño de los 16 niveles y los assets. |

---

## Bloqueante previo — ya resuelto

A diferencia de IHC-F1, en EcoBot estos puntos **ya están cerrados** (no bloquean):

1. **Stack decidido:** Python 3.11 + PyGame + NumPy + OpenCV (en `requirements.txt`).
2. **Contratos entre módulos:** congelados en [`specs/01-contracts.md`](specs/01-contracts.md)
   (esquema de nivel, instrucciones, estados, bridge Surface↔ndarray, guardado,
   coordenadas homogéneas). **Cambiarlos obliga a avisar al equipo.**

Falta solo: cada integrante deja su **entorno listo** (`pip install -r requirements.txt`,
`python main.py` corre) y se confirma el mapeo persona↔rol de arriba.

---

## Tarea 0 — Cierre de cimientos (los tres, primeros días)

| Resp. | Tarea | Issue |
|-------|-------|-------|
| MS | Repo en GitHub + regla de PR (hecho: repo y tablero ya creados) | #1 |
| AD | Esqueleto del game loop y máquina de estados | #2 |
| WP | Bridge `pygame_cv_bridge` (Surface↔ndarray) + test | #4 |

---

## División por persona

### Aaron (AD) — Rol A · Motor y lógica
**Es dueño de:** `main.py`, `settings.py`, `core/` (game, level, robot, instruction, interpreter, collision), `data/save/`.

**Tareas (issues):**
1. Esqueleto del game loop y máquina de estados (#2).
2. `Level.load` + render de la grilla (#3).
3. `Interpreter.step` básico — MOVE/TURN/ACTION (#7).
4. Movimiento del robot con **matrices homogéneas 3×3** (#8).
5. `collision.py` + victoria/derrota (condiciones congeladas §3) (#9).
6. `REPEAT(n)` + funciones `F1`/`F2` (#15) y mecánica **JUMP** (#16).
7. Estrellas + `ACTION` por tipo de celda (#17); casos límite + balanceo (#22).

**Cubre del sílabo:** U4 (coordenadas, transformaciones afines, colliders, mecánicas).

### Walter (WP) — Rol B · Gráficos, filtros y visión
**Es dueño de:** `filters/`, `utils/pygame_cv_bridge.py`, `ui/histogram_panel.py`, `core/camera.py`, `core/effects.py`.

**Tareas (issues):**
1. Bridge `pygame_cv_bridge` + test (#4).
2. `FilterEngine.apply_sobel` aislado (#5).
3. `Camera`: mundo→pantalla (concatenación) (#10); dejar `FilterEngine` invocable (#11).
4. Integrar los 3 filtros reales + conectar `FILTER_*` (#18).
5. `HistogramPanel` (histograma RGB + tooltip) (#19).
6. Filtros revelan celdas `HIDDEN` + partículas + tinte (#23).
7. Audio + cinemáticas + indicador "Planeta X%" (#26).

**Cubre del sílabo:** U1 (color, histograma, ecualización, filtros), U2 (bordes, umbral), U4 (cámara).

### Max (MS) — Rol C · UI, niveles y contenido
**Es dueño de:** `ui/` (panel, hud, map_screen, menu), `data/levels/`, `utils/level_editor.py`, `assets/`, `README` e informe.

**Tareas (issues):**
1. Repo + regla de PR (#1); menú principal + primeros assets/iconos (#6).
2. Panel **drag & drop** + slots + RESET (#12) — en pareja con AD (contrato §2).
3. Editor de niveles mínimo (#13); 5 niveles del Mundo 1 (#14).
4. Mapa de mundos + guardado + pantalla de victoria (#20); niveles Mundo 2 (#21).
5. Niveles Mundo 3 + bosses + tiles + pulido UI (#24).
6. Narrativa de cada nivel + `README` + arrancar informe (#27).
7. Informe técnico + diapositivas + guion de la demo (#29).

**Cubre del sílabo:** U4 (mecánicas de juego, diseño 2D), soporte a U1/U2 vía los niveles.

---

## Integración (los tres)

- Cada quien en su rama (`motor`, `graficos`, `contenido`); **un PR por entregable**,
  revisado por otro integrante (igual que en IHC). Usar la **Reviewer-Gem** antes del PR.
- Punto de integración al final de cada semana: se mergea a `main` y se juega entre los tres.
- Tareas compartidas: integración + playtest (#25), QA + code freeze (#28), demo + ensayo (#30).

---

## Pendiente de confirmar

- Mapeo persona↔rol final (si alguien prefiere otro rol, ajustarlo aquí el día 1).
- Agregar a MS y WP como **colaboradores** del repo en GitHub para poder asignarles issues
  (hoy solo está la cuenta `akobo05`); mientras tanto, las issues se filtran por etiqueta
  `rol-a` / `rol-b` / `rol-c`.
