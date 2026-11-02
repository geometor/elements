"""Programmatic construction for Book V, Proposition 9 (V.9)."""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure 0160.g1 for Book V, Proposition 9 using geometor.model."""
    model = Model("V.9")

    # Standalone magnitudes A, B, C
    A_1 = model.set_point(29.0, -19.0, classes=["given"], ID="A_1")
    A_2 = model.set_point(109.0, -19.0, classes=["given"], ID="A_2")
    B_1 = model.set_point(174.0, -19.0, classes=["given"], ID="B_1")
    B_2 = model.set_point(253.0, -19.0, classes=["given"], ID="B_2")
    C_1 = model.set_point(88.0, -50.0, classes=["given"], ID="C_1")
    C_2 = model.set_point(198.0, -50.0, classes=["given"], ID="C_2")

    model.set_segment(A_1, A_2)
    model.set_segment(B_1, B_2)
    model.set_segment(C_1, C_2)

    return model


if __name__ == "__main__":
    construct_g1()
