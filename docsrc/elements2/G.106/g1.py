"""Programmatic construction for Book III, Proposition 27 (III.27)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0064.g1 using geometor.model."""
    model = Model("III.27")

    # Left circle ABC with center G and point K (y-inverted)
    G = model.set_point(83.00, -86.00, ID="G")
    A = model.set_point(40.00, -37.26, classes=["given"], ID="A")
    B = model.set_point(28.88, -122.00, classes=["given"], ID="B")
    C = model.set_point(137.12, -122.00, classes=["given"], ID="C")
    K = model.set_point(120.63, -139.00, ID="K")

    # Right circle DEF with center H (y-inverted)
    H = model.set_point(244.00, -92.00, ID="H")
    D = model.set_point(218.00, -32.43, classes=["given"], ID="D")
    E = model.set_point(189.88, -128.00, classes=["given"], ID="E")
    F = model.set_point(298.12, -128.00, classes=["given"], ID="F")

    # Equal circles ABC and DEF
    model.construct_circle(G, A)
    model.construct_circle(H, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, G)
    model.set_segment(G, C)
    model.set_segment(G, K)

    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, H)
    model.set_segment(H, F)

    # Angles (wedges)
    model.set_wedge(G, B, B, C)
    model.set_wedge(G, B, B, K)
    model.set_wedge(H, E, E, F)
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, E, E, F)

    return model


if __name__ == "__main__":
    construct_g1()
