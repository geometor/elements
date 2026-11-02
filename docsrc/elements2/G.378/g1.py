"""Programmatic construction for Book X, Proposition 7 (X.7)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0032.g1 using geometor.model."""
    model = Model("X.7")

    # Single-letter magnitude segment A
    A_l = model.set_point(28.0, -18.0, classes=["given"], ID="A")
    A_r = model.set_point(98.0, -18.0, ID="A_r")

    # Single-letter magnitude segment B
    B_l = model.set_point(28.0, -39.5, classes=["given"], ID="B")
    B_r = model.set_point(80.0, -39.5, ID="B_r")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B_l, B_r)

    # Magnitude segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)

    return model


if __name__ == "__main__":
    construct_g1()
