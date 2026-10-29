"""Programmatic construction for Book IX, Proposition 18 (IX.18)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0414.g1 using geometor.model."""
    model = Model("IX.18")

    # Left column: single-letter horizontal number segments A, B
    A_l = model.set_point(27.0, -20.0, classes=["given"], ID="A")
    A_r = model.set_point(76.0, -20.0, ID="A_r")

    B_l = model.set_point(28.0, -47.5, classes=["given"], ID="B")
    B_r = model.set_point(92.0, -47.5, ID="B_r")

    # Right column: single-letter horizontal number segments D, C
    D_l = model.set_point(179.0, -25.5, classes=["given"], ID="D")
    D_r = model.set_point(261.0, -25.5, ID="D_r")

    C_l = model.set_point(145.0, -54.0, classes=["given"], ID="C")
    C_r = model.set_point(390.0, -54.0, ID="C_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(D_l, D_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_g1()
