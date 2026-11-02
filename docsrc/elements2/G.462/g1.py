"""Programmatic construction for Book X, Proposition 80 (X.80)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0173.g1 using geometor.model."""
    model = Model("X.80")

    # Straight line AD divided at B and C
    A = model.set_point(14.0, -21.0, classes=["given"], ID="A")
    B = model.set_point(82.0, -21.0, classes=["given"], ID="B")
    C = model.set_point(184.0, -21.0, classes=["given"], ID="C")
    D = model.set_point(215.0, -21.0, classes=["given"], ID="D")

    # Base line
    model.construct_line(A, D)

    # Segments
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, D)
    model.set_segment(B, C)
    model.set_segment(C, D)

    # Sections
    model.set_section([A, B, C])
    model.set_section([A, B, D])
    model.set_section([A, C, D])
    model.set_section([B, C, D])

    return model


if __name__ == "__main__":
    construct_g1()
