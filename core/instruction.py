"""Instrucciones del programa que arma el jugador.

Define los tokens de instrucción y la estructura de datos del programa (incluyendo
el bloque `REPEAT` con cuerpo anidado y las llamadas a función). NO ejecuta nada:
solo modela. La ejecución/aplanado vive en `interpreter.py`.

Dueño: Rol A (Motor).
Spec: docs/specs/02-core-engine.md
Contrato: docs/specs/01-contracts.md §3.2 (instrucciones y semántica de REPEAT/FUNCIÓN)
"""

from dataclasses import dataclass, field

# Tokens de instrucción (contrato entre intérprete, panel y filtros)
SIMPLE_OPS = {"MOVE", "TURN_L", "TURN_R", "ACTION", "JUMP"}
FILTER_OPS = {"FILTER_EDGES", "FILTER_EQ", "FILTER_THRESH"}
CALL_OPS = {"CALL_F1", "CALL_F2"}
BLOCK_OPS = {"REPEAT"}

ALL_OPS = SIMPLE_OPS | FILTER_OPS | CALL_OPS | BLOCK_OPS


@dataclass
class Instruction:
    """Una instrucción del programa.

    - `op` es uno de ALL_OPS.
    - `n` solo aplica a REPEAT (número de repeticiones).
    - `body` solo aplica a REPEAT (lista de instrucciones a repetir).
    """

    op: str
    n: int = 1
    body: list["Instruction"] = field(default_factory=list)

    def is_block(self) -> bool:
        """True si la instrucción tiene cuerpo anidado (REPEAT)."""
        raise NotImplementedError("Rol A")

    def slot_cost(self) -> int:
        """Cuántos slots del panel cuenta esta instrucción.

        DECISIÓN A CONGELAR EN SEMANA 1 (contrato §3.2): cómo se cuentan los slots
        de un bloque REPEAT.
        """
        raise NotImplementedError("Rol A — congelar regla de slots en Semana 1")


def parse_program(data: dict) -> tuple[list[Instruction], dict[str, list[Instruction]]]:
    """Convierte el JSON del programa (contrato §3.2) en (main, functions)."""
    raise NotImplementedError("Rol A")
