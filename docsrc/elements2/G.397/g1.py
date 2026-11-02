"""Programmatic construction for Book X, Proposition 23 (X.23)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0057.g1 using geometor.model."""
    model = Model("X.23")

    # Medial straight line A and commensurable straight line B
    A_l = model.set_point(16.0, -20.5, classes=["given"], ID="A")
    A_r = model.set_point(94.0, -20.5, classes=["given"], ID="A_r")
    B_l = model.set_point(136.0, -21.5, classes=["given"], ID="B")
    B_r = model.set_point(190.0, -21.5, classes=["given"], ID="B_r")

    # Rectangles CE and CF applied to rational line CD
    C = model.set_point(123.5, -50.5, classes=["given"], ID="C")
    D = model.set_point(123.5, -169.5, classes=["given"], ID="D")
    E = model.set_point(69.5, -169.5, ID="E")
    F = model.set_point(150.5, -169.5, ID="F")
    E_t = model.set_point(69.5, -50.5, ID="E_t")
    F_t = model.set_point(150.5, -50.5, ID="F_t")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B_l, B_r)
    model.construct_line(E_t, F_t)
    model.construct_line(E, F)
    model.construct_line(E_t, E)
    model.construct_line(C, D)
    model.construct_line(F_t, F)

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C, D)
    model.set_segment(E, D)
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_segment(E_t, E)
    model.set_segment(F_t, F)
    model.set_segment(E_t, C)
    model.set_segment(C, F_t)
    model.set_segment(E_t, F_t)

    # Collinear section on EF
    model.set_section([E, D, F])

    # Polygons: rectangles CE and CF
    model.set_polygon([C, D, E, E_t])
    model.set_polygon([C, D, F, F_t])
    model.set_polygon([E_t, F_t, F, E])

    return model


if __name__ == "__main__":
    construct_g1()
