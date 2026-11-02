"""Programmatic construction for Book X, Proposition 33 (X.33)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0079.g1 using geometor.model."""
    model = Model("X.33")

    # Diameter AB extended to C, with D bisecting BC, E on AB, and F on semicircle AFB
    A = model.set_point(19.0, -102.0, classes=["given"], ID="A")
    E = model.set_point(172.0, -102.0, ID="E")
    B = model.set_point(187.0, -102.0, classes=["given"], ID="B")
    D = model.set_point(232.5, -102.0, ID="D")
    C = model.set_point(278.0, -102.0, classes=["given"], ID="C")
    O = model.set_point(103.0, -102.0, ID="O")
    F = model.set_point(172.0, -54.1, ID="F")

    # Base lines and semicircle AFB
    model.construct_line(A, C)
    model.construct_circle(O, A)
    model.construct_line(A, F)
    model.construct_line(F, B)
    model.construct_line(E, F)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(E, F)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(E, C)
    model.set_segment(E, D)

    # Sections
    model.set_section([A, E, B])
    model.set_section([B, D, C])
    model.set_section([A, B, C])

    # Inscribed right triangles AFB, AFE, FEB
    model.set_polygon([A, F, B])
    model.set_polygon([A, F, E])
    model.set_polygon([F, E, B])

    # Right angles at F and E
    model.set_wedge(F, A, A, B)
    model.set_wedge(E, F, A, F)
    model.set_wedge(E, F, F, B)

    return model


if __name__ == "__main__":
    construct_g1()
