"""Programmatic construction for Book IX, Proposition 33 (IX.33)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0425.g1 using geometor.model."""
    model = Model("IX.33")

    # Single-letter horizontal number segment A
    A_l = model.set_point(15.0, -15.0, classes=["given"], ID="A")
    A_r = model.set_point(125.0, -15.0, ID="A_r")

    # Number segment
    model.set_segment(A_l, A_r)

    return model


if __name__ == "__main__":
    construct_g1()
