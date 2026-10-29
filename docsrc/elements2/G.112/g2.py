"""Programmatic construction for Book III, Proposition 33 — Right Angle Case (III.33 - g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_g2() -> Model:
    """Construct the figure 0074.g1 using geometor.model."""
    model = Model("III.33.g2")

    # Given right angle at C (y-inverted)
    C = model.set_point(88.0, -105.0, classes=["given"], ID="C")
    C1 = model.set_point(18.0, -105.0, ID="C1")
    C2 = model.set_point(88.0, -55.0, ID="C2")
    model.set_segment(C, C1)
    model.set_segment(C, C2)
    model.set_wedge(C, C1, C1, C2)

    # Circle AEB with center F(212, -105), radius 75
    F = model.set_point(212.0, -105.0, ID="F")
    A = model.set_point(212.0, -30.0, classes=["given"], ID="A")
    B = model.set_point(212.0, -180.0, classes=["given"], ID="B")
    E = model.set_point(137.54, -114.0, ID="E")
    D = model.set_point(135.0, -30.0, ID="D")
    D2 = model.set_point(295.0, -30.0, ID="D2")

    # Construction circle AEB
    model.construct_circle(F, A)

    # Segments
    model.set_segment(D, D2)
    model.set_segment(A, D)
    model.set_segment(A, B)
    model.set_segment(F, A)
    model.set_segment(F, B)
    model.set_segment(A, E)
    model.set_segment(E, B)

    # Section
    model.set_section([A, F, B])

    # Polygon
    model.set_polygon([A, E, B])

    # Angles
    model.set_wedge(A, D, D, B)
    model.set_wedge(E, A, A, B)

    return model


if __name__ == "__main__":
    construct_g2()
