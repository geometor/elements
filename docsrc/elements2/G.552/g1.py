"""Programmatic construction for Book XII, Proposition 2 (XII.2).

Circles ABCD and EFGH with diameters BD and FH, inscribed octagons AOBPCQDR
and EKFLGMHN, inscribed square EFGH, tangent rectangle on EF at K, and
auxiliary areas S and T.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0375.g1 using geometor.model."""
    model = Model("XII.2")

    # Left circle ABCD (center O1 = (111, -114), radius 88)
    O1 = model.set_point(111.0, -114.0, ID="O1")
    A = model.set_point(111.0, -26.0, classes=["given"], ID="A")
    B = model.set_point(23.0, -114.0, classes=["given"], ID="B")
    C = model.set_point(111.0, -202.0, classes=["given"], ID="C")
    D = model.set_point(199.0, -114.0, classes=["given"], ID="D")
    O = model.set_point(48.77, -51.77, ID="O")
    P = model.set_point(48.77, -176.23, ID="P")
    Q = model.set_point(173.23, -176.23, ID="Q")
    R = model.set_point(173.23, -51.77, ID="R")

    # Middle circle EFGH (center O2 = (327, -121), radius 73.5)
    O2 = model.set_point(327.0, -121.0, ID="O2")
    E = model.set_point(327.0, -47.5, classes=["given"], ID="E")
    F = model.set_point(253.5, -121.0, classes=["given"], ID="F")
    G = model.set_point(327.0, -194.5, classes=["given"], ID="G")
    H = model.set_point(400.5, -121.0, classes=["given"], ID="H")
    K = model.set_point(275.03, -69.03, ID="K")
    L = model.set_point(275.03, -172.97, ID="L")
    M = model.set_point(378.97, -172.97, ID="M")
    N = model.set_point(378.97, -69.03, ID="N")

    # Outer corners of tangent rectangle on EF at K
    U = model.set_point(238.28, -105.78, ID="U")
    V = model.set_point(311.78, -32.28, ID="V")

    # Area S rectangle corners and center label point
    S1 = model.set_point(442.0, -54.0, ID="S1")
    S2 = model.set_point(525.0, -54.0, ID="S2")
    S3 = model.set_point(525.0, -216.0, ID="S3")
    S4 = model.set_point(442.0, -216.0, ID="S4")
    S = model.set_point(483.5, -135.0, classes=["given"], ID="S")

    # Area T rectangle corners and center label point
    T1 = model.set_point(555.0, -70.0, ID="T1")
    T2 = model.set_point(636.0, -70.0, ID="T2")
    T3 = model.set_point(636.0, -178.0, ID="T3")
    T4 = model.set_point(555.0, -178.0, ID="T4")
    T = model.set_point(595.5, -124.0, classes=["given"], ID="T")

    # Circles
    model.construct_circle(O1, A)
    model.construct_circle(O2, E)

    # Segments in left circle
    for p1, p2 in [
        (B, D),
        (A, O), (O, B), (B, P), (P, C), (C, Q), (Q, D), (D, R), (R, A),
    ]:
        model.set_segment(p1, p2)

    # Segments in middle circle
    for p1, p2 in [
        (F, H),
        (E, F), (F, G), (G, H), (H, E),
        (E, K), (K, F), (F, L), (L, G), (G, M), (M, H), (H, N), (N, E),
        (F, U), (U, V), (V, E),
    ]:
        model.set_segment(p1, p2)

    # Polygons
    model.set_polygon([A, O, B, P, C, Q, D, R])
    model.set_polygon([E, F, G, H])
    model.set_polygon([E, K, F, L, G, M, H, N])
    model.set_polygon([E, K, F])
    model.set_polygon([F, L, G])
    model.set_polygon([G, M, H])
    model.set_polygon([H, N, E])
    model.set_polygon([F, U, V, E])
    model.set_polygon([S1, S2, S3, S4])
    model.set_polygon([T1, T2, T3, T4])

    return model


if __name__ == "__main__":
    construct_g1()
