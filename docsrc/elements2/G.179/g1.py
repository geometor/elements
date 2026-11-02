"""Programmatic construction for Book V, Proposition 6 (V.6)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0153.g1 for Book V, Proposition 6 using geometor.model."""
    model = Model("V.6")

    # Magnitude AB subdivided at G (with intermediate multiple marks A_1, A_2)
    A = model.set_point(27.0, -28.0, classes=["given"], ID="A")
    A_1 = model.set_point(71.0, -28.0, ID="A_1")
    A_2 = model.set_point(115.0, -28.0, ID="A_2")
    G = model.set_point(159.0, -28.0, classes=["given"], ID="G")
    B = model.set_point(204.0, -28.0, classes=["given"], ID="B")

    # Standalone magnitude E
    E_1 = model.set_point(27.0, -52.0, classes=["given"], ID="E_1")
    E_2 = model.set_point(71.0, -52.0, classes=["given"], ID="E_2")

    # Magnitude KD subdivided at C and H (with intermediate multiple marks C_1, C_2)
    K = model.set_point(27.0, -84.0, ID="K")
    C = model.set_point(56.0, -84.0, classes=["given"], ID="C")
    C_1 = model.set_point(85.0, -84.0, ID="C_1")
    C_2 = model.set_point(115.0, -84.0, ID="C_2")
    H = model.set_point(144.0, -84.0, classes=["given"], ID="H")
    D = model.set_point(173.0, -84.0, classes=["given"], ID="D")

    # Standalone magnitude F
    F_1 = model.set_point(27.0, -107.0, classes=["given"], ID="F_1")
    F_2 = model.set_point(56.0, -107.0, classes=["given"], ID="F_2")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(K, D)

    # Segments along AB
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, B)

    # Standalone magnitude E
    model.set_segment(E_1, E_2)

    # Segments along KD
    model.set_segment(K, D)
    model.set_segment(C, D)
    model.set_segment(C, H)
    model.set_segment(H, D)
    model.set_segment(C, K)
    model.set_segment(K, H)

    # Standalone magnitude F
    model.set_segment(F_1, F_2)

    return model


if __name__ == "__main__":
    construct_g1()
