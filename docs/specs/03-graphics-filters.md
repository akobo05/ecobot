# EcoBot — Specs · 03 Gráficos, filtros y visión (Rol B)

Cubre `filters/`, `utils/pygame_cv_bridge.py`, `ui/histogram_panel.py`,
`core/camera.py`, `core/effects.py`. Es la parte más cercana a "computación gráfica
de verdad" y la que cubre las Unidades 1 y 2.

Depende de los contratos: §4 (filtros Surface↔ndarray) y §6 (homogéneas) de
`01-contracts.md`. Referencia de implementación: `ECOBOT_GDD.md` §5.2.

---

## `utils/pygame_cv_bridge.py`
El puente del contrato §4. **Primera tarea del Rol B (Semana 1), con test.**

- `pygame_to_numpy(surface, rect=None) -> ndarray` — recorta y devuelve **BGR**.
- `numpy_to_pygame(array) -> Surface`.
- **Cuidado:** PyGame usa RGB y ejes `(ancho, alto)`; OpenCV usa BGR y `(filas, cols)`.
  El bridge encapsula ambas conversiones.
- **Test:** ida y vuelta preserva la imagen (`tests/test_filters.py`).

## `filters/` — filtros OpenCV reales
Funciones **puras sobre ndarrays** (testeables), envueltas por `FilterEngine` con el
bridge. El efecto visual es el output matemático real, no decoración.

| Módulo | Función pura | Unidad | Mecánica en juego |
|--------|--------------|--------|-------------------|
| `sobel.py` | `sobel_edges(bgr, ksize)` | U1+U2 | `FILTER_EDGES`: revela contorno de celdas `HIDDEN` |
| `equalization.py` | `equalize_luminance(bgr)`, `histogram_rgb(bgr)` | U1 | `FILTER_EQ`: revela contaminantes en zonas oscuras |
| `threshold.py` | `otsu_threshold(bgr)`, `adaptive_threshold(...)` | U2 | `FILTER_THRESH`: separa zona segura/tóxica |

`FilterEngine` (en `filter_engine.py`) expone `apply_sobel/apply_equalization/apply_threshold`
con la firma del contrato §4. Pasos de cada filtro en GDD §5.2.

- **Tests:** `tests/test_filters.py` (p. ej. Sobel marca un borde vertical conocido).

## `ui/histogram_panel.py` — `HistogramPanel`
El gancho educativo: al ejecutar `FILTER_EQ`/`FILTER_EDGES` muestra el histograma RGB
(con `filters.equalization.histogram_rgb`), miniaturas antes/después y un tooltip que
explica el concepto. Pertenece al Rol B (depende del cálculo de histogramas), aunque
viva en `ui/`.

- `show(before, after, tooltip)`, `render(surface)`.

## `core/camera.py` — `Camera`
Transformación **mundo → pantalla** como **concatenación escala ∘ traslación**
(contrato §6, tema directo de la U4).

- `world_to_screen(col, row) -> (x, y)`, `view_matrix() -> ndarray 3×3`,
  `follow(col, row)` (centra suavemente en grillas grandes).

## `core/effects.py` — partículas y tinte de contaminación (capa opcional)
- `ParticleSystem(kind)` con `emit/update/render` (smog, agua contaminada).
- `apply_contamination_tint(surface, contamination)` — transformación de intensidad
  (U1): a más contaminación, mundo más oscuro/desaturado; al restaurar, más vibrante.
- **Es lo primero que se recorta** si el equipo va retrasado (`ECOBOT_PLAN_TRABAJO.md` §5).

---

## Orden de implementación sugerido
1. **S1:** `pygame_cv_bridge` con test + `sobel` aislado sobre una imagen de prueba.
2. **S2:** `Camera` (render mundo→pantalla con transformaciones); dejar `FilterEngine` invocable.
3. **S3:** los tres filtros integrados como efecto real + `HistogramPanel`.
4. **S4:** filtros revelando celdas `HIDDEN`; partículas y tinte (si hay tiempo).
