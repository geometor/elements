"""Programmatic construction for Book I, Definition 16 (I.def.16 — center of a circle).

This point is called the center of the circle.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_g1() -> Model:
    """Construct the foundational figure for I.def.16 (center A of circle ( B C D ))."""
    model = Model("I.def.16")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.construct_circle(A, B)
    C = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, ID="C")
    model.set_segment(A, B)
    model.set_segment(A, C)
    return model


if __name__ == "__main__":
    construct_g1()
