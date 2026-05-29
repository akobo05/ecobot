"""`Robot` — EcoBot: posición, dirección, animación y movimiento homogéneo.

PUNTO CLAVE DE LA UNIDAD 4: el movimiento NO se hace sumando enteros, sino con
**matrices homogéneas 3×3** y NumPy (traslación y rotación). Esto es lo que conecta
el juego con la teoría de transformaciones afines / coordenadas homogéneas y se debe
poder señalar explícitamente en la sustentación.

Dueño: Rol A (Motor).
Spec: docs/specs/02-core-engine.md
Contrato: docs/specs/01-contracts.md §3.6 (coordenadas homogéneas)
"""

import numpy as np

import settings


class Robot:
    """EcoBot. Vive en coordenadas de grilla (col, row) y mira en una dirección."""

    def __init__(self, col: int, row: int, direction: str = "RIGHT") -> None:
        self.col = col
        self.row = row
        self.direction = direction  # clave de settings.DIRECTIONS
        self.anim_frame = 0

    # --- Transformaciones homogéneas (Unidad 4) ---

    @staticmethod
    def translation_matrix(dcol: int, drow: int) -> np.ndarray:
        """Matriz de traslación 3×3: T(dc,dr) = [[1,0,dc],[0,1,dr],[0,0,1]]."""
        raise NotImplementedError("Rol A — Semana 2. Ver contrato §3.6")

    @staticmethod
    def rotation_matrix(degrees: float) -> np.ndarray:
        """Matriz de rotación 3×3 para girar el vector de dirección 90°."""
        raise NotImplementedError("Rol A — Semana 2. Ver contrato §3.6")

    def position_vector(self) -> np.ndarray:
        """Posición como vector columna homogéneo [col, row, 1]ᵀ."""
        raise NotImplementedError("Rol A")

    # --- Acciones (las llama el Interpreter) ---

    def move_forward(self) -> None:
        """Avanza 1 celda en la dirección actual aplicando la matriz de traslación."""
        raise NotImplementedError("Rol A")

    def turn_left(self) -> None:
        """Rota la dirección 90° a la izquierda con la matriz de rotación."""
        raise NotImplementedError("Rol A")

    def turn_right(self) -> None:
        """Rota la dirección 90° a la derecha con la matriz de rotación."""
        raise NotImplementedError("Rol A")

    def jump(self) -> None:
        """Salta 1 celda en la dirección actual (supera obstáculos bajos)."""
        raise NotImplementedError("Rol A — Semana 3")

    def update(self, dt: float) -> None:
        """Avanza la animación del robot (interpolación entre celdas)."""
        raise NotImplementedError("Rol A")

    def render(self, surface, camera) -> None:
        """Dibuja el sprite de EcoBot en su posición de pantalla."""
        raise NotImplementedError("Rol A")
