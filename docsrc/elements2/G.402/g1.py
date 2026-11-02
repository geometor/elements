"""Programmatic construction for Book X, Proposition 28 (X.28)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0065.g1 using geometor.model."""
    model = Model("X.28")

    # Rational straight lines A, B, C and medial straight lines D, E
    A_l = model.set_point(31.0, -18.0, classes=["given"], ID="A")
    A_r = model.set_point(111.0, -18.0, classes=["given"], ID="A_r")

    B_l = model.set_point(30.0, -43.5, classes=["given"], ID="B")
    B_r = model.set_point(156.0, -43.5, classes=["given"], ID="B_r")

    C_l = model.set_point(28.0, -65.5, classes=["given"], ID="C")
    C_r = model.set_point(189.0, -65.5, classes=["given"], ID="C_r")

    D_l = model.set_point(218.0, -35.5, ID="D")
    D_r = model.set_point(319.0, -35.5, ID="D_r")

    E_l = model.set_point(218.0, -59.0, ID="E")
    E_r = model.set_point(347.0, -59.0, ID="E_r")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B_l, B_r)
    model.construct_line(C_l, C_r)
    model.construct_line(D_l, D_r)
    model.construct_line(E_l, E_r)

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
