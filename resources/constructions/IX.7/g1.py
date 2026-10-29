"""Programmatic construction for Book IX, Proposition 7 (IX.7)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0395.g1 using geometor.model."""
    model = Model("IX.7")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(30.0, -24.0, classes=["given"], ID="A")
    A_r = model.set_point(193.0, -24.0, ID="A_r")

    B_l = model.set_point(30.0, -46.5, classes=["given"], ID="B")
    B_r = model.set_point(102.0, -46.5, ID="B_r")

    C_l = model.set_point(29.0, -71.0, classes=["given"], ID="C")
    C_r = model.set_point(261.0, -71.0, ID="C_r")

    D_l = model.set_point(30.0, -94.5, classes=["given"], ID="D")
    D_r = model.set_point(84.0, -94.5, ID="D_r")

    E_l = model.set_point(146.0, -94.5, classes=["given"], ID="E")
    E_r = model.set_point(300.0, -94.5, ID="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
