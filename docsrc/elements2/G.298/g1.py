"""Programmatic construction for Book VIII, Proposition 3 (VIII.3)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0354.g1 using geometor.model."""
    model = Model("VIII.3")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H, K, L, M, N, O
    A_l = model.set_point(28.0, -15.0, classes=["given"], ID="A")
    A_r = model.set_point(93.0, -15.0, ID="A_r")

    B_l = model.set_point(132.0, -15.0, classes=["given"], ID="B")
    B_r = model.set_point(236.0, -15.0, ID="B_r")

    C_l = model.set_point(256.0, -15.0, classes=["given"], ID="C")
    C_r = model.set_point(399.0, -15.0, ID="C_r")

    D_l = model.set_point(94.0, -40.0, classes=["given"], ID="D")
    D_r = model.set_point(309.0, -40.0, ID="D_r")

    E_l = model.set_point(149.0, -68.0, classes=["given"], ID="E")
    E_r = model.set_point(172.0, -68.0, ID="E_r")

    F_l = model.set_point(226.0, -68.0, classes=["given"], ID="F")
    F_r = model.set_point(264.0, -68.0, ID="F_r")

    G_l = model.set_point(67.0, -98.0, classes=["given"], ID="G")
    G_r = model.set_point(104.0, -98.0, ID="G_r")

    H_l = model.set_point(153.0, -98.0, classes=["given"], ID="H")
    H_r = model.set_point(207.0, -98.0, ID="H_r")

    K_l = model.set_point(268.0, -98.0, classes=["given"], ID="K")
    K_r = model.set_point(337.0, -98.0, ID="K_r")

    L_l = model.set_point(24.0, -126.0, classes=["given"], ID="L")
    L_r = model.set_point(90.0, -126.0, ID="L_r")

    M_l = model.set_point(137.0, -126.0, classes=["given"], ID="M")
    M_r = model.set_point(235.0, -126.0, ID="M_r")

    N_l = model.set_point(260.0, -126.0, classes=["given"], ID="N")
    N_r = model.set_point(405.0, -126.0, ID="N_r")

    O_l = model.set_point(93.0, -152.0, classes=["given"], ID="O")
    O_r = model.set_point(302.0, -152.0, ID="O_r")

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
