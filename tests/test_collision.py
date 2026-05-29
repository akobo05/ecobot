"""Tests de colisiones y condiciones de victoria/derrota (lógica pura). Dueño: Rol A.

Marcados como skip hasta implementar collision.py (Semana 2).
"""

import pytest


@pytest.mark.skip(reason="collision.py aún no implementado — quitar al implementar (Rol A)")
def test_salir_de_la_grilla_es_derrota():
    # Cargar un nivel pequeño, mover al robot fuera de límites y verificar is_failure.
    ...


@pytest.mark.skip(reason="collision.py aún no implementado — quitar al implementar (Rol A)")
def test_victoria_requiere_tareas_completas_y_meta():
    # Robot en GOAL con tareas pendientes -> NO es victoria.
    ...
