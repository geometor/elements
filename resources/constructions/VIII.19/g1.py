"""Programmatic construction for Book VIII, Proposition 19 (VIII.19)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0379.g1 using geometor.model."""
    model = Model("VIII.19")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H, K, L, M, N, O
    A_l = model.set_point(24.0, -15.0, classes=["given"], ID="A")
    A_r = model.set_point(63.0, -15.0, ID="A_r")

    B_l = model.set_point(25.0, -37.0, classes=["given"], ID="B")
    B_r = model.set_point(312.0, -37.0, ID="B_r")

    C_l = model.set_point(25.0, -59.0, classes=["given"], ID="C")
    C_r = model.set_point(42.0, -59.0, ID="C_r")

    D_l = model.set_point(25.0, -81.0, classes=["given"], ID="D")
    D_r = model.set_point(45.0, -81.0, ID="D_r")

    E_l = model.set_point(26.0, -101.0, classes=["given"], ID="E")
    E_r = model.set_point(48.0, -101.0, ID="E_r")

    F_l = model.set_point(120.0, -59.0, classes=["given"], ID="F")
    F_r = model.set_point(148.0, -59.0, ID="F_r")

    G_l = model.set_point(120.0, -81.0, classes=["given"], ID="G")
    G_r = model.set_point(155.0, -81.0, ID="G_r")

    H_l = model.set_point(121.0, -101.0, classes=["given"], ID="H")
    H_r = model.set_point(164.0, -101.0, ID="H_r")

    K_l = model.set_point(68.0, -123.0, classes=["given"], ID="K")
    K_r = model.set_point(92.0, -123.0, ID="K_r")

    L_l = model.set_point(68.0, -145.0, classes=["given"], ID="L")
    L_r = model.set_point(127.0, -145.0, ID="L_r")

    M_l = model.set_point(70.0, -167.0, classes=["given"], ID="M")
    M_r = model.set_point(100.0, -167.0, ID="M_r")

    N_l = model.set_point(274.0, -64.0, classes=["given"], ID="N")
    N_r = model.set_point(350.0, -64.0, ID="N_r")

    O_l = model.set_point(274.0, -87.0, classes=["given"], ID="O")
    O_r = model.set_point(426.0, -87.0, ID="O_r")

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
    model.set_segment(M_l, M_r)
    model.set_segment(N_l, N_r)
    model.set_segment(O_l, O_r)

    return model


if __name__ == "__main__":
    construct_g1()
