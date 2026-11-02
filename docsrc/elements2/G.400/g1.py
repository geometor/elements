"""Programmatic construction for Book X, Proposition 26 (X.26)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0062.g1 using geometor.model."""
    model = Model("X.26")

    # Left composite rectangle: AB = AC + DB
    A = model.set_point(21.0, -16.5, classes=["given"], ID="A")
    D = model.set_point(21.0, -73.5, ID="D")
    B_l = model.set_point(21.0, -103.5, ID="B_l")
    A_r = model.set_point(122.0, -16.5, ID="A_r")
    C = model.set_point(122.0, -73.5, classes=["given"], ID="C")
    B = model.set_point(122.0, -103.5, classes=["given"], ID="B")

    # Right composite rectangle on EF: FH = FG + KH
    F = model.set_point(167.5, -17.5, classes=["given"], ID="F")
    K = model.set_point(167.5, -95.5, ID="K")
    H_l = model.set_point(167.5, -140.5, ID="H_l")
    E = model.set_point(243.0, -17.5, classes=["given"], ID="E")
    G = model.set_point(243.0, -95.5, ID="G")
    H = model.set_point(243.0, -140.5, ID="H")

    # Base lines
    model.construct_line(A, B_l)
    model.construct_line(A_r, B)
    model.construct_line(A, A_r)
    model.construct_line(D, C)
    model.construct_line(B_l, B)

    model.construct_line(F, H_l)
    model.construct_line(E, H)
    model.construct_line(F, E)
    model.construct_line(K, G)
    model.construct_line(H_l, H)

    # Segments
    model.set_segment(A, D)
    model.set_segment(D, B_l)
    model.set_segment(A, B_l)
    model.set_segment(A_r, C)
    model.set_segment(C, B)
    model.set_segment(A_r, B)
    model.set_segment(A, A_r)
    model.set_segment(D, C)
    model.set_segment(B_l, B)

    model.set_segment(F, E)
    model.set_segment(K, G)
    model.set_segment(H_l, H)
    model.set_segment(E, G)
    model.set_segment(G, H)
    model.set_segment(E, H)
    model.set_segment(F, K)
    model.set_segment(K, H_l)
    model.set_segment(F, H_l)

    # Collinear section on EH
    model.set_section([E, G, H])

    # Polygons
    model.set_polygon([A, A_r, B, B_l])
    model.set_polygon([A, A_r, C, D])
    model.set_polygon([D, C, B, B_l])
    model.set_polygon([F, E, H, H_l])
    model.set_polygon([F, E, G, K])
    model.set_polygon([K, G, H, H_l])

    return model


if __name__ == "__main__":
    construct_g1()
