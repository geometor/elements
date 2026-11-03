"""Programmatic construction for Book I, Definition 20 (I.def.20 — equilateral, isosceles, and scalene triangles).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_g1() -> Model:
    """Construct equilateral < A B C >, isosceles < D E F >, and scalene < G H K > triangles."""
    model = Model("I.def.20")
    A = model.set_point(0, 0, ID="A")
    B = model.set_point(1, 0, ID="B")
    C = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, ID="C")
    model.set_polygon([A, B, C])

    D = model.set_point(sp.Rational(3, 2), 0, ID="D")
    E = model.set_point(sp.Rational(9, 4), 0, ID="E")
    F = model.set_point(sp.Rational(15, 8), 1, ID="F")
    model.set_polygon([D, E, F])

    G = model.set_point(sp.Rational(11, 4), 0, ID="G")
    H = model.set_point(4, 0, ID="H")
    K = model.set_point(sp.Rational(25, 8), sp.Rational(7, 8), ID="K")
    model.set_polygon([G, H, K])
    return model


if __name__ == "__main__":
    construct_g1()
