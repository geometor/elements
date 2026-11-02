"""Programmatic construction for Book VIII, Proposition 4, Diagram 2 (VIII.4 - g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_g2() -> Model:
    """Construct the figure 0357.g1 using geometor.model."""
    model = Model("VIII.4.g2")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H, K, M, N, O, P, Q, R, S, T
    A_l = model.set_point(78.0, -14.0, classes=["given"], ID="A")
    A_r = model.set_point(113.0, -14.0, ID="A_r")

    C_l = model.set_point(177.0, -14.0, classes=["given"], ID="C")
    C_r = model.set_point(202.0, -14.0, ID="C_r")

    E_l = model.set_point(290.0, -16.0, classes=["given"], ID="E")
    E_r = model.set_point(339.0, -16.0, ID="E_r")

    B_l = model.set_point(77.0, -36.0, classes=["given"], ID="B")
    B_r = model.set_point(120.0, -36.0, ID="B_r")

    D_l = model.set_point(177.0, -38.0, classes=["given"], ID="D")
    D_r = model.set_point(202.0, -38.0, ID="D_r")

    F_l = model.set_point(289.0, -38.0, classes=["given"], ID="F")
    F_r = model.set_point(346.0, -38.0, ID="F_r")

    G_l = model.set_point(146.0, -60.0, classes=["given"], ID="G")
    G_r = model.set_point(225.0, -60.0, ID="G_r")

    H_l = model.set_point(287.0, -60.0, classes=["given"], ID="H")
    H_r = model.set_point(361.0, -60.0, ID="H_r")

    K_l = model.set_point(136.0, -84.0, classes=["given"], ID="K")
    K_r = model.set_point(257.0, -84.0, ID="K_r")

    Q_l = model.set_point(349.0, -86.0, classes=["given"], ID="Q")
    Q_r = model.set_point(434.0, -86.0, ID="Q_r")

    M_l = model.set_point(24.0, -109.0, classes=["given"], ID="M")
    M_r = model.set_point(261.0, -109.0, ID="M_r")

    R_l = model.set_point(348.0, -110.0, classes=["given"], ID="R")
    R_r = model.set_point(456.0, -110.0, ID="R_r")

    O_l = model.set_point(24.0, -132.0, classes=["given"], ID="O")
    O_r = model.set_point(183.0, -132.0, ID="O_r")

    S_l = model.set_point(347.0, -132.0, classes=["given"], ID="S")
    S_r = model.set_point(508.0, -132.0, ID="S_r")

    N_l = model.set_point(24.0, -158.0, classes=["given"], ID="N")
    N_r = model.set_point(152.0, -158.0, ID="N_r")

    T_l = model.set_point(344.0, -160.0, classes=["given"], ID="T")
    T_r = model.set_point(533.0, -160.0, ID="T_r")

    P_l = model.set_point(26.0, -182.0, classes=["given"], ID="P")
    P_r = model.set_point(300.0, -182.0, ID="P_r")

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
    model.set_segment(M_l, M_r)
    model.set_segment(O_l, O_r)
    model.set_segment(N_l, N_r)
    model.set_segment(P_l, P_r)
    model.set_segment(Q_l, Q_r)
    model.set_segment(R_l, R_r)
    model.set_segment(S_l, S_r)
    model.set_segment(T_l, T_r)

    return model


if __name__ == "__main__":
    construct_g2()
