"""Tests del intérprete (lógica pura, sin abrir ventana).

Verifican que `Interpreter._expand` aplana correctamente REPEAT y las llamadas a
función, y que `step()` emite los pasos en orden. Dueño: Rol A.

Estos tests están marcados como `skip` hasta que el Interpreter esté implementado.
Quitar el skip al implementar (Semana 2/3).
"""

import pytest

from core.instruction import Instruction
from core.interpreter import Interpreter


@pytest.mark.skip(reason="Interpreter aún no implementado — quitar al implementar (Rol A)")
def test_expand_repeat_aplana_n_veces():
    main = [Instruction(op="REPEAT", n=3, body=[Instruction(op="MOVE")])]
    interp = Interpreter(main, {"F1": [], "F2": []})
    ops = [interp.step().op for _ in range(3)]
    assert ops == ["MOVE", "MOVE", "MOVE"]
    assert interp.step() is None


@pytest.mark.skip(reason="Interpreter aún no implementado — quitar al implementar (Rol A)")
def test_expand_call_funcion_sustituye_cuerpo():
    main = [Instruction(op="CALL_F1")]
    functions = {"F1": [Instruction(op="TURN_R"), Instruction(op="MOVE")], "F2": []}
    interp = Interpreter(main, functions)
    assert [interp.step().op, interp.step().op] == ["TURN_R", "MOVE"]
