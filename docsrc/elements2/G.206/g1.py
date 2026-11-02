"""Programmatic construction for Book V, Proposition 23 (V.23)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0187.g1 for Book V, Proposition 23 using geometor.model."""
    model = Model("V.23")

    # Left group: A, D, G (triple of A), K (triple of D)
    A_1 = model.set_point(96.00, -16.00, classes=["given"], ID="A_1")
    A_2 = model.set_point(161.00, -16.00, classes=["given"], ID="A_2")
    D_1 = model.set_point(96.00, -36.00, classes=["given"], ID="D_1")
    D_2 = model.set_point(134.00, -36.00, classes=["given"], ID="D_2")
    G_1 = model.set_point(40.00, -58.00, classes=["given"], ID="G_1")
    G_2 = model.set_point(232.00, -58.00, classes=["given"], ID="G_2")
    K_1 = model.set_point(74.00, -86.00, classes=["given"], ID="K_1")
    K_2 = model.set_point(194.00, -86.00, classes=["given"], ID="K_2")

    # Middle group: B, E, H (triple of B), M (double of E)
    B_1 = model.set_point(298.00, -16.00, classes=["given"], ID="B_1")
    B_2 = model.set_point(326.00, -16.00, classes=["given"], ID="B_2")
    E_1 = model.set_point(298.00, -36.00, classes=["given"], ID="E_1")
    E_2 = model.set_point(372.00, -36.00, classes=["given"], ID="E_2")
    H_1 = model.set_point(298.00, -58.00, classes=["given"], ID="H_1")
    H_2 = model.set_point(381.00, -58.00, classes=["given"], ID="H_2")
    M_1 = model.set_point(262.00, -86.00, classes=["given"], ID="M_1")
    M_2 = model.set_point(410.00, -86.00, classes=["given"], ID="M_2")

    # Right group: C, F, L (double of C), N (double of F)
    C_1 = model.set_point(443.00, -16.00, classes=["given"], ID="C_1")
    C_2 = model.set_point(496.00, -16.00, classes=["given"], ID="C_2")
    F_1 = model.set_point(439.00, -36.00, classes=["given"], ID="F_1")
    F_2 = model.set_point(474.00, -36.00, classes=["given"], ID="F_2")
    L_1 = model.set_point(442.00, -58.00, classes=["given"], ID="L_1")
    L_2 = model.set_point(550.00, -58.00, classes=["given"], ID="L_2")
    N_1 = model.set_point(458.00, -86.00, classes=["given"], ID="N_1")
    N_2 = model.set_point(530.00, -86.00, classes=["given"], ID="N_2")

    for p1, p2 in [
        (A_1, A_2),
        (D_1, D_2),
        (G_1, G_2),
        (K_1, K_2),
        (B_1, B_2),
        (E_1, E_2),
        (H_1, H_2),
        (M_1, M_2),
        (C_1, C_2),
        (F_1, F_2),
        (L_1, L_2),
        (N_1, N_2),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_g1()
