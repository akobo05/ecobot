"""Constantes globales del juego.

Centraliza FPS, tamaños, colores y rutas. **Nadie hardcodea valores sueltos**
en otros módulos: si necesitas una constante nueva, va aquí.

Dueño: Rol A (Motor). Cualquier rol puede leer de aquí.
Spec: docs/specs/02-core-engine.md
"""

from pathlib import Path

# --- Rutas ---
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
LEVELS_DIR = DATA_DIR / "levels"
SAVE_PATH = DATA_DIR / "save" / "progress.json"

# --- Ventana / loop ---
WINDOW_TITLE = "EcoBot"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# --- Grilla ---
TILE_SIZE = 64           # px por celda (escala mundo -> pantalla)
ROBOT_STEP_FRAMES = 12   # frames que dura la animación de un paso

# --- Colores base (RGB) ---
COLOR_BG = (18, 18, 24)
COLOR_GRID_LINE = (40, 40, 50)
COLOR_TEXT = (235, 235, 235)

# --- Direcciones: vector (dcol, drow) en coordenadas de grilla ---
# row crece hacia ABAJO (convención de pantalla); ver docs/specs/01-contracts.md §6.
DIRECTIONS = {
    "RIGHT": (1, 0),
    "LEFT": (-1, 0),
    "UP": (0, -1),
    "DOWN": (0, 1),
}

# --- Estados del juego (máquina de estados de Game) ---
STATE_MENU = "MENU"
STATE_MAP = "MAP"
STATE_LEVEL = "LEVEL"
STATE_FILTER_EFFECT = "FILTER_EFFECT"
STATE_VICTORY = "VICTORY"
STATE_FAILURE = "FAILURE"
