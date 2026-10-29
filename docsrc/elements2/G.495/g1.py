"""Programmatic construction for Book XII, Proposition 9 (XII.9)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0402.g1 using geometor.model."""
    model = Model("XII.9")

    # First parallelepiped BGML and pyramid ABCG
    B = model.set_point(16.0, -156.0, classes=["given"], ID="B")
    A = model.set_point(58.0, -126.0, classes=["given"], ID="A")
    M = model.set_point(174.0, -126.0, ID="M")
    C = model.set_point(132.0, -156.0, classes=["given"], ID="C")
    G = model.set_point(26.0, -62.0, classes=["given"], ID="G")
    K = model.set_point(68.0, -32.0, classes=["given"], ID="K")
    L = model.set_point(184.0, -32.0, ID="L")
    N = model.set_point(142.0, -62.0, ID="N")

    # Second parallelepiped EHQP and pyramid DEFH
    E = model.set_point(262.0, -152.0, classes=["given"], ID="E")
    D = model.set_point(350.0, -152.0, classes=["given"], ID="D")
    Q = model.set_point(379.0, -198.0, ID="Q")
    F = model.set_point(291.0, -198.0, classes=["given"], ID="F")
    H = model.set_point(298.0, -22.0, classes=["given"], ID="H")
    O = model.set_point(386.0, -22.0, ID="O")
    P = model.set_point(415.0, -68.0, ID="P")
    R = model.set_point(327.0, -68.0, ID="R")

    # Edges of first parallelepiped and pyramid
    for p1, p2 in [
        (B, A), (A, M), (M, C), (C, B),
        (G, K), (K, L), (L, N), (N, G),
        (B, G), (A, K), (M, L), (C, N),
        (A, C), (G, A), (G, C),
    ]:
        model.set_segment(p1, p2)

    # Edges of second parallelepiped and pyramid
    for p1, p2 in [
        (E, D), (D, Q), (Q, F), (F, E),
        (H, O), (O, P), (P, R), (R, H),
        (E, H), (D, O), (Q, P), (F, R),
        (F, D), (H, F), (H, D),
    ]:
        model.set_segment(p1, p2)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([B, C, M, A])
    model.set_polygon([E, F, Q, D])

    return model


if __name__ == "__main__":
    construct_g1()
