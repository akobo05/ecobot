# EcoBot — Specs · 04 Niveles, interfaz y contenido (Rol C)

Cubre `ui/` (salvo `histogram_panel.py`), `data/levels/`, `utils/level_editor.py`,
`assets/`, el `README` y el informe técnico. El jugador interactúa directamente con
lo que hace este rol.

Depende de los contratos: §1 (nivel), §2 (instrucciones), §5 (guardado) de
`01-contracts.md`.

---

## `ui/panel.py` — `InstructionPanel`  *(la UI más difícil)*
Drag & drop de tarjetas hacia una secuencia de slots, incluido el bloque `REPETIR`
(con su cuerpo) y `F1`/`F2`. **Se diseña en pareja con el Rol A** porque produce la
estructura que consume el `Interpreter` (contrato §2).

- `InstructionPanel(available, max_slots)`.
- `handle_event(event)`, `slots_used() -> int`, `reset()`,
  `build_program() -> (main, functions)`, `render(surface)`.
- Respeta `available_instructions` y `max_slots` del nivel (contrato §1).
- La regla de conteo de slots de `REPEAT` es la decisión (a) del contrato §2.

## `ui/hud.py` — `HUD`
Slots usados/disponibles, tareas pendientes, nombre del nivel, botones EJECUTAR/RESET
y barra "ecosistema restaurado". `render(surface, level, panel)`.

## `ui/map_screen.py` — `MapScreen`
Mapa de los 3 mundos con niveles bloqueados/desbloqueados y estrellas (lee
`progress.json`, contrato §5) y barra global "Planeta X% restaurado".
`handle_event(event) -> "1-2"|None`, `render(surface)`.

## `ui/menu.py` — `Menu`
Menú principal: título, jugar, opciones, salir.
`handle_event(event) -> "PLAY"|"QUIT"|None`, `render(surface)`.

## `utils/level_editor.py` — `LevelEditor`  *(herramienta dev, no parte del juego)*
Carga un JSON, permite cambiar celdas por clic, colocar robot y meta, y guardar al
esquema canónico (contrato §1). Versión mínima en Semana 2; funciones avanzadas son
capa opcional.

## `data/levels/` — los 16 niveles
13 niveles + 3 bosses repartidos en 3 mundos. Cada uno cumple `level_schema.json`.
**Requisitos de diseño de cada nivel:**
- Solucionable con las `available_instructions` y dentro de `max_slots`.
- Progresivo: cada nivel introduce una idea nueva.
- `star_thresholds` justos: 3★ ≈ solución óptima, 2★ ≈ buena, 1★ ≈ completarlo.
- `intro_text` con un dato ambiental real (la narrativa no es decorativa).

Estructura de mundos: Mundo 1 Bosque (6×6, instrucciones básicas), Mundo 2 Océano
(7×7, +`JUMP`/`REPEAT`/`F1`/`FILTER_EDGES`), Mundo 3 Ciudad (8×8, +`F2`/`FILTER_EQ`/`FILTER_THRESH`).

## `assets/`
Sprites (32×32), tiles por mundo, iconos de instrucciones, fondos, audio, fuentes.
Libres de itch.io / OpenGameArt o generados (el inventario concreto lo define el Rol C).

---

## Orden de implementación sugerido
1. **S1:** repo + `README` + `.gitignore`; esqueleto de `Menu`; primeros assets/iconos.
2. **S2:** `InstructionPanel` drag&drop + contador de slots + RESET; editor mínimo; 5 niveles del Mundo 1.
3. **S3:** `MapScreen` + conexión con guardado; pantalla de victoria; niveles del Mundo 2.
4. **S4:** niveles de Mundos 2 y 3 + bosses + tiles; pulido de UI.
5. **S5–S6:** narrativa final, `README`, informe técnico y diapositivas.
