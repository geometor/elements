"""Programmatic construction for Book I, Definition 3 (I.def.3 — extremities of a segment).

The extremities of a segment are points.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the foundational figure for I.def.3 (extremities A, B of segment / A B /)."""
    model = Model("I.def.3")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.set_segment(A, B)
    return model


if __name__ == "__main__":
    construct_g1()
