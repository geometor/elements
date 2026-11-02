"""Programmatic construction for Book X, Proposition 5 (X.5)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the magnitude/number bars A, B, C, D, E for Book X, Proposition 5 (X.5)."""
    model = Model("X.5")

    # Single-letter magnitudes A, B, C and numbers D, E
    A_l = model.set_point(18.0, -25.5, classes=["given"], ID="A")
    A_r = model.set_point(144.0, -25.5, ID="A_r")

    B_l = model.set_point(186.0, -25.5, classes=["given"], ID="B")
    B_r = model.set_point(267.0, -25.5, ID="B_r")

    C_l = model.set_point(302.0, -26.5, ID="C")
    C_r = model.set_point(344.0, -26.5, ID="C_r")

    D_l = model.set_point(100.0, -49.5, ID="D")
    D_r = model.set_point(162.0, -49.5, ID="D_r")

    E_l = model.set_point(108.0, -73.5, ID="E")
    E_r = model.set_point(141.0, -73.5, ID="E_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
