"""Programmatic construction for Book VIII, Proposition 2 (VIII.2)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0352.g1 using geometor.model."""
    model = Model("VIII.2")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H, K
    A_l = model.set_point(29.0, -15.0, classes=["given"], ID="A")
    A_r = model.set_point(71.0, -15.0, ID="A_r")

    C_l = model.set_point(120.0, -15.0, classes=["given"], ID="C")
    C_r = model.set_point(180.0, -15.0, ID="C_r")

    B_l = model.set_point(27.0, -45.0, classes=["given"], ID="B")
    B_r = model.set_point(81.0, -45.0, ID="B_r")

    D_l = model.set_point(120.0, -45.0, classes=["given"], ID="D")
    D_r = model.set_point(202.0, -45.0, ID="D_r")

    E_l = model.set_point(48.0, -72.0, classes=["given"], ID="E")
    E_r = model.set_point(161.0, -72.0, ID="E_r")

    F_l = model.set_point(38.0, -100.0, classes=["given"], ID="F")
    F_r = model.set_point(140.0, -100.0, ID="F_r")

    G_l = model.set_point(178.0, -100.0, classes=["given"], ID="G")
    G_r = model.set_point(304.0, -100.0, ID="G_r")

    H_l = model.set_point(55.0, -126.0, classes=["given"], ID="H")
    H_r = model.set_point(240.0, -126.0, ID="H_r")

    K_l = model.set_point(64.0, -154.0, classes=["given"], ID="K")
    K_r = model.set_point(224.0, -154.0, ID="K_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)

    return model


if __name__ == "__main__":
    construct_g1()
