"""Programmatic construction for Book VII, Proposition 18 (VII.18)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0324.g1 using geometor.model."""
    model = Model("VII.18")

    # Single-letter horizontal number segments C, A, B, D, E
    C_l = model.set_point(23.0, -14.0, classes=["given"], ID="C")
    C_r = model.set_point(58.0, -14.0, ID="C_r")

    A_l = model.set_point(101.0, -14.0, classes=["given"], ID="A")
    A_r = model.set_point(181.0, -14.0, ID="A_r")

    B_l = model.set_point(102.0, -35.0, classes=["given"], ID="B")
    B_r = model.set_point(217.0, -35.0, ID="B_r")

    D_l = model.set_point(102.0, -55.0, classes=["given"], ID="D")
    D_r = model.set_point(197.0, -55.0, ID="D_r")

    E_l = model.set_point(102.0, -80.0, classes=["given"], ID="E")
    E_r = model.set_point(245.0, -80.0, ID="E_r")

    # Number segments
    model.set_segment(C_l, C_r)
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_g1()
