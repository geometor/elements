"""Programmatic construction for Book III, Proposition 36 Case 2 (III.36 - g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_g2() -> Model:
    """Construct the figure 0080.g2 using geometor.model."""
    model = Model("III.36.g2")

    # Circle ABC with center E(138, -70), radius 54 (y-inverted)
    E = model.set_point(138.0, -70.0, ID="E")
    B = model.set_point(138.0, -124.0, classes=["given"], ID="B")
    D = model.set_point(24.0, -128.33, classes=["given"], ID="D")
    C = model.set_point(104.66, -112.47, ID="C")
    F = model.set_point(144.80, -104.58, ID="F")
    A = model.set_point(184.94, -96.69, ID="A")

    # Circle ABC
    model.construct_circle(E, B)

    # Segments
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(A, F)
    model.set_segment(F, C)
    model.set_segment(C, D)
    model.set_segment(F, D)
    model.set_segment(D, B)
    model.set_segment(E, B)
    model.set_segment(E, F)
    model.set_segment(E, C)
    model.set_segment(E, D)

    # Sections
    model.set_section([D, C, A])
    model.set_section([D, C, F])
    model.set_section([C, F, A])
    model.set_section([D, F, A])

    # Polygons
    model.set_polygon([E, B, D])
    model.set_polygon([E, F, C])
    model.set_polygon([E, F, D])

    # Angles
    model.set_wedge(B, E, E, D)
    model.set_wedge(F, E, E, C)

    return model


if __name__ == "__main__":
    construct_g2()
