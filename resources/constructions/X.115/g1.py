"""Programmatic construction for Book X, Proposition 115 (X.115)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0258.g1 using geometor.model."""
    model = Model("X.115")

    # Four single-letter magnitude segments A, B, C, D
    A_l = model.set_point(30.0, -19.5, classes=["given"], ID="A")
    A_r = model.set_point(123.0, -19.5, ID="A_r")

    B_l = model.set_point(30.0, -48.5, classes=["given"], ID="B")
    B_r = model.set_point(268.0, -48.5, ID="B_r")

    C_l = model.set_point(29.0, -76.5, ID="C")
    C_r = model.set_point(214.0, -76.5, ID="C_r")

    D_l = model.set_point(30.0, -109.5, ID="D")
    D_r = model.set_point(239.0, -109.5, ID="D_r")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B_l, B_r)
    model.construct_line(C_l, C_r)
    model.construct_line(D_l, D_r)

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_g1()
