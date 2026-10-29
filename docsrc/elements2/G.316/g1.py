"""Programmatic construction for Book X, Proposition 3 (X.3)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the magnitude bars G, AB, CD for Book X, Proposition 3 (X.3)."""
    model = Model("X.3")

    # Single-letter magnitude G
    G_l = model.set_point(29.0, -20.5, classes=["given"], ID="G")
    G_r = model.set_point(76.0, -20.5, ID="G_r")

    # Subdivided magnitude AB (divided at F)
    A = model.set_point(179.0, -23.0, classes=["given"], ID="A")
    F = model.set_point(193.0, -23.0, ID="F")
    B = model.set_point(300.0, -23.0, classes=["given"], ID="B")

    # Subdivided magnitude CD (divided at E)
    C = model.set_point(19.0, -51.0, classes=["given"], ID="C")
    E = model.set_point(54.0, -51.0, ID="E")
    D = model.set_point(298.0, -51.0, classes=["given"], ID="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Magnitude G
    model.set_segment(G_l, G_r)

    # Segments on AB
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(A, B)

    # Segments on CD
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_segment(C, D)

    # Sections
    model.set_section([A, F, B])
    model.set_section([C, E, D])

    return model


if __name__ == "__main__":
    construct_g1()
