"""Ecualización de histograma (Unidad 1).

Función pura sobre ndarrays. Ecualiza el canal de luminancia (Y de YCbCr) para no
distorsionar el color, revelando detalles ocultos en zonas oscuras.

Dueño: Rol B (Gráficos / Visión).
Spec: docs/specs/03-graphics-filters.md
"""

import numpy as np


def equalize_luminance(bgr: np.ndarray) -> np.ndarray:
    """Ecualiza el canal Y (YCbCr) y devuelve BGR (ver GDD §5.2)."""
    raise NotImplementedError("Rol B — Semana 3")


def histogram_rgb(bgr: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Devuelve los histogramas (256 bins) de los canales B, G, R.

    Lo usa el panel de histograma educativo (ui/histogram_panel.py).
    """
    raise NotImplementedError("Rol B — Semana 3")
