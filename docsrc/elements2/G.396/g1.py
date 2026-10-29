"""Programmatic construction for Book X, Proposition 75 (X.75)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0165.g1 using geometor.model."""
    model = Model("X.75")

    # Medial straight line AB with medial straight line CB subtracted, leaving AC
    A = model.set_point(129.0, -21.5, classes=["given"], ID="A")
    C = model.set_point(161.0, -21.5, classes=["given"], ID="C")
    B = model.set_point(276.0, -21.5, classes=["given"], ID="B")

    # Rectangle DE applied to rational straight line DI, divided by FH into DH and FE
    D = model.set_point(17.0, -53.0, classes=["given"], ID="D")
    F = model.set_point(378.5, -53.0, ID="F")
    G = model.set_point(388.5, -53.0, ID="G")
    I = model.set_point(17.0, -153.5, classes=["given"], ID="I")
    H = model.set_point(378.5, -153.5, ID="H")
    E = model.set_point(388.5, -153.5, ID="E")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(D, G)
    model.construct_line(I, E)
    model.construct_line(D, I)
    model.construct_line(F, H)
    model.construct_line(G, E)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    model.set_segment(D, I)
    model.set_segment(F, H)
    model.set_segment(G, E)
    model.set_segment(D, G)
    model.set_segment(D, F)
    model.set_segment(F, G)
    model.set_segment(I, E)
    model.set_segment(I, H)
    model.set_segment(H, E)

    # Sections
    model.set_section([A, C, B])
    model.set_section([D, F, G])
    model.set_section([I, H, E])

    # Polygons
    model.set_polygon([D, I, E, G])
    model.set_polygon([D, I, H, F])
    model.set_polygon([F, H, E, G])

    return model


if __name__ == "__main__":
    construct_g1()
