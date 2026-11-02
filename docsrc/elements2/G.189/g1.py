"""Programmatic construction for Book V, Proposition 11 (V.11)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0164.g1 for Book V, Proposition 11 using geometor.model."""
    model = Model("V.11")

    # Left column: A, B, G, L
    A_1 = model.set_point(24.0, -17.0, classes=["given"], ID="A_1")
    A_2 = model.set_point(84.0, -17.0, classes=["given"], ID="A_2")
    B_1 = model.set_point(24.0, -41.0, classes=["given"], ID="B_1")
    B_2 = model.set_point(68.0, -41.0, classes=["given"], ID="B_2")
    G_1 = model.set_point(24.0, -63.0, ID="G_1")
    G_2 = model.set_point(144.0, -63.0, ID="G_2")
    L_1 = model.set_point(24.0, -88.0, ID="L_1")
    L_2 = model.set_point(160.0, -88.0, ID="L_2")

    # Middle column: C, D, H, M
    C_1 = model.set_point(210.0, -17.0, classes=["given"], ID="C_1")
    C_2 = model.set_point(256.0, -17.0, classes=["given"], ID="C_2")
    D_1 = model.set_point(205.0, -41.0, classes=["given"], ID="D_1")
    D_2 = model.set_point(242.0, -41.0, classes=["given"], ID="D_2")
    H_1 = model.set_point(205.0, -63.0, ID="H_1")
    H_2 = model.set_point(310.0, -63.0, ID="H_2")
    M_1 = model.set_point(205.0, -88.0, ID="M_1")
    M_2 = model.set_point(317.0, -88.0, ID="M_2")

    # Right column: E, F, K, N
    E_1 = model.set_point(354.0, -17.0, classes=["given"], ID="E_1")
    E_2 = model.set_point(389.0, -17.0, classes=["given"], ID="E_2")
    F_1 = model.set_point(354.0, -41.0, classes=["given"], ID="F_1")
    F_2 = model.set_point(377.0, -41.0, classes=["given"], ID="F_2")
    K_1 = model.set_point(354.0, -63.0, ID="K_1")
    K_2 = model.set_point(419.0, -63.0, ID="K_2")
    N_1 = model.set_point(354.0, -88.0, ID="N_1")
    N_2 = model.set_point(421.0, -88.0, ID="N_2")

    # Standalone magnitude segments
    for p1, p2 in [
        (A_1, A_2), (B_1, B_2), (G_1, G_2), (L_1, L_2),
        (C_1, C_2), (D_1, D_2), (H_1, H_2), (M_1, M_2),
        (E_1, E_2), (F_1, F_2), (K_1, K_2), (N_1, N_2),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_g1()
