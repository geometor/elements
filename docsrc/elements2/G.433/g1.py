"""Programmatic construction for Book X, Proposition 53 (X.53)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0116.g1 using geometor.model."""
    model = Model("X.53")

    # Number line AB divided at C
    A = model.set_point(22.5, -18.0, classes=["given"], ID="A")
    C = model.set_point(22.5, -93.0, classes=["given"], ID="C")
    B = model.set_point(22.5, -144.0, classes=["given"], ID="B")

    # Single-letter magnitude segments D, E, K
    D_t = model.set_point(63.5, -20.0, classes=["given"], ID="D")
    D_b = model.set_point(63.5, -93.0, ID="D_b")

    E_t = model.set_point(95.5, -21.0, classes=["given"], ID="E")
    E_b = model.set_point(95.5, -92.0, ID="E_b")

    K_t = model.set_point(94.5, -116.0, classes=["given"], ID="K")
    K_b = model.set_point(94.5, -177.0, ID="K_b")

    # Line FH divided at G
    F = model.set_point(138.0, -20.0, classes=["given"], ID="F")
    G = model.set_point(138.0, -113.0, classes=["given"], ID="G")
    H = model.set_point(138.0, -192.0, classes=["given"], ID="H")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(D_t, D_b)
    model.construct_line(E_t, E_b)
    model.construct_line(K_t, K_b)
    model.construct_line(F, H)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(D_t, D_b)
    model.set_segment(E_t, E_b)
    model.set_segment(K_t, K_b)
    model.set_segment(F, H)
    model.set_segment(F, G)
    model.set_segment(G, H)

    # Collinear sections
    model.set_section([A, C, B])
    model.set_section([F, G, H])

    return model


if __name__ == "__main__":
    construct_g1()
