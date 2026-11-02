"""Programmatic construction for Book XII, Proposition 16 (XII.16).

Two concentric circles ABCD and EFGH about center K, with diameter BKD, tangent
chord AGC at G, and chord LMN parallel to AC with inscribed sides LD, DN.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0428.g1 using geometor.model."""
    model = Model("XII.16")

    K = model.set_point(112.0, -104.0, classes=["given"], ID="K")
    B = model.set_point(28.0, -104.0, classes=["given"], ID="B")
    D = model.set_point(196.0, -104.0, classes=["given"], ID="D")
    E = model.set_point(48.0, -104.0, classes=["given"], ID="E")
    G = model.set_point(176.0, -104.0, classes=["given"], ID="G")
    H = model.set_point(112.0, -40.0, classes=["given"], ID="H")
    F = model.set_point(112.0, -168.0, classes=["given"], ID="F")

    A = model.set_point(176.0, -49.4, classes=["given"], ID="A")
    C = model.set_point(176.0, -158.6, classes=["given"], ID="C")

    M = model.set_point(190.0, -104.0, classes=["given"], ID="M")
    L = model.set_point(190.0, -73.1, classes=["given"], ID="L")
    N = model.set_point(190.0, -134.9, classes=["given"], ID="N")

    # Concentric circles
    model.construct_circle(K, D)
    model.construct_circle(K, G)

    # Segments
    for p1, p2 in [
        (B, E), (E, K), (K, G), (G, M), (M, D),
        (B, K), (K, D), (B, D),
        (A, G), (G, C), (A, C),
        (L, M), (M, N), (L, N),
        (L, D), (D, N),
    ]:
        model.set_segment(p1, p2)

    # Collinear sections
    model.set_section([B, K, D])

    return model


if __name__ == "__main__":
    construct_g1()
