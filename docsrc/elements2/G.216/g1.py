"""Programmatic construction for Book VII, Proposition 16 (VII.16)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0322.g1 using geometor.model."""
    model = Model("VII.16")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(22.0, -16.0, classes=["given"], ID="A")
    A_r = model.set_point(105.0, -16.0, ID="A_r")

    B_l = model.set_point(23.0, -39.0, classes=["given"], ID="B")
    B_r = model.set_point(134.0, -39.0, ID="B_r")

    C_l = model.set_point(22.0, -63.0, classes=["given"], ID="C")
    C_r = model.set_point(256.0, -63.0, ID="C_r")

    D_l = model.set_point(21.0, -85.0, classes=["given"], ID="D")
    D_r = model.set_point(278.0, -85.0, ID="D_r")

    E_l = model.set_point(23.0, -111.0, classes=["given"], ID="E")
    E_r = model.set_point(51.0, -111.0, ID="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
