"""Programmatic construction for Book X, Proposition 20 (X.20)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0053.g1 using geometor.model."""
    model = Model("X.20")

    # Vertices of square AD (A, B, D, D_r) and rectangle AC (A, B, C, C_r)
    D = model.set_point(26.0, -15.5, ID="D")
    B = model.set_point(26.0, -88.5, classes=["given"], ID="B")
    C = model.set_point(26.0, -180.0, classes=["given"], ID="C")
    A = model.set_point(97.0, -88.5, classes=["given"], ID="A")
    D_r = model.set_point(97.0, -15.5, ID="D_r")
    C_r = model.set_point(97.0, -180.0, ID="C_r")

    # Base lines
    model.construct_line(D, C)
    model.construct_line(D_r, C_r)
    model.construct_line(D, D_r)
    model.construct_line(B, A)
    model.construct_line(C, C_r)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(D, B)
    model.set_segment(D, C)
    model.set_segment(D, D_r)
    model.set_segment(C, C_r)
    model.set_segment(D_r, A)
    model.set_segment(A, C_r)
    model.set_segment(D_r, C_r)

    # Collinear section on DC
    model.set_section([D, B, C])

    # Polygons: square AD and rectangle AC
    model.set_polygon([A, B, D, D_r])
    model.set_polygon([A, B, C, C_r])
    model.set_polygon([D, C, C_r, D_r])

    return model


if __name__ == "__main__":
    construct_g1()
