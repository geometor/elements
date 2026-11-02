"""Programmatic construction for Book VI, Proposition 31 (VI.31).

In right-angled triangles the figure on the side subtending the right angle is equal
to the similar and similarly described figures on the sides containing the right angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0275.g1 (VI.31) using geometor.model."""
    model = Model("VI.31")

    # 1. Vertices of right-angled triangle ABC and altitude foot D
    A = model.set_point(85.0, -65.0, classes=["given"], ID="A")
    B = model.set_point(46.0, -139.0, classes=["given"], ID="B")
    C = model.set_point(221.0, -139.0, classes=["given"], ID="C")
    D = model.set_point(85.0, -139.0, ID="D")

    # Outer vertices of the three similar rectangles on BC, BA, AC
    B1 = model.set_point(46.0, -202.0, ID="B1")
    C1 = model.set_point(221.0, -202.0, ID="C1")
    B2 = model.set_point(17.0, -124.0, ID="B2")
    A2 = model.set_point(56.0, -50.0, ID="A2")
    A3 = model.set_point(111.0, -16.0, ID="A3")
    C3 = model.set_point(246.0, -90.0, ID="C3")

    # 2. Construction Lines
    model.construct_line(B, C)
    model.construct_line(A, D)

    # 3. Segments of triangle ABC and altitude AD
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, D)

    # Segments of similar figures on BC, BA, AC
    model.set_segment(B, B1)
    model.set_segment(B1, C1)
    model.set_segment(C1, C)

    model.set_segment(B, B2)
    model.set_segment(B2, A2)
    model.set_segment(A2, A)

    model.set_segment(A, A3)
    model.set_segment(A3, C3)
    model.set_segment(C3, C)

    # 4. Collinear Section along hypotenuse BC
    model.set_section([B, D, C])

    # 5. Polygons (Triangles and similar figures on the three sides)
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([B, C, C1, B1])
    model.set_polygon([B, A, A2, B2])
    model.set_polygon([A, C, C3, A3])

    # 6. Angles (Wedges)
    model.set_wedge(A, C, C, B)  # Right angle BAC

    return model


if __name__ == "__main__":
    construct_g1()
