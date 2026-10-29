"""Programmatic construction for Book III, Proposition 6 (III.6)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0019.g1 using geometor.model."""
    model = Model("III.6")

    # Points (y-inverted for standard mathematical coordinates)
    O1 = model.set_point(102, -102, classes=["auxiliary"], ID="O1")
    O2 = model.set_point(82.8, -87.6, classes=["auxiliary"], ID="O2")
    C = model.set_point(33.2, -50.4, classes=["given"], ID="C")
    F = model.set_point(94, -96, ID="F")
    E = model.set_point(142.12, -105.62, ID="E")
    B = model.set_point(187.07, -114.61, ID="B")
    D = model.set_point(82.8, -149.6, classes=["given"], ID="D")
    A = model.set_point(85, -186.3, classes=["given"], ID="A")

    # Construction circles ABC and CDE touching internally at C
    model.construct_circle(O1, C)
    model.construct_circle(O2, C)

    # Segments
    model.set_segment(F, C)
    model.set_segment(F, B)
    model.set_segment(F, E)
    model.set_segment(E, B)

    # Sections
    model.set_section([F, E, B])

    return model


if __name__ == "__main__":
    construct_g1()
