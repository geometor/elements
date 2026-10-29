"""Programmatic construction for Book X, Proposition 18 (X.18)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0049.g1 using geometor.model."""
    model = Model("X.18")

    # Vertical line BC with division points F, E, D
    B = model.set_point(28.5, -17.0, classes=["given"], ID="B")
    F = model.set_point(28.5, -61.0, ID="F")
    E = model.set_point(28.5, -101.0, ID="E")
    D = model.set_point(28.5, -139.0, ID="D")
    C = model.set_point(28.5, -184.0, classes=["given"], ID="C")

    # Standalone vertical straight line A
    A_t = model.set_point(64.5, -27.0, classes=["given"], ID="A")
    A_b = model.set_point(64.5, -171.0, classes=["given"], ID="A_b")

    # Base lines
    model.construct_line(B, C)
    model.construct_line(A_t, A_b)

    # Segments and sub-segments on BC
    model.set_segment(B, C)
    model.set_segment(B, F)
    model.set_segment(F, E)
    model.set_segment(E, D)
    model.set_segment(D, C)
    model.set_segment(B, E)
    model.set_segment(E, C)
    model.set_segment(B, D)
    model.set_segment(F, D)
    model.set_segment(F, C)

    # Collinear sections
    model.set_section([B, D, C])
    model.set_section([B, E, C])
    model.set_section([B, F, D])
    model.set_section([F, E, D])

    # Straight line A
    model.set_segment(A_t, A_b)

    return model


if __name__ == "__main__":
    construct_g1()
