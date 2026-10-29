"""Programmatic construction for Book VIII, Proposition 9 (VIII.9)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0365.g1 using geometor.model."""
    model = Model("VIII.9")

    # Single-letter horizontal number segments A, C, D, B, E, F, G, H, K, L, M, N, O, P
    A_l = model.set_point(24.0, -16.0, classes=["given"], ID="A")
    A_r = model.set_point(127.0, -16.0, ID="A_r")

    C_l = model.set_point(25.0, -34.0, classes=["given"], ID="C")
    C_r = model.set_point(165.0, -34.0, ID="C_r")

    D_l = model.set_point(24.0, -57.0, classes=["given"], ID="D")
    D_r = model.set_point(216.0, -57.0, ID="D_r")

    B_l = model.set_point(26.0, -76.0, classes=["given"], ID="B")
    B_r = model.set_point(274.0, -76.0, ID="B_r")

    E_l = model.set_point(138.0, -99.0, classes=["given"], ID="E")
    E_r = model.set_point(160.0, -99.0, ID="E_r")

    F_l = model.set_point(138.0, -122.0, classes=["given"], ID="F")
    F_r = model.set_point(169.0, -122.0, ID="F_r")

    G_l = model.set_point(138.0, -145.0, classes=["given"], ID="G")
    G_r = model.set_point(186.0, -145.0, ID="G_r")

    H_l = model.set_point(316.0, -16.0, classes=["given"], ID="H")
    H_r = model.set_point(355.0, -16.0, ID="H_r")

    K_l = model.set_point(317.0, -35.0, classes=["given"], ID="K")
    K_r = model.set_point(366.0, -35.0, ID="K_r")

    L_l = model.set_point(317.0, -57.0, classes=["given"], ID="L")
    L_r = model.set_point(384.0, -57.0, ID="L_r")

    M_l = model.set_point(317.0, -102.0, classes=["given"], ID="M")
    M_r = model.set_point(427.0, -102.0, ID="M_r")

    N_l = model.set_point(320.0, -126.0, classes=["given"], ID="N")
    N_r = model.set_point(462.0, -126.0, ID="N_r")

    O_l = model.set_point(319.0, -152.0, classes=["given"], ID="O")
    O_r = model.set_point(513.0, -152.0, ID="O_r")

    P_l = model.set_point(320.0, -176.0, classes=["given"], ID="P")
    P_r = model.set_point(571.0, -176.0, ID="P_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(B_l, B_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)
    model.set_segment(L_l, L_r)
    model.set_segment(M_l, M_r)
    model.set_segment(N_l, N_r)
    model.set_segment(O_l, O_r)
    model.set_segment(P_l, P_r)

    return model


if __name__ == "__main__":
    construct_g1()
