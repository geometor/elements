"""Programmatic construction for Book I, Proposition 8 (I.8).

If two triangles have the two sides equal to two sides respectively, and have
also the base equal to the base, they will also have the angles equal which are
contained by the equal straight lines.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for Book I, Proposition 8 using geometor.model."""
    model = Model("I.8")

    # 1. Triangle ABC
    A = model.set_point(45, -36, classes=["given"], ID="A")
    B = model.set_point(19, -130, classes=["given"], ID="B")
    C = model.set_point(96, -104, classes=["given"], ID="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # 2. Triangle DEF and hypothetical displaced configuration EGF
    D = model.set_point(194, -34, classes=["given"], ID="D")
    E = model.set_point(170, -130, classes=["given"], ID="E")
    F = model.set_point(247, -104, classes=["given"], ID="F")
    G = model.set_point(223, -36, ID="G")

    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_segment(E, G)
    model.set_segment(G, F)

    model.set_polygon([D, E, F])
    model.set_polygon([G, E, F])

    return model


if __name__ == "__main__":
    construct_g1()
