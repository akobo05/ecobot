"""`Interpreter` — aplana y ejecuta paso a paso el programa del jugador.

Recibe el `main` y las `functions` (ver instruction.py / contrato §3.2), expande los
bloques `REPEAT` y las llamadas `CALL_F1`/`CALL_F2` en una lista plana de instrucciones
simples, y la entrega de a un paso por vez para que `Game` la anime.

Esta es la pieza de LÓGICA PURA más importante: se prueba sin abrir ventana
(ver tests/test_interpreter.py).

Dueño: Rol A (Motor).
Spec: docs/specs/02-core-engine.md
Contrato: docs/specs/01-contracts.md §3.2
"""

from core.instruction import Instruction


class Interpreter:
    """Expande un programa a pasos simples y los emite uno por uno."""

    def __init__(
        self,
        main: list[Instruction],
        functions: dict[str, list[Instruction]],
    ) -> None:
        self.queue: list[Instruction] = self._expand(main, functions)
        self.index = 0

    def _expand(
        self,
        instructions: list[Instruction],
        functions: dict[str, list[Instruction]],
    ) -> list[Instruction]:
        """Aplana REPEAT (n veces) y CALL_Fx (sustituye por el cuerpo) en pasos simples.

        Regla congelada (contrato §3.2): sin anidamiento de REPEAT dentro de REPEAT
        (solo un nivel). Una llamada a función no contiene bloques.
        """
        raise NotImplementedError("Rol A — Semana 3")

    def step(self) -> Instruction | None:
        """Devuelve la siguiente instrucción simple a ejecutar, o None si terminó."""
        raise NotImplementedError("Rol A — Semana 2")

    def is_finished(self) -> bool:
        """True si ya no quedan instrucciones por ejecutar."""
        raise NotImplementedError("Rol A")

    def reset(self) -> None:
        """Reinicia el cursor de ejecución al inicio de la cola."""
        raise NotImplementedError("Rol A")
