"""Programmatic construction for Book VI, Proposition 26 (VI.26).

If from a parallelogram there be taken away a parallelogram similar and similarly
situated to the whole and having a common angle with it, it is about the same
diameter with the whole.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for 0261.g1 (VI.26) using geometor.model."""
    model = Model("VI.26")

    # 1. Points of parallelogram ABCD, taken-away parallelogram AF (AEFG), and hypothetical KG (AKHG)
    A = model.set_point(35.0, -29.0, classes=["given"], ID="A")
    G = model.set_point(95.0, -29.0, classes=["given"], ID="G")
    D = model.set_point(180.0, -29.0, classes=["given"], ID="D")

    E = model.set_point(28.0, -72.0, classes=["given"], ID="E")
    F = model.set_point(88.0, -72.0, classes=["given"], ID="F")

    K = model.set_point(26.0, -89.0, ID="K")
    H = model.set_point(86.0, -89.0, ID="H")

    B = model.set_point(19.0, -134.0, classes=["given"], ID="B")
    C = model.set_point(164.0, -134.0, classes=["given"], ID="C")

    # 2. Construction lines
    model.construct_line(A, C)
    model.construct_line(G, H)

    # 3. Segments and sub-segments
    model.set_segment(A, D)
    model.set_segment(A, G)
    model.set_segment(G, D)

    model.set_segment(E, F)
    model.set_segment(K, H)
    model.set_segment(B, C)

    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, K)
    model.set_segment(K, B)
    model.set_segment(A, K)
    model.set_segment(E, B)

    model.set_segment(G, H)
    model.set_segment(G, F)
    model.set_segment(F, H)

    model.set_segment(D, C)

    model.set_segment(A, C)
    model.set_segment(A, F)
    model.set_segment(F, C)

    model.set_segment(A, H)
    model.set_segment(H, C)

    # 4. Collinear sections
    model.set_section([A, G, D])
    model.set_section([A, E, K])
    model.set_section([A, K, B])
    model.set_section([G, F, H])
    model.set_section([A, F, C])

    # 5. Parallelograms and Triangles
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, E, F, G])
    model.set_polygon([A, K, H, G])
    model.set_polygon([A, E, F])
    model.set_polygon([A, B, C])

    # 6. Angles
    model.set_wedge(A, D, D, B)  # < D A B )
    model.set_wedge(E, A, A, F)  # < A E F )
    model.set_wedge(B, A, A, C)  # < A B C )
    model.set_wedge(A, F, F, E)  # < F A E ) / < C A B )

    return model


if __name__ == "__main__":
    construct_g1()
