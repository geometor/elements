"""Programmatic construction for Book X, Proposition 76 (X.76)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0167.g1 using geometor.model."""
    model = Model("X.76")

    # Straight line AB with straight line BC subtracted, leaving minor AC
    A = model.set_point(17.0, -18.5, classes=["given"], ID="A")
    C = model.set_point(91.0, -18.5, classes=["given"], ID="C")
    B = model.set_point(191.0, -18.5, classes=["given"], ID="B")

    # Base line
    model.construct_line(A, B)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Section
    model.set_section([A, C, B])

    return model


if __name__ == "__main__":
    construct_g1()
