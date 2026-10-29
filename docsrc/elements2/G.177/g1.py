"""Programmatic construction for Book VI, Proposition 14 (VI.14).

In equal and equiangular parallelograms the sides about the equal angles are
reciprocally proportional; and equiangular parallelograms in which the sides
about the equal angles are reciprocally proportional are equal.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0223.g1 (VI.14) using geometor.model."""
    model = Model("VI.14")

    # 1. Points
    A = model.set_point(19.0, -163.0, classes=["given"], ID="A")
    D = model.set_point(74.0, -163.0, classes=["given"], ID="D")
    F = model.set_point(47.0, -72.0, classes=["given"], ID="F")
    B = model.set_point(102.0, -72.0, classes=["given"], ID="B")
    G = model.set_point(216.0, -72.0, classes=["given"], ID="G")
    E = model.set_point(115.0, -30.0, classes=["given"], ID="E")
    C = model.set_point(229.0, -30.0, classes=["given"], ID="C")
    H = model.set_point(60.0, -30.0, ID="H")

    # 2. Segments
    model.set_segment(A, D)
    model.set_segment(F, G)
    model.set_segment(F, B)
    model.set_segment(B, G)
    model.set_segment(H, C)
    model.set_segment(H, E)
    model.set_segment(E, C)

    model.set_segment(A, H)
    model.set_segment(A, F)
    model.set_segment(F, H)

    model.set_segment(D, E)
    model.set_segment(D, B)
    model.set_segment(B, E)

    model.set_segment(G, C)

    # 3. Collinear Sections
    model.set_section([F, B, G])
    model.set_section([D, B, E])
    model.set_section([A, F, H])
    model.set_section([H, E, C])

    # 4. Polygons (Parallelograms)
    model.set_polygon([F, A, D, B])
    model.set_polygon([E, B, G, C])
    model.set_polygon([H, F, B, E])

    # 5. Angles / Wedges
    model.set_wedge(B, D, D, F)
    model.set_wedge(B, G, G, E)
    model.set_wedge(B, F, F, E)

    return model


if __name__ == "__main__":
    construct_g1()
