"""Programmatic construction for Book VIII, Proposition 13 (VIII.13)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0372.g1 using geometor.model."""
    model = Model("VIII.13")

    # Single-letter horizontal number segments A, B, C, D, E, F, L, O, G, H, K, M, N, P, Q
    A_l = model.set_point(26.0, -16.0, classes=["given"], ID="A")
    A_r = model.set_point(71.0, -16.0, ID="A_r")

    B_l = model.set_point(27.0, -38.0, classes=["given"], ID="B")
    B_r = model.set_point(78.0, -38.0, ID="B_r")

    C_l = model.set_point(26.0, -62.0, classes=["given"], ID="C")
    C_r = model.set_point(86.0, -62.0, ID="C_r")

    D_l = model.set_point(26.0, -86.0, classes=["given"], ID="D")
    D_r = model.set_point(113.0, -86.0, ID="D_r")

    E_l = model.set_point(26.0, -110.0, classes=["given"], ID="E")
    E_r = model.set_point(131.0, -110.0, ID="E_r")

    F_l = model.set_point(27.0, -134.0, classes=["given"], ID="F")
    F_r = model.set_point(156.0, -134.0, ID="F_r")

    L_l = model.set_point(25.0, -156.0, classes=["given"], ID="L")
    L_r = model.set_point(122.0, -156.0, ID="L_r")

    O_l = model.set_point(26.0, -180.0, classes=["given"], ID="O")
    O_r = model.set_point(138.0, -180.0, ID="O_r")

    G_l = model.set_point(247.0, -18.0, classes=["given"], ID="G")
    G_r = model.set_point(383.0, -18.0, ID="G_r")

    H_l = model.set_point(247.0, -39.0, classes=["given"], ID="H")
    H_r = model.set_point(428.0, -39.0, ID="H_r")

    K_l = model.set_point(248.0, -62.0, classes=["given"], ID="K")
    K_r = model.set_point(494.0, -62.0, ID="K_r")

    M_l = model.set_point(248.0, -103.0, classes=["given"], ID="M")
    M_r = model.set_point(393.0, -103.0, ID="M_r")

    N_l = model.set_point(247.0, -128.0, classes=["given"], ID="N")
    N_r = model.set_point(413.0, -128.0, ID="N_r")

    P_l = model.set_point(248.0, -152.0, classes=["given"], ID="P")
    P_r = model.set_point(449.0, -152.0, ID="P_r")

    Q_l = model.set_point(247.0, -180.0, classes=["given"], ID="Q")
    Q_r = model.set_point(466.0, -180.0, ID="Q_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(L_l, L_r)
    model.set_segment(O_l, O_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)
    model.set_segment(M_l, M_r)
    model.set_segment(N_l, N_r)
    model.set_segment(P_l, P_r)
    model.set_segment(Q_l, Q_r)

    return model


if __name__ == "__main__":
    construct_g1()
