"""Programmatic construction for Book I, Common Notion 4 (I.cn.4 — coincidence).

Things that coincide with one another are equal.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_g1() -> Model:
    """Construct superposed segments / A B / and / D E / demonstrating coincidence."""
    model = Model("I.cn.4")
    A = model.set_point(0, sp.Rational(1, 3), classes=["given"], ID="A")
    B = model.set_point(1, sp.Rational(1, 3), classes=["given"], ID="B")
    model.set_segment(A, B)

    D = model.set_point(0, 0, classes=["given"], ID="D")
    E = model.set_point(1, 0, classes=["given"], ID="E")
    model.set_segment(D, E)
    return model


if __name__ == "__main__":
    construct_g1()
