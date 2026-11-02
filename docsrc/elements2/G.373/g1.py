"""Programmatic construction for Book X, Proposition 2 (X.2)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the magnitude bars E, AB, CD for Book X, Proposition 2 (X.2)."""
    model = Model("X.2")

    # Single-letter magnitude E
    E_l = model.set_point(70.0, -23.5, classes=["given"], ID="E")
    E_r = model.set_point(118.0, -23.5, ID="E_r")

    # Subdivided magnitude AB (divided at G)
    A = model.set_point(205.0, -23.5, classes=["given"], ID="A")
    G = model.set_point(230.0, -23.5, ID="G")
    B = model.set_point(339.0, -23.5, classes=["given"], ID="B")

    # Subdivided magnitude CD (divided at F)
    C = model.set_point(17.0, -50.0, classes=["given"], ID="C")
    F = model.set_point(75.0, -50.0, ID="F")
    D = model.set_point(337.0, -50.0, classes=["given"], ID="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Magnitude E
    model.set_segment(E_l, E_r)

    # Segments on AB
    model.set_segment(A, G)
    model.set_segment(G, B)
    model.set_segment(A, B)

    # Segments on CD
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(C, D)

    # Sections
    model.set_section([A, G, B])
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_g1()
