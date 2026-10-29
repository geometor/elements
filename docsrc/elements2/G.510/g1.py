"""Programmatic construction for Book XIII, Proposition 3 (XIII.3).

If a straight line be cut in extreme and mean ratio, the square on the lesser
segment added to the half of the greater segment is five times the square on
the half of the greater segment.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for Book XIII, Proposition 3 using geometor.model."""
    model = Model("XIII.3")

    # Straight line AB cut in extreme and mean ratio at C, with AC bisected at D
    A = model.set_point(22.0, -25.0, classes=["given"], ID="A")
    D = model.set_point(87.0, -25.0, classes=["given"], ID="D")
    C = model.set_point(151.0, -25.0, classes=["given"], ID="C")
    B = model.set_point(230.0, -25.0, classes=["given"], ID="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(D, C)
    model.set_segment(C, B)

    # Grid points of square AE on AB
    R = model.set_point(22.0, -109.0, ID="R")
    G = model.set_point(87.0, -109.0, ID="G")
    U = model.set_point(151.0, -109.0, ID="U")
    M = model.set_point(230.0, -109.0, ID="M")

    H = model.set_point(22.0, -173.0, ID="H")
    K = model.set_point(87.0, -173.0, ID="K")
    F = model.set_point(151.0, -173.0, ID="F")
    N = model.set_point(230.0, -173.0, ID="N")

    T = model.set_point(22.0, -238.0, ID="T")
    L = model.set_point(87.0, -238.0, ID="L")
    S = model.set_point(151.0, -238.0, ID="S")
    E = model.set_point(230.0, -238.0, ID="E")

    # Horizontal segments
    model.set_segment(R, M)
    model.set_segment(R, G)
    model.set_segment(G, U)
    model.set_segment(U, M)
    model.set_segment(H, N)
    model.set_segment(H, K)
    model.set_segment(K, F)
    model.set_segment(F, N)
    model.set_segment(T, E)
    model.set_segment(T, L)
    model.set_segment(L, S)
    model.set_segment(S, E)

    # Vertical segments
    model.set_segment(A, T)
    model.set_segment(A, R)
    model.set_segment(R, H)
    model.set_segment(H, T)
    model.set_segment(D, L)
    model.set_segment(D, G)
    model.set_segment(G, K)
    model.set_segment(K, L)
    model.set_segment(C, S)
    model.set_segment(C, U)
    model.set_segment(U, F)
    model.set_segment(F, S)
    model.set_segment(B, E)
    model.set_segment(B, M)
    model.set_segment(M, N)
    model.set_segment(N, E)

    # Diagonal BT
    model.set_segment(B, T)
    model.set_segment(B, U)
    model.set_segment(U, K)
    model.set_segment(K, T)

    # Polygons (squares, rectangles, and gnomon OPQ)
    model.set_polygon([A, B, E, T])
    model.set_polygon([R, U, S, T])
    model.set_polygon([G, U, F, K])
    model.set_polygon([H, K, L, T])
    model.set_polygon([C, B, E, S])
    model.set_polygon([U, M, N, F])
    model.set_polygon([F, N, E, S])
    model.set_polygon([D, C, U, G])
    model.set_polygon([C, B, N, F])
    model.set_polygon([D, B, N, K])
    model.set_polygon([G, D, B, N, F, U])

    return model


if __name__ == "__main__":
    construct_g1()
