"""Editor de niveles mínimo (herramienta de desarrollo, no parte del juego).

Permite cargar un JSON de nivel, hacer clic sobre la grilla para cambiar el token de
una celda, colocar al robot y la meta, y guardar de nuevo a JSON — para no escribir
los 16 niveles a mano. Versión mínima en Semana 2; las funciones avanzadas son capa
opcional.

Dueño: Rol C (Contenido).
Spec: docs/specs/04-ui-content.md
Uso:  python -m utils.level_editor data/levels/world1/level_1.json
"""

import sys


class LevelEditor:
    """Editor por clics de la grilla de un nivel."""

    def __init__(self, path: str | None = None) -> None:
        self.path = path
        self.grid: list[list[str]] = []

    def load(self, path: str) -> None:
        """Carga un nivel desde JSON (o crea una grilla vacía si no existe)."""
        raise NotImplementedError("Rol C — Semana 2")

    def run(self) -> None:
        """Abre la ventana del editor y procesa clics hasta guardar/salir."""
        raise NotImplementedError("Rol C — Semana 2")

    def save(self, path: str | None = None) -> None:
        """Serializa la grilla al esquema canónico (contrato §3.1) y guarda."""
        raise NotImplementedError("Rol C — Semana 2")


if __name__ == "__main__":
    editor = LevelEditor(sys.argv[1] if len(sys.argv) > 1 else None)
    editor.run()
