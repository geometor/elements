"""Programmatic construction for Book VII, Proposition 24 (VII.24)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0331.g1 using geometor.model."""
    model = Model("VII.24")

    # Single-letter vertical number segments A, B, C, D, E, F
    A_t = model.set_point(15.0, -11.0, classes=["given"], ID="A")
    A_b = model.set_point(15.0, -108.0, ID="A_b")

    B_t = model.set_point(39.0, -10.0, classes=["given"], ID="B")
    B_b = model.set_point(39.0, -87.0, ID="B_b")

    C_t = model.set_point(60.0, -11.0, classes=["given"], ID="C")
    C_b = model.set_point(60.0, -124.0, ID="C_b")

    D_t = model.set_point(86.0, -10.0, classes=["given"], ID="D")
    D_b = model.set_point(86.0, -160.0, ID="D_b")

    E_t = model.set_point(109.0, -13.0, classes=["given"], ID="E")
    E_b = model.set_point(109.0, -91.0, ID="E_b")

    F_t = model.set_point(136.0, -16.0, classes=["given"], ID="F")
    F_b = model.set_point(136.0, -80.0, ID="F_b")

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
