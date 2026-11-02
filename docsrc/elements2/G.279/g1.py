"""Programmatic construction for Book VII, Proposition 25 (VII.25)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0332.g1 using geometor.model."""
    model = Model("VII.25")

    # Single-letter vertical number segments A, D, B, C
    A_t = model.set_point(22.0, -10.0, classes=["given"], ID="A")
    A_b = model.set_point(22.0, -71.0, ID="A_b")

    D_t = model.set_point(22.0, -83.0, classes=["given"], ID="D")
    D_b = model.set_point(22.0, -141.0, ID="D_b")

    B_t = model.set_point(48.0, -12.0, classes=["given"], ID="B")
    B_b = model.set_point(48.0, -60.0, ID="B_b")

    C_t = model.set_point(72.0, -13.0, classes=["given"], ID="C")
    C_b = model.set_point(72.0, -119.0, ID="C_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(D_t, D_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)

    return model


if __name__ == "__main__":
    construct_g1()
