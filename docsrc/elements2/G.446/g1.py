"""Programmatic construction for Book X, Proposition 66 (X.66)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0149.g1 using geometor.model."""
    model = Model("X.66")

    # Binomial straight line AB divided into its terms at E
    A = model.set_point(36.0, -19.0, classes=["given"], ID="A")
    E = model.set_point(151.0, -19.0, classes=["given"], ID="E")
    B = model.set_point(218.0, -19.0, classes=["given"], ID="B")

    # Straight line CD commensurable in length with AB, divided at F
    C = model.set_point(18.0, -46.5, classes=["given"], ID="C")
    F = model.set_point(159.0, -46.5, ID="F")
    D = model.set_point(244.0, -46.5, classes=["given"], ID="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    # Sections
    model.set_section([A, E, B])
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_g1()
