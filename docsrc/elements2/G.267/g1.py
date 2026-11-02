"""Programmatic construction for Book VII, Proposition 14 (VII.14)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0319.g2 using geometor.model."""
    model = Model("VII.14")

    # Left column: single-letter horizontal number segments A, B, C
    A_l = model.set_point(8.0, -42.0, classes=["given"], ID="A")
    A_r = model.set_point(132.0, -42.0, ID="A_r")

    B_l = model.set_point(12.0, -66.0, classes=["given"], ID="B")
    B_r = model.set_point(107.0, -66.0, ID="B_r")

    C_l = model.set_point(12.0, -89.0, classes=["given"], ID="C")
    C_r = model.set_point(90.0, -89.0, ID="C_r")

    # Right column: single-letter horizontal number segments D, E, F
    D_l = model.set_point(181.0, -37.0, classes=["given"], ID="D")
    D_r = model.set_point(322.0, -37.0, ID="D_r")

    E_l = model.set_point(182.0, -60.0, classes=["given"], ID="E")
    E_r = model.set_point(296.0, -60.0, ID="E_r")

    F_l = model.set_point(183.0, -89.0, classes=["given"], ID="F")
    F_r = model.set_point(274.0, -89.0, ID="F_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_g1()
