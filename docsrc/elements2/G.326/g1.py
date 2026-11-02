"""Programmatic construction for Book VIII, Proposition 24 (VIII.24)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0386.g1 using geometor.model."""
    model = Model("VIII.24")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(23.0, -15.0, classes=["given"], ID="A")
    A_r = model.set_point(146.0, -15.0, ID="A_r")

    B_l = model.set_point(24.0, -36.0, classes=["given"], ID="B")
    B_r = model.set_point(188.0, -36.0, ID="B_r")

    C_l = model.set_point(24.0, -55.0, classes=["given"], ID="C")
    C_r = model.set_point(78.0, -55.0, ID="C_r")

    D_l = model.set_point(25.0, -75.0, classes=["given"], ID="D")
    D_r = model.set_point(96.0, -75.0, ID="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_g1()
