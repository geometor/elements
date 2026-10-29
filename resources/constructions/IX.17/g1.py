"""Programmatic construction for Book IX, Proposition 17 (IX.17)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0412.g2 using geometor.model."""
    model = Model("IX.17")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(32.0, -22.0, classes=["given"], ID="A")
    A_r = model.set_point(69.0, -22.0, ID="A_r")

    B_l = model.set_point(124.0, -23.5, classes=["given"], ID="B")
    B_r = model.set_point(178.0, -23.5, ID="B_r")

    C_l = model.set_point(34.0, -49.5, classes=["given"], ID="C")
    C_r = model.set_point(115.0, -49.5, ID="C_r")

    D_l = model.set_point(33.0, -70.0, classes=["given"], ID="D")
    D_r = model.set_point(159.0, -70.0, ID="D_r")

    E_l = model.set_point(36.0, -94.5, classes=["given"], ID="E")
    E_r = model.set_point(226.0, -94.5, ID="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
