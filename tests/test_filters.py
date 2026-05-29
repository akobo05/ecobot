"""Tests de los filtros y del bridge PyGame↔OpenCV (lógica pura). Dueño: Rol B.

El bridge se prueba convirtiendo ida y vuelta; los filtros comparando su salida
contra un resultado conocido sobre una imagen de prueba. Marcados como skip hasta
implementar (Semana 1/3).
"""

import pytest


@pytest.mark.skip(reason="pygame_cv_bridge aún no implementado — quitar al implementar (Rol B)")
def test_bridge_ida_y_vuelta_preserva_imagen():
    # numpy_to_pygame(pygame_to_numpy(surface)) ~= surface
    ...


@pytest.mark.skip(reason="filters aún no implementados — quitar al implementar (Rol B)")
def test_sobel_detecta_borde_vertical():
    # Imagen mitad negra / mitad blanca -> Sobel marca el borde en la columna central.
    ...
