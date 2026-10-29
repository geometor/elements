"""Programmatic construction for Book VII, Proposition 23 (VII.23)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0330.g1 using geometor.model."""
    model = Model("VII.23")

    # Single-letter vertical number segments A, B, C, D
    A_t = model.set_point(14.0, -9.0, classes=["given"], ID="A")
    A_b = model.set_point(14.0, -144.0, ID="A_b")

    B_t = model.set_point(44.0, -43.0, classes=["given"], ID="B")
    B_b = model.set_point(44.0, -144.0, ID="B_b")

    C_t = model.set_point(72.0, -99.0, classes=["given"], ID="C")
    C_b = model.set_point(72.0, -146.0, ID="C_b")

    D_t = model.set_point(96.0, -108.0, classes=["given"], ID="D")
    D_b = model.set_point(96.0, -145.0, ID="D_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)

    return model


if __name__ == "__main__":
    construct_g1()
