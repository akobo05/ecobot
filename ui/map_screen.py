"""`MapScreen` — mapa de mundos y selección de nivel.

Muestra los 3 mundos con sus niveles bloqueados/desbloqueados y las estrellas
obtenidas (lee `progress.json`, contrato §3.5), además de la barra global
"Planeta X% restaurado".

Dueño: Rol C (UI).
Spec: docs/specs/04-ui-content.md
"""

import pygame


class MapScreen:
    """Pantalla de selección de nivel entre mundos."""

    def __init__(self, progress: dict) -> None:
        self.progress = progress

    def handle_event(self, event: pygame.event.Event) -> str | None:
        """Devuelve el id de nivel seleccionado (p. ej. "1-2") o None."""
        raise NotImplementedError("Rol C — Semana 3")

    def render(self, surface: pygame.Surface) -> None:
        """Dibuja el mapa de mundos, candados, estrellas y progreso global."""
        raise NotImplementedError("Rol C — Semana 3")
