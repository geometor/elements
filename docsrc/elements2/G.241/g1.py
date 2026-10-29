"""Programmatic construction for Book VIII, Proposition 1 (VIII.1)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0351.g1 using geometor.model."""
    model = Model("VIII.1")

    # Left column: single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(26.0, -14.0, classes=["given"], ID="A")
    A_r = model.set_point(80.0, -14.0, ID="A_r")

    B_l = model.set_point(26.0, -36.0, classes=["given"], ID="B")
    B_r = model.set_point(104.0, -36.0, ID="B_r")

    C_l = model.set_point(26.0, -58.0, classes=["given"], ID="C")
    C_r = model.set_point(124.0, -58.0, ID="C_r")

    D_l = model.set_point(27.0, -80.0, classes=["given"], ID="D")
    D_r = model.set_point(156.0, -80.0, ID="D_r")

    # Right column: single-letter horizontal number segments E, F, G, H
    E_l = model.set_point(204.0, -14.0, classes=["given"], ID="E")
    E_r = model.set_point(233.0, -14.0, ID="E_r")

    F_l = model.set_point(205.0, -38.0, classes=["given"], ID="F")
    F_r = model.set_point(245.0, -38.0, ID="F_r")

    G_l = model.set_point(204.0, -58.0, classes=["given"], ID="G")
    G_r = model.set_point(253.0, -58.0, ID="G_r")

    H_l = model.set_point(204.0, -82.0, classes=["given"], ID="H")
    H_r = model.set_point(263.0, -82.0, ID="H_r")

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
