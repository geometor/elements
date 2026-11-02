"""Programmatic construction for Book I, Definition 1 (I.def.1 — point).

A point is that which has no part.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the foundational figure for I.def.1 (point A)."""
    model = Model("I.def.1")
    model.set_point(0, 0, classes=["given"], ID="A")
    return model


if __name__ == "__main__":
    construct_g1()
