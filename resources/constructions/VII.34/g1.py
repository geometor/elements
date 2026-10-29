"""Programmatic construction for Book VII, Proposition 34, Case 1 (VII.34 - g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0342.g1 using geometor.model."""
    model = Model("VII.34.g1")

    # Given prime numbers A, B
    A_l = model.set_point(41.0, -17.0, classes=["given"], ID="A")
    A_r = model.set_point(98.0, -17.0, ID="A_r")

    B_l = model.set_point(128.0, -17.0, classes=["given"], ID="B")
    B_r = model.set_point(196.0, -17.0, ID="B_r")

    # Product C and lesser number D
    C_l = model.set_point(43.0, -42.0, classes=["given"], ID="C")
    C_r = model.set_point(199.0, -42.0, ID="C_r")

    D_l = model.set_point(46.0, -65.0, classes=["given"], ID="D")
    D_r = model.set_point(156.0, -65.0, ID="D_r")

    # Unit counts E, F
    E_l = model.set_point(24.0, -95.0, classes=["given"], ID="E")
    E_r = model.set_point(78.0, -95.0, ID="E_r")

    F_l = model.set_point(126.0, -95.0, classes=["given"], ID="F")
    F_r = model.set_point(167.0, -95.0, ID="F_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_g1()
