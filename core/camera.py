"""`Camera` — transforma coordenadas de mundo a pantalla y sigue a EcoBot.

Implementa la transformación **mundo → pantalla** como concatenación de una matriz
de escala (tamaño de tile) con una de traslación (desplazamiento de cámara) — esto
es, literalmente, el tema "concatenación de transformaciones" de la Unidad 4.

Dueño: Rol B (Gráficos).
Spec: docs/specs/03-graphics-filters.md
Contrato: docs/specs/01-contracts.md §3.6
"""

import numpy as np


class Camera:
    """Cámara 2D que mapea celdas de grilla a píxeles y sigue al robot."""

    def __init__(self, tile_size: int, viewport_size: tuple[int, int]) -> None:
        self.tile_size = tile_size
        self.viewport_w, self.viewport_h = viewport_size
        self.offset = np.array([0.0, 0.0])  # desplazamiento en píxeles

    def world_to_screen(self, col: float, row: float) -> tuple[int, int]:
        """Convierte coordenadas de grilla a píxeles vía escala ∘ traslación."""
        raise NotImplementedError("Rol B — Semana 2")

    def view_matrix(self) -> np.ndarray:
        """Matriz 3×3 escala∘traslación que aplica la cámara (concatenación)."""
        raise NotImplementedError("Rol B — Semana 2. Ver contrato §3.6")

    def follow(self, col: float, row: float) -> None:
        """Centra (suavemente) la cámara sobre una celda — para grillas grandes."""
        raise NotImplementedError("Rol B")
