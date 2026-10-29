"""Programmatic construction for Book XII, Proposition 13 (XII.13).

Cylinder AD cut by plane GH parallel to opposite planes AB, CD, with axis EF
produced to L and M, and circles PQ, RS, AB, GH, CD, TU, VW about centers
L, N, E, K, F, O, M.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0421.g1 using geometor.model."""
    model = Model("XII.13")

    # Axis centers from left to right
    L = model.set_point(41.0, -60.5, classes=["given"], ID="L")
    N = model.set_point(96.0, -60.5, classes=["given"], ID="N")
    E = model.set_point(158.0, -60.5, classes=["given"], ID="E")
    K = model.set_point(221.0, -60.5, classes=["given"], ID="K")
    F = model.set_point(256.0, -60.5, classes=["given"], ID="F")
    O = model.set_point(289.0, -60.5, classes=["given"], ID="O")
    M = model.set_point(321.0, -60.5, classes=["given"], ID="M")

    # Top generator points
    P = model.set_point(41.0, -25.0, classes=["given"], ID="P")
    R = model.set_point(96.0, -25.0, classes=["given"], ID="R")
    A = model.set_point(158.0, -25.0, classes=["given"], ID="A")
    G = model.set_point(221.0, -25.0, classes=["given"], ID="G")
    C = model.set_point(256.0, -25.0, classes=["given"], ID="C")
    T = model.set_point(289.0, -25.0, classes=["given"], ID="T")
    V = model.set_point(321.0, -25.0, classes=["given"], ID="V")

    # Bottom generator points
    Q = model.set_point(41.0, -96.0, classes=["given"], ID="Q")
    S = model.set_point(96.0, -96.0, classes=["given"], ID="S")
    B = model.set_point(158.0, -96.0, classes=["given"], ID="B")
    H = model.set_point(221.0, -96.0, classes=["given"], ID="H")
    D = model.set_point(256.0, -96.0, classes=["given"], ID="D")
    U = model.set_point(289.0, -96.0, classes=["given"], ID="U")
    W = model.set_point(321.0, -96.0, classes=["given"], ID="W")

    # Circular sections (modeled as circles in 3D, rendered as ellipses in SVG)
    for center, top in [
        (L, P), (N, R), (E, A), (K, G), (F, C), (O, T), (M, V),
    ]:
        model.construct_circle(center, top)

    # Generator segments and axis sub-segments
    for p1, p2 in [
        (P, V), (Q, W),
        (L, N), (N, E), (E, K), (K, F), (F, O), (O, M),
        (E, F), (L, M), (K, L), (K, M),
    ]:
        model.set_segment(p1, p2)

    # Cylindrical sub-regions
    model.set_polygon([A, B, D, C])  # Cylinder AD
    model.set_polygon([A, B, H, G])  # Cylinder BG / GB
    model.set_polygon([G, H, D, C])  # Cylinder GD
    model.set_polygon([P, Q, W, V])  # Cylinder PW
    model.set_polygon([P, Q, S, R])  # Cylinder QR
    model.set_polygon([R, S, B, A])  # Cylinder RB
    model.set_polygon([P, Q, H, G])  # Cylinder QG
    model.set_polygon([G, H, W, V])  # Cylinder WG / GW

    return model


if __name__ == "__main__":
    construct_g1()
