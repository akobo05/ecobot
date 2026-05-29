"""Puente PyGame ↔ OpenCV: convierte `Surface` ↔ ndarray de NumPy.

Es el contrato §3.4 entre el motor (Rol A, que entrega la Surface del nivel) y los
filtros (Rol B). OpenCV trabaja en BGR; PyGame en RGB. Estas dos funciones encapsulan
la conversión de orden de canales y de ejes.

Es lógica pura testeable (tests/test_filters.py): convertir ida y vuelta debe
devolver una imagen equivalente.

Dueño: Rol B (Gráficos / Visión).
Spec: docs/specs/03-graphics-filters.md
Contrato: docs/specs/01-contracts.md §3.4
"""

import numpy as np
import pygame


def pygame_to_numpy(surface: pygame.Surface, rect: pygame.Rect | None = None) -> np.ndarray:
    """Recorta `rect` de `surface` y devuelve un ndarray BGR (formato OpenCV).

    Si `rect` es None, convierte la superficie completa.
    """
    raise NotImplementedError("Rol B — Semana 1 (con test)")


def numpy_to_pygame(array: np.ndarray) -> pygame.Surface:
    """Convierte un ndarray BGR de OpenCV a una `pygame.Surface` (RGB)."""
    raise NotImplementedError("Rol B — Semana 1 (con test)")
