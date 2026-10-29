"""Programmatic construction for Book VI, Proposition 22 (VI.22).

If four straight lines be proportional, the rectilineal figures similar and similarly
described upon them will also be proportional; and conversely.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0247.g1 (VI.22) using geometor.model."""
    model = Model("VI.22")

    # 1. Similar triangles KAB on AB and LCD on CD
    K = model.set_point(69.0, -24.0, ID="K")
    A = model.set_point(19.0, -107.0, classes=["given"], ID="A")
    B = model.set_point(101.0, -107.0, classes=["given"], ID="B")
    model.set_segment(A, B)
    model.set_segment(A, K)
    model.set_segment(K, B)
    model.set_polygon([K, A, B])

    L = model.set_point(213.0, -33.0, ID="L")
    C = model.set_point(167.0, -107.0, classes=["given"], ID="C")
    D = model.set_point(239.0, -107.0, classes=["given"], ID="D")
    model.set_segment(C, D)
    model.set_segment(C, L)
    model.set_segment(L, D)
    model.set_polygon([L, C, D])

    # 2. Similar parallelograms MF on EF, NH on GH, and SR on QR
    M = model.set_point(332.0, -56.0, ID="M")
    M2 = model.set_point(397.0, -56.0, ID="M2")
    F = model.set_point(369.0, -108.0, classes=["given"], ID="F")
    E = model.set_point(304.0, -108.0, classes=["given"], ID="E")
    model.set_segment(E, F)
    model.set_segment(E, M)
    model.set_segment(M, M2)
    model.set_segment(M2, F)
    model.set_polygon([M, M2, F, E])

    N = model.set_point(456.0, -66.0, ID="N")
    N2 = model.set_point(508.0, -66.0, ID="N2")
    H = model.set_point(484.0, -109.0, classes=["given"], ID="H")
    G = model.set_point(432.0, -109.0, classes=["given"], ID="G")
    model.set_segment(G, H)
    model.set_segment(G, N)
    model.set_segment(N, N2)
    model.set_segment(N2, H)
    model.set_polygon([N, N2, H, G])

    S = model.set_point(373.0, -144.0, ID="S")
    S2 = model.set_point(429.0, -144.0, ID="S2")
    R = model.set_point(406.0, -193.0, ID="R")
    Q = model.set_point(350.0, -193.0, ID="Q")
    model.set_segment(Q, R)
    model.set_segment(Q, S)
    model.set_segment(S, S2)
    model.set_segment(S2, R)
    model.set_polygon([S, S2, R, Q])

    # 3. Third proportionals O and P
    O1 = model.set_point(119.0, -190.0, ID="O1")
    O2 = model.set_point(178.0, -190.0, ID="O2")
    model.set_segment(O1, O2)

    P1 = model.set_point(237.0, -191.0, ID="P1")
    P2 = model.set_point(285.0, -191.0, ID="P2")
    model.set_segment(P1, P2)

    return model


if __name__ == "__main__":
    construct_g1()
