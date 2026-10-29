"""Programmatic construction for Book VIII, Proposition 6 (VIII.6)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0361.g1 using geometor.model."""
    model = Model("VIII.6")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H
    A_l = model.set_point(30.0, -15.0, classes=["given"], ID="A")
    A_r = model.set_point(92.0, -15.0, ID="A_r")

    B_l = model.set_point(31.0, -39.0, classes=["given"], ID="B")
    B_r = model.set_point(124.0, -39.0, ID="B_r")

    C_l = model.set_point(29.0, -59.0, classes=["given"], ID="C")
    C_r = model.set_point(167.0, -59.0, ID="C_r")

    D_l = model.set_point(28.0, -89.0, classes=["given"], ID="D")
    D_r = model.set_point(243.0, -89.0, ID="D_r")

    E_l = model.set_point(27.0, -117.0, classes=["given"], ID="E")
    E_r = model.set_point(353.0, -117.0, ID="E_r")

    F_l = model.set_point(29.0, -141.0, classes=["given"], ID="F")
    F_r = model.set_point(59.0, -141.0, ID="F_r")

    G_l = model.set_point(26.0, -161.0, classes=["given"], ID="G")
    G_r = model.set_point(78.0, -161.0, ID="G_r")

    H_l = model.set_point(27.0, -179.0, classes=["given"], ID="H")
    H_r = model.set_point(98.0, -179.0, ID="H_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)

    return model


if __name__ == "__main__":
    construct_g1()
