"""Programmatic construction for Book VII, Proposition 38 (VII.38)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0348.g1 using geometor.model."""
    model = Model("VII.38")

    # Number A, part B, homonymous number C, and unit D
    A_l = model.set_point(19.0, -14.0, classes=["given"], ID="A")
    A_r = model.set_point(163.0, -14.0, ID="A_r")

    B_l = model.set_point(21.0, -40.0, classes=["given"], ID="B")
    B_r = model.set_point(95.0, -40.0, ID="B_r")

    C_l = model.set_point(21.0, -62.0, classes=["given"], ID="C")
    C_r = model.set_point(72.0, -62.0, ID="C_r")

    D_l = model.set_point(23.0, -86.0, classes=["given"], ID="D")
    D_r = model.set_point(46.0, -86.0, ID="D_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_g1()
