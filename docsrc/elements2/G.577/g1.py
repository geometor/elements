"""Programmatic construction for Book XII, Proposition 17 (XII.17).

Two concentric spheres about center A, with great circle BCDE in the outer
sphere, circle FGH in the inner sphere, perpendicular semicircles BOD and KON,
and polyhedral facets KBPS, SPQT, TQRU, URO.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0429.g1 using geometor.model."""
    model = Model("XII.17")

    # Center A and main poles/diameters
    A = model.set_point(250.0, -252.5, classes=["given"], ID="A")
    O = model.set_point(250.0, -23.5, classes=["given"], ID="O")
    B = model.set_point(479.0, -252.5, classes=["given"], ID="B")
    D = model.set_point(21.0, -252.5, classes=["given"], ID="D")

    # Inner sphere circle FGH points
    G = model.set_point(386.0, -252.5, classes=["given"], ID="G")
    H = model.set_point(281.9, -205.0, classes=["given"], ID="H")
    F = model.set_point(218.1, -300.0, classes=["given"], ID="F")

    # Equatorial ellipse BCDE points
    C = model.set_point(312.0, -160.1, classes=["given"], ID="C")
    E = model.set_point(188.0, -344.9, classes=["given"], ID="E")
    M = model.set_point(265.0, -348.3, classes=["given"], ID="M")
    L = model.set_point(340.0, -340.8, classes=["given"], ID="L")
    K = model.set_point(412.4, -320.2, classes=["given"], ID="K")
    N = model.set_point(87.6, -184.8, classes=["given"], ID="N")

    # Quadrant BO points
    R = model.set_point(337.6, -40.9, classes=["given"], ID="R")
    Q = model.set_point(411.9, -90.6, classes=["given"], ID="Q")
    P = model.set_point(461.6, -164.9, classes=["given"], ID="P")

    # Quadrant KO points
    U = model.set_point(331.0, -51.2, classes=["given"], ID="U")
    T = model.set_point(388.0, -118.9, classes=["given"], ID="T")
    S = model.set_point(416.8, -207.2, classes=["given"], ID="S")

    # Foot of perpendiculars and auxiliary points V, W, Z, X
    V = model.set_point(461.6, -252.5, classes=["given"], ID="V")
    W = model.set_point(401.6, -315.7, classes=["given"], ID="W")
    Z = model.set_point(456.0, -252.5, classes=["given"], ID="Z")
    X = model.set_point(445.0, -232.0, classes=["given"], ID="X")

    # Concentric spheres / circles
    model.construct_circle(A, B)
    model.construct_circle(A, G)

    # Segments
    for p1, p2 in [
        (D, A), (A, G), (G, Z), (Z, V), (V, B),
        (D, B), (A, B), (A, V), (B, V), (D, Z), (B, Z), (A, Z),
        (C, H), (H, A), (A, F), (F, E), (C, E),
        (N, A), (A, W), (W, K), (A, K), (K, N),
        (A, O),
        (B, K), (K, L), (L, M), (M, E),
        (B, P), (P, Q), (Q, R), (R, O),
        (K, S), (S, T), (T, U), (U, O),
        (S, P), (T, Q), (U, R),
        (P, V), (S, W), (W, V),
        (A, X), (B, X), (K, X),
        (K, Z), (K, D),
    ]:
        model.set_segment(p1, p2)

    # Polyhedral facets
    model.set_polygon([K, B, P, S])
    model.set_polygon([S, P, Q, T])
    model.set_polygon([T, Q, R, U])
    model.set_polygon([U, R, O])

    return model


if __name__ == "__main__":
    construct_g1()
