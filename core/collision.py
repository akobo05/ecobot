"""Detección de colisiones y condiciones de victoria/derrota.

Lógica pura (sin PyGame): dado el estado del nivel y la posición/dirección del robot,
decide si un movimiento es válido y si la partida se ganó o se perdió.

Dueño: Rol A (Motor).
Spec: docs/specs/02-core-engine.md
Contrato: docs/specs/01-contracts.md §3.2 (condiciones de derrota a congelar)
"""

from core.level import Level
from core.robot import Robot


def can_move(level: Level, robot: Robot, dcol: int, drow: int) -> bool:
    """True si el robot puede moverse (dcol, drow) sin salir de la grilla ni chocar."""
    raise NotImplementedError("Rol A — Semana 2")


def is_victory(level: Level, robot: Robot) -> bool:
    """True si todas las tareas están completas y el robot está en la meta (GOAL)."""
    raise NotImplementedError("Rol A — Semana 2")


def is_failure(level: Level, robot: Robot, instructions_left: bool) -> bool:
    """True si se cumple alguna condición de derrota.

    Condiciones a congelar en Semana 1 (contrato §3.2):
      - salir de la grilla,
      - pisar WALL,
      - pisar DIRTY/SPILL sin neutralizar,
      - quedarse sin instrucciones con tareas pendientes.
    """
    raise NotImplementedError("Rol A — congelar condiciones en Semana 1")
