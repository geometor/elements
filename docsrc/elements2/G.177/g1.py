"""Programmatic construction for Book V, Proposition 4 (V.4)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0148.g1 using geometor.model."""
    model = Model("V.4")

    # Upper group of magnitudes: A, B, E, G, K, M
    A_l = model.set_point(31.0, -23.0, classes=["given"], ID="A")
    A_r = model.set_point(78.0, -23.0, ID="A_r")
    B_l = model.set_point(31.0, -48.0, classes=["given"], ID="B")
    B_r = model.set_point(71.0, -48.0, ID="B_r")
    E_l = model.set_point(31.0, -73.0, ID="E")
    E_r = model.set_point(134.0, -73.0, ID="E_r")
    G_l = model.set_point(31.0, -96.0, ID="G")
    G_r = model.set_point(147.0, -96.0, ID="G_r")
    K_l = model.set_point(31.0, -119.0, ID="K")
    K_r = model.set_point(237.0, -119.0, ID="K_r")
    M_l = model.set_point(31.0, -145.0, ID="M")
    M_r = model.set_point(378.0, -145.0, ID="M_r")

    # Lower group of magnitudes: C, D, F, H, L, N
    C_l = model.set_point(28.0, -172.0, classes=["given"], ID="C")
    C_r = model.set_point(67.0, -172.0, ID="C_r")
    D_l = model.set_point(28.0, -201.0, classes=["given"], ID="D")
    D_r = model.set_point(58.0, -201.0, ID="D_r")
    F_l = model.set_point(28.0, -227.0, ID="F")
    F_r = model.set_point(114.0, -227.0, ID="F_r")
    H_l = model.set_point(28.0, -253.0, ID="H")
    H_r = model.set_point(124.0, -253.0, ID="H_r")
    L_l = model.set_point(28.0, -280.0, ID="L")
    L_r = model.set_point(196.0, -280.0, ID="L_r")
    N_l = model.set_point(28.0, -306.0, ID="N")
    N_r = model.set_point(312.0, -306.0, ID="N_r")

    # Magnitude segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(E_l, E_r)
    model.set_segment(G_l, G_r)
    model.set_segment(K_l, K_r)
    model.set_segment(M_l, M_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(F_l, F_r)
    model.set_segment(H_l, H_r)
    model.set_segment(L_l, L_r)
    model.set_segment(N_l, N_r)

    return model


if __name__ == "__main__":
    construct_g1()
