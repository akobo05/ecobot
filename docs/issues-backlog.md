# EcoBot — Backlog de trabajo (issues para el tablero Kanban)

Reparto del trabajo entre los **3 integrantes** por rol, según el cronograma de
[`../CONTRIBUTING.md`](../CONTRIBUTING.md). Cada ítem es una **issue** lista para el tablero.

## Roles (asignar nombres del equipo)

| Rol | Área | Perfil sugerido | Integrante |
|-----|------|-----------------------------|------------|
| **A** | Motor y lógica (`core/`, `main`, intérprete, colisiones, guardado) | El más fuerte en algoritmos | **Aaron (AD)** |
| **B** | Gráficos, filtros y visión (`filters/`, bridge, cámara, histograma, efectos) | El de matrices/OpenCV | **Walter (WP)** |
| **C** | Niveles, UI, contenido y docs (`ui/`, `data/levels/`, assets, informe) | El de diseño/redacción/orden | **Max (MS)** |

> Mapeo según afinidad demostrada en el proyecto de IHC. Detalle y justificación en
> [`division-trabajo.md`](division-trabajo.md). Ajustable el día 1 si el equipo prefiere otro reparto.

## Etiquetas del tablero
`rol-a` · `rol-b` · `rol-c` · `semana-1`…`semana-6` · `P0` (bloquea/contrato) ·
`P1` (núcleo jugable) · `P2` (pulido/opcional) · `spec` · `infra`

## Columnas Kanban sugeridas
`Backlog` → `Por hacer (semana actual)` → `En progreso` → `En revisión (PR)` → `Hecho`

---

## Semana 1 — Cimientos y contratos *(milestone: corre el menú y una grilla)*

- **#1 [infra] Subir repo a GitHub + protección de `main`** — `rol-c` `semana-1` `P0`.
  README, `.gitignore` y commit inicial ya están; falta el remoto y la regla de PR.
  *Listo:* `main` en GitHub, PRs obligatorios.
- **#2 [A] Esqueleto del game loop y máquina de estados** — `rol-a` `semana-1` `P0`.
  `Game.run()` con los 6 estados y transiciones vacías; corre sin crashear.
  *Listo:* abre ventana, muestra MENU y entra a LEVEL.
- **#3 [A] `Level.load` + render de la grilla** — `rol-a` `semana-1` `P1`.
  Carga `level_1.json` (contrato §1) y dibuja la grilla; `Robot` quieto.
- **#4 [B] Bridge `pygame_cv_bridge` (Surface↔ndarray) + test** — `rol-b` `semana-1` `P0`.
  Contrato §4. *Listo:* test ida-y-vuelta pasa.
- **#5 [B] `FilterEngine.apply_sobel` aislado** — `rol-b` `semana-1` `P1`.
  Sobel sobre una imagen de prueba (aún sin integrar al juego). *Listo:* test de borde.
- **#6 [C] Menú principal (esqueleto) + primer lote de assets/iconos** — `rol-c` `semana-1` `P1`.

---

## Semana 2 — Núcleo jugable *(milestone: vertical slice del Mundo 1)*

- **#7 [A] `Instruction` + `Interpreter.step` básico (MOVE/TURN/ACTION)** — `rol-a` `semana-2` `P0`.
- **#8 [A] Movimiento del robot con matrices homogéneas 3×3** — `rol-a` `semana-2` `P0`.
  Contrato §6 (traslación/rotación con NumPy). *Listo:* señalar las matrices en código.
- **#9 [A] `collision.py` + victoria/derrota (condiciones congeladas §3)** — `rol-a` `semana-2` `P0`.
- **#10 [B] `Camera`: mundo→pantalla (concatenación escala∘traslación)** — `rol-b` `semana-2` `P1`.
- **#11 [B] Dejar `FilterEngine` invocable dentro del juego** — `rol-b` `semana-2` `P2`.
- **#12 [C] Panel de instrucciones drag & drop + contador de slots + RESET** — `rol-c` `semana-2` `P0`.
  (Diseñar el modelo de datos del programa EN PAREJA con Rol A — contrato §2.)
- **#13 [C] Editor de niveles mínimo** — `rol-c` `semana-2` `P1`.
- **#14 [C] 5 niveles del Mundo 1 (JSON validados, con solución)** — `rol-c` `semana-2` `P1`.

---

## Semana 3 — Mundo 1 completo + filtros *(milestone: Mundo 1 100% + filtros)*

- **#15 [A] `REPEAT(n)` + funciones `F1`/`F2` en el intérprete** — `rol-a` `semana-3` `P1`.
- **#16 [A] Mecánica `JUMP` (spec + implementación)** — `rol-a` `semana-3` `P0` `spec`.
  Traslación x2 ignorando la celda intermedia; colisión de la celda destino.
- **#17 [A] Sistema de estrellas + `ACTION` por tipo de celda** — `rol-a` `semana-3` `P1`.
- **#18 [B] Integrar los 3 filtros como efecto real + conectar `FILTER_*`** — `rol-b` `semana-3` `P1`.
- **#19 [B] `HistogramPanel` (histograma RGB + tooltip educativo)** — `rol-b` `semana-3` `P1` `spec`.
- **#20 [C] Mapa de mundos + guardado `progress.json` + pantalla de victoria** — `rol-c` `semana-3` `P1`.
- **#21 [C] Niveles del Mundo 2 (JSON)** — `rol-c` `semana-3` `P1`.

---

## Semana 4 — Mundos 2 y 3 *(milestone: 3 mundos jugables)*

- **#22 [A] Casos límite de derrota + balanceo de `star_thresholds`** — `rol-a` `semana-4` `P1`.
- **#23 [B] Filtros revelan celdas `HIDDEN` + partículas + tinte por contaminación** — `rol-b` `semana-4` `P2` `spec`.
- **#24 [C] Niveles Mundo 2 y 3 + bosses + tiles por mundo + pulido UI** — `rol-c` `semana-4` `P1`.

---

## Semana 5 — Integración y pulido *(milestone: juego completo y estable)*

- **#25 [todos] Ronda de integración + bugfix + playtest de todos los niveles** — `semana-5` `P1`.
- **#26 [B] Audio (música por mundo + SFX) + cinemáticas + indicador "Planeta X%"** — `rol-b` `semana-5` `P2`.
- **#27 [C] Narrativa final de cada nivel + `README` + arrancar informe técnico** — `rol-c` `semana-5` `P1`.

---

## Semana 6 — Cierre *(milestone: entregable + presentación)*

- **#28 [todos] QA final + code freeze a mitad de semana** — `semana-6` `P0`.
- **#29 [C] Informe técnico + diapositivas + guion de la demo** — `rol-c` `semana-6` `P0`.
- **#30 [A/B] Demo en vivo + ensayo + "save de demo" como plan B** — `semana-6` `P0`.

---

## Capa opcional (se recorta primero si vamos retrasados — ver `../CONTRIBUTING.md`)
Partículas → cinemáticas → audio → funciones avanzadas del editor → reducir a 3 niveles/mundo → último recurso: 2 mundos.
