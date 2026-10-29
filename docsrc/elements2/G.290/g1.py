"""Programmatic construction for Book IX, Proposition 19 (IX.19)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0415.g1 using geometor.model."""
    model = Model("IX.19")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(29.0, -21.5, classes=["given"], ID="A")
    A_r = model.set_point(88.0, -21.5, ID="A_r")

    B_l = model.set_point(30.0, -46.5, classes=["given"], ID="B")
    B_r = model.set_point(100.0, -46.5, ID="B_r")

    C_l = model.set_point(30.0, -70.5, classes=["given"], ID="C")
    C_r = model.set_point(136.0, -70.5, ID="C_r")

    D_l = model.set_point(31.0, -89.5, classes=["given"], ID="D")
    D_r = model.set_point(156.0, -89.5, ID="D_r")

    E_l = model.set_point(30.0, -115.0, classes=["given"], ID="E")
    E_r = model.set_point(216.0, -115.0, ID="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
