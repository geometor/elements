"""Programmatic construction for Book V, Proposition 13 (V.13)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0166.g1 for Book V, Proposition 13 using geometor.model."""
    model = Model("V.13")

    # Top rows: A, B; C, D; M, N; G, K
    A_1 = model.set_point(27.0, -23.0, classes=["given"], ID="A_1")
    A_2 = model.set_point(90.0, -23.0, classes=["given"], ID="A_2")
    B_1 = model.set_point(27.0, -48.0, classes=["given"], ID="B_1")
    B_2 = model.set_point(56.0, -48.0, classes=["given"], ID="B_2")

    C_1 = model.set_point(158.0, -23.0, classes=["given"], ID="C_1")
    C_2 = model.set_point(242.0, -23.0, classes=["given"], ID="C_2")
    D_1 = model.set_point(143.0, -48.0, classes=["given"], ID="D_1")
    D_2 = model.set_point(182.0, -48.0, classes=["given"], ID="D_2")

    M_1 = model.set_point(290.0, -23.0, ID="M_1")
    M_2 = model.set_point(416.0, -23.0, ID="M_2")
    N_1 = model.set_point(246.0, -48.0, ID="N_1")
    N_2 = model.set_point(344.0, -48.0, ID="N_2")

    G_1 = model.set_point(453.0, -23.0, ID="G_1")
    G_2 = model.set_point(614.0, -23.0, ID="G_2")
    K_1 = model.set_point(428.0, -48.0, ID="K_1")
    K_2 = model.set_point(552.0, -48.0, ID="K_2")

    # Bottom rows: E, F, H, L
    E_1 = model.set_point(95.0, -84.0, classes=["given"], ID="E_1")
    E_2 = model.set_point(198.0, -84.0, classes=["given"], ID="E_2")
    F_1 = model.set_point(95.0, -113.0, classes=["given"], ID="F_1")
    F_2 = model.set_point(182.0, -113.0, classes=["given"], ID="F_2")
    H_1 = model.set_point(95.0, -138.0, ID="H_1")
    H_2 = model.set_point(293.0, -138.0, ID="H_2")
    L_1 = model.set_point(95.0, -164.0, ID="L_1")
    L_2 = model.set_point(344.0, -164.0, ID="L_2")

    for p1, p2 in [
        (A_1, A_2), (B_1, B_2), (C_1, C_2), (D_1, D_2),
        (M_1, M_2), (N_1, N_2), (G_1, G_2), (K_1, K_2),
        (E_1, E_2), (F_1, F_2), (H_1, H_2), (L_1, L_2),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_g1()
