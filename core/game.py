"""`Game` — máquina de estados y game loop principal.

Coordina las pantallas (MENU, MAP, LEVEL, FILTER_EFFECT, VICTORY, FAILURE),
delega el renderizado y el manejo de eventos según el estado actual, y persiste
el progreso del jugador.

Dueño: Rol A (Motor).
Spec: docs/specs/02-core-engine.md
Contratos: docs/specs/01-contracts.md  (§3 estados, §5 guardado)
"""

import pygame

import settings


class Game:
    """Orquesta el ciclo de vida del juego mediante una máquina de estados.

    Estados válidos (ver settings): MENU, MAP, LEVEL, FILTER_EFFECT, VICTORY, FAILURE.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = settings.STATE_MENU
        self.progress: dict = {}  # cargado desde data/save/progress.json

    def run(self) -> None:
        """Game loop principal: eventos -> update -> render, a FPS fijos."""
        raise NotImplementedError("Rol A — Semana 1/2")

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Despacha eventos de input según el estado actual."""
        raise NotImplementedError("Rol A")

    def update(self, dt: float) -> None:
        """Avanza la lógica del estado actual un frame."""
        raise NotImplementedError("Rol A")

    def render(self) -> None:
        """Dibuja la pantalla del estado actual."""
        raise NotImplementedError("Rol A")

    def change_state(self, new_state: str) -> None:
        """Transición controlada entre estados de la máquina."""
        raise NotImplementedError("Rol A")

    def load_progress(self) -> dict:
        """Lee `data/save/progress.json` (ver contrato §3.5). Devuelve dict vacío si no existe."""
        raise NotImplementedError("Rol A")

    def save_progress(self) -> None:
        """Escribe el progreso actual a `data/save/progress.json` (ver contrato §3.5)."""
        raise NotImplementedError("Rol A")
