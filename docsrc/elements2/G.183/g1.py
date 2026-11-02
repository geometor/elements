"""Programmatic construction for Book V, Proposition 7 (V.7)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0154.g1 for Book V, Proposition 7 using geometor.model."""
    model = Model("V.7")

    # Left column magnitudes: A, B, C
    A_1 = model.set_point(28.0, -18.0, classes=["given"], ID="A_1")
    A_2 = model.set_point(72.0, -18.0, classes=["given"], ID="A_2")
    B_1 = model.set_point(28.0, -45.0, classes=["given"], ID="B_1")
    B_2 = model.set_point(72.0, -45.0, classes=["given"], ID="B_2")
    C_1 = model.set_point(28.0, -74.0, classes=["given"], ID="C_1")
    C_2 = model.set_point(84.0, -74.0, classes=["given"], ID="C_2")

    # Right column multiples: D, E, F
    D_1 = model.set_point(127.0, -18.0, ID="D_1")
    D_2 = model.set_point(169.0, -18.0, ID="D_2")
    D_3 = model.set_point(211.0, -18.0, ID="D_3")
    D_4 = model.set_point(254.0, -18.0, ID="D_4")
    D_5 = model.set_point(296.0, -18.0, ID="D_5")

    E_1 = model.set_point(127.0, -45.0, ID="E_1")
    E_2 = model.set_point(169.0, -45.0, ID="E_2")
    E_3 = model.set_point(211.0, -45.0, ID="E_3")
    E_4 = model.set_point(254.0, -45.0, ID="E_4")
    E_5 = model.set_point(296.0, -45.0, ID="E_5")

    F_1 = model.set_point(127.0, -74.0, ID="F_1")
    F_2 = model.set_point(183.0, -74.0, ID="F_2")
    F_3 = model.set_point(238.0, -74.0, ID="F_3")
    F_4 = model.set_point(294.0, -74.0, ID="F_4")

    # Segments for standalone magnitudes A, B, C, D, E, F
    model.set_segment(A_1, A_2)
    model.set_segment(B_1, B_2)
    model.set_segment(C_1, C_2)
    model.set_segment(D_1, D_5)
    model.set_segment(E_1, E_5)
    model.set_segment(F_1, F_4)

    return model


if __name__ == "__main__":
    construct_g1()
