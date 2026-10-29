"""Programmatic construction for Book IX, Proposition 34 (IX.34)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0425.g2 using geometor.model."""
    model = Model("IX.34")

    # Single-letter horizontal number segment A
    A_l = model.set_point(10.0, -14.0, classes=["given"], ID="A")
    A_r = model.set_point(160.0, -14.0, ID="A_r")

    # Number segment
    model.set_segment(A_l, A_r)

    return model


if __name__ == "__main__":
    construct_g1()
