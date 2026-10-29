"""
Pseudocode and tightened enunciation generator for GEOMETOR Elements 2.0.

Transforms classical Heath RST propositions and statements into tightened,
fact-oriented enunciations and structured ``.. step:: <kind> [justification]``
sequences highlighting the GEOMETOR functional hierarchy (``given``,
``construct``, ``intersect``, ``assert``, ``conclude``) and native symbolic
indications.
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple


# Curated fact-oriented enunciations for foundational Elements (keyed by canonical Euclid ID)
CURATED_ENUNCIATIONS: Dict[str, str] = {
    # Book I Definitions
    "I.def.1": "A point is that which has no part.",
    "I.def.2": "A line is breadthless length.",
    "I.def.3": "The extremities of a line are points.",
    "I.def.4": "A straight line lies evenly with the points on itself.",
    "I.def.5": "A surface is that which has length and breadth only.",
    "I.def.6": "The extremities of a surface are lines.",
    "I.def.7": "A plane surface lies evenly with the straight lines on itself.",
    "I.def.8": "A plane angle is the inclination to one another of two lines in a plane that meet and do not lie in a straight line.",
    "I.def.9": "A rectilineal angle is contained by two straight lines.",
    "I.def.10": "When a straight line standing on a straight line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing line is perpendicular to that on which it stands.",
    "I.def.11": "An obtuse angle is greater than a right angle.",
    "I.def.12": "An acute angle is less than a right angle.",
    "I.def.13": "A boundary is the extremity of anything.",
    "I.def.14": "A figure is that which is contained by any boundary or boundaries.",
    "I.def.15": "A circle is a plane figure contained by one line such that all segments falling upon it from its center are equal.",
    "I.def.16": "This point is called the center of the circle.",
    "I.def.17": "A diameter of a circle is any segment drawn through the center and terminated in both directions by the circumference; it bisects the circle.",
    "I.def.18": "A semicircle is the figure contained by a diameter and the circumference cut off by it.",
    "I.def.19": "Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.",
    "I.def.20": "Of trilateral figures, an equilateral triangle has three equal sides, an isosceles triangle has two equal sides, and a scalene triangle has three unequal sides.",
    "I.def.21": "A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.",
    "I.def.22": "Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opposite sides and angles equal but is neither equilateral nor right-angled.",
    "I.def.23": "Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.",
    # Book I Postulates
    "I.post.1": "Construct a segment between any two points.",
    "I.post.2": "Extend a finite segment continuously in a straight line.",
    "I.post.3": "Construct a circle with any center and radius.",
    "I.post.4": "All right angles are equal.",
    "I.post.5": "Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.",
    # Book I Common Notions
    "I.cn.1": "Things equal to the same thing are equal to one another.",
    "I.cn.2": "If equals are added to equals, the wholes are equal.",
    "I.cn.3": "If equals are subtracted from equals, the remainders are equal.",
    "I.cn.4": "Things that coincide with one another are equal.",
    "I.cn.5": "The whole is greater than the part.",
    # Book I Propositions
    "I.1": "Construct an equilateral triangle on a given finite segment.",
    "I.2": "Construct at a given point a segment equal to a given segment.",
    "I.3": "Cut off from the greater of two unequal segments a segment equal to the less.",
    "I.4": "Triangles with two sides and the included angle equal are congruent (SAS).",
    "I.5": "In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.",
    "I.6": "If two angles of a triangle are equal, the sides subtending the equal angles are also equal.",
    "I.7": "On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.",
    "I.8": "Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).",
    "I.9": "Bisect a given angle.",
    "I.10": "Bisect a given finite segment.",
    "I.11": "Construct a line at right angles to a given line from a given point on it.",
    "I.12": "Construct a perpendicular to a given infinite line from a given point not on it.",
    "I.13": "A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.",
    "I.14": "If two rays at a point on a line on opposite sides make adjacent angles summing to two right angles, the two rays are collinear.",
    "I.15": "Intersecting lines make their vertical angles equal.",
    "I.16": "In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.",
    "I.17": "In any triangle, the sum of any two angles is less than two right angles.",
    "I.18": "In any triangle, the greater side subtends the greater angle.",
    "I.19": "In any triangle, the greater angle is subtended by the greater side.",
    "I.20": "In any triangle, the sum of any two sides is greater than the remaining side.",
    "I.21": "Segments constructed from the endpoints of one side of a triangle to an interior point have a lesser sum but contain a greater angle than the other two sides.",
    "I.22": "Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.",
    "I.23": "Construct on a given line at a given point an angle equal to a given angle.",
    "I.24": "If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.",
    "I.25": "If two triangles have two sides equal to two sides respectively, the one with the greater base has the greater included angle.",
    "I.26": "Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).",
    "I.27": "If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.",
    "I.28": "If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.",
    "I.29": "A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.",
    "I.30": "Lines parallel to the same line are parallel to one another.",
    "I.31": "Construct through a given point a line parallel to a given line.",
    "I.32": "In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.",
    "I.33": "Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.",
    "I.34": "In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.",
    "I.35": "Parallelograms on the same base and in the same parallels are equal in area.",
    "I.36": "Parallelograms on equal bases and in the same parallels are equal in area.",
    "I.37": "Triangles on the same base and in the same parallels are equal in area.",
    "I.38": "Triangles on equal bases and in the same parallels are equal in area.",
    "I.39": "Equal triangles on the same base and on the same side lie in the same parallels.",
    "I.40": "Equal triangles on equal bases and on the same side lie in the same parallels.",
    "I.41": "If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.",
    "I.42": "Construct, in a given angle, a parallelogram equal in area to a given triangle.",
    "I.43": "In any parallelogram, the complements of the parallelograms about the diagonal are equal in area.",
    "I.44": "Apply to a given segment, in a given angle, a parallelogram equal in area to a given triangle.",
    "I.45": "Construct, in a given angle, a parallelogram equal in area to a given polygon.",
    "I.46": "Construct a square on a given segment.",
    "I.47": "In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).",
    "I.48": "If the square on one side of a triangle equals the sum of the squares on the other two sides, the angle contained by those two sides is right.",
}


def tighten_enunciation_text(text: str, canonical_ref: str = "") -> str:
    """Return a concise, fact-oriented enunciation string."""
    if canonical_ref in CURATED_ENUNCIATIONS:
        return CURATED_ENUNCIATIONS[canonical_ref]

    s = re.sub(r"^(?:\[\d+\]\s*)*(?:\*\*\d+\.\*\*|\d+\.)?\s*", "", text.strip())
    s = " ".join(line.strip() for line in s.splitlines() if line.strip())

    # Clean archaic constructions into direct imperative / declarative facts
    replacements = [
        (r"^On a given finite straight line to (construct|describe)\b", r"\1 on a given segment"),
        (r"^On a given straight line to (construct|describe)\b", r"\1 on a given segment"),
        (r"^To bisect a given\b", "Bisect a given"),
        (r"^To construct\b", "Construct"),
        (r"^To describe\b", "Construct"),
        (r"^To draw\b", "Construct"),
        (r"^To find\b", "Find"),
        (r"^To cut off\b", "Cut off"),
        (r"^To cut\b", "Cut"),
        (r"^From a given\b", "From a given"),
        (r"^In a given circle to inscribe\b", "Inscribe in a given circle"),
        (r"^About a given circle to circumscribe\b", "Circumscribe about a given circle"),
        (r"^In a given triangle to inscribe\b", "Inscribe in a given triangle"),
        (r"^About a given triangle to circumscribe\b", "Circumscribe about a given triangle"),
        (r"\brectilineal angle\b", "angle"),
        (r"\brectilineal angles\b", "angles"),
        (r"\brectilineal figure\b", "polygon"),
        (r"\brectilineal figures\b", "polygons"),
        (r"\bfinite straight line\b", "segment"),
        (r"\bare equal to one another\b", "are equal"),
        (r"\bwill be equal to one another\b", "are equal"),
        (r"\bbe equal to\b", "equals"),
        (r"\bwill also be\b", "is"),
        (r"\bwill be\b", "is"),
        (r"\s+;", ";"),
        (r"\s+:", ":"),
    ]
    for pat, repl in replacements:
        s = re.sub(pat, repl, s)

    if s and s[0].islower():
        s = s[0].upper() + s[1:]
    return s


_ROLE_PROTECT_RE = re.compile(r":[A-Za-z0-9_.-]+:`[^`]+`")


def _split_clauses_preserving_roles(paragraph_text: str) -> List[str]:
    """Split a paragraph on ';' boundaries (and compound ', and let' construction boundaries) outside RST roles."""
    placeholders: Dict[str, str] = {}
    counter = 0

    def _protect(m: re.Match) -> str:
        nonlocal counter
        counter += 1
        tok = f"__ROLE_{counter}__"
        placeholders[tok] = m.group(0)
        return tok

    protected = _ROLE_PROTECT_RE.sub(_protect, paragraph_text)
    # Keep '; and it has been ...' attached to the preceding conclusion clause
    protected = re.sub(r";\s+and\s+it\s+has\s+been\b", ", and it has been", protected, flags=re.IGNORECASE)
    # Attach trailing :just:`...` after a semicolon to the clause BEFORE the semicolon
    protected = re.sub(
        r";\s*(__ROLE_\d+__)",
        lambda m: f" {m.group(1)};" if placeholders.get(m.group(1), "").startswith(":just:") else m.group(0),
        protected,
    )
    # Split compound construction clauses like "let DE be joined, and on DE let ... be constructed"
    protected = re.sub(
        r",\s+and\s+((?:on|from|with|at|through|in)\s+[^;]+?\blet\b|\blet\b)",
        r"; \1",
        protected,
        flags=re.IGNORECASE,
    )

    parts = [p.strip() for p in protected.split(";") if p.strip()]
    restored_parts: List[str] = []
    for p in parts:
        for tok, orig in placeholders.items():
            p = p.replace(tok, orig)
        restored_parts.append(p)
    return restored_parts


def _extract_inline_justifications(clause: str) -> Tuple[str, Optional[str]]:
    """Extract any `:just:`[G.x] <G.x>`` roles from a clause and return (cleaned_clause, combined_just_arg)."""
    just_matches = list(re.finditer(r":just:`([^`]+)`", clause))
    if not just_matches:
        return clause.strip(), None

    targets: List[str] = []
    for m in just_matches:
        raw = m.group(1).strip()
        m_t = re.search(r"<([^>]+)>", raw)
        t_str = m_t.group(1) if m_t else raw.strip("[]")
        for part in t_str.split(","):
            p = part.strip()
            if p and p not in targets:
                targets.append(p)

    cleaned = re.sub(r"\s*:just:`[^`]+`", "", clause).strip()
    cleaned = re.sub(r"[;,]\s*$", ".", cleaned)
    if targets:
        t_joined = ", ".join(targets)
        return cleaned, f"[{t_joined}] <{t_joined}>"
    return cleaned, None


def _rewrite_clause_to_pseudocode(clause: str, is_first_step: bool = False) -> Optional[Tuple[str, str]]:
    """Rewrite a single Heath clause into (step_kind, concise_pseudocode_text) or None if redundant."""
    s = " ".join(line.strip() for line in clause.strip().splitlines() if line.strip())
    if not s:
        return None

    # Strip trailing "Thus it is required..." if attached to the first sentence
    s = re.sub(r"\s*Thus it is required\b.*$", "", s, flags=re.IGNORECASE).strip()
    if not s:
        return None

    # 1. Skip pure restatement / QED boilerplate that adds no geometric elements or equalities
    if re.match(
        r"^(?:Thus it is required\b|I say that\b|\(Being\) what it was required\b|Q\.\s*E\.\s*[DF]\.?$)",
        s,
        re.IGNORECASE,
    ):
        if ":eq:`" not in s:
            return None
        s = re.sub(r"^I say that\s+", "", s, flags=re.IGNORECASE).strip()

    # 2. Check for "Given" step
    if re.match(r"^Let\b.*\bbe (?:the )?given\b", s, re.IGNORECASE) or (
        is_first_step
        and re.match(r"^Let\b", s, re.IGNORECASE)
        and not re.search(r"\bbe\s+(?:described|joined|drawn|constructed|cut|taken|produced|bisected)\b", s, re.IGNORECASE)
    ):
        body = s
        body = re.sub(r"^Let\s+", "", body, flags=re.IGNORECASE)
        body = _strip_redundant_type_nouns(body)
        body = re.sub(
            r"\s+be\s+(?:the\s+)?given\s+(?:finite\s+straight\s+lines?|straight\s+lines?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)\.?$",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(
            r"\bbe\s+(?:the\s+)?given\s+(?:finite\s+straight\s+lines?|straight\s+lines?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)\b",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(
            r"\b(?:the\s+)?given\s+(?:finite\s+straight\s+lines?|straight\s+lines?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)\.?$",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(r"\s*,\s*and\s+", ", ", body, flags=re.IGNORECASE)
        body = re.sub(r"\s{2,}", " ", body).strip(" ,.")
        return ("given", body)

    # 3. Check for Circle construction: "with centre A and distance AB let the circle BCD be described"
    m_circle = re.match(
        r"^(?:again,\s*|and\s+again,\s*|and\s+)?with\s+centre\s+(:g:`[^`]+`)\s+and\s+(?:distance|radius)\s+(:g:`[^`]+`)\s+let\s+(?:the\s+)?circle\s+(:g:`[^`]+`)\s+be\s+described\.?$",
        s,
        re.IGNORECASE,
    )
    if m_circle:
        center, radius, circle = m_circle.group(1), m_circle.group(2), m_circle.group(3)
        return ("construct", f"**circle** {circle} with center {center} and radius {radius}")

    # 4. Check for Intersection + Join: "from the point C, in which the circles cut one another, to the points A, B let the straight lines CA, CB be joined"
    m_int_join = re.match(
        r"^(?:and\s+)?from\s+(?:the\s+point\s+)?(:g:`[^`]+`),\s*in\s+which\s+the\s+circles\s+cut\s+one\s+another,\s*to\s+(?:the\s+points\s+)?(.+?)\s+let\s+(?:the\s+straight\s+lines\s+)?(.+?)\s+be\s+joined\.?$",
        s,
        re.IGNORECASE,
    )
    if m_int_join:
        pt_c, pts_to, segs = m_int_join.group(1), m_int_join.group(2), m_int_join.group(3)
        return (
            "intersect_and_join",
            f"**point** {pt_c} at intersection of circles|||**segment** {segs} joining {pt_c} to {pts_to}",
        )

    # 5. Check for simple Segment Join: "from A to B let AB be joined" or "let AB be joined"
    m_from_join = re.match(
        r"^(?:and\s+)?from\s+(?:the\s+point\s+)?(:g:`[^`]+`)\s+to\s+(?:the\s+point\s+)?(:g:`[^`]+`)\s+let\s+(?:the\s+straight\s+line\s+)?(:g:`[^`]+`)\s+be\s+joined\.?$",
        s,
        re.IGNORECASE,
    )
    if m_from_join:
        p1, p2, seg = m_from_join.group(1), m_from_join.group(2), m_from_join.group(3)
        return ("construct", f"**segment** {seg} from {p1} to {p2}")

    m_let_join = re.match(
        r"^(?:and\s+|then\s+)?let\s+(?:the\s+straight\s+lines?\s+)?(.+?)\s+be\s+joined\.?$",
        s,
        re.IGNORECASE,
    )
    if m_let_join:
        segs = _strip_redundant_type_nouns(m_let_join.group(1))
        return ("construct", f"**segment** {segs}")

    # 6. Check for Equilateral Triangle construction: "on it / on AB let the equilateral triangle DAB be constructed"
    m_equi = re.match(
        r"^(?:and\s+)?on\s+(.+?)\s+let\s+the\s+(.+?)\s+triangle\s+(:g:`[^`]+`)\s+be\s+constructed\.?$",
        s,
        re.IGNORECASE,
    )
    if m_equi:
        base, eq_role, tri = _strip_redundant_type_nouns(m_equi.group(1)), m_equi.group(2), m_equi.group(3)
        return ("construct", f"**triangle** {tri} ({eq_role}) on {base}")

    # 7. Check for Line Extension (produced): "let AE, BF be produced in a straight line with DA, DB"
    m_prod = re.match(
        r"^(?:and\s+)?let\s+(?:the\s+straight\s+lines?\s+)?(.+?)\s+be\s+produced\s+in\s+a\s+straight\s+line\s+with\s+(.+?)\.?$",
        s,
        re.IGNORECASE,
    )
    if m_prod:
        ext, orig = _strip_redundant_type_nouns(m_prod.group(1)), _strip_redundant_type_nouns(m_prod.group(2))
        return ("construct", f"**extend** {orig} to {ext}")

    # 8. Check for Cut Off equal segment: "let AE be cut off from AC equal to AD"
    m_cut = re.match(
        r"^(?:and\s+)?let\s+(:g:`[^`]+`)\s+be\s+cut\s+off\s+from\s+(:g:`[^`]+`)\s+(.+?)\.?$",
        s,
        re.IGNORECASE,
    )
    if m_cut:
        seg, src, rest = m_cut.group(1), m_cut.group(2), _strip_redundant_type_nouns(m_cut.group(3))
        return ("construct", f"**cut off** {seg} on {src} {rest}")

    # 9. Check for Point taken at random: "let a point D be taken at random on AB"
    m_pt = re.match(
        r"^(?:and\s+)?let\s+(?:a\s+point\s+)?(:g:`[^`]+`)\s+be\s+taken\s+(?:at\s+random\s+)?on\s+(.+?)\.?$",
        s,
        re.IGNORECASE,
    )
    if m_pt:
        pt, target = m_pt.group(1), _strip_redundant_type_nouns(m_pt.group(2))
        return ("construct", f"**point** {pt} on {target}")

    # 10. General construction vs assertion vs conclusion classification
    cleaned = _strip_redundant_type_nouns(s)
    cleaned = re.sub(r"^(?:Now,\s*|Again,\s*|Then,\s*|And\s+|But\s+|For,\s*)", "", cleaned)
    if cleaned and cleaned[0].islower():
        cleaned = cleaned[0].upper() + cleaned[1:]

    if re.search(
        r"\blet\b.+\bbe\s+(?:described|constructed|drawn|joined|produced|bisected|cut|placed|applied|made|taken|set\s+up)\b",
        s,
        re.IGNORECASE,
    ):
        return ("construct", cleaned)
    if re.search(r"\bcut\s+one\s+another\s+at\b|\bmeet\s+(?:one\s+another\s+)?at\b", s, re.IGNORECASE):
        return ("intersect", cleaned)
    return ("assert", cleaned)


def _strip_redundant_type_nouns(text: str) -> str:
    """Strip verbose Euclidean type prefixes immediately preceding symbolic :g: indications."""
    s = text
    patterns = [
        (r"\bthe\s+given\s+finite\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+given\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+given\s+rectilineal\s+angle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+given\s+point\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+finite\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+three\s+straight\s+lines\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+two\s+straight\s+lines\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+straight\s+lines\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+points\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+point\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+circles\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+circle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+rectilineal\s+angles\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+rectilineal\s+angle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+angles\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+angle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+triangles\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+triangle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bcentre\b", "center"),
    ]
    for pat, repl in patterns:
        s = re.sub(pat, repl, s, flags=re.IGNORECASE)
    return s


def generate_pseudocode_rst(
    heath_content_rst: str,
    canonical_ref: str,
    node_type: str,
) -> str:
    """Transform a Heath RST body (with G-Index roles/justifications) into Track 1 Pseudocode RST."""
    if node_type in ("def", "post", "cn"):
        m_enun = re.match(
            r"^\.\.\s+enunciation::\n+((?:[ \t]+[^\n]*\n?|\n)*)(.*)",
            heath_content_rst.strip(),
            re.DOTALL,
        )
        if m_enun:
            raw_enun = m_enun.group(1)
            rest = m_enun.group(2).strip()
            tight_enun = tighten_enunciation_text(raw_enun, canonical_ref)
            indented = "\n".join(f"   {line}" for line in tight_enun.splitlines())
            out = f".. enunciation::\n\n{indented}"
            if rest:
                out += f"\n\n{rest}"
            return out
        return heath_content_rst

    lines = heath_content_rst.strip().splitlines()
    blocks: List[str] = []
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if not line.strip():
            idx += 1
            continue
        if line.startswith(".. "):
            block_lines = [line]
            idx += 1
            while idx < len(lines) and (not lines[idx].strip() or lines[idx].startswith((" ", "\t"))):
                block_lines.append(lines[idx])
                idx += 1
            blocks.append("\n".join(block_lines).rstrip())
        else:
            block_lines = [line]
            idx += 1
            while idx < len(lines) and lines[idx].strip() and not lines[idx].startswith(".. "):
                block_lines.append(lines[idx])
                idx += 1
            blocks.append("\n".join(block_lines).rstrip())

    header_blocks: List[str] = []
    step_items: List[Tuple[str, Optional[str], str]] = []  # (kind, justification, body)
    footer_blocks: List[str] = []
    pending_premise: Optional[str] = None
    pending_just: Optional[str] = None

    for b in blocks:
        b_strip = b.strip()
        if b_strip.startswith(".. enunciation::"):
            b_lines = b_strip.splitlines()
            raw_enun = "\n".join(l.strip() for l in b_lines[1:] if l.strip())
            tight_enun = tighten_enunciation_text(raw_enun, canonical_ref)
            header_blocks.append(f".. enunciation::\n\n   {tight_enun}")
            continue

        if b_strip.startswith(".. picture::"):
            header_blocks.append(b_strip)
            continue

        if b_strip.startswith((".. porism::", ".. lemma::", ".. scholium::")):
            footer_blocks.append(b_strip)
            continue

        if b_strip.startswith(".. qed::"):
            continue

        m_dir = re.match(
            r"^\.\.\s+(assertion|subclause|sub-clause)::(?:[ \t]+([^\n]+))?\n+([\s\S]+)$",
            b_strip,
        )
        if m_dir:
            dir_just = (m_dir.group(2) or "").strip() or None
            dir_body = " ".join(l.strip() for l in m_dir.group(3).splitlines() if l.strip())
            dir_body, inline_just = _extract_inline_justifications(dir_body)
            just = dir_just or inline_just or pending_just
            pending_just = None
            if pending_premise:
                prem = pending_premise.rstrip(",; ")
                combined = f"{prem} → {dir_body}"
                pending_premise = None
            else:
                combined = dir_body
            cleaned = _strip_redundant_type_nouns(combined)
            cleaned = re.sub(r"^(?:Now,\s*|Again,\s*|Then,\s*|And\s+|But\s+|For,\s*)", "", cleaned)
            if cleaned and cleaned[0].islower():
                cleaned = cleaned[0].upper() + cleaned[1:]
            step_items.append(("assert", just, cleaned))
            continue

        clauses = _split_clauses_preserving_roles(b_strip)
        for c in clauses:
            c_clean, c_just = _extract_inline_justifications(c)
            if c_clean.endswith(",") and re.match(
                r"^(?:Now,\s*|Again,\s*|Then,\s*|For,\s*|Since\b|And\s+since\b)",
                c_clean,
                re.IGNORECASE,
            ):
                pending_premise = _strip_redundant_type_nouns(c_clean)
                if c_just:
                    pending_just = c_just
                continue

            if re.match(r"^And\s+things\s+which\s+are\s+equal\b", c_clean, re.IGNORECASE) and c_just:
                pending_just = c_just
                continue

            rewritten = _rewrite_clause_to_pseudocode(c_clean, is_first_step=(len(step_items) == 0))
            if not rewritten:
                continue

            kind, text = rewritten
            just = c_just or pending_just
            pending_just = None
            if pending_premise:
                text = f"{pending_premise.rstrip(',; ')} → {text}"
                pending_premise = None

            if kind == "intersect_and_join":
                int_text, join_text = text.split("|||", 1)
                step_items.append(("intersect", None, int_text))
                step_items.append(("construct", just, join_text))
            else:
                step_items.append((kind, just, text))

    if step_items:
        last_kind, last_just, last_body = step_items[-1]
        if last_kind == "assert":
            step_items[-1] = ("conclude", last_just, last_body)

    rendered_steps: List[str] = []
    for kind, just, body in step_items:
        arg_str = f"{kind} {just}" if just else kind
        clean_body = " ".join(l.strip() for l in body.splitlines() if l.strip())
        rendered_steps.append(f".. step:: {arg_str}\n\n   {clean_body}")

    all_parts = header_blocks + rendered_steps + footer_blocks
    return "\n\n".join(all_parts)
