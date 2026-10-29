"""Programmatic construction for Book III, Proposition 35 Case 1 (III.35 - g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0077.g2 using geometor.model."""
    model = Model("III.35.g1")

    # Center E(86, -76) and points on circle ABCD, radius 61 (y-inverted)
    E = model.set_point(86.0, -76.0, ID="E")
    B = model.set_point(25.0, -76.0, classes=["given"], ID="B")
    D = model.set_point(147.0, -76.0, classes=["given"], ID="D")
    A = model.set_point(39.27, -36.79, classes=["given"], ID="A")
    C = model.set_point(132.73, -115.21, classes=["given"], ID="C")

    # Circle ABCD
    model.construct_circle(E, B)

    # Segments
    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_segment(E, B)

    # Sections
    model.set_section([A, E, C])
    model.set_section([B, E, D])

    return model


if __name__ == "__main__":
    construct_g1()
