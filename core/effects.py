"""Efectos visuales: partículas ambientales y ajuste de brillo/contraste del mundo.

Partículas de smog/agua contaminada y la transformación de intensidad que oscurece o
ilumina el mundo según el nivel de contaminación (Unidad 1: transformaciones de
intensidad). Capa de pulido: es lo primero que se recorta si el equipo va retrasado.

Dueño: Rol B (Gráficos).
Spec: docs/specs/03-graphics-filters.md
"""

import pygame


class ParticleSystem:
    """Emisor simple de partículas (smog, salpicaduras de agua contaminada)."""

    def __init__(self, kind: str) -> None:
        self.kind = kind
        self.particles: list = []

    def emit(self, pos: tuple[int, int], n: int = 1) -> None:
        """Crea `n` partículas en `pos`."""
        raise NotImplementedError("Rol B — capa opcional")

    def update(self, dt: float) -> None:
        """Avanza la simulación de las partículas."""
        raise NotImplementedError("Rol B — capa opcional")

    def render(self, surface: pygame.Surface) -> None:
        """Dibuja las partículas vivas."""
        raise NotImplementedError("Rol B — capa opcional")


def apply_contamination_tint(surface: pygame.Surface, contamination: float) -> pygame.Surface:
    """Ajusta brillo/contraste del mundo según el % de contaminación (0.0–1.0).

    Unidad 1: transformación de intensidad. A más contaminación, mundo más oscuro
    y desaturado; al restaurar, más vibrante.
    """
    raise NotImplementedError("Rol B")
