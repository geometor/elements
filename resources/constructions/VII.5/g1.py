"""Programmatic construction for Book VII, Proposition 5 (VII.5)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0310.g1 using geometor.model."""
    model = Model("VII.5")

    # Single-letter vertical number segment A
    A_t = model.set_point(25.0, -54.0, classes=["given"], ID="A")
    A_b = model.set_point(25.0, -102.0, ID="A_b")

    # Vertical number segment BC (divided at G)
    B = model.set_point(49.0, -12.0, classes=["given"], ID="B")
    G = model.set_point(49.0, -60.0, ID="G")
    C = model.set_point(49.0, -108.0, classes=["given"], ID="C")

    # Single-letter vertical number segment D
    D_t = model.set_point(88.0, -62.0, classes=["given"], ID="D")
    D_b = model.set_point(88.0, -97.0, ID="D_b")

    # Vertical number segment EF (divided at H)
    E = model.set_point(116.0, -36.0, classes=["given"], ID="E")
    H = model.set_point(116.0, -72.0, ID="H")
    F = model.set_point(116.0, -108.0, classes=["given"], ID="F")

    # Base lines
    model.construct_line(B, C)
    model.construct_line(E, F)

    # Whole and subdivided segments
    model.set_segment(A_t, A_b)
    model.set_segment(B, C)
    model.set_segment(B, G)
    model.set_segment(G, C)
    model.set_segment(D_t, D_b)
    model.set_segment(E, F)
    model.set_segment(E, H)
    model.set_segment(H, F)

    # Collinear sections
    model.set_section([B, G, C])
    model.set_section([E, H, F])

    return model


if __name__ == "__main__":
    construct_g1()
