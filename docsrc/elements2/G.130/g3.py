"""Programmatic construction for Book III, Proposition 25 Case 3 (III.25 - g3)."""

from __future__ import annotations

from geometor.model import Model


def construct_g3() -> Model:
    """Construct the figure 0062.g1 using geometor.model."""
    model = Model("III.25.g3")

    # Points (y-inverted)
    E = model.set_point(83.00, -72.00, ID="E")
    D = model.set_point(110.00, -72.00, ID="D")
    A = model.set_point(110.00, -24.00, classes=["given"], ID="A")
    C = model.set_point(110.00, -120.00, classes=["given"], ID="C")
    B = model.set_point(27.93, -72.00, classes=["given"], ID="B")

    # Circle for segment ABC
    model.construct_circle(E, A)

    # Segments and sections
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(E, D)
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_section([A, D, C])
    model.set_section([B, E, D])

    # Polygons
    model.set_polygon([A, B, D])
    model.set_polygon([A, B, E])
    model.set_polygon([A, E, D])

    # Angles (wedges)
    model.set_wedge(B, A, A, D)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, B, B, E)

    return model


if __name__ == "__main__":
    construct_g3()
