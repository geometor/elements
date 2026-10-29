"""Programmatic construction for Book VIII, Proposition 25 (VIII.25)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0387.g1 using geometor.model."""
    model = Model("VIII.25")

    # Single-letter horizontal number segments A, B, C, D, E, F
    A_l = model.set_point(22.0, -14.0, classes=["given"], ID="A")
    A_r = model.set_point(66.0, -14.0, ID="A_r")

    B_l = model.set_point(21.0, -37.0, classes=["given"], ID="B")
    B_r = model.set_point(153.0, -37.0, ID="B_r")

    C_l = model.set_point(22.0, -58.0, classes=["given"], ID="C")
    C_r = model.set_point(88.0, -58.0, ID="C_r")

    D_l = model.set_point(22.0, -80.0, classes=["given"], ID="D")
    D_r = model.set_point(229.0, -80.0, ID="D_r")

    E_l = model.set_point(290.0, -14.0, classes=["given"], ID="E")
    E_r = model.set_point(356.0, -14.0, ID="E_r")

    F_l = model.set_point(290.0, -37.0, classes=["given"], ID="F")
    F_r = model.set_point(382.0, -37.0, ID="F_r")

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
