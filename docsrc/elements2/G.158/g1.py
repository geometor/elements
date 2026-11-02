"""Programmatic construction for Book IV, Proposition 6 (IV.6)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0097.g1 using geometor.model."""
    model = Model("IV.6")

    # Points (y-inverted for standard mathematical coordinates)
    E = model.set_point(99.00, -99.00, ID="E")
    A = model.set_point(99.00, -28.00, classes=["given"], ID="A")
    B = model.set_point(28.00, -99.00, ID="B")
    C = model.set_point(99.00, -170.00, ID="C")
    D = model.set_point(170.00, -99.00, ID="D")

    # Circle ABCD
    model.construct_circle(E, A)

    # Construction lines (diameters)
    model.construct_line(A, C)
    model.construct_line(B, D)

    # Segments
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(B, E)
    model.set_segment(E, D)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)

    # Collinear sections
    model.set_section([A, E, C])
    model.set_section([B, E, D])

    # Polygons
    model.set_polygon([A, B, C, D])

    # Angles (wedges)
    model.set_wedge(A, B, B, D)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, B, B, D)
    model.set_wedge(D, C, C, A)

    return model


if __name__ == "__main__":
    construct_g1()
