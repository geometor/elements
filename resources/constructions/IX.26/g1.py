"""Programmatic construction for Book IX, Proposition 26 (IX.26)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0421.g2 using geometor.model."""
    model = Model("IX.26")

    # Horizontal number segment AB divided at C and D
    A = model.set_point(13.0, -28.0, classes=["given"], ID="A")
    C = model.set_point(110.0, -28.0, ID="C")
    D = model.set_point(147.0, -28.0, ID="D")
    B = model.set_point(171.0, -28.0, classes=["given"], ID="B")

    # Base line
    model.construct_line(A, B)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(C, D)
    model.set_segment(C, B)
    model.set_segment(D, B)

    # Collinear sections
    model.set_section([A, C, B])
    model.set_section([A, D, B])
    model.set_section([C, D, B])

    return model


if __name__ == "__main__":
    construct_g1()
