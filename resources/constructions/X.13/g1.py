"""Programmatic construction for Book X, Proposition 13 (X.13 - g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0040.g1 using geometor.model."""
    model = Model("X.13.g1")

    # Magnitudes A, C, B
    A_l = model.set_point(30.0, -18.5, classes=["given"], ID="A")
    A_r = model.set_point(141.0, -18.5, ID="A_r")

    C_l = model.set_point(28.0, -40.5, classes=["given"], ID="C")
    C_r = model.set_point(127.0, -40.5, ID="C_r")

    B_l = model.set_point(28.0, -60.5, classes=["given"], ID="B")
    B_r = model.set_point(167.0, -60.5, ID="B_r")

    for p_l, p_r in [(A_l, A_r), (C_l, C_r), (B_l, B_r)]:
        model.construct_line(p_l, p_r)
        model.set_segment(p_l, p_r)

    return model


if __name__ == "__main__":
    construct_g1()
