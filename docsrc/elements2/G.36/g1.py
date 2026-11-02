"""Programmatic construction for Book I, Proposition 13 (I.13)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0289.g1 using geometor.model."""
    model = Model("I.13")

    # Points
    C = model.set_point(28, -96.5, classes=["given"], ID="C")
    B = model.set_point(114, -96.5, classes=["given"], ID="B")
    D = model.set_point(196, -96.5, classes=["given"], ID="D")
    E = model.set_point(114, -30, ID="E")
    A = model.set_point(147.5, -30, classes=["given"], ID="A")

    # Construction lines
    model.construct_line(C, D)
    model.construct_line(B, A)
    model.construct_line(B, E)

    # Segments
    model.set_segment(C, D)
    model.set_segment(B, E)
    model.set_segment(B, A)
    model.set_segment(C, B)
    model.set_segment(B, D)

    # Collinear / broken sections
    model.set_section([C, B, D])

    # Polygons
    model.set_polygon([C, B, E])
    model.set_polygon([E, B, A])
    model.set_polygon([A, B, D])

    # Angles (wedges)
    model.set_wedge(B, C, C, A)
    model.set_wedge(B, A, A, D)
    model.set_wedge(B, C, C, E)
    model.set_wedge(B, E, E, D)
    model.set_wedge(B, A, A, E)

    return model


if __name__ == "__main__":
    construct_g1()
