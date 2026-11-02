"""Programmatic construction for Book X, Proposition 67 (X.67)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0151.g1 using geometor.model."""
    model = Model("X.67")

    # Bimedial straight line AB divided into its medials at E
    A = model.set_point(18.0, -18.5, classes=["given"], ID="A")
    E = model.set_point(112.0, -18.5, classes=["given"], ID="E")
    B = model.set_point(159.0, -18.5, classes=["given"], ID="B")

    # Straight line CD commensurable in length with AB, divided at F
    C = model.set_point(30.0, -41.5, classes=["given"], ID="C")
    F = model.set_point(103.0, -41.5, ID="F")
    D = model.set_point(137.0, -41.5, classes=["given"], ID="D")

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
