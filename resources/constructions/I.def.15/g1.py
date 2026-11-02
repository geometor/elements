"""Programmatic construction for Book I, Definition 15 (I.def.15 — circle).

A circle is a plane figure contained by one arc such that all segments falling upon it from its center are equal.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_g1() -> Model:
    """Construct the foundational figure for I.def.15 (circle ( B C D ) with equal radii)."""
    model = Model("I.def.15")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.construct_circle(A, B)
    C = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, ID="C")
    D = model.set_point(-1, 0, ID="D")
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    return model


if __name__ == "__main__":
    construct_g1()
