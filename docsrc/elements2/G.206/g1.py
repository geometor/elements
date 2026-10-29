"""Programmatic construction for Book VII, Proposition 7 (VII.7)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0312.g1 using geometor.model."""
    model = Model("VII.7")

    # Top horizontal number segment AB (divided at E)
    A = model.set_point(17.0, -24.0, classes=["given"], ID="A")
    E = model.set_point(56.0, -24.0, ID="E")
    B = model.set_point(130.0, -24.0, classes=["given"], ID="B")

    # Bottom horizontal number segment GD (divided at C and F)
    G = model.set_point(11.0, -53.0, classes=["given"], ID="G")
    C = model.set_point(166.0, -53.0, classes=["given"], ID="C")
    F = model.set_point(240.0, -53.0, ID="F")
    D = model.set_point(395.0, -53.0, classes=["given"], ID="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(G, D)

    # Whole and subdivided segments on AB
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)

    # Whole and subdivided segments on GD
    model.set_segment(G, D)
    model.set_segment(G, C)
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(G, F)
    model.set_segment(C, D)

    # Collinear sections
    model.set_section([A, E, B])
    model.set_section([G, C, F])
    model.set_section([C, F, D])
    model.set_section([G, C, D])
    model.set_section([G, F, D])

    return model


if __name__ == "__main__":
    construct_g1()
