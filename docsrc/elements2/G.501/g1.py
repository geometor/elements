"""Programmatic construction for Book XII, Proposition 14 (XII.14).

Cylinders EB, FD and cones ABG, CDK on equal circular bases AB, CD with axes
GH and KL (produced to N with cylinder CM).
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0423.g1 using geometor.model."""
    model = Model("XII.14")

    # Left cylinder EB and cone ABG
    G = model.set_point(52.0, -85.0, classes=["given"], ID="G")
    E = model.set_point(23.0, -85.0, classes=["given"], ID="E")
    E2 = model.set_point(81.0, -85.0, ID="E2")
    H = model.set_point(52.0, -148.0, classes=["given"], ID="H")
    A = model.set_point(23.0, -148.0, classes=["given"], ID="A")
    B = model.set_point(81.0, -148.0, classes=["given"], ID="B")

    # Right cylinder FM (FD + CM) and cone CDK
    K = model.set_point(199.0, -34.0, classes=["given"], ID="K")
    F = model.set_point(170.0, -34.0, classes=["given"], ID="F")
    F2 = model.set_point(228.0, -34.0, ID="F2")
    L = model.set_point(199.0, -85.0, classes=["given"], ID="L")
    C = model.set_point(170.0, -85.0, classes=["given"], ID="C")
    D = model.set_point(228.0, -85.0, classes=["given"], ID="D")
    N = model.set_point(199.0, -152.0, classes=["given"], ID="N")
    M2 = model.set_point(170.0, -152.0, ID="M2")
    M = model.set_point(228.0, -152.0, classes=["given"], ID="M")

    # Circular bases and sections
    for center, rim in [(G, E), (H, A), (K, F), (L, C), (N, M)]:
        model.construct_circle(center, rim)

    # Segments (generators, axes, cone edges)
    for p1, p2 in [
        (E, A), (E2, B), (G, H), (G, A), (G, B),
        (F, C), (C, M2), (F, M2),
        (F2, D), (D, M), (F2, M),
        (K, L), (L, N), (K, N),
        (K, C), (K, D),
    ]:
        model.set_segment(p1, p2)

    # Cylinders and cones
    model.set_polygon([E, A, B, E2])   # Cylinder EB
    model.set_polygon([F, C, D, F2])   # Cylinder FD
    model.set_polygon([C, M2, M, D])   # Cylinder CM
    model.set_polygon([F, M2, M, F2])  # Cylinder FM
    model.set_polygon([A, B, G])       # Cone ABG
    model.set_polygon([C, D, K])       # Cone CDK

    return model


if __name__ == "__main__":
    construct_g1()
