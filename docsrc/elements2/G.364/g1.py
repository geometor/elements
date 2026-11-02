"""Programmatic construction for Book IX, Proposition 32 (IX.32)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0424.g1 using geometor.model."""
    model = Model("IX.32")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(27.0, -22.5, classes=["given"], ID="A")
    A_r = model.set_point(57.0, -22.5, ID="A_r")

    B_l = model.set_point(28.0, -43.5, classes=["given"], ID="B")
    B_r = model.set_point(90.0, -43.5, ID="B_r")

    C_l = model.set_point(30.0, -64.5, classes=["given"], ID="C")
    C_r = model.set_point(150.0, -64.5, ID="C_r")

    D_l = model.set_point(30.0, -84.5, classes=["given"], ID="D")
    D_r = model.set_point(270.0, -84.5, ID="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_g1()
