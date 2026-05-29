"""Detección de bordes Sobel (Unidades 1 y 2).

Función pura sobre ndarrays: separada de PyGame para poder testearla contra una
salida conocida (tests/test_filters.py). `FilterEngine.apply_sobel` la envuelve con
el bridge Surface↔ndarray.

Dueño: Rol B (Gráficos / Visión).
Spec: docs/specs/03-graphics-filters.md
"""

import numpy as np


def sobel_edges(bgr: np.ndarray, ksize: int = 3) -> np.ndarray:
    """Magnitud del gradiente Sobel, normalizada a 0–255 (BGR de 3 canales).

    Pasos (ver docs/specs/03-graphics-filters.md): BGR→GRAY, Sobel x e y, magnitud, normalizar, GRAY→BGR.
    """
    raise NotImplementedError("Rol B — Semana 3")
