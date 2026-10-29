"""Programmatic construction for Book X, Proposition 88 (X.88)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0188.g1 using geometor.model."""
    model = Model("X.88")

    # Single-letter magnitude segments A and H
    A_l = model.set_point(28.0, -20.5, classes=["given"], ID="A")
    A_r = model.set_point(126.0, -20.5, ID="A_r")

    H_l = model.set_point(25.0, -54.0, classes=["given"], ID="H")
    H_r = model.set_point(136.0, -54.0, ID="H_r")

    # Line BG divided at C
    B = model.set_point(259.0, -20.5, classes=["given"], ID="B")
    C = model.set_point(312.0, -20.5, classes=["given"], ID="C")
    G = model.set_point(387.0, -20.5, classes=["given"], ID="G")

    # Number line DE divided at F
    D = model.set_point(231.0, -55.0, classes=["given"], ID="D")
    F = model.set_point(352.0, -55.0, classes=["given"], ID="F")
    E = model.set_point(412.0, -55.0, classes=["given"], ID="E")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B, G)
    model.construct_line(H_l, H_r)
    model.construct_line(D, E)

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B, G)
    model.set_segment(B, C)
    model.set_segment(C, G)
    model.set_segment(H_l, H_r)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(F, E)

    # Collinear sections
    model.set_section([B, C, G])
    model.set_section([D, F, E])

    return model


if __name__ == "__main__":
    construct_g1()
