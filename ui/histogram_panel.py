"""`HistogramPanel` — panel educativo de histograma (se muestra al aplicar un filtro).

Cuando EcoBot ejecuta ECUALIZAR o FILTRO_BORDES, aparece este panel con:
  - el histograma RGB del área afectada (dibujado con NumPy + PyGame),
  - miniaturas antes/después del filtro,
  - un tooltip educativo que explica el concepto.

Es el gancho "el juego enseña computación gráfica sin decirlo". Pertenece al Rol B
(no al Rol C) porque depende del cálculo de histogramas de `filters/`.

Dueño: Rol B (Gráficos / Visión).
Spec: docs/specs/03-graphics-filters.md
"""

import pygame


class HistogramPanel:
    """Panel lateral con el histograma RGB y el antes/después de un filtro."""

    def __init__(self) -> None:
        self.visible = False

    def show(self, before: pygame.Surface, after: pygame.Surface, tooltip: str) -> None:
        """Activa el panel con las miniaturas y el texto educativo del filtro aplicado."""
        raise NotImplementedError("Rol B — Semana 3")

    def render(self, surface: pygame.Surface) -> None:
        """Dibuja el histograma RGB (con filters.equalization.histogram_rgb) y miniaturas."""
        raise NotImplementedError("Rol B — Semana 3")
