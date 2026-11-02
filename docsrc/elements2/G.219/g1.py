"""Programmatic construction for Book VI, Proposition 9 (VI.9).

From a given straight line to cut off a prescribed part.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0218.g1 (VI.9) using geometor.model."""
    model = Model("VI.9")

    # 1. Points
    A = model.set_point(19.0, -118.0, classes=["given"], ID="A")
    B = model.set_point(182.0, -118.0, classes=["given"], ID="B")
    C = model.set_point(129.0, -40.0, ID="C")
    D = model.set_point(55.67, -92.0, ID="D")
    E = model.set_point(92.33, -66.0, ID="E")
    F = model.set_point(73.33, -118.0, ID="F")

    # 2. Construction Lines
    model.construct_line(A, C)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, E)
    model.set_segment(E, C)
    model.set_segment(D, C)
    model.set_segment(A, E)
    model.set_segment(B, C)
    model.set_segment(D, F)

    # 4. Collinear Sections
    model.set_section([A, F, B])
    model.set_section([A, D, E])
    model.set_section([D, E, C])
    model.set_section([A, D, C])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, F, D])

    return model


if __name__ == "__main__":
    construct_g1()
