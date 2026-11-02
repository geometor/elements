"""Programmatic construction for Book VII, Proposition 15 (VII.15)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0321.g1 using geometor.model."""
    model = Model("VII.15")

    # Single-letter horizontal unit segment A
    A_l = model.set_point(24.0, -21.0, classes=["given"], ID="A")
    A_r = model.set_point(62.0, -21.0, ID="A_r")

    # Horizontal number segment BC (divided at G and H)
    B = model.set_point(109.0, -23.0, classes=["given"], ID="B")
    G = model.set_point(150.0, -23.0, ID="G")
    H = model.set_point(191.0, -23.0, ID="H")
    C = model.set_point(232.0, -23.0, classes=["given"], ID="C")

    # Single-letter horizontal number segment D
    D_l = model.set_point(99.0, -49.0, classes=["given"], ID="D")
    D_r = model.set_point(177.0, -49.0, ID="D_r")

    # Horizontal number segment EF (divided at K and L)
    E = model.set_point(14.0, -75.0, classes=["given"], ID="E")
    K = model.set_point(96.0, -75.0, ID="K")
    L = model.set_point(178.0, -75.0, ID="L")
    F = model.set_point(260.0, -75.0, classes=["given"], ID="F")

    # Base lines
    model.construct_line(B, C)
    model.construct_line(E, F)

    # Whole and subdivided segments
    model.set_segment(A_l, A_r)
    model.set_segment(B, C)
    model.set_segment(B, G)
    model.set_segment(G, H)
    model.set_segment(H, C)
    model.set_segment(B, H)
    model.set_segment(G, C)

    model.set_segment(D_l, D_r)
    model.set_segment(E, F)
    model.set_segment(E, K)
    model.set_segment(K, L)
    model.set_segment(L, F)
    model.set_segment(E, L)
    model.set_segment(K, F)

    # Collinear sections
    model.set_section([B, G, H])
    model.set_section([G, H, C])
    model.set_section([E, K, L])
    model.set_section([K, L, F])

    return model


if __name__ == "__main__":
    construct_g1()
