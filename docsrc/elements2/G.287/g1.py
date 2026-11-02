"""Programmatic construction for Book VII, Proposition 31 (VII.31)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0338.g1 using geometor.model."""
    model = Model("VII.31")

    # Single-letter horizontal number segments A, B, C
    A_l = model.set_point(23.0, -12.0, classes=["given"], ID="A")
    A_r = model.set_point(174.0, -12.0, ID="A_r")

    B_l = model.set_point(24.0, -37.0, classes=["given"], ID="B")
    B_r = model.set_point(135.0, -37.0, ID="B_r")

    C_l = model.set_point(24.0, -61.0, classes=["given"], ID="C")
    C_r = model.set_point(79.0, -61.0, ID="C_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_g1()
