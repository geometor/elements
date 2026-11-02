"""Programmatic construction for Book IX, Proposition 21 (IX.21)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0419.g1 using geometor.model."""
    model = Model("IX.21")

    # Subdivided horizontal number segment AE (divided at B, C, D)
    A = model.set_point(13.0, -27.5, classes=["given"], ID="A")
    B = model.set_point(58.0, -27.5, ID="B")
    C = model.set_point(135.0, -27.5, ID="C")
    D = model.set_point(262.0, -27.5, ID="D")
    E = model.set_point(294.0, -27.5, classes=["given"], ID="E")

    # Base line
    model.construct_line(A, E)

    # Whole and subdivided segments on AE
    model.set_segment(A, E)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(C, E)

    # Collinear sections
    model.set_section([A, B, C])
    model.set_section([B, C, D])
    model.set_section([C, D, E])
    model.set_section([A, C, E])

    return model


if __name__ == "__main__":
    construct_g1()
