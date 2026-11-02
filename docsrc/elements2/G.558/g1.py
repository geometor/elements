"""Programmatic construction for Book XII, Proposition 7 (XII.7)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0398.g1 using geometor.model."""
    model = Model("XII.7")

    # Points of the triangular prism ABC-DEF
    A = model.set_point(191.0, -175.0, classes=["given"], ID="A")
    B = model.set_point(62.0, -175.0, classes=["given"], ID="B")
    C = model.set_point(139.0, -140.0, classes=["given"], ID="C")
    D = model.set_point(152.0, -62.0, classes=["given"], ID="D")
    E = model.set_point(21.0, -62.0, classes=["given"], ID="E")
    F = model.set_point(98.0, -21.0, classes=["given"], ID="F")

    # Prism edges
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, D)
    model.set_segment(A, D)
    model.set_segment(B, E)
    model.set_segment(C, F)

    # Joined diagonals
    model.set_segment(B, D)
    model.set_segment(E, C)
    model.set_segment(C, D)

    # Polygons (bases, parallelogram faces, and divided triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([A, B, E, D])
    model.set_polygon([F, C, B, E])
    model.set_polygon([A, B, D])
    model.set_polygon([E, B, D])
    model.set_polygon([E, B, C])
    model.set_polygon([C, E, F])

    return model


if __name__ == "__main__":
    construct_g1()
