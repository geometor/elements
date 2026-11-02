"""Programmatic construction for Book IX, Proposition 9 (IX.9)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0398.g1 using geometor.model."""
    model = Model("IX.9")

    # Single-letter horizontal number segments A, B, C, D, E, F
    A_l = model.set_point(32.0, -19.5, classes=["given"], ID="A")
    A_r = model.set_point(76.0, -19.5, ID="A_r")

    B_l = model.set_point(33.0, -38.5, classes=["given"], ID="B")
    B_r = model.set_point(88.0, -38.5, ID="B_r")

    C_l = model.set_point(33.0, -59.0, classes=["given"], ID="C")
    C_r = model.set_point(111.0, -59.0, ID="C_r")

    D_l = model.set_point(34.0, -79.5, classes=["given"], ID="D")
    D_r = model.set_point(127.0, -79.5, ID="D_r")

    E_l = model.set_point(35.0, -100.5, classes=["given"], ID="E")
    E_r = model.set_point(143.0, -100.5, ID="E_r")

    F_l = model.set_point(37.0, -120.5, classes=["given"], ID="F")
    F_r = model.set_point(169.0, -120.5, ID="F_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_g1()
