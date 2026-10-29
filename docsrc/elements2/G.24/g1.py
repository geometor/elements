"""Programmatic construction for Book I, Proposition 14 (I.14)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0290.g1 using geometor.model."""
    model = Model("I.14")

    # Points
    C = model.set_point(5, -79.5, classes=["given"], ID="C")
    B = model.set_point(87, -79.5, classes=["given"], ID="B")
    D = model.set_point(168, -79.5, classes=["given"], ID="D")
    A = model.set_point(58, -22, classes=["given"], ID="A")
    E = model.set_point(150, -18, ID="E")

    # Construction lines
    model.construct_line(C, D)
    model.construct_line(A, B)
    model.construct_line(B, E)

    # Segments
    model.set_segment(C, D)
    model.set_segment(A, B)
    model.set_segment(B, E)
    model.set_segment(B, C)
    model.set_segment(B, D)

    # Collinear / broken sections
    model.set_section([C, B, D])
    model.set_section([C, B, E])

    # Polygons
    model.set_polygon([C, B, A])
    model.set_polygon([A, B, E])
    model.set_polygon([E, B, D])

    # Angles (wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, A, A, D)
    model.set_wedge(B, A, A, E)
    model.set_wedge(B, E, E, D)

    return model


if __name__ == "__main__":
    construct_g1()
