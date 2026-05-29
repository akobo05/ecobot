"""Umbralización (Unidad 2).

Función pura sobre ndarrays. Umbral de Otsu (global) para separar zona segura de
zona tóxica; opcionalmente umbral local/adaptativo.

Dueño: Rol B (Gráficos / Visión).
Spec: docs/specs/03-graphics-filters.md
"""

import numpy as np


def otsu_threshold(bgr: np.ndarray) -> np.ndarray:
    """Umbral de Otsu sobre la versión en grises; devuelve BGR binarizado (ver docs/specs/03-graphics-filters.md)."""
    raise NotImplementedError("Rol B — Semana 3")


def adaptive_threshold(bgr: np.ndarray, block_size: int = 11, c: int = 2) -> np.ndarray:
    """Umbral local/adaptativo (opcional, refuerza la Unidad 2)."""
    raise NotImplementedError("Rol B — opcional")
