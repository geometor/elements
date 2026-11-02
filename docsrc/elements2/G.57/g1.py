"""Programmatic construction for Book I, Proposition 30 (I.30).

Straight lines parallel to the same straight line are also parallel to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for Book I, Proposition 30 (I.30) using geometor.model."""
    model = Model("I.30")

    A = model.set_point(24, -53.5, classes=["given"], ID="A")
    B = model.set_point(175, -53.5, classes=["given"], ID="B")
    E = model.set_point(24, -84, classes=["given"], ID="E")
    F = model.set_point(175, -84, classes=["given"], ID="F")
    C = model.set_point(24, -123.5, classes=["given"], ID="C")
    D = model.set_point(175, -123.5, classes=["given"], ID="D")

    G = model.set_point(117.5, -53.5, ID="G")
    H = model.set_point(105.5, -84, ID="H")
    K = model.set_point(89.5, -123.5, ID="K")

    model.construct_line(A, B)
    model.construct_line(E, F)
    model.construct_line(C, D)
    model.construct_line(G, K)

    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, B)
    model.set_section([A, G, B])

    model.set_segment(E, F)
    model.set_segment(E, H)
    model.set_segment(H, F)
    model.set_section([E, H, F])

    model.set_segment(C, D)
    model.set_segment(C, K)
    model.set_segment(K, D)
    model.set_section([C, K, D])

    model.set_segment(G, K)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_section([G, H, K])

    model.set_polygon([A, G, H, E])
    model.set_polygon([G, B, F, H])
    model.set_polygon([E, H, K, C])
    model.set_polygon([H, F, D, K])

    # Angles: < A G K ), < G H F ), < G K D )
    model.set_wedge(G, A, A, K)
    model.set_wedge(H, G, G, F)
    model.set_wedge(K, G, G, D)

    return model


if __name__ == "__main__":
    construct_g1()
