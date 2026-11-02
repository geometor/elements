"""Programmatic construction for Book I, Postulate 2 (I.post.2 — extend a segment).

Extend a segment continuously along a line.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Extend given segment / A B / along line [ A B ] to C."""
    model = Model("I.post.2")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.set_segment(A, B)
    model.construct_line(A, B)
    C = model.set_point(2, 0, ID="C")
    model.set_segment(B, C)
    return model


if __name__ == "__main__":
    construct_g1()
