"""Programmatic construction for Book X, Proposition 51 (X.51)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0113.g1 using geometor.model."""
    model = Model("X.51")

    # Number line AB divided at C
    A = model.set_point(24.5, -19.0, classes=["given"], ID="A")
    C = model.set_point(24.5, -94.0, classes=["given"], ID="C")
    B = model.set_point(24.5, -145.0, classes=["given"], ID="B")

    # Single-letter magnitude segments D and H
    D_t = model.set_point(61.5, -18.0, classes=["given"], ID="D")
    D_b = model.set_point(61.5, -92.0, ID="D_b")

    H_t = model.set_point(60.5, -122.0, classes=["given"], ID="H")
    H_b = model.set_point(60.5, -187.0, ID="H_b")

    # Line EG divided at F
    E = model.set_point(98.0, -24.0, classes=["given"], ID="E")
    F = model.set_point(98.0, -115.0, classes=["given"], ID="F")
    G = model.set_point(98.0, -195.0, classes=["given"], ID="G")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(D_t, D_b)
    model.construct_line(H_t, H_b)
    model.construct_line(E, G)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(D_t, D_b)
    model.set_segment(H_t, H_b)
    model.set_segment(E, G)
    model.set_segment(E, F)
    model.set_segment(F, G)

    # Collinear sections
    model.set_section([A, C, B])
    model.set_section([E, F, G])

    return model


if __name__ == "__main__":
    construct_g1()
