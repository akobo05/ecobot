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
    """True si se cumple alguna condición de derrota (contrato §3, congelado).

    Se dispara FAILURE si ocurre CUALQUIERA:
      1. moverse fuera de la grilla ([0, cols-1] x [0, rows-1]),
      2. pisar una celda WALL,
      3. pisar una celda DIRTY (peligro intransitable),
      4. agotar las instrucciones (not instructions_left) con tareas pendientes
         (level.tasks_remaining() > 0).

    Nota: las celdas-tarea (DEAD_TREE/TRASH/SPILL) son transitables; pisarlas NO falla.
    """
    raise NotImplementedError("Rol A — Semana 2 (condiciones ya congeladas, contrato §3)")
