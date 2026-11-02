"""Programmatic construction for Book VII, Proposition 20 (VII.20)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0326.g1 using geometor.model."""
    model = Model("VII.20")

    # Single-letter vertical number segments A, B
    A_t = model.set_point(19.0, -10.0, classes=["given"], ID="A")
    A_b = model.set_point(19.0, -175.0, ID="A_b")

    B_t = model.set_point(49.0, -16.0, classes=["given"], ID="B")
    B_b = model.set_point(49.0, -133.0, ID="B_b")

    # Vertical number segment CD (divided at G)
    C = model.set_point(101.0, -80.0, classes=["given"], ID="C")
    G = model.set_point(101.0, -121.0, ID="G")
    D = model.set_point(101.0, -163.0, classes=["given"], ID="D")

    # Vertical number segment EF (divided at H)
    E = model.set_point(123.0, -84.0, classes=["given"], ID="E")
    H = model.set_point(123.0, -112.0, ID="H")
    F = model.set_point(123.0, -141.0, classes=["given"], ID="F")

    # Base lines
    model.construct_line(C, D)
    model.construct_line(E, F)

    # Whole and subdivided segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C, D)
    model.set_segment(C, G)
    model.set_segment(G, D)
    model.set_segment(E, F)
    model.set_segment(E, H)
    model.set_segment(H, F)

    # Collinear sections
    model.set_section([C, G, D])
    model.set_section([E, H, F])

    return model


if __name__ == "__main__":
    construct_g1()
