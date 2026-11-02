"""Programmatic construction for Book X, Proposition 6 (X.6)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the magnitude/number bars A, B, C, D, E, F for Book X, Proposition 6 (X.6)."""
    model = Model("X.6")

    # Single-letter magnitudes A, B, C, F and numbers D, E
    A_l = model.set_point(14.0, -19.0, classes=["given"], ID="A")
    A_1 = model.set_point(56.0, -19.0, ID="A_1")
    A_2 = model.set_point(98.0, -19.0, ID="A_2")
    A_r = model.set_point(140.0, -19.0, ID="A_r")

    B_l = model.set_point(193.0, -18.5, classes=["given"], ID="B")
    B_r = model.set_point(270.0, -18.5, ID="B_r")

    C_l = model.set_point(326.0, -18.0, ID="C")
    C_r = model.set_point(370.0, -18.0, ID="C_r")

    D_l = model.set_point(104.0, -43.0, classes=["given"], ID="D")
    D_r = model.set_point(172.0, -43.0, ID="D_r")

    E_l = model.set_point(104.0, -65.5, classes=["given"], ID="E")
    E_r = model.set_point(149.0, -65.5, ID="E_r")

    F_l = model.set_point(249.0, -64.5, ID="F")
    F_r = model.set_point(321.0, -64.5, ID="F_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    # Subdivisions of A
    model.set_section([A_l, A_1, A_2])
    model.set_section([A_1, A_2, A_r])

    return model


if __name__ == "__main__":
    construct_g1()
