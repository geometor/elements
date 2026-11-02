"""Programmatic construction for Book III, Proposition 7 (III.7)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0020.g1 using geometor.model."""
    model = Model("III.7")

    # Points (y-inverted for standard mathematical coordinates)
    E = model.set_point(106, -98, ID="E")
    A = model.set_point(25, -98, classes=["given"], ID="A")
    D = model.set_point(187, -98, classes=["given"], ID="D")
    F = model.set_point(156, -98, classes=["given"], ID="F")
    B = model.set_point(33.94, -61, classes=["given"], ID="B")
    C = model.set_point(65.24, -28, classes=["given"], ID="C")
    G = model.set_point(175.26, -56, classes=["given"], ID="G")
    H = model.set_point(175.26, -140, ID="H")
    K = model.set_point(160.42, -158, ID="K")

    # Construction circle ABCD
    model.construct_circle(E, A)

    # Segments
    model.set_segment(A, D)
    model.set_segment(F, A)
    model.set_segment(F, D)
    model.set_segment(A, E)
    model.set_segment(E, D)
    model.set_segment(E, F)
    model.set_segment(F, B)
    model.set_segment(F, C)
    model.set_segment(F, G)
    model.set_segment(F, H)
    model.set_segment(F, K)
    model.set_segment(E, B)
    model.set_segment(E, C)
    model.set_segment(E, G)
    model.set_segment(E, H)
    model.set_segment(E, K)

    # Sections
    model.set_section([A, E, D])
    model.set_section([A, F, D])
    model.set_section([E, F, D])
    model.set_section([B, E, F])
    model.set_section([C, E, F])
    model.set_section([G, F, E])
    model.set_section([H, E, F])

    # Polygons
    model.set_polygon([B, E, F])
    model.set_polygon([C, E, F])
    model.set_polygon([G, E, F])
    model.set_polygon([H, E, F])

    # Angles (wedges)
    model.set_wedge(E, B, B, F)
    model.set_wedge(E, C, C, F)
    model.set_wedge(E, G, G, F)
    model.set_wedge(E, F, F, H)
    model.set_wedge(F, B, B, D)
    model.set_wedge(F, C, C, D)

    return model


if __name__ == "__main__":
    construct_g1()
