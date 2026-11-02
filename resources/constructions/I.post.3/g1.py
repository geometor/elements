"""Programmatic construction for Book I, Postulate 3 (I.post.3 — construct a circle).

Construct a circle with any center and radius.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct circle ( B C D ) with center A and radius / A B /."""
    model = Model("I.post.3")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.set_segment(A, B)
    model.construct_circle(A, B)
    return model


if __name__ == "__main__":
    construct_g1()
