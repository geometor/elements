"""Programmatic construction for Book VII, Proposition 28 (VII.28)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0335.g1 using geometor.model."""
    model = Model("VII.28")

    # Horizontal number segment AC divided at B
    A = model.set_point(10.0, -12.0, classes=["given"], ID="A")
    B = model.set_point(138.0, -12.0, classes=["given"], ID="B")
    C = model.set_point(197.0, -12.0, classes=["given"], ID="C")

    # Single-letter horizontal number segment D
    D_l = model.set_point(9.0, -43.0, classes=["given"], ID="D")
    D_r = model.set_point(66.0, -43.0, ID="D_r")

    # Base line AC
    model.construct_line(A, C)

    # Whole and subdivided segments on AC
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)

    # Single-letter segment D
    model.set_segment(D_l, D_r)

    # Collinear section ABC
    model.set_section([A, B, C])

    return model


if __name__ == "__main__":
    construct_g1()
