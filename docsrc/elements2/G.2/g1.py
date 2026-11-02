"""Programmatic construction for Book I, Definition 2 (I.def.2 — line).

A line is a projection of a relationship of two points.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the foundational figure for I.def.2 (line [ A B ])."""
    model = Model("I.def.2")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.construct_line(A, B)
    return model


if __name__ == "__main__":
    construct_g1()
