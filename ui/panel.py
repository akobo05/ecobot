"""`InstructionPanel` — el panel de instrucciones con arrastrar y soltar.

Es la UI más difícil del proyecto: el jugador arrastra tarjetas de instrucción a una
secuencia de slots, incluido el bloque `REPETIR` (con su cuerpo) y las llamadas a
`F1`/`F2`. Produce la estructura de datos del programa que consume el `Interpreter`
(contrato §3.2). Se diseña EN PAREJA con el Rol A.

Dueño: Rol C (UI).
Spec: docs/specs/04-ui-content.md
Contrato: docs/specs/01-contracts.md §3.2
"""

import pygame

from core.instruction import Instruction


class InstructionPanel:
    """Panel lateral donde el jugador construye el programa de EcoBot."""

    def __init__(self, available: list[str], max_slots: int) -> None:
        self.available = available      # instrucciones desbloqueadas este nivel
        self.max_slots = max_slots
        self.program: list[Instruction] = []
        self.functions: dict[str, list[Instruction]] = {"F1": [], "F2": []}

    def handle_event(self, event: pygame.event.Event) -> None:
        """Procesa drag & drop de tarjetas hacia/desde los slots."""
        raise NotImplementedError("Rol C — Semana 2/3")

    def slots_used(self) -> int:
        """Total de slots ocupados (ver regla de conteo de REPEAT, contrato §3.2)."""
        raise NotImplementedError("Rol C")

    def build_program(self) -> tuple[list[Instruction], dict[str, list[Instruction]]]:
        """Devuelve (main, functions) listos para el Interpreter."""
        raise NotImplementedError("Rol C")

    def reset(self) -> None:
        """Vacía la secuencia armada (botón RESET)."""
        raise NotImplementedError("Rol C")

    def render(self, surface: pygame.Surface) -> None:
        """Dibuja el panel, las tarjetas disponibles y la secuencia armada."""
        raise NotImplementedError("Rol C")
