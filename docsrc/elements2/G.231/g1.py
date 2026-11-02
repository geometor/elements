"""Programmatic construction for Book VI, Proposition 19 (VI.19).

Similar triangles ABC and DEF, with third proportional BG to BC, EF and AG joined.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0238.g2 (VI.19) using geometor.model."""
    model = Model("VI.19")

    # 1. Points
    A = model.set_point(101.0, -27.0, classes=["given"], ID="A")
    B = model.set_point(21.0, -123.0, classes=["given"], ID="B")
    G = model.set_point(74.0, -123.0, classes=["given"], ID="G")
    C = model.set_point(146.0, -123.0, classes=["given"], ID="C")

    D = model.set_point(272.0, -56.0, classes=["given"], ID="D")
    E = model.set_point(221.0, -124.0, classes=["given"], ID="E")
    F = model.set_point(300.0, -124.0, classes=["given"], ID="F")

    # 2. Construction Lines
    model.construct_line(B, C)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, G)
    model.set_segment(B, C)
    model.set_segment(B, G)
    model.set_segment(G, C)

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(D, F)

    # 4. Collinear Sections
    model.set_section([B, G, C])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, G])
    model.set_polygon([A, G, C])
    model.set_polygon([D, E, F])

    # 6. Angles / Wedges
    model.set_wedge(B, A, A, C)
    model.set_wedge(E, D, D, F)

    return model


if __name__ == "__main__":
    construct_g1()
