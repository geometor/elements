"""Programmatic construction for Book VI, Proposition 10 (VI.10).

To cut a given uncut straight line similarly to a given cut straight line.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0219.g1 (VI.10) using geometor.model."""
    model = Model("VI.10")

    # 1. Points
    A = model.set_point(19.0, -145.0, classes=["given"], ID="A")
    B = model.set_point(211.0, -145.0, classes=["given"], ID="B")
    C = model.set_point(227.0, -27.0, classes=["given"], ID="C")
    D = model.set_point(71.0, -115.5, classes=["given"], ID="D")
    E = model.set_point(168.76, -60.04, classes=["given"], ID="E")
    F = model.set_point(67.0, -145.0, ID="F")
    G = model.set_point(157.24, -145.0, ID="G")
    H = model.set_point(161.24, -115.5, ID="H")
    K = model.set_point(215.0, -115.5, ID="K")

    # 2. Segments
    model.set_segment(A, B)
    model.set_segment(A, F)
    model.set_segment(F, G)
    model.set_segment(G, B)
    model.set_segment(A, G)
    model.set_segment(F, B)

    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, E)
    model.set_segment(E, C)
    model.set_segment(A, E)
    model.set_segment(D, C)

    model.set_segment(C, B)
    model.set_segment(C, K)
    model.set_segment(K, B)

    model.set_segment(D, F)
    model.set_segment(E, G)
    model.set_segment(E, H)
    model.set_segment(H, G)

    model.set_segment(D, K)
    model.set_segment(D, H)
    model.set_segment(H, K)

    # 3. Collinear Sections
    model.set_section([A, F, G])
    model.set_section([F, G, B])
    model.set_section([A, D, E])
    model.set_section([D, E, C])
    model.set_section([D, H, K])
    model.set_section([E, H, G])
    model.set_section([C, K, B])

    # 4. Polygons (Triangles and Parallelograms)
    model.set_polygon([A, B, C])
    model.set_polygon([A, G, E])
    model.set_polygon([D, K, C])
    model.set_polygon([D, F, G, H])
    model.set_polygon([H, G, B, K])
    model.set_polygon([D, F, B, K])

    return model


if __name__ == "__main__":
    construct_g1()
