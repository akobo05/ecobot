"""`Menu` — menú principal del juego.

Pantalla de inicio: título, botón de jugar (lleva al mapa de mundos), opciones y
salir.

Dueño: Rol C (UI).
Spec: docs/specs/04-ui-content.md
"""

import pygame


class Menu:
    """Menú principal."""

    def __init__(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event) -> str | None:
        """Devuelve la acción elegida ("PLAY", "QUIT", ...) o None."""
        raise NotImplementedError("Rol C — Semana 1")

    def render(self, surface: pygame.Surface) -> None:
        """Dibuja el menú principal."""
        raise NotImplementedError("Rol C — Semana 1")
