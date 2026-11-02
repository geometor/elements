"""Programmatic construction for Book IX, Proposition 15 (IX.15)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0410.g1 using geometor.model."""
    model = Model("IX.15")

    # Single-letter horizontal number segments A, B, C
    A_l = model.set_point(33.0, -21.5, classes=["given"], ID="A")
    A_r = model.set_point(68.0, -21.5, ID="A_r")

    B_l = model.set_point(153.0, -21.5, classes=["given"], ID="B")
    B_r = model.set_point(206.0, -21.5, ID="B_r")

    C_l = model.set_point(80.0, -47.5, classes=["given"], ID="C")
    C_r = model.set_point(163.0, -47.5, ID="C_r")

    # Subdivided horizontal number segment DF (divided at E)
    D = model.set_point(86.0, -75.0, classes=["given"], ID="D")
    E = model.set_point(106.0, -75.0, ID="E")
    F = model.set_point(136.0, -75.0, classes=["given"], ID="F")

    # Base line for DF
    model.construct_line(D, F)

    # Number segments A, B, C
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    # Whole and subdivided segments on DF
    model.set_segment(D, F)
    model.set_segment(D, E)
    model.set_segment(E, F)

    # Collinear section
    model.set_section([D, E, F])

    return model


if __name__ == "__main__":
    construct_g1()
