"""Entry point de EcoBot.

Inicializa PyGame, crea la ventana y arranca el game loop delegando en `core.game.Game`.
Mantener este archivo mínimo: la lógica vive en `core/`.

Dueño: Rol A (Motor).
Spec: docs/specs/02-core-engine.md

Estado actual: STUB. Importa todo y abre la ventana, pero `Game.run()` aún no está
implementado (lanza NotImplementedError). Esto permite verificar que el árbol de
imports no esté roto antes de implementar la lógica.
"""

import pygame

import settings
from core.game import Game


def main() -> None:
    """Punto de entrada. Inicializa PyGame y corre el juego."""
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption(settings.WINDOW_TITLE)

    game = Game(screen)
    try:
        game.run()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
