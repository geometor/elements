"""Programmatic construction for Book IX, Proposition 2 (IX.2)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0391.g1 using geometor.model."""
    model = Model("IX.2")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(30.0, -22.5, classes=["given"], ID="A")
    A_r = model.set_point(101.0, -22.5, ID="A_r")

    B_l = model.set_point(29.0, -49.5, classes=["given"], ID="B")
    B_r = model.set_point(122.0, -49.5, ID="B_r")

    C_l = model.set_point(27.0, -73.5, classes=["given"], ID="C")
    C_r = model.set_point(246.0, -73.5, ID="C_r")

    D_l = model.set_point(26.0, -94.0, classes=["given"], ID="D")
    D_r = model.set_point(192.0, -94.0, ID="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_g1()
