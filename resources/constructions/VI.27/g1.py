"""Programmatic construction for Book VI, Proposition 27 (VI.27).

Of all the parallelograms applied to the same straight line AB and deficient by
parallelogrammic figures similar and similarly situated to DB described on the
half CB, the parallelogram AD applied to the half is greatest.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0263.g1 (VI.27) using geometor.model."""
    model = Model("VI.27")

    # 1. Grid of points for the applied parallelograms on AB
    A2 = model.set_point(20.0, -29.0, ID="A2")
    D = model.set_point(104.0, -29.0, classes=["given"], ID="D")
    N2 = model.set_point(129.0, -29.0, ID="N2")
    E = model.set_point(186.0, -29.0, classes=["given"], ID="E")

    G = model.set_point(26.0, -60.0, ID="G")
    L2 = model.set_point(110.0, -60.0, ID="L2")
    F = model.set_point(135.0, -60.0, ID="F")
    H = model.set_point(192.0, -60.0, ID="H")

    A = model.set_point(41.0, -132.0, classes=["given"], ID="A")
    C = model.set_point(125.0, -132.0, classes=["given"], ID="C")
    K = model.set_point(150.0, -132.0, ID="K")
    B = model.set_point(207.0, -132.0, classes=["given"], ID="B")

    # 2. Construction lines
    model.construct_line(A, B)
    model.construct_line(G, H)
    model.construct_line(A2, E)
    model.construct_line(D, C)
    model.construct_line(N2, K)
    model.construct_line(D, B)

    # 3. Segments and sub-segments
    model.set_segment(A2, E)
    model.set_segment(A2, D)
    model.set_segment(D, N2)
    model.set_segment(N2, E)
    model.set_segment(D, E)

    model.set_segment(G, H)
    model.set_segment(G, L2)
    model.set_segment(L2, F)
    model.set_segment(F, H)
    model.set_segment(G, F)
    model.set_segment(L2, H)

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, K)
    model.set_segment(K, B)
    model.set_segment(A, K)
    model.set_segment(C, B)

    model.set_segment(A2, A)
    model.set_segment(A2, G)
    model.set_segment(G, A)

    model.set_segment(D, C)
    model.set_segment(D, L2)
    model.set_segment(L2, C)

    model.set_segment(N2, K)
    model.set_segment(N2, F)
    model.set_segment(F, K)

    model.set_segment(E, B)
    model.set_segment(E, H)
    model.set_segment(H, B)

    model.set_segment(D, B)
    model.set_segment(D, F)
    model.set_segment(F, B)

    # 4. Parallelograms AD, DB, AF, FB, CF, FE, CH, KE (EK), CG (GC)
    model.set_polygon([A2, D, C, A])
    model.set_polygon([D, E, B, C])
    model.set_polygon([G, F, K, A])
    model.set_polygon([F, H, B, K])
    model.set_polygon([L2, F, K, C])
    model.set_polygon([N2, E, H, F])
    model.set_polygon([L2, H, B, C])
    model.set_polygon([N2, E, B, K])
    model.set_polygon([G, L2, C, A])
    model.set_polygon([D, N2, F, L2])

    # 5. L-shaped Gnomon LMN inside DB around D-N2-F-L2
    model.set_polygon([N2, E, B, C, L2, F])

    return model


if __name__ == "__main__":
    construct_g1()
