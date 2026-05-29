"""`Level` — carga un nivel desde JSON y lo renderiza como grilla.

Lee el esquema canónico de nivel (docs/specs/01-contracts.md §3.1), mantiene el
estado de las celdas (qué tareas faltan, qué celdas siguen ocultas) y dibuja la
grilla sobre la pantalla. Entrega al Rol B la superficie ya renderizada para los
filtros.

Dueño: Rol A (Motor).
Spec: docs/specs/02-core-engine.md
"""

import pygame


# Tokens de celda válidos (ver contrato §3.1)
CELL_TOKENS = {
    "GROUND",     # transitable
    "DIRTY",      # contaminada, intransitable hasta limpiar
    "WALL",       # inaccesible
    "GOAL",       # meta
    "DEAD_TREE",  # tarea PLANT
    "TRASH",      # tarea COLLECT
    "SPILL",      # tarea NEUTRALIZE
    "HIDDEN",     # oculta hasta aplicar un filtro
}


class Level:
    """Estado y renderizado de un nivel cargado desde JSON."""

    def __init__(self, data: dict) -> None:
        self.data = data
        self.name: str = data.get("name", "")
        self.cols, self.rows = data.get("grid_size", (0, 0))
        self.grid: list[list[str]] = data.get("grid", [])
        self.tasks: list[dict] = data.get("tasks", [])
        self.max_slots: int = data.get("max_slots", 0)

    @classmethod
    def load(cls, path: str) -> "Level":
        """Carga y valida un nivel desde un archivo JSON."""
        raise NotImplementedError("Rol A — Semana 1")

    def validate(self) -> None:
        """Verifica que el JSON cumpla el contrato §3.1 (tokens, tamaños, robot_start)."""
        raise NotImplementedError("Rol A")

    def cell_at(self, col: int, row: int) -> str:
        """Token de la celda (col, row). Lanza IndexError si está fuera de la grilla."""
        raise NotImplementedError("Rol A")

    def is_walkable(self, col: int, row: int) -> bool:
        """True si EcoBot puede pisar la celda (GROUND/GOAL y celdas ya limpiadas)."""
        raise NotImplementedError("Rol A")

    def tasks_remaining(self) -> int:
        """Número de tareas (PLANT/COLLECT/NEUTRALIZE) aún sin completar."""
        raise NotImplementedError("Rol A")

    def render(self, surface: pygame.Surface, camera) -> None:
        """Dibuja la grilla en `surface` aplicando el desplazamiento de `camera`."""
        raise NotImplementedError("Rol A")
