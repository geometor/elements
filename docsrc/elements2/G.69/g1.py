"""Programmatic construction for Book I, I.40 (I.40).

Equal triangles which are on equal bases and on the same side are also in the same parallels.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0351.g1 (I.40) using geometor.model."""
    model = Model("I.40")

    # 1. Points
    A = model.set_point(31, -34, classes=["given"], ID="A")
    B = model.set_point(31, -105, classes=["given"], ID="B")
    C = model.set_point(111, -105, classes=["given"], ID="C")
    D = model.set_point(167, -34, classes=["given"], ID="D")
    E = model.set_point(191, -105, classes=["given"], ID="E")
    F = model.set_point(156, -48, ID="F")

    # 3. Segments
    model.set_segment(B, E)
    model.set_segment(B, C)
    model.set_segment(C, E)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(D, E)
    model.set_segment(A, F)
    model.set_segment(F, E)

    # 4. Collinear Sections
    model.set_section([B, C, E])
    model.set_section([C, F, D])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([C, D, E])
    model.set_polygon([F, C, E])

    return model


if __name__ == "__main__":
    construct_g1()
