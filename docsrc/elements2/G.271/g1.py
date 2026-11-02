"""Programmatic construction for Book VII, Proposition 17 (VII.17)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0323.g1 using geometor.model."""
    model = Model("VII.17")

    # Single-letter horizontal number segments A, B, C, D, E, F
    A_l = model.set_point(48.0, -16.0, classes=["given"], ID="A")
    A_r = model.set_point(123.0, -16.0, ID="A_r")

    B_l = model.set_point(30.0, -39.0, classes=["given"], ID="B")
    B_r = model.set_point(133.0, -39.0, ID="B_r")

    C_l = model.set_point(201.0, -39.0, classes=["given"], ID="C")
    C_r = model.set_point(328.0, -39.0, ID="C_r")

    D_l = model.set_point(19.0, -65.0, classes=["given"], ID="D")
    D_r = model.set_point(158.0, -65.0, ID="D_r")

    E_l = model.set_point(196.0, -65.0, classes=["given"], ID="E")
    E_r = model.set_point(374.0, -65.0, ID="E_r")

    F_l = model.set_point(54.0, -90.0, classes=["given"], ID="F")
    F_r = model.set_point(79.0, -90.0, ID="F_r")

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
