"""Programmatic construction for Book X, Proposition 104 (X.104)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0235.g1 using geometor.model."""
    model = Model("X.104")

    # Line AE divided at B
    A = model.set_point(32.0, -22.5, classes=["given"], ID="A")
    B = model.set_point(91.0, -22.5, classes=["given"], ID="B")
    E = model.set_point(148.0, -22.5, classes=["given"], ID="E")

    # Line CF divided at D
    C = model.set_point(16.0, -51.5, classes=["given"], ID="C")
    D = model.set_point(91.0, -51.5, classes=["given"], ID="D")
    F = model.set_point(168.0, -51.5, classes=["given"], ID="F")

    # Base lines
    model.construct_line(A, E)
    model.construct_line(C, F)

    # Segments
    model.set_segment(A, E)
    model.set_segment(A, B)
    model.set_segment(B, E)
    model.set_segment(C, F)
    model.set_segment(C, D)
    model.set_segment(D, F)

    # Sections
    model.set_section([A, B, E])
    model.set_section([C, D, F])

    return model


if __name__ == "__main__":
    construct_g1()
