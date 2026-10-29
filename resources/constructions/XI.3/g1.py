"""Programmatic construction for Book XI, Proposition 3 (XI.3)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0280.g1 using geometor.model."""
    model = Model("XI.3")

    # Plane AB corners
    P1 = model.set_point(22.0, -58.0, classes=["plane_corner"])
    P2 = model.set_point(158.0, -58.0, classes=["plane_corner"])
    A = model.set_point(158.0, -123.0, classes=["given"], ID="A")
    P4 = model.set_point(22.0, -123.0, classes=["plane_corner"])

    # Plane BC corners
    Q1 = model.set_point(136.0, -21.0, classes=["plane_corner"])
    Q2 = model.set_point(136.0, -81.0, classes=["plane_corner"])
    C = model.set_point(46.0, -169.0, classes=["given"], ID="C")
    Q4 = model.set_point(46.0, -102.0, classes=["plane_corner"])

    # Common section endpoints B, D and curved path points E, F
    B = model.set_point(92.0, -58.0, classes=["given"], ID="B")
    D = model.set_point(92.0, -123.0, classes=["given"], ID="D")
    E = model.set_point(99.0, -90.5, ID="E")
    F = model.set_point(85.0, -90.5, ID="F")

    # Segments
    model.set_segment(D, B)
    model.set_segment(P1, P2)
    model.set_segment(P2, A)
    model.set_segment(A, P4)
    model.set_segment(P4, P1)
    model.set_segment(Q1, Q2)
    model.set_segment(Q2, C)
    model.set_segment(C, Q4)
    model.set_segment(Q4, Q1)

    # Sections for DEB and DFB
    model.set_section([D, E, B])
    model.set_section([D, F, B])

    # Planes AB and BC
    model.set_polygon([P1, P2, A, P4])
    model.set_polygon([Q1, Q2, C, Q4])

    return model


if __name__ == "__main__":
    construct_g1()
