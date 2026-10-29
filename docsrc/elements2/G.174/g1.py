"""Programmatic construction for Book VI, Proposition 11 (VI.11).

To two given straight lines to find a third proportional.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0220.g1 (VI.11) using geometor.model."""
    model = Model("VI.11")

    # 1. Points
    A = model.set_point(49.0, -25.0, classes=["given"], ID="A")
    B = model.set_point(37.4, -71.4, classes=["given"], ID="B")
    C = model.set_point(92.2, -86.6, classes=["given"], ID="C")
    D = model.set_point(20.0, -141.0, ID="D")
    E = model.set_point(157.0, -179.0, ID="E")

    # 2. Segments
    model.set_segment(A, D)
    model.set_segment(A, B)
    model.set_segment(B, D)

    model.set_segment(A, E)
    model.set_segment(A, C)
    model.set_segment(C, E)

    model.set_segment(B, C)
    model.set_segment(D, E)

    # 3. Collinear Sections
    model.set_section([A, B, D])
    model.set_section([A, C, E])

    # 4. Polygons
    model.set_polygon([A, D, E])
    model.set_polygon([A, B, C])

    return model


if __name__ == "__main__":
    construct_g1()
