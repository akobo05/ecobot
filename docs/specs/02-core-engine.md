# EcoBot — Specs · 02 Motor y lógica del juego (Rol A)

Cubre `main.py`, `settings.py` y `core/` (salvo `camera.py` y `effects.py`, que son
del Rol B). Es la parte más exigente en lógica.

Depende de los contratos: §1 (nivel), §2 (instrucciones), §3 (estados), §5 (guardado),
§6 (homogéneas) de `01-contracts.md`.

---

## `settings.py`
Constantes globales (FPS, tamaños, colores, rutas, direcciones, nombres de estados).
Fuente única de configuración. No tiene lógica.

## `main.py`
Inicializa PyGame, crea la ventana y delega en `Game.run()`. Mínimo.

## `core/game.py` — `Game`
Máquina de estados y game loop.

- **Estado:** `screen`, `clock`, `running`, `state`, `progress`.
- **Interfaz pública:** `run()`, `handle_events(events)`, `update(dt)`, `render()`,
  `change_state(new_state)`, `load_progress() -> dict`, `save_progress()`.
- **Invariantes:** `state` siempre es uno de los 6 valores del contrato §3.
  `main` no crashea ante un nivel mal formado: se valida al cargar.
- **Depende de:** todos los módulos de `core/`, `ui/`, `filters/`.

## `core/level.py` — `Level`
Carga/valida/renderiza un nivel.

- **Interfaz:** `Level.load(path)`, `validate()`, `cell_at(col,row)`,
  `is_walkable(col,row)`, `tasks_remaining()`, `render(surface, camera)`.
- **Invariante:** tras `validate()`, la grilla cumple el contrato §1 (tokens y
  tamaños correctos, `robot_start` dentro de límites).
- Entrega al Rol B la superficie del nivel ya renderizada (contrato §4).

## `core/robot.py` — `Robot`
EcoBot: posición `(col,row)`, `direction`, animación.

- **Transformaciones (Unidad 4, contrato §6):** `translation_matrix(dc,dr)`,
  `rotation_matrix(deg)`, `position_vector()` — todas con NumPy 3×3.
- **Acciones (las llama el `Interpreter`):** `move_forward()`, `turn_left()`,
  `turn_right()`, `jump()`, `update(dt)`, `render(surface, camera)`.
- **Invariante crítico:** el movimiento se computa multiplicando matrices, no sumando
  enteros. Esto es revisable en la sustentación.

## `core/instruction.py` — `Instruction`
Modela (no ejecuta) el programa del jugador.

- `Instruction(op, n=1, body=[])`; helpers `is_block()`, `slot_cost()`.
- `parse_program(data) -> (main, functions)` según contrato §2.
- La regla de `slot_cost()` para `REPEAT` es la decisión (a) del contrato §2.

## `core/interpreter.py` — `Interpreter`
Aplana y ejecuta el programa. **Lógica pura más importante** (se testea sin ventana).

- `Interpreter(main, functions)` → construye `queue` con `_expand()`.
- **Interfaz:** `step() -> Instruction|None`, `is_finished()`, `reset()`.
- **`_expand()`** repite `REPEAT` `n` veces y sustituye `CALL_Fx` por su cuerpo, sin
  anidar `REPEAT` (decisión (b), contrato §2).
- **Tests:** `tests/test_interpreter.py`.

## `core/collision.py`
Lógica pura de validez de movimiento y fin de partida.

- `can_move(level, robot, dcol, drow) -> bool`
- `is_victory(level, robot) -> bool` (tareas completas + en `GOAL`)
- `is_failure(level, robot, instructions_left) -> bool` (condiciones del contrato §3)
- **Tests:** `tests/test_collision.py`.

## Sistema de estrellas
`Game` calcula estrellas comparando `slots_usados` contra `star_thresholds` del nivel
(contrato §1) al ganar, y lo persiste en `progress.json` (contrato §5).

---

## Orden de implementación sugerido (alineado al cronograma)
1. **S1:** `settings.py`, esqueleto de `Game` (loop + estados), `Level.load`+`render`, `Robot` dibujado quieto.
2. **S2:** `Instruction`, `Interpreter.step` con instrucciones básicas, movimiento homogéneo del robot, `collision.py`, victoria/derrota.
3. **S3:** `_expand` con `REPEAT` y funciones, `JUMP`, sistema de estrellas, `ACTION` por tipo de celda.
4. **S4:** casos límite de derrota y balanceo de `star_thresholds`.
