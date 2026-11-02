"""Programmatic construction for Book X, Proposition 77 (X.77)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0168.g1 using geometor.model."""
    model = Model("X.77")

    # Straight line AB with straight line BC subtracted, leaving AC
    A = model.set_point(26.5, -15.0, classes=["given"], ID="A")
    C = model.set_point(26.5, -106.0, classes=["given"], ID="C")
    B = model.set_point(26.5, -148.0, classes=["given"], ID="B")

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
