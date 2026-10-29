"""Programmatic construction for Book IX, Proposition 13 (IX.13)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0405.g1 using geometor.model."""
    model = Model("IX.13")

    # Left column: single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(31.0, -23.5, classes=["given"], ID="A")
    A_r = model.set_point(110.0, -23.5, ID="A_r")

    B_l = model.set_point(34.0, -45.5, classes=["given"], ID="B")
    B_r = model.set_point(129.0, -45.5, ID="B_r")

    C_l = model.set_point(30.0, -71.5, classes=["given"], ID="C")
    C_r = model.set_point(165.0, -71.5, ID="C_r")

    D_l = model.set_point(31.0, -95.0, classes=["given"], ID="D")
    D_r = model.set_point(206.0, -95.0, ID="D_r")

    # Right column: single-letter horizontal number segments E, F, G, H
    E_l = model.set_point(265.0, -23.5, classes=["given"], ID="E")
    E_r = model.set_point(306.0, -23.5, ID="E_r")

    F_l = model.set_point(265.0, -45.5, classes=["given"], ID="F")
    F_r = model.set_point(390.0, -45.5, ID="F_r")

    G_l = model.set_point(265.0, -71.5, classes=["given"], ID="G")
    G_r = model.set_point(322.0, -71.5, ID="G_r")

    H_l = model.set_point(273.0, -95.5, classes=["given"], ID="H")
    H_r = model.set_point(350.0, -95.5, ID="H_r")

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
