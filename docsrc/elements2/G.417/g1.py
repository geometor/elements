"""Programmatic construction for Book X, Proposition 43 (X.43)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0098.g1 using geometor.model."""
    model = Model("X.43")

    # First bimedial straight line AB divided at C and D
    A = model.set_point(16.0, -19.0, classes=["given"], ID="A")
    D = model.set_point(134.0, -19.0, ID="D")
    C = model.set_point(164.0, -19.0, classes=["given"], ID="C")
    B = model.set_point(236.0, -19.0, classes=["given"], ID="B")

    model.construct_line(A, B)

    # Whole and all sub-segments on AB
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(D, C)
    model.set_segment(D, B)
    model.set_segment(C, B)

    # Collinear sections on AB
    model.set_section([A, C, B])
    model.set_section([A, D, B])

    return model


if __name__ == "__main__":
    construct_g1()
