"""Programmatic construction for Book I, Proposition 48 (I.48).

Converse of the Pythagorean Theorem: if the square on BC equals the sum of the
squares on BA and AC, then angle BAC is right.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct Book I, Proposition 48 figure (I.48) using geometor.model."""
    model = Model("I.48")

    A = model.set_point(71.5, -147, classes=["given"], ID="A")
    B = model.set_point(123, -147, classes=["given"], ID="B")
    C = model.set_point(71.5, -23, classes=["given"], ID="C")
    D = model.set_point(20, -147, ID="D")

    # Classical construction: line AD perpendicular to AC at A, circle (A, B) giving D, join DC
    L_AC = model.construct_line(A, C)
    model.construct_line(A, D)
    model.construct_circle(A, B)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, C])

    # Segments
    for p1, p2 in [(A, B), (A, C), (B, C), (A, D), (D, C)]:
        model.set_segment(p1, p2)

    # Angles
    model.set_wedge(A, B, B, C)  # < B A C )
    model.set_wedge(A, D, D, C)  # < D A C )

    return model


if __name__ == "__main__":
    construct_g1()
