"""Programmatic construction for Book VIII, Proposition 26 (VIII.26)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0387.g2 using geometor.model."""
    model = Model("VIII.26")

    # Single-letter horizontal number segments A, B, C, D, E, F
    A_l = model.set_point(25.0, -14.0, classes=["given"], ID="A")
    A_r = model.set_point(95.0, -14.0, ID="A_r")

    B_l = model.set_point(144.0, -14.0, classes=["given"], ID="B")
    B_r = model.set_point(431.0, -14.0, ID="B_r")

    C_l = model.set_point(112.0, -44.0, classes=["given"], ID="C")
    C_r = model.set_point(253.0, -44.0, ID="C_r")

    D_l = model.set_point(19.0, -68.0, classes=["given"], ID="D")
    D_r = model.set_point(58.0, -68.0, ID="D_r")

    E_l = model.set_point(114.0, -68.0, classes=["given"], ID="E")
    E_r = model.set_point(181.0, -68.0, ID="E_r")

    F_l = model.set_point(243.0, -68.0, classes=["given"], ID="F")
    F_r = model.set_point(388.0, -68.0, ID="F_r")

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
