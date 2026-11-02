"""Programmatic construction for Book V, Proposition 20 (V.20)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0182.g1 for Book V, Proposition 20 using geometor.model."""
    model = Model("V.20")

    # Left column standalone magnitudes A, B, C
    A_1 = model.set_point(24.00, -15.00, classes=["given"], ID="A_1")
    A_2 = model.set_point(141.00, -15.00, classes=["given"], ID="A_2")
    B_1 = model.set_point(24.00, -41.00, classes=["given"], ID="B_1")
    B_2 = model.set_point(66.00, -41.00, classes=["given"], ID="B_2")
    C_1 = model.set_point(24.00, -65.00, classes=["given"], ID="C_1")
    C_2 = model.set_point(101.00, -65.00, classes=["given"], ID="C_2")

    # Right column standalone magnitudes D, E, F
    D_1 = model.set_point(214.00, -15.00, classes=["given"], ID="D_1")
    D_2 = model.set_point(286.00, -15.00, classes=["given"], ID="D_2")
    E_1 = model.set_point(214.00, -41.00, classes=["given"], ID="E_1")
    E_2 = model.set_point(239.00, -41.00, classes=["given"], ID="E_2")
    F_1 = model.set_point(214.00, -65.00, classes=["given"], ID="F_1")
    F_2 = model.set_point(262.00, -65.00, classes=["given"], ID="F_2")

    model.set_segment(A_1, A_2)
    model.set_segment(B_1, B_2)
    model.set_segment(C_1, C_2)
    model.set_segment(D_1, D_2)
    model.set_segment(E_1, E_2)
    model.set_segment(F_1, F_2)

    return model


if __name__ == "__main__":
    construct_g1()
