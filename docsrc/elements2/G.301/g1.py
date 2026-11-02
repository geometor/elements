"""Programmatic construction for Book VIII, Proposition 5 (VIII.5)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0360.g1 using geometor.model."""
    model = Model("VIII.5")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H, K, L
    A_l = model.set_point(23.0, -15.0, classes=["given"], ID="A")
    A_r = model.set_point(154.0, -15.0, ID="A_r")

    B_l = model.set_point(24.0, -40.0, classes=["given"], ID="B")
    B_r = model.set_point(72.0, -40.0, ID="B_r")

    C_l = model.set_point(26.0, -61.0, classes=["given"], ID="C")
    C_r = model.set_point(60.0, -61.0, ID="C_r")

    D_l = model.set_point(131.0, -61.0, classes=["given"], ID="D")
    D_r = model.set_point(171.0, -61.0, ID="D_r")

    E_l = model.set_point(26.0, -83.0, classes=["given"], ID="E")
    E_r = model.set_point(48.0, -83.0, ID="E_r")

    F_l = model.set_point(129.0, -83.0, classes=["given"], ID="F")
    F_r = model.set_point(155.0, -83.0, ID="F_r")

    G_l = model.set_point(27.0, -107.0, classes=["given"], ID="G")
    G_r = model.set_point(183.0, -107.0, ID="G_r")

    H_l = model.set_point(28.0, -129.0, classes=["given"], ID="H")
    H_r = model.set_point(107.0, -129.0, ID="H_r")

    K_l = model.set_point(28.0, -153.0, classes=["given"], ID="K")
    K_r = model.set_point(76.0, -153.0, ID="K_r")

    L_l = model.set_point(27.0, -179.0, classes=["given"], ID="L")
    L_r = model.set_point(107.0, -179.0, ID="L_r")

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
    model.set_segment(L_l, L_r)

    return model


if __name__ == "__main__":
    construct_g1()
