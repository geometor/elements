"""Programmatic construction for Book XIII, Proposition 15 (XIII.15).

Left: Semicircle ADB on diameter AB cut at C with AC = 2 CB, perpendicular CD,
and chord DB.
Right: Cube EFGH-KLMN (FN) with side equal to DB, face diagonal EG, and
space diagonal KG equal to sphere diameter AB.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0482.g1 using geometor.model."""
    model = Model("XIII.15")

    # Left: Semicircle ADB on diameter AB (centre (94, -110), radius 78)
    A = model.set_point(16.0, -110.0, classes=["given"], ID="A")
    B = model.set_point(172.0, -110.0, classes=["given"], ID="B")
    C = model.set_point(120.0, -110.0, classes=["constructed"], ID="C")
    D = model.set_point(120.0, -36.5, classes=["constructed"], ID="D")
    O = model.set_point(94.0, -110.0, classes=["auxiliary"], ID="O")
    model.construct_circle(O, A)

    # Right: Cube EFGH-KLMN
    E = model.set_point(274.0, -24.0, classes=["given"], ID="E")
    F = model.set_point(274.0, -116.0, classes=["given"], ID="F")
    G = model.set_point(366.0, -116.0, classes=["given"], ID="G")
    H = model.set_point(366.0, -24.0, classes=["given"], ID="H")

    K = model.set_point(250.0, -42.0, classes=["constructed"], ID="K")
    L = model.set_point(250.0, -134.0, classes=["constructed"], ID="L")
    M = model.set_point(342.0, -134.0, classes=["constructed"], ID="M")
    N = model.set_point(342.0, -42.0, classes=["constructed"], ID="N")

    # Polygons, Squares, and Cube
    model.set_polygon([C, D, B])
    model.set_polygon([E, F, G, H])
    model.set_polygon([K, L, M, N])
    model.set_polygon([E, F, L, K])
    model.set_polygon([K, E, G])
    model.set_polygon([E, F, G])
    model.set_polygon([E, F, G, H, K, L, M, N])

    # Segments
    for p1, p2 in [
        (A, B), (A, C), (C, B), (C, D), (D, B),
        (E, F), (F, G), (G, H), (H, E),
        (K, L), (L, M), (M, N), (N, K),
        (E, K), (F, L), (G, M), (H, N),
        (E, G), (K, G), (F, K),
    ]:
        model.set_segment(p1, p2)

    # Section
    model.set_section([A, C, B])

    # Angles
    model.set_wedge(E, K, K, G)
    model.set_wedge(F, E, E, G)

    return model


if __name__ == "__main__":
    construct_g1()
