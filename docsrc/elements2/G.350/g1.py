"""Programmatic construction for Book IX, Proposition 20 (IX.20)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0418.g1 using geometor.model."""
    model = Model("IX.20")

    # Single-letter horizontal number segments A, B, C, G
    A_l = model.set_point(28.0, -16.5, classes=["given"], ID="A")
    A_r = model.set_point(47.0, -16.5, ID="A_r")

    B_l = model.set_point(30.0, -37.5, classes=["given"], ID="B")
    B_r = model.set_point(53.0, -37.5, ID="B_r")

    C_l = model.set_point(29.0, -64.0, classes=["given"], ID="C")
    C_r = model.set_point(68.0, -64.0, ID="C_r")

    G_l = model.set_point(181.0, -38.5, classes=["given"], ID="G")
    G_r = model.set_point(250.0, -38.5, ID="G_r")

    # Subdivided horizontal number segment EF (divided at D, where ED = DE and DF = unit)
    E = model.set_point(27.0, -88.0, classes=["given"], ID="E")
    D = model.set_point(258.0, -88.0, ID="D")
    F = model.set_point(267.0, -88.0, classes=["given"], ID="F")

    # Base line for EF
    model.construct_line(E, F)

    # Number segments A, B, C, G
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(G_l, G_r)

    # Whole and subdivided segments on EF
    model.set_segment(E, F)
    model.set_segment(E, D)
    model.set_segment(D, F)

    # Collinear section
    model.set_section([E, D, F])

    return model


if __name__ == "__main__":
    construct_g1()
