# EcoBot 🤖🌱

> Programa el cambio que quieres ver en el mundo.

Juego de **pensamiento computacional** (estilo *Lightbot*) con temática ambiental.
El jugador no controla al robot directamente: arma una **secuencia de instrucciones**
(con bucles `REPETIR` y subrutinas) para que **EcoBot** limpie y restaure ecosistemas
destruidos por la contaminación.

**Curso:** Computación Gráfica (CC431) — UNI, Facultad de Ciencias, 2026-I
**Equipo:** Max Serrano Aróstegui · Aaron Dávila Santos · Walter Poma Navarro
**Stack:** Python 3.11 · PyGame 2.x · NumPy · OpenCV

---

## Qué cubre del curso

| Unidad | Cómo se ve en EcoBot |
|--------|----------------------|
| **U4 — Videojuegos y 3D** (núcleo) | PyGame completo, cámara, colliders, victoria/derrota, mecánicas, y **movimiento del robot con matrices homogéneas 3×3 reales** (traslación/rotación/escala concatenadas). |
| **U1 — Procesamiento de imágenes** | Filtros espaciales (Sobel), histograma + ecualización, modelos de color (RGB/YCbCr/HSV), transformaciones de intensidad. |
| **U2 — Segmentación** | Umbralización (Otsu) y detección de bordes, integradas como **mecánica real**: los filtros de OpenCV se aplican sobre la superficie de PyGame para revelar celdas ocultas. |

El detalle tema-por-tema está en [`docs/specs/05-syllabus-coverage.md`](docs/specs/05-syllabus-coverage.md).

---

## Instalación y ejecución

```bash
# 1. (recomendado) entorno virtual
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 2. dependencias
pip install -r requirements.txt

# 3. correr el juego
python main.py
```

> El scaffold actual arranca e importa todos los módulos, pero la lógica está como
> `stub` (`NotImplementedError`). El plan de trabajo y las tareas están en
> [`CONTRIBUTING.md`](CONTRIBUTING.md) y [`docs/issues-backlog.md`](docs/issues-backlog.md).

---

## Estructura

```
ecobot/
├── main.py              # entry point + game loop          (Rol A)
├── settings.py          # constantes globales
├── core/                # motor: grilla, robot, intérprete  (Rol A)
│   └── camera.py effects.py                                 (Rol B)
├── filters/             # filtros OpenCV reales             (Rol B)
├── ui/                  # paneles, menús, mapa              (Rol C)
│   └── histogram_panel.py                                   (Rol B)
├── utils/               # bridge PyGame↔OpenCV, editor      (Rol B / C)
├── data/levels/         # 16 niveles en JSON                (Rol C)
├── assets/              # sprites, tiles, audio, fuentes    (Rol C)
├── tests/               # pytest de la lógica pura
└── docs/                # specs, contratos y backlog del equipo
```

---

## Cómo trabajamos (resumen)

- `main` **siempre** corre sin crashear. Nada roto se mergea a `main`.
- Cada quien trabaja en su rama (`motor`, `graficos`, `contenido`) y abre **Pull Request**;
  otro integrante lo revisa antes de mergear.
- Commits en español: `area: descripción` (ej. `motor: el intérprete expande REPETIR`).
- Nombres de código en inglés; textos del juego y comentarios en español.
- Los **contratos compartidos** entre roles están congelados en
  [`docs/specs/01-contracts.md`](docs/specs/01-contracts.md). Cambiarlos obliga a avisar al equipo.

Convenciones completas, roles y *Definition of Done* en [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Subir a GitHub

```bash
git remote add origin https://github.com/<usuario-o-org>/ecobot.git
git branch -M main
git push -u origin main
```

## Tests

```bash
pytest            # corre la lógica pura: intérprete, colisiones, filtros
```
