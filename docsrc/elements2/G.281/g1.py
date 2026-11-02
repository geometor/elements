"""Programmatic construction for Book VII, Proposition 27 (VII.27)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0334.g1 using geometor.model."""
    model = Model("VII.27")

    # Single-letter vertical number segments A, B, C, D, E, F
    A_t = model.set_point(23.0, -17.0, classes=["given"], ID="A")
    A_b = model.set_point(23.0, -74.0, ID="A_b")

    B_t = model.set_point(25.0, -112.0, classes=["given"], ID="B")
    B_b = model.set_point(25.0, -155.0, ID="B_b")

    C_t = model.set_point(51.0, -14.0, classes=["given"], ID="C")
    C_b = model.set_point(51.0, -106.0, ID="C_b")

    D_t = model.set_point(80.0, -11.0, classes=["given"], ID="D")
    D_b = model.set_point(80.0, -141.0, ID="D_b")

    E_t = model.set_point(110.0, -11.0, classes=["given"], ID="E")
    E_b = model.set_point(110.0, -78.0, ID="E_b")

    F_t = model.set_point(141.0, -10.0, classes=["given"], ID="F")
    F_b = model.set_point(141.0, -102.0, ID="F_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)
    model.set_segment(E_t, E_b)
    model.set_segment(F_t, F_b)

    return model


if __name__ == "__main__":
    construct_g1()
