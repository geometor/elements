"""Programmatic construction for Book V, Proposition 22 (V.22)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0186.g1 for Book V, Proposition 22 using geometor.model."""
    model = Model("V.22")

    # Left group: A, D, G (double of A), H (double of D)
    A_1 = model.set_point(106.00, -17.00, classes=["given"], ID="A_1")
    A_2 = model.set_point(190.00, -17.00, classes=["given"], ID="A_2")
    D_1 = model.set_point(106.00, -41.00, classes=["given"], ID="D_1")
    D_2 = model.set_point(164.00, -41.00, classes=["given"], ID="D_2")
    G_1 = model.set_point(21.00, -63.00, classes=["given"], ID="G_1")
    G_2 = model.set_point(187.00, -63.00, classes=["given"], ID="G_2")
    H_1 = model.set_point(51.00, -89.00, classes=["given"], ID="H_1")
    H_2 = model.set_point(166.00, -89.00, classes=["given"], ID="H_2")

    # Middle group: B, E, K (triple of B), L (triple of E)
    B_1 = model.set_point(258.00, -17.00, classes=["given"], ID="B_1")
    B_2 = model.set_point(300.00, -17.00, classes=["given"], ID="B_2")
    E_1 = model.set_point(258.00, -41.00, classes=["given"], ID="E_1")
    E_2 = model.set_point(286.00, -41.00, classes=["given"], ID="E_2")
    K_1 = model.set_point(239.00, -63.00, classes=["given"], ID="K_1")
    K_2 = model.set_point(371.00, -63.00, classes=["given"], ID="K_2")
    L_1 = model.set_point(252.00, -89.00, classes=["given"], ID="L_1")
    L_2 = model.set_point(344.00, -89.00, classes=["given"], ID="L_2")

    # Right group: C, F, M (double of C), N (double of F)
    C_1 = model.set_point(370.00, -17.00, classes=["given"], ID="C_1")
    C_2 = model.set_point(451.00, -17.00, classes=["given"], ID="C_2")
    F_1 = model.set_point(370.00, -41.00, classes=["given"], ID="F_1")
    F_2 = model.set_point(430.00, -41.00, classes=["given"], ID="F_2")
    M_1 = model.set_point(416.00, -63.00, classes=["given"], ID="M_1")
    M_2 = model.set_point(597.00, -63.00, classes=["given"], ID="M_2")
    N_1 = model.set_point(444.00, -89.00, classes=["given"], ID="N_1")
    N_2 = model.set_point(571.00, -89.00, classes=["given"], ID="N_2")

    for p1, p2 in [
        (A_1, A_2),
        (D_1, D_2),
        (G_1, G_2),
        (H_1, H_2),
        (B_1, B_2),
        (E_1, E_2),
        (K_1, K_2),
        (L_1, L_2),
        (C_1, C_2),
        (F_1, F_2),
        (M_1, M_2),
        (N_1, N_2),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_g1()
