"""Programmatic construction for Book X, Proposition 36 (X.36)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0087.g1 using geometor.model."""
    model = Model("X.36")

    # Straight line AC divided into rational straight lines AB, BC
    A = model.set_point(19.0, -17.5, classes=["given"], ID="A")
    B = model.set_point(111.0, -17.5, classes=["given"], ID="B")
    C = model.set_point(198.0, -17.5, classes=["given"], ID="C")

    model.construct_line(A, C)

    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)

    model.set_section([A, B, C])

    return model


if __name__ == "__main__":
    construct_g1()
