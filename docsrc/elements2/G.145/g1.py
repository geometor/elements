"""Programmatic construction for Book III, Proposition 37 (III.37)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0082.g1 using geometor.model."""
    model = Model("III.37")

    # Circle ABC with center F(156, -84), radius 52 (y-inverted)
    F = model.set_point(156.0, -84.0, ID="F")
    E = model.set_point(156.0, -32.0, ID="E")
    D = model.set_point(24.0, -32.0, classes=["given"], ID="D")
    B = model.set_point(120.54, -122.02, classes=["given"], ID="B")
    C = model.set_point(104.08, -81.19, ID="C")
    A = model.set_point(181.97, -129.04, ID="A")

    # Circle ABC
    model.construct_circle(F, E)

    # Segments
    model.set_segment(D, E)
    model.set_segment(D, B)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(F, E)
    model.set_segment(F, B)
    model.set_segment(F, D)

    # Section
    model.set_section([D, C, A])

    # Polygons
    model.set_polygon([F, E, D])
    model.set_polygon([F, B, D])

    # Angles
    model.set_wedge(E, F, F, D)
    model.set_wedge(B, D, D, F)

    return model


if __name__ == "__main__":
    construct_g1()
