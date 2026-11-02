"""Programmatic construction for Book V, Proposition 21 (V.21)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0184.g1 for Book V, Proposition 21 using geometor.model."""
    model = Model("V.21")

    # Left column standalone magnitudes A, B, C
    A_1 = model.set_point(24.00, -16.00, classes=["given"], ID="A_1")
    A_2 = model.set_point(141.00, -16.00, classes=["given"], ID="A_2")
    B_1 = model.set_point(24.00, -35.00, classes=["given"], ID="B_1")
    B_2 = model.set_point(105.00, -35.00, classes=["given"], ID="B_2")
    C_1 = model.set_point(24.00, -54.00, classes=["given"], ID="C_1")
    C_2 = model.set_point(129.00, -54.00, classes=["given"], ID="C_2")

    # Right column standalone magnitudes D, E, F
    D_1 = model.set_point(227.00, -16.00, classes=["given"], ID="D_1")
    D_2 = model.set_point(331.00, -16.00, classes=["given"], ID="D_2")
    E_1 = model.set_point(227.00, -35.00, classes=["given"], ID="E_1")
    E_2 = model.set_point(359.00, -35.00, classes=["given"], ID="E_2")
    F_1 = model.set_point(227.00, -54.00, classes=["given"], ID="F_1")
    F_2 = model.set_point(317.00, -54.00, classes=["given"], ID="F_2")

    model.set_segment(A_1, A_2)
    model.set_segment(B_1, B_2)
    model.set_segment(C_1, C_2)
    model.set_segment(D_1, D_2)
    model.set_segment(E_1, E_2)
    model.set_segment(F_1, F_2)

    return model


if __name__ == "__main__":
    construct_g1()
