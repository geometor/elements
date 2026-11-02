"""Programmatic construction for Book X, Proposition 112 (X.112)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0247.g1 using geometor.model."""
    model = Model("X.112")

    # Single-letter magnitude segments A and G
    A_l = model.set_point(18.0, -20.5, classes=["given"], ID="A")
    A_r = model.set_point(138.0, -20.5, ID="A_r")

    G_l = model.set_point(247.0, -46.5, classes=["given"], ID="G")
    G_r = model.set_point(563.0, -46.5, ID="G_r")

    # Line BC divided at D
    B = model.set_point(18.0, -50.5, classes=["given"], ID="B")
    D = model.set_point(72.0, -50.5, classes=["given"], ID="D")
    C = model.set_point(183.0, -50.5, classes=["given"], ID="C")

    # Line KH divided at E and F
    K = model.set_point(76.0, -85.5, ID="K")
    E = model.set_point(142.0, -85.5, ID="E")
    F = model.set_point(232.0, -85.5, ID="F")
    H = model.set_point(455.0, -85.5, ID="H")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B, C)
    model.construct_line(G_l, G_r)
    model.construct_line(K, H)

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(G_l, G_r)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(K, H)
    model.set_segment(K, F)
    model.set_segment(K, E)
    model.set_segment(E, H)
    model.set_segment(E, F)
    model.set_segment(F, H)

    # Sections
    model.set_section([B, D, C])
    model.set_section([K, E, F])
    model.set_section([K, F, H])
    model.set_section([E, F, H])

    return model


if __name__ == "__main__":
    construct_g1()
