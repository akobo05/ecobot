# EcoBot — Specs · 00 Overview

**Curso:** Computación Gráfica (CC431) — UNI, 2026-I
**Equipo:** Max Serrano · Aaron Dávila · Walter Poma
**Stack:** Python 3.11 · PyGame 2.x · NumPy · OpenCV

---

## Qué es esto

Estas specs son el **contrato de trabajo del equipo**. Describen *qué* hace cada
módulo, *qué interfaz* expone y *de qué depende*, para que tres personas puedan
programar en paralelo sin pisarse. No repiten el diseño del juego — eso vive en los
documentos de diseño.

## Documentos de diseño (fuente de verdad del juego)

Están en la carpeta superior, **fuera del repo**:

- `ECOBOT_CONCEPTO.md` — la idea: cómo se juega y cómo se siente.
- `ECOBOT_GDD.md` — diseño técnico completo: mecánicas, mundos, niveles, arquitectura, assets.
- `ECOBOT_PLAN_TRABAJO.md` — roles, metodología, cronograma de 6 semanas, contratos.

Estas specs **derivan** de esos documentos; si hay conflicto, manda el GDD/Plan y se
actualiza la spec.

## Mapa de las specs

| Doc | Tema | Para quién |
|-----|------|-----------|
| `00-overview.md` | Este archivo: cómo leer las specs | Todos |
| `01-contracts.md` | **Contratos congelados** entre roles (los puntos de dependencia mutua) | Todos |
| `02-core-engine.md` | Motor: grilla, robot, intérprete, colisiones, estados | Rol A |
| `03-graphics-filters.md` | Bridge, filtros OpenCV, cámara, histograma, efectos | Rol B |
| `04-ui-content.md` | Panel drag&drop, HUD, mapa, menú, editor, diseño de niveles | Rol C |
| `05-syllabus-coverage.md` | Mapa tema-del-sílabo → implementación → sustentación | Todos |

## Los tres roles (resumen)

- **Rol A — Motor y lógica:** `main.py`, `settings.py`, `core/` (salvo camera/effects), `data/save/`.
- **Rol B — Gráficos, filtros y visión:** `filters/`, `utils/pygame_cv_bridge.py`, `ui/histogram_panel.py`, `core/camera.py`, `core/effects.py`.
- **Rol C — Niveles, UI, contenido y docs:** `ui/` (salvo histograma), `data/levels/`, `utils/level_editor.py`, `assets/`, `README.md` e informe.

El reparto archivo por archivo está en `ECOBOT_PLAN_TRABAJO.md` §1.5.

## Convenciones (resumen)

- Nombres de código en **inglés**; textos del juego y comentarios en **español**.
- Type hints y docstrings en clases/funciones públicas.
- Constantes centralizadas en `settings.py`; nadie hardcodea valores sueltos.
- `main` siempre corre sin crashear. Código a `main` solo vía Pull Request revisado.
- Tests con `pytest` para la lógica pura (intérprete, colisiones, filtros, bridge).

La *Definition of Done* y la metodología de Git completas están en `ECOBOT_PLAN_TRABAJO.md` §2.
