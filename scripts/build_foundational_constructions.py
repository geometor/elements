"""Generate foundational SVG figures (g1.svg) and geometor.model scripts (g1.py) for Elements 2.0.

Covers early definitions, postulates, and common notions:
- I.def.1 (point)
- I.def.2 (line)
- I.def.3 (extremities of a segment)
- I.def.4 (segment)
- I.def.15 (circle)
- I.def.16 (center of a circle)
- I.def.20 (equilateral, isosceles, and scalene triangles)
- I.post.1 (construct a segment between two points)
- I.post.2 (extend a segment along a line)
- I.post.3 (construct a circle from center and radius)
- I.cn.4 (things that coincide are equal)
"""

from __future__ import annotations

from pathlib import Path

SVG_STYLE_AND_DEFS = """  <style>
    :root {
      --geom-fg: #18181b;
      --geom-bg: #ffffff;
      --geom-point-stroke: #ffffff;
      --geom-poly-fill: #000000;
      --geom-accent: #c88a1e;
      --geom-assert: #16a34a;
      --geom-coincide: #38bdf8;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --geom-fg: #d6cfc5;
        --geom-bg: #1e1e20;
        --geom-point-stroke: #1e1e20;
        --geom-poly-fill: #d6cfc5;
        --geom-accent: #e8b85a;
        --geom-assert: #5ec27e;
        --geom-coincide: #38bdf8;
      }
    }
    .euclid-graphic {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-style: normal;
      font-weight: 700;
      background-color: var(--geom-bg);
    }
    .geom-line {
      stroke: var(--geom-fg);
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-bold {
      stroke: var(--geom-fg);
      stroke-width: 2.2;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-circle, .geom-curve, .geom-ellipse {
      stroke: var(--geom-fg);
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-arc {
      stroke: var(--geom-fg);
      stroke-width: 1.6;
      stroke-linecap: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-dashed, .geom-line-dashed, .geom-arc-dashed, .geom-aux, .geom-Auxiliary, .geom-construction {
      stroke: var(--geom-fg);
      stroke-width: 1.5;
      stroke-dasharray: 4, 3;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      opacity: 0.7;
      transition: stroke 0.15s, stroke-width 0.15s, opacity 0.15s;
    }
    .geom-tick-mark {
      stroke: var(--geom-assert);
      stroke-width: 2;
      stroke-linecap: round;
      fill: none;
    }
    .geom-polygon {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.04;
      stroke: none;
      transition: fill-opacity 0.15s, stroke 0.15s;
    }
    .geom-point {
      fill: var(--geom-fg);
      stroke: var(--geom-point-stroke);
      stroke-width: 1;
      transition: fill 0.15s, r 0.15s;
    }
    .geom-label {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 14.5px;
      font-weight: 700;
      font-style: normal;
      fill: var(--geom-fg);
      user-select: none;
    }
    .geom-overlay {
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.12s ease;
    }
    [data-ref]:hover, .highlight, .geom-highlight-active {
      opacity: 1 !important;
      stroke: var(--geom-accent) !important;
      cursor: pointer;
    }
    text[data-ref]:hover, text.highlight, text.geom-highlight-active, text.geom-highlight-secondary, text.geom-highlight-active *, text.geom-highlight-secondary * {
      opacity: 1 !important;
      fill: var(--geom-accent) !important;
      stroke: none !important;
    }
    .geom-polygon:hover, .geom-polygon.highlight, polygon.geom-highlight-active, path.geom-polygon.geom-highlight-active {
      opacity: 1 !important;
      fill-opacity: 0.24 !important;
      fill: var(--geom-accent) !important;
      stroke: var(--geom-accent) !important;
    }
    .geom-point:hover, .geom-point.highlight, circle.geom-point.geom-highlight-active, circle.geom-highlight-active {
      opacity: 1 !important;
      fill: var(--geom-accent) !important;
      stroke: none !important;
    }
    .geom-assert-active {
      opacity: 1 !important;
      stroke: var(--geom-assert) !important;
    }
    text.geom-assert-active, text.geom-assert-secondary, text.geom-assert-active *, text.geom-assert-secondary * {
      opacity: 1 !important;
      fill: var(--geom-assert) !important;
      stroke: none !important;
    }
    polygon.geom-assert-active, path.geom-polygon.geom-assert-active {
      opacity: 1 !important;
      fill-opacity: 0.22 !important;
      fill: var(--geom-assert) !important;
      stroke: var(--geom-assert) !important;
    }
    circle.geom-point.geom-assert-active, circle.geom-assert-active {
      opacity: 1 !important;
      fill: var(--geom-assert) !important;
      stroke: none !important;
    }
    path.geom-assert-active.geom-tick-1 {
      marker-mid: url(#geom-tick-1);
    }
    path.geom-assert-active.geom-tick-2 {
      marker-mid: url(#geom-tick-2);
    }
    path.geom-assert-active.geom-tick-3 {
      marker-mid: url(#geom-tick-3);
    }
  </style>
  <defs>
    <marker id="geom-tick-1" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="-1.8" y1="-4.5" x2="-1.8" y2="4.5" class="geom-tick-mark" />
      <line x1="1.8" y1="-4.5" x2="1.8" y2="4.5" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="-3.2" y1="-4.5" x2="-3.2" y2="4.5" class="geom-tick-mark" />
      <line x1="0" y1="-4.5" x2="0" y2="4.5" class="geom-tick-mark" />
      <line x1="3.2" y1="-4.5" x2="3.2" y2="4.5" class="geom-tick-mark" />
    </marker>
  </defs>"""


def wrap_svg(prop_id: str, width: int, height: int, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="euclid-graphic" '
        f'data-graphic-id="g1" data-graphic="g1" data-proposition="{prop_id}">\n'
        f"{SVG_STYLE_AND_DEFS}\n"
        f"{body.rstrip()}\n"
        f"</svg>\n"
    )


FOUNDATIONAL_UNITS = {
    "I.def.1": {
        "width": 240,
        "height": 110,
        "svg": """  <g id="elements"></g>
  <g id="graphics"></g>
  <g id="highlights" style="pointer-events: none;"></g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="120" cy="58" r="4" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="120" y="42" text-anchor="middle" class="geom-label">A</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Definition 1 (I.def.1 — point).

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
''',
    },
    "I.def.2": {
        "width": 280,
        "height": 110,
        "svg": """  <g id="elements">
    <path id="el-line-AB" data-ref="[ A B ]" data-type="line" class="geom-dashed" d="M 24 58 L 140 58 L 256 58" />
  </g>
  <g id="graphics"></g>
  <g id="highlights" style="pointer-events: none;">
    <path id="hl-line-AB" data-ref="[ A B ]" class="geom-line geom-overlay" d="M 24 58 L 140 58 L 256 58" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="84" cy="58" r="3.5" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="196" cy="58" r="3.5" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="84" y="42" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="196" y="42" text-anchor="middle" class="geom-label">B</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Definition 2 (I.def.2 — line).

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
''',
    },
    "I.def.3": {
        "width": 280,
        "height": 110,
        "svg": """  <g id="elements"></g>
  <g id="graphics">
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-line" d="M 76 58 L 140 58 L 204 58" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-line geom-overlay" d="M 76 58 L 140 58 L 204 58" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="76" cy="58" r="4" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="204" cy="58" r="4" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="76" y="42" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="204" y="42" text-anchor="middle" class="geom-label">B</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Definition 3 (I.def.3 — extremities of a segment).

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
''',
    },
    "I.def.4": {
        "width": 280,
        "height": 110,
        "svg": """  <g id="elements">
    <path id="el-line-AB" data-ref="[ A B ]" data-type="line" class="geom-dashed" d="M 24 58 L 140 58 L 256 58" />
  </g>
  <g id="graphics">
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-bold" d="M 76 58 L 140 58 L 204 58" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <path id="hl-line-AB" data-ref="[ A B ]" class="geom-line geom-overlay" d="M 24 58 L 140 58 L 256 58" />
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-bold geom-overlay" d="M 76 58 L 140 58 L 204 58" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="76" cy="58" r="3.8" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="204" cy="58" r="3.8" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="76" y="42" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="204" y="42" text-anchor="middle" class="geom-label">B</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Definition 4 (I.def.4 — segment).

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
''',
    },
    "I.def.15": {
        "width": 260,
        "height": 190,
        "svg": """  <g id="elements">
    <circle id="el-circle-BCD" data-ref="( B C D )" data-aliases="( A B )" data-type="circle" cx="130" cy="96" r="68" class="geom-circle" />
  </g>
  <g id="graphics">
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-line" d="M 130 96 L 164 96 L 198 96" />
    <path id="el-seg-AC" data-ref="/ A C /" data-type="segment" class="geom-line" d="M 130 96 L 147 66.55 L 164 37.11" />
    <path id="el-seg-AD" data-ref="/ A D /" data-type="segment" class="geom-line" d="M 130 96 L 96 96 L 62 96" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <circle id="hl-circle-BCD" data-ref="( B C D )" data-aliases="( A B )" cx="130" cy="96" r="68" class="geom-circle geom-overlay" />
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-line geom-overlay" d="M 130 96 L 164 96 L 198 96" />
    <path id="hl-seg-AC" data-ref="/ A C /" class="geom-line geom-overlay" d="M 130 96 L 147 66.55 L 164 37.11" />
    <path id="hl-seg-AD" data-ref="/ A D /" class="geom-line geom-overlay" d="M 130 96 L 96 96 L 62 96" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="130" cy="96" r="3.5" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="198" cy="96" r="3.5" class="geom-point" />
    <circle id="el-pt-C" data-ref="C" data-type="point" cx="164" cy="37.11" r="3.5" class="geom-point" />
    <circle id="el-pt-D" data-ref="D" data-type="point" cx="62" cy="96" r="3.5" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="130" y="114" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="208" y="100" text-anchor="start" class="geom-label">B</text>
    <text id="lbl-C" data-ref="C" x="171" y="29" text-anchor="start" class="geom-label">C</text>
    <text id="lbl-D" data-ref="D" x="52" y="100" text-anchor="end" class="geom-label">D</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Definition 15 (I.def.15 — circle).

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
''',
    },
    "I.def.16": {
        "width": 260,
        "height": 190,
        "svg": """  <g id="elements">
    <circle id="el-circle-BCD" data-ref="( B C D )" data-aliases="( A B )" data-type="circle" cx="130" cy="96" r="68" class="geom-circle" />
  </g>
  <g id="graphics">
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-line" d="M 130 96 L 164 96 L 198 96" />
    <path id="el-seg-AC" data-ref="/ A C /" data-type="segment" class="geom-line" d="M 130 96 L 147 66.55 L 164 37.11" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <circle id="hl-circle-BCD" data-ref="( B C D )" data-aliases="( A B )" cx="130" cy="96" r="68" class="geom-circle geom-overlay" />
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-line geom-overlay" d="M 130 96 L 164 96 L 198 96" />
    <path id="hl-seg-AC" data-ref="/ A C /" class="geom-line geom-overlay" d="M 130 96 L 147 66.55 L 164 37.11" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="130" cy="96" r="4" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="198" cy="96" r="3.5" class="geom-point" />
    <circle id="el-pt-C" data-ref="C" data-type="point" cx="164" cy="37.11" r="3.5" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="130" y="114" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="208" y="100" text-anchor="start" class="geom-label">B</text>
    <text id="lbl-C" data-ref="C" x="171" y="29" text-anchor="start" class="geom-label">C</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Definition 16 (I.def.16 — center of a circle).

This point is called the center of the circle.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_g1() -> Model:
    """Construct the foundational figure for I.def.16 (center A of circle ( B C D ))."""
    model = Model("I.def.16")
    A = model.set_point(0, 0, classes=["given"], ID="A")
    B = model.set_point(1, 0, classes=["given"], ID="B")
    model.construct_circle(A, B)
    C = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, ID="C")
    model.set_segment(A, B)
    model.set_segment(A, C)
    return model


if __name__ == "__main__":
    construct_g1()
''',
    },
    "I.def.20": {
        "width": 320,
        "height": 140,
        "svg": """  <g id="elements"></g>
  <g id="graphics">
    <polygon id="el-tri-ABC" data-ref="&lt; A B C &gt;" data-type="polygon" points="24,108 96,108 60,45.65" class="geom-polygon" />
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-line" d="M 24 108 L 60 108 L 96 108" />
    <path id="el-seg-BC" data-ref="/ B C /" data-type="segment" class="geom-line" d="M 96 108 L 78 76.82 L 60 45.65" />
    <path id="el-seg-CA" data-ref="/ C A /" data-type="segment" class="geom-line" d="M 60 45.65 L 42 76.82 L 24 108" />
    <polygon id="el-tri-DEF" data-ref="&lt; D E F &gt;" data-type="polygon" points="126,108 182,108 154,34" class="geom-polygon" />
    <path id="el-seg-DE" data-ref="/ D E /" data-type="segment" class="geom-line" d="M 126 108 L 154 108 L 182 108" />
    <path id="el-seg-EF" data-ref="/ E F /" data-type="segment" class="geom-line" d="M 182 108 L 168 71 L 154 34" />
    <path id="el-seg-FD" data-ref="/ F D /" data-type="segment" class="geom-line" d="M 154 34 L 140 71 L 126 108" />
    <polygon id="el-tri-GHK" data-ref="&lt; G H K &gt;" data-type="polygon" points="212,108 298,108 238,44" class="geom-polygon" />
    <path id="el-seg-GH" data-ref="/ G H /" data-type="segment" class="geom-line" d="M 212 108 L 255 108 L 298 108" />
    <path id="el-seg-HK" data-ref="/ H K /" data-type="segment" class="geom-line" d="M 298 108 L 268 76 L 238 44" />
    <path id="el-seg-KG" data-ref="/ K G /" data-type="segment" class="geom-line" d="M 238 44 L 225 76 L 212 108" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <polygon id="hl-tri-ABC" data-ref="&lt; A B C &gt;" points="24,108 96,108 60,45.65" class="geom-polygon geom-overlay" />
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-line geom-overlay" d="M 24 108 L 60 108 L 96 108" />
    <path id="hl-seg-BC" data-ref="/ B C /" class="geom-line geom-overlay" d="M 96 108 L 78 76.82 L 60 45.65" />
    <path id="hl-seg-CA" data-ref="/ C A /" class="geom-line geom-overlay" d="M 60 45.65 L 42 76.82 L 24 108" />
    <polygon id="hl-tri-DEF" data-ref="&lt; D E F &gt;" points="126,108 182,108 154,34" class="geom-polygon geom-overlay" />
    <path id="hl-seg-DE" data-ref="/ D E /" class="geom-line geom-overlay" d="M 126 108 L 154 108 L 182 108" />
    <path id="hl-seg-EF" data-ref="/ E F /" class="geom-line geom-overlay" d="M 182 108 L 168 71 L 154 34" />
    <path id="hl-seg-FD" data-ref="/ F D /" class="geom-line geom-overlay" d="M 154 34 L 140 71 L 126 108" />
    <polygon id="hl-tri-GHK" data-ref="&lt; G H K &gt;" points="212,108 298,108 238,44" class="geom-polygon geom-overlay" />
    <path id="hl-seg-GH" data-ref="/ G H /" class="geom-line geom-overlay" d="M 212 108 L 255 108 L 298 108" />
    <path id="hl-seg-HK" data-ref="/ H K /" class="geom-line geom-overlay" d="M 298 108 L 268 76 L 238 44" />
    <path id="hl-seg-KG" data-ref="/ K G /" class="geom-line geom-overlay" d="M 238 44 L 225 76 L 212 108" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="24" cy="108" r="3" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="96" cy="108" r="3" class="geom-point" />
    <circle id="el-pt-C" data-ref="C" data-type="point" cx="60" cy="45.65" r="3" class="geom-point" />
    <circle id="el-pt-D" data-ref="D" data-type="point" cx="126" cy="108" r="3" class="geom-point" />
    <circle id="el-pt-E" data-ref="E" data-type="point" cx="182" cy="108" r="3" class="geom-point" />
    <circle id="el-pt-F" data-ref="F" data-type="point" cx="154" cy="34" r="3" class="geom-point" />
    <circle id="el-pt-G" data-ref="G" data-type="point" cx="212" cy="108" r="3" class="geom-point" />
    <circle id="el-pt-H" data-ref="H" data-type="point" cx="298" cy="108" r="3" class="geom-point" />
    <circle id="el-pt-K" data-ref="K" data-type="point" cx="238" cy="44" r="3" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="20" y="124" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="98" y="124" text-anchor="middle" class="geom-label">B</text>
    <text id="lbl-C" data-ref="C" x="60" y="36" text-anchor="middle" class="geom-label">C</text>
    <text id="lbl-D" data-ref="D" x="122" y="124" text-anchor="middle" class="geom-label">D</text>
    <text id="lbl-E" data-ref="E" x="184" y="124" text-anchor="middle" class="geom-label">E</text>
    <text id="lbl-F" data-ref="F" x="154" y="25" text-anchor="middle" class="geom-label">F</text>
    <text id="lbl-G" data-ref="G" x="208" y="124" text-anchor="middle" class="geom-label">G</text>
    <text id="lbl-H" data-ref="H" x="300" y="124" text-anchor="middle" class="geom-label">H</text>
    <text id="lbl-K" data-ref="K" x="238" y="34" text-anchor="middle" class="geom-label">K</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Definition 20 (I.def.20 — equilateral, isosceles, and scalene triangles).
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
''',
    },
    "I.post.1": {
        "width": 280,
        "height": 110,
        "svg": """  <g id="elements"></g>
  <g id="graphics">
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-line" d="M 76 58 L 140 58 L 204 58" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-line geom-overlay" d="M 76 58 L 140 58 L 204 58" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="76" cy="58" r="3.8" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="204" cy="58" r="3.8" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="76" y="42" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="204" y="42" text-anchor="middle" class="geom-label">B</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Postulate 1 (I.post.1 — construct a segment).

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
''',
    },
    "I.post.2": {
        "width": 280,
        "height": 110,
        "svg": """  <g id="elements">
    <path id="el-line-AB" data-ref="[ A B ]" data-type="line" class="geom-dashed" d="M 24 58 L 140 58 L 256 58" />
  </g>
  <g id="graphics">
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-bold" d="M 60 58 L 105 58 L 150 58" />
    <path id="el-seg-BC" data-ref="/ B C /" data-aliases="/ A C /" data-type="segment" class="geom-line" d="M 150 58 L 188 58 L 226 58" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <path id="hl-line-AB" data-ref="[ A B ]" class="geom-line geom-overlay" d="M 24 58 L 140 58 L 256 58" />
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-bold geom-overlay" d="M 60 58 L 105 58 L 150 58" />
    <path id="hl-seg-BC" data-ref="/ B C /" data-aliases="/ A C /" class="geom-line geom-overlay" d="M 150 58 L 188 58 L 226 58" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="60" cy="58" r="3.8" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="150" cy="58" r="3.8" class="geom-point" />
    <circle id="el-pt-C" data-ref="C" data-type="point" cx="226" cy="58" r="3.8" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="60" y="42" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="150" y="42" text-anchor="middle" class="geom-label">B</text>
    <text id="lbl-C" data-ref="C" x="226" y="42" text-anchor="middle" class="geom-label">C</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Postulate 2 (I.post.2 — extend a segment).

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
''',
    },
    "I.post.3": {
        "width": 260,
        "height": 190,
        "svg": """  <g id="elements">
    <circle id="el-circle-BCD" data-ref="( B C D )" data-aliases="( A B )" data-type="circle" cx="130" cy="96" r="68" class="geom-circle" />
  </g>
  <g id="graphics">
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-line" d="M 130 96 L 164 96 L 198 96" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <circle id="hl-circle-BCD" data-ref="( B C D )" data-aliases="( A B )" cx="130" cy="96" r="68" class="geom-circle geom-overlay" />
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-line geom-overlay" d="M 130 96 L 164 96 L 198 96" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="130" cy="96" r="3.8" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="198" cy="96" r="3.8" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="122" y="92" text-anchor="end" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="208" y="100" text-anchor="start" class="geom-label">B</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Postulate 3 (I.post.3 — construct a circle).

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
''',
    },
    "I.cn.4": {
        "width": 280,
        "height": 135,
        "svg": """  <g id="elements">
    <path id="el-guide-AD" class="geom-dashed" d="M 68 44 L 68 92" />
    <path id="el-guide-BE" class="geom-dashed" d="M 212 44 L 212 92" />
  </g>
  <g id="graphics">
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-line" d="M 68 44 L 140 44 L 212 44" />
    <path id="el-seg-DE" data-ref="/ D E /" data-type="segment" class="geom-line" d="M 68 92 L 140 92 L 212 92" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-line geom-overlay" d="M 68 44 L 140 44 L 212 44" />
    <path id="hl-seg-DE" data-ref="/ D E /" class="geom-line geom-overlay" d="M 68 92 L 140 92 L 212 92" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="68" cy="44" r="3.8" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="212" cy="44" r="3.8" class="geom-point" />
    <circle id="el-pt-D" data-ref="D" data-type="point" cx="68" cy="92" r="3.8" class="geom-point" />
    <circle id="el-pt-E" data-ref="E" data-type="point" cx="212" cy="92" r="3.8" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="68" y="28" text-anchor="middle" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="212" y="28" text-anchor="middle" class="geom-label">B</text>
    <text id="lbl-D" data-ref="D" x="68" y="116" text-anchor="middle" class="geom-label">D</text>
    <text id="lbl-E" data-ref="E" x="212" y="116" text-anchor="middle" class="geom-label">E</text>
  </g>""",
        "py": '''"""Programmatic construction for Book I, Common Notion 4 (I.cn.4 — coincidence).

Things that coincide with one another are equal.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_g1() -> Model:
    """Construct superposed segments / A B / and / D E / demonstrating coincidence."""
    model = Model("I.cn.4")
    A = model.set_point(0, sp.Rational(1, 3), classes=["given"], ID="A")
    B = model.set_point(1, sp.Rational(1, 3), classes=["given"], ID="B")
    model.set_segment(A, B)

    D = model.set_point(0, 0, classes=["given"], ID="D")
    E = model.set_point(1, 0, classes=["given"], ID="E")
    model.set_segment(D, E)
    return model


if __name__ == "__main__":
    construct_g1()
''',
    },
}


def main() -> None:
    root = Path(__file__).resolve().parent.parent / "resources" / "constructions"
    for unit_id, spec in FOUNDATIONAL_UNITS.items():
        unit_dir = root / unit_id
        unit_dir.mkdir(parents=True, exist_ok=True)
        svg_str = wrap_svg(unit_id, spec["width"], spec["height"], spec["svg"])
        (unit_dir / "g1.svg").write_text(svg_str, encoding="utf-8")
        (unit_dir / "g1.py").write_text(spec["py"], encoding="utf-8")
        print(f"Wrote {unit_dir}/g1.svg and g1.py")


if __name__ == "__main__":
    main()
