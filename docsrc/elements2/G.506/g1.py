"""Programmatic construction for Book XII, Proposition 18 (XII.18).

Spheres ABC (diameter BC), DEF (diameter EF) concentric with lesser sphere GHK
(diameter HK), and greater sphere LMN.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0439.g1 using geometor.model."""
    model = Model("XII.18")

    # Top-left sphere ABC
    O1 = model.set_point(90.2, -92.0, ID="O1")
    A = model.set_point(90.2, -22.8, classes=["given"], ID="A")
    B = model.set_point(21.0, -92.0, classes=["given"], ID="B")
    C = model.set_point(159.4, -92.0, classes=["given"], ID="C")

    # Top-right concentric spheres DEF and GHK
    O2 = model.set_point(360.8, -105.0, ID="O2")
    D = model.set_point(392.0, -27.2, classes=["given"], ID="D")
    E = model.set_point(277.0, -105.0, classes=["given"], ID="E")
    F = model.set_point(444.6, -105.0, classes=["given"], ID="F")
    G = model.set_point(382.0, -34.3, classes=["given"], ID="G")
    H = model.set_point(287.0, -105.0, classes=["given"], ID="H")
    K = model.set_point(434.6, -105.0, classes=["given"], ID="K")

    # Bottom sphere LMN
    O3 = model.set_point(228.8, -286.8, ID="O3")
    L = model.set_point(228.8, -190.0, classes=["given"], ID="L")
    M = model.set_point(132.0, -286.8, classes=["given"], ID="M")
    N = model.set_point(325.6, -286.8, classes=["given"], ID="N")

    # Spheres (modeled as circles)
    model.construct_circle(O1, B)
    model.construct_circle(O2, E)
    model.construct_circle(O2, H)
    model.construct_circle(O3, M)

    # Diameters and sub-segments
    for p1, p2 in [
        (B, C),
        (E, H), (H, K), (K, F), (E, F),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_g1()
