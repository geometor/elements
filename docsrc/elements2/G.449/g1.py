"""Programmatic construction for Book X, Proposition 69 (X.69)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0154.g1 using geometor.model."""
    model = Model("X.69")

    # Side of a rational plus a medial area AB divided at E
    A = model.set_point(22.5, -15.0, classes=["given"], ID="A")
    E = model.set_point(22.5, -110.0, classes=["given"], ID="E")
    B = model.set_point(22.5, -160.0, classes=["given"], ID="B")

    # Commensurable straight line CD divided at F
    C = model.set_point(54.5, -53.0, classes=["given"], ID="C")
    F = model.set_point(54.5, -128.0, ID="F")
    D = model.set_point(54.5, -157.0, classes=["given"], ID="D")

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
