"""Programmatic construction for Book V, Proposition 3 (V.3)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0147.g1 using geometor.model."""
    model = Model("V.3")

    # Single-letter magnitudes A, B, C, D
    A_l = model.set_point(33.0, -20.0, classes=["given"], ID="A")
    A_r = model.set_point(183.0, -20.0, ID="A_r")
    B_l = model.set_point(33.0, -49.0, classes=["given"], ID="B")
    B_r = model.set_point(83.0, -49.0, ID="B_r")
    C_l = model.set_point(33.0, -107.0, classes=["given"], ID="C")
    C_r = model.set_point(135.0, -107.0, ID="C_r")
    D_l = model.set_point(33.0, -132.0, classes=["given"], ID="D")
    D_r = model.set_point(67.0, -132.0, ID="D_r")

    # Subdivided magnitudes EF (at K) and GH (at L)
    E = model.set_point(33.0, -80.0, classes=["given"], ID="E")
    K = model.set_point(183.0, -80.0, ID="K")
    F = model.set_point(328.0, -80.0, classes=["given"], ID="F")

    G = model.set_point(33.0, -160.0, classes=["given"], ID="G")
    L = model.set_point(135.0, -160.0, ID="L")
    H = model.set_point(237.0, -160.0, classes=["given"], ID="H")

    # Base lines
    model.construct_line(E, F)
    model.construct_line(G, H)

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(E, F)
    model.set_segment(E, K)
    model.set_segment(K, F)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(G, H)
    model.set_segment(G, L)
    model.set_segment(L, H)

    # Collinear sections
    model.set_section([E, K, F])
    model.set_section([G, L, H])

    return model


if __name__ == "__main__":
    construct_g1()
