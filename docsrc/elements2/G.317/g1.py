"""Programmatic construction for Book X, Proposition 4 (X.4)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the magnitude bars A, B, C, D, E, F for Book X, Proposition 4 (X.4)."""
    model = Model("X.4")

    # Single-letter magnitudes A, B, C, D, E, F
    A_l = model.set_point(29.0, -21.5, classes=["given"], ID="A")
    A_r = model.set_point(161.0, -21.5, ID="A_r")

    B_l = model.set_point(28.0, -44.5, classes=["given"], ID="B")
    B_r = model.set_point(115.0, -44.5, ID="B_r")

    C_l = model.set_point(27.0, -66.5, classes=["given"], ID="C")
    C_r = model.set_point(95.0, -66.5, ID="C_r")

    D_l = model.set_point(48.0, -95.5, ID="D")
    D_r = model.set_point(93.0, -95.5, ID="D_r")

    E_l = model.set_point(130.0, -95.5, ID="E")
    E_r = model.set_point(152.0, -95.5, ID="E_r")

    F_l = model.set_point(175.0, -95.5, ID="F")
    F_r = model.set_point(206.0, -95.5, ID="F_r")

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
