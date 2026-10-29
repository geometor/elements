"""Programmatic construction for Book VIII, Proposition 14 (VIII.14)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0373.g1 using geometor.model."""
    model = Model("VIII.14")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(25.0, -15.0, classes=["given"], ID="A")
    A_r = model.set_point(62.0, -15.0, ID="A_r")

    B_l = model.set_point(25.0, -39.0, classes=["given"], ID="B")
    B_r = model.set_point(148.0, -39.0, ID="B_r")

    C_l = model.set_point(27.0, -62.0, classes=["given"], ID="C")
    C_r = model.set_point(47.0, -62.0, ID="C_r")

    D_l = model.set_point(110.0, -62.0, classes=["given"], ID="D")
    D_r = model.set_point(147.0, -62.0, ID="D_r")

    E_l = model.set_point(61.0, -87.0, classes=["given"], ID="E")
    E_r = model.set_point(125.0, -87.0, ID="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
