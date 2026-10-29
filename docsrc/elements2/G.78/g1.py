"""Programmatic construction for Book III, Proposition 3 (III.3)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0016.g1 using geometor.model."""
    model = Model("III.3")

    # Points (y-inverted for standard mathematical coordinates)
    E = model.set_point(93, -104, ID="E")
    C = model.set_point(93, -28, classes=["given"], ID="C")
    D = model.set_point(93, -180, classes=["given"], ID="D")
    F = model.set_point(93, -140, ID="F")
    A = model.set_point(26.07, -140, classes=["given"], ID="A")
    B = model.set_point(159.93, -140, classes=["given"], ID="B")

    # Construction circle ABC
    model.construct_circle(E, C)

    # Segments
    model.set_segment(C, D)
    model.set_segment(A, B)
    model.set_segment(E, A)
    model.set_segment(E, B)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(F, E)
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    # Sections
    model.set_section([A, F, B])
    model.set_section([C, E, D])
    model.set_section([C, F, D])

    # Polygons
    model.set_polygon([E, A, F])
    model.set_polygon([E, B, F])
    model.set_polygon([E, A, B])

    # Angles (wedges)
    model.set_wedge(F, A, A, E)
    model.set_wedge(F, E, E, B)
    model.set_wedge(A, E, E, F)
    model.set_wedge(B, F, F, E)

    return model


if __name__ == "__main__":
    construct_g1()
