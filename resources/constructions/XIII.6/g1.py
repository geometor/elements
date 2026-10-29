"""Programmatic construction for Book XIII, Proposition 6 (XIII.6).

If a rational straight line be cut in extreme and mean ratio, each of the
segments is the irrational straight line called apotome.
"""

from __future__ import annotations

from geometor.model import Model


def construct_g1() -> Model:
    """Construct the figure for Book XIII, Proposition 6 using geometor.model."""
    model = Model("XIII.6")

    D = model.set_point(12.0, -26.0, classes=["given"], ID="D")
    A = model.set_point(78.0, -26.0, classes=["given"], ID="A")
    C = model.set_point(156.0, -26.0, classes=["given"], ID="C")
    B = model.set_point(211.0, -26.0, classes=["given"], ID="B")

    model.construct_line(D, B)
    model.set_segment(D, B)
    model.set_segment(D, C)
    model.set_segment(D, A)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    return model


if __name__ == "__main__":
    construct_g1()
