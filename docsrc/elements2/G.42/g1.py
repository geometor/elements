"""Programmatic construction for Book I, Proposition 17 (I.17)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0296.g1 using geometor.model."""
    model = Model("I.17")

    # Points
    A = model.set_point(44, -35, classes=["given"], ID="A")
    B = model.set_point(88, -116.5, classes=["given"], ID="B")
    C = model.set_point(191, -116.5, classes=["given"], ID="C")
    D = model.set_point(305, -116.5, ID="D")

    # Construction lines
    model.construct_line(B, D)

    # Segments
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(C, D)

    # Collinear / broken sections
    model.set_section([B, C, D])

    # Polygons
    model.set_polygon([A, B, C])

    # Angles (wedges)
    model.set_wedge(C, A, A, D)
    model.set_wedge(C, A, A, B)
    model.set_wedge(B, A, A, C)
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    construct_g1()
