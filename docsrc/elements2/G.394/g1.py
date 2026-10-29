"""Programmatic construction for Book X, Proposition 73 (X.73)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0162.g1 using geometor.model."""
    model = Model("X.73")

    # Rational straight line AB with rational straight line BC subtracted, leaving apotome AC
    A = model.set_point(17.0, -19.0, classes=["given"], ID="A")
    C = model.set_point(72.0, -19.0, classes=["given"], ID="C")
    B = model.set_point(169.0, -19.0, classes=["given"], ID="B")

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
