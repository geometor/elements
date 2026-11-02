"""Programmatic construction for Book I, Definition 4 (I.def.4 — segment).

A segment is a portion of a line between two points on the line.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the foundational figure for I.def.4 (segment / A B / on line [ A B ])."""
    model = Model("I.def.4")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.construct_line(A, B)
    model.set_segment(A, B)
    return model


if __name__ == "__main__":
    construct_g1()
