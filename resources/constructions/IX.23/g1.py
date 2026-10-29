"""Programmatic construction for Book IX, Proposition 23 (IX.23)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0420.g2 using geometor.model."""
    model = Model("IX.23")

    # Subdivided horizontal number segment AD (divided at B, C, E)
    A = model.set_point(13.0, -26.5, classes=["given"], ID="A")
    B = model.set_point(63.0, -26.5, ID="B")
    C = model.set_point(177.0, -26.5, ID="C")
    E = model.set_point(237.0, -26.5, ID="E")
    D = model.set_point(254.0, -26.5, classes=["given"], ID="D")

    # Base line
    model.construct_line(A, D)

    # Whole and subdivided segments on AD
    model.set_segment(A, D)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(B, E)
    model.set_segment(B, D)

    # Collinear sections
    model.set_section([A, B, C])
    model.set_section([B, C, D])
    model.set_section([C, E, D])
    model.set_section([A, C, E])
    model.set_section([A, E, D])

    return model


if __name__ == "__main__":
    construct_g1()
