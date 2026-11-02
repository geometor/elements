"""Programmatic construction for Book X, Proposition 14 (X.14)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0041.g1 using geometor.model."""
    model = Model("X.14")

    # Vertical straight lines A, B, E, C, D, F
    A_t = model.set_point(19.5, -12.0, classes=["given"], ID="A")
    A_b = model.set_point(19.5, -175.0, ID="A_b")

    B_t = model.set_point(44.5, -33.0, classes=["given"], ID="B")
    B_b = model.set_point(44.5, -175.0, ID="B_b")

    E_t = model.set_point(78.5, -16.0, ID="E")
    E_b = model.set_point(78.5, -98.0, ID="E_b")

    C_t = model.set_point(103.5, -34.0, classes=["given"], ID="C")
    C_b = model.set_point(103.5, -172.0, ID="C_b")

    D_t = model.set_point(130.5, -58.0, classes=["given"], ID="D")
    D_b = model.set_point(130.5, -178.0, ID="D_b")

    F_t = model.set_point(153.5, -18.0, ID="F")
    F_b = model.set_point(153.5, -91.0, ID="F_b")

    for p_t, p_b in [
        (A_t, A_b),
        (B_t, B_b),
        (E_t, E_b),
        (C_t, C_b),
        (D_t, D_b),
        (F_t, F_b),
    ]:
        model.construct_line(p_t, p_b)
        model.set_segment(p_t, p_b)

    return model


if __name__ == "__main__":
    construct_g1()
