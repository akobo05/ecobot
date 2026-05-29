# Cómo contribuir a EcoBot

Guía de trabajo del equipo (3 integrantes). Es autocontenida: todo lo necesario para
desarrollar está en este repo (specs en `docs/specs/`, este archivo y el código).

## Roles y propiedad de archivos

El código se divide en tres áreas que casi no se pisan; cada integrante es dueño de una.

| Rol | Área | Es dueño de |
|-----|------|-------------|
| **A** | Motor y lógica | `main.py`, `settings.py`, `core/` (game, level, robot, instruction, interpreter, collision), `data/save/` |
| **B** | Gráficos, filtros y visión | `filters/`, `utils/pygame_cv_bridge.py`, `ui/histogram_panel.py`, `core/camera.py`, `core/effects.py` |
| **C** | Niveles, UI, contenido y docs | `ui/` (panel, hud, map_screen, menu), `data/levels/`, `utils/level_editor.py`, `assets/`, `README.md`, informe |

Nadie trabaja aislado: el panel con bloques `REPEAT` (Rol C) y el intérprete (Rol A) se
diseñan en pareja. Los `tests/` los escribe cada rol para su módulo.

## Flujo de Git

- `main` **siempre** se ejecuta sin crashear. Nada roto se mergea a `main`.
- Cada quien trabaja en su rama: `motor`, `graficos`, `contenido`, o por tarea
  (`feat/interprete`, `feat/filtro-sobel`).
- Para llevar código a `main` se abre un **Pull Request**; otro integrante lo revisa
  antes de mergear.
- Commits frecuentes y pequeños, en español con formato `area: descripción`
  (ej. `motor: el intérprete expande REPEAT`, `filtros: Sobel sobre Surface`).
- Al empezar: `git pull`. Antes de abrir un PR: traer `main` y resolver conflictos en local.

## Convenciones de código

- Nombres de clases y funciones en **inglés** (`MOVE`, `Interpreter`, `apply_sobel`);
  textos del juego y comentarios en **español**.
- Type hints y docstrings en clases y funciones públicas.
- `settings.py` centraliza las constantes (FPS, tamaños, colores). Nadie hardcodea
  valores sueltos.
- Comentar con generosidad: el proyecto se sustenta de forma oral y cada quien debe
  poder explicar su módulo.

## Definition of Done

Una tarea está terminada solo cuando:

1. El código corre sin crashear.
2. Cumple lo que pedía la tarea.
3. Otro integrante lo probó (lo jugó o revisó el PR).
4. Está commiteado y mergeado a `main`.
5. Si es lógica pura (intérprete, colisiones, filtros), tiene su test.

## Testing

`pytest` para la **lógica pura** (sin abrir ventana): intérprete (`interpreter.py`),
colisiones (`collision.py`), filtros y el bridge (comparar contra una salida conocida).
El resto (UI, niveles, animaciones) se prueba jugando en cada integración.

## Cronograma (6 semanas) y milestones

| Semana | Objetivo | Milestone |
|--------|----------|-----------|
| 1 | Cimientos y contratos | Corre el menú y una grilla con EcoBot quieto |
| 2 | Movimiento e intérprete | Vertical slice jugable del Mundo 1 |
| 3 | Mundo 1 completo + filtros | Mundo 1 100% (mapa, estrellas, guardado) + filtros |
| 4 | Mundos 2 y 3 | Los 3 mundos jugables de inicio a fin |
| 5 | Integración y pulido | Juego completo y estable, sin bugs bloqueantes |
| 6 | Cierre | Entregable + informe + presentación ensayada |

El detalle por rol y tarea está en [`docs/issues-backlog.md`](docs/issues-backlog.md)
y en el tablero de issues.

## Capa opcional (lo primero que se recorta si vamos retrasados)

Orden de recorte: partículas → cinemáticas → audio → funciones avanzadas del editor →
reducir de 4 a 3 niveles por mundo → último recurso: dejar 2 mundos en vez de 3.
El núcleo que **no** se recorta: motor, intérprete con `REPEAT`, ≥2 mundos con sus
bosses, los 3 filtros y el panel de histograma.
