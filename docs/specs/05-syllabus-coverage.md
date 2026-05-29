# EcoBot — Specs · 05 Cobertura del sílabo

Mapa **tema del sílabo CC431 → dónde se implementa en EcoBot → cómo señalarlo en la
sustentación**. La única regla del proyecto es usar temas del curso (uno o varios);
EcoBot cubre el núcleo de la **Unidad 4** y partes de las **Unidades 1 y 2**.

> Honestidad académica: marcamos qué temas **sí** cubrimos, cuáles **parcialmente** y
> cuáles **no** (la Unidad 3 — Deep Learning — queda fuera del alcance; no es necesaria
> para aprobar, pero conviene poder decir por qué se dejó fuera).

---

## Unidad 4 — Videojuegos y componentes 3D  *(núcleo del proyecto)*

| Tema del sílabo | ¿Cubierto? | Dónde | Qué mostrar en la sustentación |
|---|---|---|---|
| Introducción a PyGame | ✅ | todo el motor | el juego corriendo |
| Manejo de recursos y cámara | ✅ | `core/camera.py`, `assets/` | cámara siguiendo a EcoBot en una grilla grande |
| Control y movimiento del personaje | ✅ | `core/robot.py` | EcoBot ejecutando una secuencia |
| Colliders y condición de victoria/derrota | ✅ | `core/collision.py` | un choque (derrota) y una victoria |
| Mecánicas de videojuegos | ✅ | intérprete, slots, estrellas | resolver un nivel con bucle = 3★ |
| Sistemas de coordenadas | ✅ | grilla→pantalla en `camera.py` | el vector `[col,row,1]ᵀ` |
| Transformaciones afines | ✅ | `robot.py` (traslación/rotación) | la matriz `T(dc,dr)` de `MOVE` |
| Coordenadas homogéneas | ✅ | `robot.py`, contrato §6 | que el movimiento es producto de matrices 3×3, no suma de enteros |
| Concatenación de transformaciones | ✅ | `camera.py` (escala ∘ traslación) | `view_matrix()` como concatenación |
| Implementación de transformaciones | ✅ | NumPy en `robot.py`/`camera.py` | el código de las matrices |
| Diseño y desarrollo de videojuegos 2D | ✅ | todo el proyecto | — |
| OpenGL / shaders / GLSL | ❌ | — | EcoBot es 2D en PyGame; no usa OpenGL |
| Proyecciones / cámara virtual 3D | ❌ | — | fuera de alcance (juego 2D) |
| Representación poligonal / modelos paramétricos | ❌ | — | fuera de alcance |

> La parte 3D/OpenGL de la U4 **no** se cubre: EcoBot es 2D. Esto es una decisión de
> alcance consciente — el proyecto usa "uno o varios temas del curso", y el gancho con
> la U4 son las **transformaciones con coordenadas homogéneas reales**.

---

## Unidad 1 — Fundamentos de procesamiento de imágenes  *(parcial)*

| Tema del sílabo | ¿Cubierto? | Dónde | Qué mostrar |
|---|---|---|---|
| Introducción a Python | ✅ | todo | — |
| Modelos de color (RGB, HSV, YCbCr) | ✅ | `filters/equalization.py` (YCbCr), indicador de salud en HSV | conversión de color en el filtro |
| Brillo y contraste / transformaciones de intensidad | ✅ | `core/effects.py` (tinte por contaminación) | mundo oscuro→vibrante al restaurar |
| Histograma y ecualización | ✅ | `filters/equalization.py` + `ui/histogram_panel.py` | el panel de histograma antes/después |
| Filtros (dominio espacial) | ✅ | `filters/sobel.py` | Sobel aplicado en vivo sobre el nivel |
| Transformaciones geométricas | 🟡 | implícito en `robot`/`camera` | las matrices afines |
| Dominio de la frecuencia | ❌ | — | no se usa (opcional como extra) |
| Ruido y entropía | ❌ | — | fuera de alcance |

## Unidad 2 — Segmentación, compresión y descripción  *(parcial)*

| Tema del sílabo | ¿Cubierto? | Dónde | Qué mostrar |
|---|---|---|---|
| Detección de bordes | ✅ | `filters/sobel.py` | `FILTER_EDGES` revelando celdas `HIDDEN` |
| Umbral global y local (Otsu) | ✅ | `filters/threshold.py` | `FILTER_THRESH` separando zona segura/tóxica |
| Segmentación por regiones / watershed | ❌ | — | fuera de alcance |
| Compresión | ❌ | — | fuera de alcance |
| Descriptores | ❌ | — | fuera de alcance |

## Unidad 3 — ML / Deep Learning  *(fuera de alcance)*

No se cubre. EcoBot no requiere entrenar redes. Si se quisiera tocar la U3 en una
versión futura, la mecánica natural sería un clasificador del estado del ecosistema;
está fuera del alcance de las 6 semanas y del valor del juego.

---

## Resumen para el informe

EcoBot cubre, de forma **aplicada y verificable en código**:
- **Unidad 4 (núcleo):** PyGame completo, cámara, control de personaje, colliders,
  victoria/derrota, mecánicas, y transformaciones afines / coordenadas homogéneas /
  concatenación con matrices 3×3 reales.
- **Unidad 1:** modelos de color, transformaciones de intensidad, histograma y
  ecualización, filtros del dominio espacial (Sobel).
- **Unidad 2:** detección de bordes y umbralización (Otsu), integradas como mecánica
  real con OpenCV sobre la superficie de PyGame.

El diferenciador es que **los filtros no son decorativos**: son OpenCV ejecutándose
sobre el frame del juego, con un panel de histograma que explica el concepto.
