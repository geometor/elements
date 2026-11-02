"""Programmatic construction for Book I, Proposition 19 (I.19).

In any triangle the greater angle is subtended by the greater side.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0298.g1 (I.19) using geometor.model."""
    model = Model("I.19")

    # Points
    pt_A = model.set_point(75, -18.5, classes=["given"], ID="A")
    pt_B = model.set_point(22, -54, classes=["given"], ID="B")
    pt_C = model.set_point(75, -115, classes=["given"], ID="C")

    # Segments
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_B, pt_C)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_B, pt_A, pt_A, pt_C)
    model.set_wedge(pt_C, pt_A, pt_A, pt_B)

    return model


if __name__ == "__main__":
    construct_g1()
