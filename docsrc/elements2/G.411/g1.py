"""Programmatic construction for Book X, Proposition 87 (X.87)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0185.g1 using geometor.model."""
    model = Model("X.87")

    # Single-letter magnitude segments A, K, E
    A_l = model.set_point(31.0, -16.5, classes=["given"], ID="A")
    A_r = model.set_point(200.0, -16.5, ID="A_r")

    K_l = model.set_point(64.0, -80.5, classes=["given"], ID="K")
    K_r = model.set_point(197.0, -80.5, ID="K_r")

    E_l = model.set_point(106.0, -110.5, classes=["given"], ID="E")
    E_r = model.set_point(192.0, -110.5, ID="E_r")

    # Line FG divided at H
    F = model.set_point(22.0, -44.0, classes=["given"], ID="F")
    H = model.set_point(61.0, -44.0, classes=["given"], ID="H")
    G = model.set_point(245.0, -44.0, classes=["given"], ID="G")

    # Number line BC divided at D
    B = model.set_point(79.0, -137.0, classes=["given"], ID="B")
    D = model.set_point(132.0, -137.0, classes=["given"], ID="D")
    C = model.set_point(228.0, -137.0, classes=["given"], ID="C")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(F, G)
    model.construct_line(K_l, K_r)
    model.construct_line(E_l, E_r)
    model.construct_line(B, C)

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(F, G)
    model.set_segment(F, H)
    model.set_segment(H, G)
    model.set_segment(K_l, K_r)
    model.set_segment(E_l, E_r)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)

    # Collinear sections
    model.set_section([F, H, G])
    model.set_section([B, D, C])

    return model


if __name__ == "__main__":
    construct_g1()
