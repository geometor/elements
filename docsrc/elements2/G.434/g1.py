"""Programmatic construction for Book X, Proposition 54 (X.54)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0121.g1 using geometor.model."""
    model = Model("X.54")

    # Left rectangle ABCD divided by vertical segments GH, EK, FL
    A = model.set_point(20.5, -18.5, classes=["given"], ID="A")
    G = model.set_point(120.0, -18.5, ID="G")
    E = model.set_point(136.5, -18.5, classes=["given"], ID="E")
    F = model.set_point(180.5, -18.5, ID="F")
    D = model.set_point(220.5, -18.5, classes=["given"], ID="D")

    B = model.set_point(20.5, -69.5, classes=["given"], ID="B")
    H = model.set_point(120.0, -69.5, ID="H")
    K = model.set_point(136.5, -69.5, ID="K")
    L = model.set_point(180.5, -69.5, ID="L")
    C = model.set_point(220.5, -69.5, classes=["given"], ID="C")

    # Right square SQ divided by MO and RP intersecting at N
    Q_tl = model.set_point(309.5, -18.5, ID="Q_tl")
    R = model.set_point(383.5, -18.5, ID="R")
    Q = model.set_point(416.0, -18.5, ID="Q")

    M = model.set_point(309.5, -51.5, ID="M")
    N = model.set_point(383.5, -51.5, ID="N")
    O = model.set_point(416.0, -51.5, ID="O")

    S = model.set_point(309.5, -123.5, ID="S")
    P = model.set_point(383.5, -123.5, ID="P")
    S_br = model.set_point(416.0, -123.5, ID="S_br")

    # Base lines
    for p1, p2 in [
        (A, D), (B, C), (A, B), (G, H), (E, K), (F, L), (D, C),
        (Q_tl, Q), (M, O), (S, S_br), (Q_tl, S), (R, P), (Q, S_br),
    ]:
        model.construct_line(p1, p2)

    # Top and bottom segments of ABCD
    top_pts = [A, G, E, F, D]
    bot_pts = [B, H, K, L, C]
    for pts in (top_pts, bot_pts):
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                model.set_segment(pts[i], pts[j])

    # Vertical segments of ABCD
    for p1, p2 in [(A, B), (G, H), (E, K), (F, L), (D, C)]:
        model.set_segment(p1, p2)

    # Segments of square SQ
    for p1, p2 in [
        (Q_tl, Q), (Q_tl, R), (R, Q),
        (M, O), (M, N), (N, O),
        (S, S_br), (S, P), (P, S_br),
        (Q_tl, S), (Q_tl, M), (M, S),
        (R, P), (R, N), (N, P),
        (Q, S_br), (Q, O), (O, S_br),
    ]:
        model.set_segment(p1, p2)

    # Key collinear sections
    model.set_section([A, G, E])
    model.set_section([A, E, D])
    model.set_section([E, F, D])
    model.set_section([M, N, O])
    model.set_section([R, N, P])

    # Polygons (rectangles and squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, H, G])
    model.set_polygon([G, H, K, E])
    model.set_polygon([E, K, L, F])
    model.set_polygon([F, L, C, D])
    model.set_polygon([E, K, C, D])
    model.set_polygon([S, S_br, Q, Q_tl])
    model.set_polygon([S, P, N, M])
    model.set_polygon([N, O, Q, R])
    model.set_polygon([M, N, R, Q_tl])
    model.set_polygon([P, S_br, O, N])

    return model


if __name__ == "__main__":
    construct_g1()
