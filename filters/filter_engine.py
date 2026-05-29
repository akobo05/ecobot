"""`FilterEngine` — aplica filtros OpenCV REALES sobre superficies de PyGame.

Diferenciador del proyecto: cuando EcoBot ejecuta un filtro, el efecto visual NO es
decorativo — es el output matemático real de OpenCV sobre el frame del nivel.

Cada método: recorta `rect` de `surface`, lo pasa a ndarray (BGR) con el bridge,
aplica el filtro y devuelve una nueva `pygame.Surface`.

Dueño: Rol B (Gráficos / Visión).
Spec: docs/specs/03-graphics-filters.md
Contrato: docs/specs/01-contracts.md §3.4 (Surface ↔ ndarray)
Recetas de cada filtro: docs/specs/03-graphics-filters.md
"""

import pygame


class FilterEngine:
    """Filtros de imagen integrados como mecánica de juego."""

    @staticmethod
    def apply_sobel(surface: pygame.Surface, rect: pygame.Rect) -> pygame.Surface:
        """Detección de bordes Sobel sobre el área `rect` (Unidades 1 y 2).

        Revela el contorno de las celdas HIDDEN. Ver filters/sobel.py.
        """
        raise NotImplementedError("Rol B — Semana 3. Ver docs/specs/03-graphics-filters.md y filters/sobel.py")

    @staticmethod
    def apply_equalization(surface: pygame.Surface, rect: pygame.Rect) -> pygame.Surface:
        """Ecualización de histograma sobre el canal Y (YCbCr) (Unidad 1).

        Revela contaminantes en zonas oscuras. Ver filters/equalization.py.
        """
        raise NotImplementedError("Rol B — Semana 3. Ver docs/specs/03-graphics-filters.md y filters/equalization.py")

    @staticmethod
    def apply_threshold(surface: pygame.Surface, rect: pygame.Rect) -> pygame.Surface:
        """Umbralización de Otsu (Unidad 2): separa zona segura de zona tóxica.

        Ver filters/threshold.py.
        """
        raise NotImplementedError("Rol B — Semana 3. Ver docs/specs/03-graphics-filters.md y filters/threshold.py")
