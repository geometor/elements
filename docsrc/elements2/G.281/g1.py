"""Programmatic construction for Book IX, Proposition 11 (IX.11)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0402.g1 using geometor.model."""
    model = Model("IX.11")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(34.0, -22.5, classes=["given"], ID="A")
    A_r = model.set_point(73.0, -22.5, ID="A_r")

    B_l = model.set_point(32.0, -47.5, classes=["given"], ID="B")
    B_r = model.set_point(84.0, -47.5, ID="B_r")

    C_l = model.set_point(34.0, -69.5, classes=["given"], ID="C")
    C_r = model.set_point(110.0, -69.5, ID="C_r")

    D_l = model.set_point(35.0, -89.5, classes=["given"], ID="D")
    D_r = model.set_point(134.0, -89.5, ID="D_r")

    E_l = model.set_point(31.0, -112.0, classes=["given"], ID="E")
    E_r = model.set_point(169.0, -112.0, ID="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
