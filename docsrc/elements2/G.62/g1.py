"""Programmatic construction for Book II, Proposition 1 (II.1).

If there be two straight lines, and one of them be cut into any number of
segments whatever, the rectangle contained by the two straight lines is equal to
the rectangles contained by the uncut straight line and each of the segments.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for Book II, Proposition 1 using geometor.model."""
    model = Model("II.1")

    # Standalone given straight line A
    A1 = model.set_point(105.0, -20.0, classes=["given"], ID="A1")
    A2 = model.set_point(194.0, -20.0, classes=["given"], ID="A2")
    model.set_segment(A1, A2)

    # Straight line BC cut at random at D, E
    B = model.set_point(27.5, -38.5, classes=["given"], ID="B")
    D = model.set_point(136.5, -38.5, classes=["given"], ID="D")
    E = model.set_point(195.5, -38.5, classes=["given"], ID="E")
    C = model.set_point(242.5, -38.5, classes=["given"], ID="C")

    model.construct_line(B, C)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_segment(E, C)
    model.set_segment(B, E)
    model.set_segment(D, C)

    # BF drawn at right angles to BC, with BG = A
    G = model.set_point(27.5, -127.5, ID="G")
    F = model.set_point(27.5, -172.0, ID="F")
    model.construct_line(B, F)
    model.set_segment(B, F)
    model.set_segment(B, G)
    model.set_segment(G, F)

    # Parallel GH to BC through G, and parallels DK, EL, CH to BG through D, E, C
    K = model.set_point(136.5, -127.5, ID="K")
    L = model.set_point(195.5, -127.5, ID="L")
    H = model.set_point(242.5, -127.5, ID="H")

    model.construct_line(G, H)
    model.set_segment(G, H)
    model.set_segment(G, K)
    model.set_segment(K, L)
    model.set_segment(L, H)
    model.set_segment(G, L)
    model.set_segment(K, H)

    model.set_segment(D, K)
    model.set_segment(E, L)
    model.set_segment(C, H)

    # Rectangles BH (BCHG), BK (BDKG), DL (DELK), EH (ECHL)
    model.set_polygon([B, C, H, G])
    model.set_polygon([B, D, K, G])
    model.set_polygon([D, E, L, K])
    model.set_polygon([E, C, H, L])

    return model


if __name__ == "__main__":
    construct_g1()
