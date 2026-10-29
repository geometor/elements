"""Programmatic construction for Book X, Proposition 70 (X.70)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0155.g1 using geometor.model."""
    model = Model("X.70")

    # Side of the sum of two medial areas AB divided at E
    A = model.set_point(23.5, -13.0, classes=["given"], ID="A")
    E = model.set_point(23.5, -105.0, classes=["given"], ID="E")
    B = model.set_point(23.5, -157.0, classes=["given"], ID="B")

    # Commensurable straight line CD divided at F
    C = model.set_point(52.5, -50.0, classes=["given"], ID="C")
    F = model.set_point(52.5, -108.0, ID="F")
    D = model.set_point(52.5, -141.0, classes=["given"], ID="D")

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
