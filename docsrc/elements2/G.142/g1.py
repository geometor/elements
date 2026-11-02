"""Programmatic construction for Book III, Proposition 34 (III.34)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0077.g1 using geometor.model."""
    model = Model("III.34")

    # Circle ABC with center O(97, -95), radius 67 (y-inverted)
    O = model.set_point(97.0, -95.0, ID="O")
    B = model.set_point(30.0, -95.0, classes=["given"], ID="B")
    C = model.set_point(86.0, -28.91, ID="C")
    A = model.set_point(138.0, -148.0, ID="A")
    F = model.set_point(30.0, -28.0, ID="F")
    E = model.set_point(30.0, -158.0, ID="E")

    # Given angle at D
    D = model.set_point(233.0, -138.0, classes=["given"], ID="D")
    D1 = model.set_point(301.0, -138.0, ID="D1")
    D2 = model.set_point(289.0, -92.0, ID="D2")
    model.set_segment(D, D1)
    model.set_segment(D, D2)
    model.set_wedge(D, D1, D1, D2)

    # Construction circle ABC
    model.construct_circle(O, B)

    # Segments
    model.set_segment(E, F)
    model.set_segment(F, B)
    model.set_segment(B, E)
    model.set_segment(B, C)
    model.set_segment(B, A)
    model.set_segment(C, A)

    # Section
    model.set_section([E, B, F])

    # Polygon
    model.set_polygon([A, B, C])

    # Angles
    model.set_wedge(B, F, F, C)
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    construct_g1()
