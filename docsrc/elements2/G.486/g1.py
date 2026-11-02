"""Programmatic construction for Book X, Proposition 100 (X.100)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0225.g1 using geometor.model."""
    model = Model("X.100")

    # Top segment AG divided at B
    A = model.set_point(124.0, -21.0, classes=["given"], ID="A")
    B = model.set_point(211.0, -21.0, classes=["given"], ID="B")
    G = model.set_point(262.0, -21.0, classes=["given"], ID="G")

    # Rectangle CDLM divided by vertical lines FE, NO, KH
    C = model.set_point(19.5, -56.5, classes=["given"], ID="C")
    F = model.set_point(133.5, -56.5, ID="F")
    N = model.set_point(244.5, -56.5, ID="N")
    K = model.set_point(315.5, -56.5, ID="K")
    M = model.set_point(356.5, -56.5, ID="M")

    D = model.set_point(19.5, -120.5, classes=["given"], ID="D")
    E = model.set_point(133.5, -120.5, ID="E")
    O = model.set_point(244.5, -120.5, ID="O")
    H = model.set_point(315.5, -120.5, ID="H")
    L = model.set_point(356.5, -120.5, ID="L")

    # Base lines
    for p1, p2 in [
        (A, G),
        (C, M),
        (D, L),
        (C, D),
        (F, E),
        (N, O),
        (K, H),
        (M, L),
    ]:
        model.construct_line(p1, p2)

    # Segments on AG and CDLM
    for pts in ([A, B, G], [C, F, N, K, M], [D, E, O, H, L]):
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                model.set_segment(pts[i], pts[j])

    # Vertical segments on CDLM
    for p1, p2 in [(C, D), (F, E), (N, O), (K, H), (M, L)]:
        model.set_segment(p1, p2)

    # Collinear sections
    model.set_section([A, B, G])
    model.set_section([C, F, M])
    model.set_section([C, K, M])
    model.set_section([F, N, M])

    # Polygons in CDLM
    model.set_polygon([C, M, L, D])  # CL / DM
    model.set_polygon([C, F, E, D])  # CE
    model.set_polygon([C, K, H, D])  # CH
    model.set_polygon([K, M, L, H])  # KL
    model.set_polygon([F, M, L, E])  # FL
    model.set_polygon([F, N, O, E])  # FO
    model.set_polygon([N, M, L, O])  # NL / LN
    model.set_polygon([N, K, H, O])  # NH
    model.set_polygon([C, N, O, D])  # CO
    model.set_polygon([F, K, H, E])  # FH

    return model


if __name__ == "__main__":
    construct_g1()
