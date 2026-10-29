"""Programmatic construction for Book VII, Proposition 19 (VII.19)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0325.g1 using geometor.model."""
    model = Model("VII.19")

    # Single-letter vertical number segments A, B, C, D, E, F, G
    A_t = model.set_point(22.0, -33.0, classes=["given"], ID="A")
    A_b = model.set_point(22.0, -155.0, ID="A_b")

    B_t = model.set_point(46.0, -35.0, classes=["given"], ID="B")
    B_b = model.set_point(46.0, -113.0, ID="B_b")

    C_t = model.set_point(70.0, -34.0, classes=["given"], ID="C")
    C_b = model.set_point(70.0, -127.0, ID="C_b")

    D_t = model.set_point(96.0, -35.0, classes=["given"], ID="D")
    D_b = model.set_point(96.0, -98.0, ID="D_b")

    E_t = model.set_point(126.0, -37.0, classes=["given"], ID="E")
    E_b = model.set_point(126.0, -189.0, ID="E_b")

    F_t = model.set_point(154.0, -39.0, classes=["given"], ID="F")
    F_b = model.set_point(154.0, -188.0, ID="F_b")

    G_t = model.set_point(180.0, -10.0, classes=["given"], ID="G")
    G_b = model.set_point(180.0, -237.0, ID="G_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)
    model.set_segment(E_t, E_b)
    model.set_segment(F_t, F_b)
    model.set_segment(G_t, G_b)

    return model


if __name__ == "__main__":
    construct_g1()
