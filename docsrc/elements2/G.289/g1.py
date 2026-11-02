"""Programmatic construction for Book VII, Proposition 33 (VII.33)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0339.g2 using geometor.model."""
    model = Model("VII.33")

    # Given numbers A, B, C and greatest common measure D
    A_t = model.set_point(58.0, -12.0, classes=["given"], ID="A")
    A_b = model.set_point(58.0, -83.0, ID="A_b")

    B_t = model.set_point(87.0, -15.0, classes=["given"], ID="B")
    B_b = model.set_point(87.0, -119.0, ID="B_b")

    C_t = model.set_point(118.0, -12.0, classes=["given"], ID="C")
    C_b = model.set_point(118.0, -150.0, ID="C_b")

    D_t = model.set_point(144.0, -14.0, classes=["given"], ID="D")
    D_b = model.set_point(144.0, -50.0, ID="D_b")

    # Numbers H, K, L and unit-count M
    H_t = model.set_point(22.0, -115.0, classes=["given"], ID="H")
    H_b = model.set_point(22.0, -145.0, ID="H_b")

    K_t = model.set_point(44.0, -116.0, classes=["given"], ID="K")
    K_b = model.set_point(44.0, -153.0, ID="K_b")

    L_t = model.set_point(64.0, -113.0, classes=["given"], ID="L")
    L_b = model.set_point(64.0, -162.0, ID="L_b")

    M_t = model.set_point(87.0, -137.0, classes=["given"], ID="M")
    M_b = model.set_point(87.0, -163.0, ID="M_b")

    # Least numbers in the same ratio E, F, G
    E_t = model.set_point(144.0, -87.0, classes=["given"], ID="E")
    E_b = model.set_point(144.0, -133.0, ID="E_b")

    F_t = model.set_point(170.0, -86.0, classes=["given"], ID="F")
    F_b = model.set_point(170.0, -157.0, ID="F_b")

    G_t = model.set_point(198.0, -85.0, classes=["given"], ID="G")
    G_b = model.set_point(198.0, -173.0, ID="G_b")

    # Segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)
    model.set_segment(H_t, H_b)
    model.set_segment(K_t, K_b)
    model.set_segment(L_t, L_b)
    model.set_segment(M_t, M_b)
    model.set_segment(E_t, E_b)
    model.set_segment(F_t, F_b)
    model.set_segment(G_t, G_b)

    return model


if __name__ == "__main__":
    construct_g1()
