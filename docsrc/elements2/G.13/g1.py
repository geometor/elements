"""Programmatic construction for Book I, Postulate 1 (I.post.1 — construct a segment).

Construct a segment between any two points.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct segment / A B / joining points A and B."""
    model = Model("I.post.1")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.set_segment(A, B)
    return model


if __name__ == "__main__":
    construct_g1()
