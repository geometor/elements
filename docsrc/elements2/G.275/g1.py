"""Programmatic construction for Book VII, Proposition 21 (VII.21)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0328.g1 using geometor.model."""
    model = Model("VII.21")

    # Single-letter vertical number segments A, B, C, D, E
    A_t = model.set_point(22.0, -10.0, classes=["given"], ID="A")
    A_b = model.set_point(22.0, -114.0, ID="A_b")

    B_t = model.set_point(49.0, -16.0, classes=["given"], ID="B")
    B_b = model.set_point(49.0, -89.0, ID="B_b")

    C_t = model.set_point(128.0, -15.0, classes=["given"], ID="C")
    C_b = model.set_point(128.0, -70.0, ID="C_b")

    D_t = model.set_point(152.0, -12.0, classes=["given"], ID="D")
    D_b = model.set_point(152.0, -54.0, ID="D_b")

    E_t = model.set_point(198.0, -17.0, classes=["given"], ID="E")
    E_b = model.set_point(198.0, -43.0, ID="E_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)
    model.set_segment(E_t, E_b)

    return model


if __name__ == "__main__":
    construct_g1()
