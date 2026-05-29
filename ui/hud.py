"""`HUD` — información en pantalla durante un nivel.

Muestra slots usados / disponibles, tareas pendientes, el nombre del nivel, los
botones EJECUTAR y RESET, y la barra de "ecosistema restaurado".

Dueño: Rol C (UI).
Spec: docs/specs/04-ui-content.md
"""

import pygame


class HUD:
    """Capa de interfaz sobre el nivel."""

    def __init__(self) -> None:
        pass

    def render(self, surface: pygame.Surface, level, panel) -> None:
        """Dibuja contadores, botones y barra de restauración."""
        raise NotImplementedError("Rol C — Semana 2")
