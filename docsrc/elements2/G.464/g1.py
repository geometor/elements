"""Programmatic construction for Book X, Proposition 82 (X.82)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0176.g1 using geometor.model."""
    model = Model("X.82")

    # Straight line AD divided at B and C
    A = model.set_point(15.0, -20.0, classes=["given"], ID="A")
    B = model.set_point(72.0, -20.0, classes=["given"], ID="B")
    C = model.set_point(168.0, -20.0, classes=["given"], ID="C")
    D = model.set_point(200.0, -20.0, classes=["given"], ID="D")

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
