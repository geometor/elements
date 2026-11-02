"""Programmatic construction for Book III, Proposition 5 (III.5)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0018.g1 using geometor.model."""
    model = Model("III.5")

    # Points (y-inverted for standard mathematical coordinates)
    O1 = model.set_point(76, -80, classes=["auxiliary"], ID="O1")
    O2 = model.set_point(105, -102, classes=["auxiliary"], ID="O2")
    C = model.set_point(105.94, -28.01, classes=["given"], ID="C")
    B = model.set_point(34.0, -122.85, classes=["given"], ID="B")
    A = model.set_point(24.04, -50.0, classes=["given"], ID="A")
    D = model.set_point(38.5, -69.84, classes=["given"], ID="D")
    E = model.set_point(92, -92, ID="E")
    F = model.set_point(124, -116, ID="F")
    G = model.set_point(164.32, -146.24, ID="G")

    # Construction circles ABC and CDG
    model.construct_circle(O1, C)
    model.construct_circle(O2, C)

    # Segments
    model.set_segment(E, C)
    model.set_segment(E, G)
    model.set_segment(E, F)
    model.set_segment(F, G)

    # Sections
    model.set_section([E, F, G])

    return model


if __name__ == "__main__":
    construct_g1()
