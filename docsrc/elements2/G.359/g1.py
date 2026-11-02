"""Programmatic construction for Book IX, Proposition 28 (IX.28)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0422.g2 using geometor.model."""
    model = Model("IX.28")

    # Single-letter horizontal number segments A, B, C
    A_l = model.set_point(32.0, -17.5, classes=["given"], ID="A")
    A_r = model.set_point(57.0, -17.5, ID="A_r")

    B_l = model.set_point(32.0, -39.0, classes=["given"], ID="B")
    B_r = model.set_point(81.0, -39.0, ID="B_r")

    C_l = model.set_point(33.0, -59.5, classes=["given"], ID="C")
    C_r = model.set_point(172.0, -59.5, ID="C_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_g1()
