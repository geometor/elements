"""Programmatic construction for Book VI, Proposition 4 (VI.4).

In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0207.g1 (VI.4) using geometor.model."""
    model = Model("VI.4")

    # 1. Points
    A = model.set_point(147, -74, classes=["given"], ID="A")
    B = model.set_point(19, -171, classes=["given"], ID="B")
    C = model.set_point(168, -171, classes=["given"], ID="C")
    D = model.set_point(235.87, -119.57, classes=["given"], ID="D")
    E = model.set_point(247, -171, classes=["given"], ID="E")
    F = model.set_point(214.87, -22.57, ID="F")

    # 2. Construction Lines
    model.construct_line(B, E)
    model.construct_line(B, F)
    model.construct_line(E, F)

    # 3. Segments
    model.set_segment(B, A)
    model.set_segment(A, F)
    model.set_segment(B, F)
    model.set_segment(B, C)
    model.set_segment(C, E)
    model.set_segment(B, E)
    model.set_segment(F, D)
    model.set_segment(D, E)
    model.set_segment(F, E)
    model.set_segment(A, C)
    model.set_segment(C, D)

    # 4. Collinear Sections
    model.set_section([B, A, F])
    model.set_section([B, C, E])
    model.set_section([F, D, E])

    # 5. Polygons (Triangles and Parallelogram)
    model.set_polygon([A, B, C])
    model.set_polygon([D, C, E])
    model.set_polygon([F, B, E])
    model.set_polygon([F, A, C, D])

    # 6. Angles (Wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(A, B, B, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(C, D, D, E)
    model.set_wedge(D, C, C, E)
    model.set_wedge(E, C, C, D)

    return model


if __name__ == "__main__":
    construct_g1()
