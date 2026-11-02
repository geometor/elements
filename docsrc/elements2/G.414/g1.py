"""Programmatic construction for Book X, Proposition 40 (X.40)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0093.g1 using geometor.model."""
    model = Model("X.40")

    # Straight line AC divided into straight lines AB, BC incommensurable in square
    A = model.set_point(16.0, -25.5, classes=["given"], ID="A")
    B = model.set_point(108.0, -25.5, classes=["given"], ID="B")
    C = model.set_point(161.0, -25.5, classes=["given"], ID="C")

    model.construct_line(A, C)

    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)

    model.set_section([A, B, C])

    return model


if __name__ == "__main__":
    construct_g1()
