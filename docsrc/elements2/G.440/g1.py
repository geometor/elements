"""Programmatic construction for Book X, Proposition 113 (X.113)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0252.g1 using geometor.model."""
    model = Model("X.113")

    # Single-letter vertical magnitude segments A and G
    A_t = model.set_point(28.0, -18.0, classes=["given"], ID="A")
    A_b = model.set_point(28.0, -110.0, ID="A_b")

    G_t = model.set_point(137.5, -19.0, classes=["given"], ID="G")
    G_b = model.set_point(137.5, -73.0, ID="G_b")

    # Vertical line CB divided at D
    C = model.set_point(63.0, -18.0, classes=["given"], ID="C")
    D = model.set_point(63.0, -110.0, classes=["given"], ID="D")
    B = model.set_point(63.0, -171.0, classes=["given"], ID="B")

    # Vertical line KH divided at E and F
    K = model.set_point(103.0, -18.0, ID="K")
    E = model.set_point(103.0, -82.0, ID="E")
    F = model.set_point(103.0, -107.0, ID="F")
    H = model.set_point(103.0, -142.0, ID="H")

    # Base lines
    model.construct_line(A_t, A_b)
    model.construct_line(C, B)
    model.construct_line(K, H)
    model.construct_line(G_t, G_b)

    # Segments
    model.set_segment(A_t, A_b)
    model.set_segment(G_t, G_b)
    model.set_segment(C, B)
    model.set_segment(C, D)
    model.set_segment(D, B)
    model.set_segment(K, H)
    model.set_segment(K, F)
    model.set_segment(K, E)
    model.set_segment(E, H)
    model.set_segment(E, F)
    model.set_segment(F, H)

    # Sections
    model.set_section([C, D, B])
    model.set_section([K, E, F])
    model.set_section([K, F, H])
    model.set_section([E, F, H])

    return model


if __name__ == "__main__":
    construct_g1()
