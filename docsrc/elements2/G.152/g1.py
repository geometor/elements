"""Programmatic construction for Book V, Proposition 15 (V.15)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0169.g1 (Book V, Prop. 15 subdivided magnitudes AB, DE and parts C, F)."""
    model = Model("V.15")

    # Subdivided magnitude AB = AG + GH + HB
    A = model.set_point(28.00, -27.00, classes=["given"], ID="A")
    G = model.set_point(83.00, -27.00, ID="G")
    H = model.set_point(137.00, -27.00, ID="H")
    B = model.set_point(192.00, -27.00, classes=["given"], ID="B")
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, H)
    model.set_segment(H, B)
    model.set_section([A, G, H])
    model.set_section([G, H, B])

    # Subdivided magnitude DE = DK + KL + LE
    D = model.set_point(28.00, -55.00, classes=["given"], ID="D")
    K = model.set_point(73.00, -55.00, ID="K")
    L = model.set_point(117.00, -55.00, ID="L")
    E = model.set_point(162.00, -55.00, classes=["given"], ID="E")
    model.set_segment(D, E)
    model.set_segment(D, K)
    model.set_segment(K, L)
    model.set_segment(L, E)
    model.set_section([D, K, L])
    model.set_section([K, L, E])

    # Single-letter magnitude C
    C1 = model.set_point(262.00, -27.00, classes=["given"], ID="C")
    C2 = model.set_point(317.00, -27.00, classes=["given"], ID="C2")
    model.set_segment(C1, C2)

    # Single-letter magnitude F
    F1 = model.set_point(262.00, -55.00, classes=["given"], ID="F")
    F2 = model.set_point(308.00, -55.00, classes=["given"], ID="F2")
    model.set_segment(F1, F2)

    return model


if __name__ == "__main__":
    construct_g1()
