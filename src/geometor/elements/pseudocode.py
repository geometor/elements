"""
Pseudocode, formal signature, and tightened enunciation generator for GEOMETOR Elements 2.0.

Transforms classical Heath RST propositions and statements into:
- Tightened, fact-oriented enunciations (``.. enunciation::``)
- Formal proposition/rule signatures (``.. signature::``) with ``given`` and ``construct`` / ``prove`` contracts
- Composable function invocations (``:fn:`name <G.x>`(...) → ...``) for ``construct`` steps
- Symbolic intersection steps (``... ∩ ... → ...``) for ``intersect`` steps
- Semantic rule justifications (``∵ rule_name``) for ``assert`` / ``conclude`` steps
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


# Canonical semantic function & rule names keyed by Euclid ID
SEMANTIC_NAMES: Dict[str, str] = {
    # Book I Postulates
    "I.post.1": "segment",
    "I.post.2": "extend",
    "I.post.3": "circle",
    "I.post.4": "right_angles_equal",
    "I.post.5": "parallel_postulate",
    # Book I Common Notions
    "I.cn.1": "equal_transitive",
    "I.cn.2": "add_equals",
    "I.cn.3": "subtract_equals",
    "I.cn.4": "coinciding_equal",
    "I.cn.5": "whole_greater_than_part",
    # Book I Definitions
    "I.def.1": "point_def",
    "I.def.2": "line_def",
    "I.def.3": "line_extremities",
    "I.def.4": "straight_line_def",
    "I.def.5": "surface_def",
    "I.def.6": "surface_extremities",
    "I.def.7": "plane_surface_def",
    "I.def.8": "plane_angle_def",
    "I.def.9": "rectilineal_angle_def",
    "I.def.10": "right_angle_perpendicular",
    "I.def.11": "obtuse_angle_def",
    "I.def.12": "acute_angle_def",
    "I.def.13": "boundary_def",
    "I.def.14": "figure_def",
    "I.def.15": "circle_radii",
    "I.def.16": "circle_center",
    "I.def.17": "circle_diameter",
    "I.def.18": "semicircle_def",
    "I.def.19": "polygon_def",
    "I.def.20": "triangle_sides_def",
    "I.def.21": "triangle_angles_def",
    "I.def.22": "quadrilateral_def",
    "I.def.23": "parallel_lines_def",
    # Book I Propositions
    "I.1": "equilateral_triangle",
    "I.2": "transfer_segment",
    "I.3": "cut_equal_segment",
    "I.4": "sas_congruence",
    "I.5": "isosceles_base_angles",
    "I.6": "equal_angles_isosceles",
    "I.7": "unique_triangle_sides",
    "I.8": "sss_congruence",
    "I.9": "bisect_angle",
    "I.10": "bisect_segment",
    "I.11": "perpendicular_at",
    "I.12": "perpendicular_from",
    "I.13": "adjacent_angles_supplementary",
    "I.14": "supplementary_angles_collinear",
    "I.15": "vertical_angles_equal",
    "I.16": "exterior_angle_greater",
    "I.17": "two_angles_less_than_two_right",
    "I.18": "greater_side_greater_angle",
    "I.19": "greater_angle_greater_side",
    "I.20": "triangle_inequality",
    "I.21": "interior_triangle_bounds",
    "I.22": "triangle_from_segments",
    "I.23": "copy_angle",
    "I.24": "hinge_theorem",
    "I.25": "converse_hinge_theorem",
    "I.26": "asa_aas_congruence",
    "I.27": "alternate_angles_parallel",
    "I.28": "corresponding_angles_parallel",
    "I.29": "parallel_transversal_angles",
    "I.30": "parallel_transitive",
    "I.31": "parallel_line",
    "I.32": "triangle_angle_sum",
    "I.33": "join_equal_parallels",
    "I.34": "parallelogram_properties",
    "I.35": "parallelograms_same_base",
    "I.36": "parallelograms_equal_bases",
    "I.37": "triangles_same_base",
    "I.38": "triangles_equal_bases",
    "I.39": "equal_triangles_same_base_parallel",
    "I.40": "equal_triangles_equal_bases_parallel",
    "I.41": "parallelogram_double_triangle",
    "I.42": "parallelogram_from_triangle",
    "I.43": "parallelogram_complements",
    "I.44": "apply_parallelogram_on_segment",
    "I.45": "parallelogram_from_polygon",
    "I.46": "square_on_segment",
    "I.47": "pythagorean_theorem",
    "I.48": "converse_pythagorean",
    # Selected key Book II–VI Propositions
    "II.1": "distribute_rectangle",
    "II.2": "square_sum_rectangles",
    "II.3": "rectangle_whole_and_part",
    "II.4": "square_of_sum",
    "II.5": "difference_of_squares_equal_unequal",
    "II.6": "bisected_and_extended_segment",
    "II.7": "square_of_difference",
    "II.8": "four_rectangles_plus_square",
    "II.9": "sum_of_squares_equal_unequal",
    "II.10": "sum_of_squares_bisected_extended",
    "II.11": "cut_extreme_and_mean_ratio",
    "II.12": "law_of_cosines_obtuse",
    "II.13": "law_of_cosines_acute",
    "II.14": "square_from_polygon",
    "III.1": "find_circle_center",
    "III.17": "tangent_to_circle",
    "III.20": "inscribed_angle_theorem",
    "III.31": "thales_semicircle_theorem",
    "IV.1": "fit_chord_in_circle",
    "IV.2": "inscribe_triangle_in_circle",
    "IV.3": "circumscribe_triangle_about_circle",
    "IV.4": "inscribe_circle_in_triangle",
    "IV.5": "circumscribe_circle_about_triangle",
    "IV.6": "inscribe_square_in_circle",
    "IV.10": "golden_isosceles_triangle",
    "IV.11": "inscribe_pentagon_in_circle",
    "IV.15": "inscribe_hexagon_in_circle",
    "IV.16": "inscribe_pentadecagon_in_circle",
    "VI.9": "cut_nth_part",
    "VI.10": "cut_similarly",
    "VI.11": "third_proportional",
    "VI.12": "fourth_proportional",
    "VI.13": "mean_proportional",
    "VI.30": "extreme_and_mean_ratio",
}

_STOP_WORDS = {
    "a", "an", "the", "of", "to", "in", "on", "from", "with", "by", "for",
    "at", "into", "unto", "upon", "about", "between", "through", "under",
    "over", "after", "before", "be", "is", "are", "was", "were", "been",
    "being", "have", "has", "had", "having", "do", "does", "did", "will",
    "shall", "may", "can", "cannot", "must", "let", "if", "then", "than",
    "that", "which", "who", "whom", "whose", "this", "these", "those",
    "it", "its", "they", "them", "their", "one", "another", "other",
    "each", "either", "neither", "both", "any", "all", "some", "no", "not",
    "nor", "or", "and", "but", "so", "as", "such", "same", "given",
    "two", "three", "four", "first", "second", "third", "fourth",
    "things", "thing", "also", "respectively", "whenever", "when", "where",
}


def get_semantic_name(
    canonical_ref: str,
    node_type: str = "prop",
    subtype: Optional[str] = None,
    enun_text: str = "",
) -> str:
    """Return a concise snake_case function or rule name for any G-node."""
    if canonical_ref in SEMANTIC_NAMES:
        return SEMANTIC_NAMES[canonical_ref]

    cleaned = re.sub(r":[A-Za-z0-9_.-]+:`([^`]+)`", r"\1", enun_text)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    words = [
        w.lower()
        for w in re.findall(r"[A-Za-z]{3,}", cleaned)
        if w.lower() not in _STOP_WORDS
    ]
    if words:
        selected = words[:3]
        base = "_".join(selected)
        if node_type == "def" and not base.endswith("_def"):
            base = f"{base}_def"
        return base

    return re.sub(r"[^a-z0-9]+", "_", canonical_ref.lower()).strip("_")


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
    """Split a paragraph on ';' and sentence/construction boundaries outside RST roles."""
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
    protected = re.sub(
        r";\s+and\s+it\s+has\s+been\b",
        ", and it has been",
        protected,
        flags=re.IGNORECASE,
    )
    # Attach trailing :just:`...` after a semicolon or period to the preceding clause
    protected = re.sub(
        r"([;.])\s*(__ROLE_\d+__)",
        lambda m: f" {m.group(2)}{m.group(1)}"
        if placeholders.get(m.group(2), "").startswith(":just:")
        else m.group(0),
        protected,
    )
    # Split sentence boundaries before transition/proof keywords
    protected = re.sub(
        r"\.\s+(?=(?:Now|Then|And|But|For|Therefore|Since|Again|If|Let|I\s+say|Thus|Through|From|At|On|With)\b)",
        "; ",
        protected,
    )
    # Split compound construction clauses where the first clause already has a construction verb ("be joined, and on DE let...")
    protected = re.sub(
        r"(\bbe\s+(?:joined|drawn(?:\s+through)?|described|constructed|produced|made|cut(?:\s+off)?|taken(?:\s+at\s+random)?|placed|applied|bisected)\b[^,;]*),\s+(?:and\s+)?((?:on|from|with|at|through|in)\s+[^;]+?\blet\b|\blet\b)",
        r"\1; \2",
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
    """Extract any `:just:`[G.x] <G.x>`` roles from a clause and return (cleaned_clause, combined_targets_str)."""
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
        return cleaned, ", ".join(targets)
    return cleaned, None


def _parse_just_targets(just_str: Optional[str]) -> List[str]:
    """Extract list of G.<n> target IDs from a justification string like `[G.4] <G.4>` or `G.4`."""
    if not just_str:
        return []
    m = re.search(r"<([^>]+)>", just_str)
    raw = m.group(1) if m else just_str.strip("[] ")
    return [p.strip() for p in raw.split(",") if p.strip()]


def _fn_tag(fn_name: str, g_target: Optional[str]) -> str:
    """Format a `:fn:` role linking `fn_name` to `g_target` (or plain `**fn_name**` if no target) followed by `\\ ` for `(`."""
    if g_target:
        return f":fn:`{fn_name} <{g_target}>`\\ "
    return f"**{fn_name}**\\ "


def _endpoints_of_seg_role(seg_role: str) -> Optional[Tuple[str, str]]:
    """Given a segment role like `:g:`/ C A / <g1:/ C A />``, return point roles `(:g:`C <g1:C>`, :g:`A <g1:A>`)`."""
    m = re.match(r"^:g:`/\s*([A-Za-z0-9_]+)\s+([A-Za-z0-9_]+)\s*/\s*<(?:([^:>]+):)?[^>]+>`$", seg_role.strip())
    if not m:
        return None
    p1, p2, gid = m.group(1), m.group(2), m.group(3) or "g1"
    return (f":g:`{p1} <{gid}:{p1}>`", f":g:`{p2} <{gid}:{p2}>`")


def _rewrite_clause_to_pseudocode(
    clause: str,
    is_first_step: bool = False,
    id_map: Optional[Dict[str, str]] = None,
    last_constructed_seg: Optional[str] = None,
    constructed_circles: Optional[List[str]] = None,
) -> Optional[Tuple[str, str, Optional[str]]]:
    """Rewrite a single Heath clause into (step_kind, concise_pseudocode_text, used_fn_target) or None."""
    s = " ".join(line.strip() for line in clause.strip().splitlines() if line.strip())
    if not s:
        return None

    id_map = id_map or {}
    g_segment = id_map.get("I.post.1", "G.3")
    g_extend = id_map.get("I.post.2", "G.7")
    g_circle = id_map.get("I.post.3", "G.4")
    g_equi = id_map.get("I.1", "G.5")
    g_transfer = id_map.get("I.2", "G.8")
    g_cut = id_map.get("I.3", "G.9")
    g_bisect_ang = id_map.get("I.9", "G.16")
    g_bisect_seg = id_map.get("I.10", "G.17")
    g_perp_at = id_map.get("I.11", "G.19")
    g_perp_from = id_map.get("I.12", "G.20")
    g_tri_segs = id_map.get("I.22", "G.33")
    g_copy_ang = id_map.get("I.23", "G.34")
    g_parallel = id_map.get("I.31", "G.44")
    g_pgram_tri = id_map.get("I.42", "G.55")
    g_apply_pgram = id_map.get("I.44", "G.57")
    g_square = id_map.get("I.46", "G.59")

    # Strip bracketed editorial interpolations like `[I say that they are also in the same parallels.]`
    s = re.sub(r"^\[I say that[^\]]*\]\s*(?:And\s*\[For\]\s*|And\s+|For\s+)?", "", s, flags=re.IGNORECASE).strip()

    # 0. Check for Diorismos ("Thus it is required..." or "I say that...") -> return ("goal", goal_text, None)
    m_req = re.match(r"^Thus it is required\s+to\s+(.+?)\.?$", s, re.IGNORECASE)
    if m_req:
        return ("goal", _strip_redundant_type_nouns(m_req.group(1).strip()), None)

    # If "Thus it is required..." is appended to the first sentence, strip it
    s = re.sub(r"\s*Thus it is required\b.*$", "", s, flags=re.IGNORECASE).strip()
    if not s:
        return None

    m_isay = re.match(r"^(?:Therefore\s+etc\.|I\s+say\s+that\s+(.+?)\.?)$", s, re.IGNORECASE)
    if m_isay:
        if m_isay.group(1):
            return ("goal", _strip_redundant_type_nouns(m_isay.group(1).strip()), None)
        return None

    if re.match(r"^(?:\(Being\)\s+what\s+it\s+was\s+required\b|Q\.\s*E\.\s*[DF]\.?$)", s, re.IGNORECASE):
        return None

    # 1. Check for "Given" step
    if re.match(r"^Let\b.*\bbe (?:the )?(?:two |three )?given\b", s, re.IGNORECASE) or (
        is_first_step
        and re.match(r"^Let\b", s, re.IGNORECASE)
        and not re.search(
            r"\bbe\s+(?:described|joined|drawn|constructed|cut|taken|produced|bisected|placed|made|applied)\b",
            s,
            re.IGNORECASE,
        )
    ):
        body = s
        body = re.sub(r"^Let\s+", "", body, flags=re.IGNORECASE)
        body = _strip_redundant_type_nouns(body)
        body = re.sub(
            r"\s+be\s+(?:the\s+)?(?:two\s+|three\s+)?given\s+(?:unequal\s+|infinite\s+|finite\s+)?(?:straight\s+lines?|segments?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)(?:\s+which\s+is\s+not\s+on\s+it)?\.?$",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(
            r"\bbe\s+(?:the\s+)?(?:two\s+|three\s+)?given\s+(?:unequal\s+|infinite\s+|finite\s+)?(?:straight\s+lines?|segments?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)\b",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(
            r"\b(?:the\s+)?given\s+(?:unequal\s+|infinite\s+|finite\s+)?(?:straight\s+lines?|segments?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)\b",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(r"\s*,\s*and\s+", ", ", body, flags=re.IGNORECASE)
        body = re.sub(r"\s{2,}", " ", body).strip(" ,.")
        return ("given", body, None)

    # Normalize leading conjunctions and strip redundant type nouns for construction matching
    s_norm = _strip_redundant_type_nouns(s)
    s_norm = re.sub(
        r"^(?:For\s+|And\s+again,\s*|Again,\s*|And\s+|Then\s+|Now\s+|But,\s*if\s+not,\s*|If\s+not,\s*)",
        "",
        s_norm,
        flags=re.IGNORECASE,
    ).strip()

    # 2. Circle construction: "with centre A and distance AB let the circle BCD be described"
    m_circle = re.match(
        r"^with\s+(?:centre|center)\s+(:g:`[^`]+`)\s+and\s+(?:distance|radius)\s+(:g:`[^`]+`)\s+let\s+(?:the\s+)?(?:circle\s+)?(:g:`[^`]+`)\s+be\s+described\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_circle:
        center, radius, circle = m_circle.group(1), m_circle.group(2), m_circle.group(3)
        if constructed_circles is not None:
            constructed_circles.append(circle)
        return (
            "construct",
            f"{_fn_tag('circle', g_circle)}({center}, {radius}) → {circle}",
            g_circle,
        )

    # 3. Intersection + Join: "from the point C, in which the circles cut one another, to the points A, B let the straight lines CA, CB be joined"
    m_int_join = re.match(
        r"^from\s+(?:the\s+point\s+)?(:g:`[^`]+`),\s*in\s+which\s+the\s+circles\s+cut\s+one\s+another,\s*to\s+(?:the\s+points\s+)?(.+?)\s+let\s+(?:the\s+straight\s+lines\s+)?(.+?)\s+be\s+joined\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_int_join:
        pt_c, pts_to, segs_str = m_int_join.group(1), m_int_join.group(2), m_int_join.group(3)
        if constructed_circles and len(constructed_circles) >= 2:
            c1, c2 = constructed_circles[-2], constructed_circles[-1]
            int_expr = f"{c1} ∩ {c2} → {pt_c}"
        else:
            int_expr = f"circles ∩ → {pt_c}"

        seg_roles = re.findall(r":g:`[^`]+`", segs_str)
        pt_roles = re.findall(r":g:`[^`]+`", pts_to)
        if len(seg_roles) == len(pt_roles) and len(seg_roles) > 1:
            calls = [
                f"{_fn_tag('segment', g_segment)}({pt_c}, {pt_r}) → {seg_r}"
                for pt_r, seg_r in zip(pt_roles, seg_roles)
            ]
            join_expr = ", ".join(calls)
        else:
            join_expr = f"{_fn_tag('segment', g_segment)}({pt_c}, {pts_to}) → {segs_str}"
        return ("intersect_and_join", f"{int_expr}|||{join_expr}", g_segment)

    # 4. Simple Segment Join: "from A to B let AB be joined" or "let AB be joined"
    m_from_join = re.match(
        r"^from\s+(?:the\s+point\s+)?(:g:`[^`]+`)\s+to\s+(?:the\s+point\s+)?(:g:`[^`]+`)\s+let\s+(?:the\s+straight\s+line\s+)?(:g:`[^`]+`)\s+be\s+joined\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_from_join:
        p1, p2, seg = m_from_join.group(1), m_from_join.group(2), m_from_join.group(3)
        return (
            "construct",
            f"{_fn_tag('segment', g_segment)}({p1}, {p2}) → {seg}",
            g_segment,
        )

    m_let_join = re.match(
        r"^let\s+(?:the\s+straight\s+lines?\s+)?(.+?)\s+be\s+joined\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_let_join:
        segs_raw = _strip_redundant_type_nouns(m_let_join.group(1))
        seg_roles = re.findall(r":g:`[^`]+`", segs_raw)
        if seg_roles:
            calls: List[str] = []
            for sr in seg_roles:
                eps = _endpoints_of_seg_role(sr)
                if eps:
                    calls.append(f"{_fn_tag('segment', g_segment)}({eps[0]}, {eps[1]}) → {sr}")
                else:
                    calls.append(f"{_fn_tag('segment', g_segment)}() → {sr}")
            return ("construct", ", ".join(calls), g_segment)
        return ("construct", f"{_fn_tag('segment', g_segment)}() → {segs_raw}", g_segment)

    # 5. Join and produce: "let BE be joined and produced in a straight line to F"
    m_join_prod = re.match(
        r"^let\s+(?:the\s+straight\s+line\s+)?(:g:`[^`]+`)\s+be\s+joined\s+and\s+produced\s+(?:in\s+a\s+straight\s+line\s+)?to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_join_prod:
        seg, pt_to = m_join_prod.group(1), m_join_prod.group(2)
        eps = _endpoints_of_seg_role(seg)
        seg_call = (
            f"{_fn_tag('segment', g_segment)}({eps[0]}, {eps[1]}) → {seg}"
            if eps
            else f"{_fn_tag('segment', g_segment)}() → {seg}"
        )
        ext_call = f"{_fn_tag('extend', g_extend)}({seg}) → {pt_to}"
        return ("construct", f"{seg_call}, {ext_call}", g_extend)

    # 6. Equilateral Triangle construction:
    # "on it / on AB let the equilateral triangle DAB be constructed" OR "let the equilateral triangle ABC be constructed on it"
    m_equi1 = re.match(
        r"^on\s+(.+?)\s+let\s+the\s+(.+?)\s+triangle\s+(:g:`[^`]+`)\s+be\s+constructed\.?$",
        s_norm,
        re.IGNORECASE,
    )
    m_equi2 = re.match(
        r"^let\s+the\s+(.+?)\s+triangle\s+(:g:`[^`]+`)\s+be\s+constructed\s+on\s+(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_equi1 or m_equi2:
        if m_equi1:
            base_raw, eq_role, tri = m_equi1.group(1), m_equi1.group(2), m_equi1.group(3)
        else:
            eq_role, tri, base_raw = m_equi2.group(1), m_equi2.group(2), m_equi2.group(3)
        base = _strip_redundant_type_nouns(base_raw).strip()
        if base.lower() == "it" and last_constructed_seg:
            base = last_constructed_seg
        return (
            "construct",
            f"{_fn_tag('equilateral_triangle', g_equi)}({base}) → {tri} ({eq_role})",
            g_equi,
        )

    # 7. Line Extension (produced):
    # "let AE, BF be produced (further) in a straight line with DA, DB"
    m_prod = re.match(
        r"^let\s+(?:the\s+straight\s+lines?\s+)?(.+?)\s+be\s+produced\s+(?:further\s+)?in\s+a\s+straight\s+line\s+with\s+(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_prod:
        ext, orig = _strip_redundant_type_nouns(m_prod.group(1)), _strip_redundant_type_nouns(m_prod.group(2))
        return ("construct", f"{_fn_tag('extend', g_extend)}({orig}) → {ext}", g_extend)

    # "let (one side of it) BC be produced / drawn through (in both directions) to D"
    m_prod_to = re.match(
        r"^let\s+(?:one\s+side\s+of\s+it\s+)?(?:the\s+straight\s+lines?\s+)?(.+?)\s+be\s+(?:produced|drawn\s+through)(?:\s+in\s+both\s+directions)?\s+to\s+(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_prod_to:
        orig, ext = _strip_redundant_type_nouns(m_prod_to.group(1)), _strip_redundant_type_nouns(m_prod_to.group(2))
        return ("construct", f"{_fn_tag('extend', g_extend)}({orig}) → {ext}", g_extend)

    # 8. Transfer segment: "at A let AD be placed equal to C"
    m_transfer = re.match(
        r"^at\s+(?:the\s+point\s+)?(:g:`[^`]+`)\s+let\s+(?:the\s+straight\s+line\s+)?(:g:`[^`]+`)\s+be\s+placed\s+(.+?)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_transfer:
        pt, seg, eq_part, src = (
            m_transfer.group(1),
            m_transfer.group(2),
            m_transfer.group(3),
            m_transfer.group(4),
        )
        return (
            "construct",
            f"{_fn_tag('transfer_segment', g_transfer)}({pt}, {src}) → {seg} ({eq_part})",
            g_transfer,
        )

    # 9. Cut off / make equal segment (G.9):
    # "from AE the greater let AG be cut off equal to AF the less" OR "let AE be cut off from AC equal to AD"
    m_cut1 = re.match(
        r"^from\s+(:g:`[^`]+`)(?:\s+the\s+greater)?\s+let\s+(:g:`[^`]+`)\s+be\s+cut\s+off\s+(.+?)\s+to\s+(:g:`[^`]+`)(?:\s+the\s+less)?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_cut1:
        greater, seg, eq_part, less = m_cut1.group(1), m_cut1.group(2), m_cut1.group(3), m_cut1.group(4)
        return (
            "construct",
            f"{_fn_tag('cut_equal_segment', g_cut)}({greater}, {less}) → {seg} ({eq_part})",
            g_cut,
        )

    m_cut2 = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+cut\s+off\s+from\s+(:g:`[^`]+`)\s+(.+?)\s+to\s+(:g:`[^`]+`)(?:\s+the\s+less)?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_cut2:
        seg, greater, eq_part, less = m_cut2.group(1), m_cut2.group(2), m_cut2.group(3), m_cut2.group(4)
        return (
            "construct",
            f"{_fn_tag('cut_equal_segment', g_cut)}({greater}, {less}) → {seg} ({eq_part})",
            g_cut,
        )

    m_made_eq = re.match(
        r"^(?:since\s+[^,]+,\s*)?let\s+(:g:`[^`]+`)\s+be\s+made\s+(:eq:`[^`]+`|equal)\s+to\s+(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_made_eq:
        seg, eq_part, target = m_made_eq.group(1), m_made_eq.group(2), _strip_redundant_type_nouns(m_made_eq.group(3))
        return (
            "construct",
            f"{_fn_tag('cut_equal_segment', g_cut)}({target}) → {seg} ({eq_part})",
            g_cut,
        )

    # 10. Bisect angle (G.16): "let < ACB ) be bisected by / CD /"
    m_bis_ang = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+(:eq:`bisected[^`]*`|bisected)\s+by\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_bis_ang:
        ang, eq_part, seg = m_bis_ang.group(1), m_bis_ang.group(2), m_bis_ang.group(3)
        return (
            "construct",
            f"{_fn_tag('bisect_angle', g_bisect_ang)}({ang}) → {seg} ({eq_part})",
            g_bisect_ang,
        )

    # 11. Bisect segment (G.17): "let / EG / be bisected at H"
    m_bis_seg = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+(:eq:`bisected[^`]*`|bisected)\s+at\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_bis_seg:
        seg, eq_part, pt = m_bis_seg.group(1), m_bis_seg.group(2), m_bis_seg.group(3)
        return (
            "construct",
            f"{_fn_tag('bisect_segment', g_bisect_seg)}({seg}) → {pt} ({eq_part})",
            g_bisect_seg,
        )

    # 12. Perpendicular at point on line (G.19): "let / AC / be drawn (from A) at right angles to / AB / (from A on it)"
    m_perp_at = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+drawn\s+(?:from\s+(:g:`[^`]+`)\s+)?at\s+(:eq:`right\s+angles[^`]*`|right\s+angles)\s+to\s+(:g:`[^`]+`)(?:\s+from\s+(:g:`[^`]+`)(?:\s+on\s+it)?)?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_perp_at:
        perp = m_perp_at.group(1)
        pt = m_perp_at.group(2) or m_perp_at.group(5) or ""
        line = m_perp_at.group(4)
        args = f"{line}, {pt}" if pt else line
        return (
            "construct",
            f"{_fn_tag('perpendicular_at', g_perp_at)}({args}) → {perp}",
            g_perp_at,
        )

    # 13. Perpendicular from point to line (G.20):
    m_perp_from = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+drawn\s+(:eq:`perpendicular[^`]*`|perpendicular)\s+to\s+(:g:`[^`]+`)\s+from\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_perp_from:
        perp, line, pt = m_perp_from.group(1), m_perp_from.group(3), m_perp_from.group(4)
        return (
            "construct",
            f"{_fn_tag('perpendicular_from', g_perp_from)}({line}, {pt}) → {perp}",
            g_perp_from,
        )

    # 14. Copy angle (G.34):
    # "at A on it, let < DAE ) be constructed equal to < ADC )" or "let there be constructed, on / DE /, and at D on it, < EDG ) equal to < BAC )"
    m_copy_ang1 = re.match(
        r"^(?:since\s+[^,]+,\s*)?(?:on\s+(:g:`[^`]+`),\s*and\s+)?at\s+(:g:`[^`]+`)(?:\s+on\s+(?:it|:g:`[^`]+`))?,?\s*let\s+(:g:`[^`]+`)\s+be\s+constructed\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    m_copy_ang2 = re.match(
        r"^(?:since\s+[^,]+,\s*)?let\s+there\s+be\s+constructed,\s*on\s+(:g:`[^`]+`),\s*and\s+at\s+(:g:`[^`]+`)\s+on\s+it,\s*(:g:`[^`]+`)\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_copy_ang1 or m_copy_ang2:
        m_ca = m_copy_ang1 or m_copy_ang2
        assert m_ca is not None
        line_opt, pt, new_ang, eq_part, src_ang = (
            m_ca.group(1),
            m_ca.group(2),
            m_ca.group(3),
            m_ca.group(4),
            m_ca.group(5),
        )
        args = f"{line_opt}, {pt}, {src_ang}" if line_opt else f"{pt}, {src_ang}"
        return (
            "construct",
            f"{_fn_tag('copy_angle', g_copy_ang)}({args}) → {new_ang} ({eq_part})",
            g_copy_ang,
        )

    # 15. Parallel line through point (G.44):
    # "through B let / BE / be drawn parallel to / CA /" OR "let / CE / be drawn through C parallel to / AB /"
    m_par1 = re.match(
        r"^through\s+(:g:`[^`]+`)\s+let\s+(:g:`[^`]+`)\s+be\s+drawn\s+parallel\s+to\s+(?:either\s+)?(.+?)(?:,\s*and)?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    m_par2 = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+drawn\s+through\s+(:g:`[^`]+`)\s+parallel\s+to\s+(?:either\s+)?(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_par1 or m_par2:
        if m_par1:
            pt, new_line, target_line = m_par1.group(1), m_par1.group(2), _strip_redundant_type_nouns(m_par1.group(3))
        else:
            new_line, pt, target_line = m_par2.group(1), m_par2.group(2), _strip_redundant_type_nouns(m_par2.group(3))
        return (
            "construct",
            f"{_fn_tag('parallel_line', g_parallel)}({pt}, {target_line}) → {new_line}",
            g_parallel,
        )

    # 16. Square on segment (G.59):
    m_sq = re.match(
        r"^let\s+there\s+be\s+(?:described|constructed)\s+on\s+(:g:`[^`]+`)\s+the\s+square\s+(:g:`[^`]+`)(?:,\s*and\s+on\s+(:g:`[^`]+`),\s*(:g:`[^`]+`)\s+the\s+squares\s+(:g:`[^`]+`),\s*(:g:`[^`]+`))?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_sq:
        s1, sq1 = m_sq.group(1), m_sq.group(2)
        calls = [f"{_fn_tag('square_on_segment', g_square)}({s1}) → {sq1}"]
        if m_sq.group(3) and m_sq.group(5):
            calls.append(f"{_fn_tag('square_on_segment', g_square)}({m_sq.group(3)}) → {m_sq.group(5)}")
        if m_sq.group(4) and m_sq.group(6):
            calls.append(f"{_fn_tag('square_on_segment', g_square)}({m_sq.group(4)}) → {m_sq.group(6)}")
        return ("construct", ", ".join(calls), g_square)

    # 17. Parallelogram from triangle (G.55) and Apply parallelogram (G.57):
    m_pg55 = re.match(
        r"^let\s+the\s+parallelogram\s+(:g:`[^`]+`)\s+be\s+constructed\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`),\s*in\s+(:g:`[^`]+`)\s+which\s+is\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_pg55:
        pg, eq1, tri, ang, eq2, given_ang = m_pg55.groups()
        return (
            "construct",
            f"{_fn_tag('parallelogram_from_triangle', g_pgram_tri)}({tri}, {given_ang}) → {pg} ({eq1}, {ang} {eq2})",
            g_pgram_tri,
        )

    m_pg57 = re.match(
        r"^let\s+the\s+parallelogram\s+(:g:`[^`]+`)\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\s+be\s+applied\s+to\s+(:g:`[^`]+`),\s*in\s+(:g:`[^`]+`)\s+which\s+is\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_pg57:
        pg, eq1, tri, seg, ang, eq2, given_ang = m_pg57.groups()
        return (
            "construct",
            f"{_fn_tag('apply_parallelogram_on_segment', g_apply_pgram)}({seg}, {tri}, {given_ang}) → {pg} ({eq1}, {ang} {eq2})",
            g_apply_pgram,
        )

    # 18. Point taken at random: "let a point D be taken at random on AB" or "on CD, CE respectively let D, E be taken at random"
    m_pt1 = re.match(
        r"^let\s+(?:a\s+point\s+)?(:g:`[^`]+`)\s+be\s+taken\s+(?:at\s+random\s+)?on\s+(?:the\s+other\s+side\s+of\s+)?(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_pt1:
        pt, target = m_pt1.group(1), _strip_redundant_type_nouns(m_pt1.group(2))
        return ("construct", f"**point**\\ ({target}) → {pt}", None)

    m_pt2 = re.match(
        r"^on\s+(.+?)\s+(?:respectively\s+)?let\s+(.+?)\s+be\s+taken\s+at\s+random\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_pt2:
        target, pts = _strip_redundant_type_nouns(m_pt2.group(1)), _strip_redundant_type_nouns(m_pt2.group(2))
        return ("construct", f"**point**\\ ({target}) → {pts}", None)

    # 19. General construction vs assertion classification
    cleaned = _strip_redundant_type_nouns(s)
    cleaned = re.sub(r"^(?:Now,\s*|Again,\s*|Then,\s*|And\s+|But\s+|For,\s*|For\s+)", "", cleaned)
    if cleaned and cleaned[0].islower():
        cleaned = cleaned[0].upper() + cleaned[1:]

    if re.search(
        r"\blet\b.+\bbe\s+(?:described|constructed|drawn|joined|produced|bisected|cut|placed|applied|made|taken|set\s+up|inscribed|circumscribed|added|subtracted|measured|found)\b",
        s,
        re.IGNORECASE,
    ):
        return ("construct", cleaned, None)
    if re.search(r"\bcut\s+one\s+another\s+at\b|\bmeet\s+(?:one\s+another\s+)?at\b", s, re.IGNORECASE):
        return ("intersect", cleaned, None)
    inferred_rule = None
    if re.search(r"\bis\s+the\s+(?:centre|center)\s+of\b", cleaned, re.IGNORECASE):
        inferred_rule = id_map.get("I.def.15", "G.2")
    return ("assert", cleaned, inferred_rule)


def _strip_redundant_type_nouns(text: str) -> str:
    """Strip verbose Euclidean type prefixes immediately preceding symbolic :g: indications."""
    s = text
    patterns = [
        (r"\bthe\s+given\s+finite\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+given\s+infinite\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
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


def _format_rule_justification(
    just_targets: List[str],
    g_to_sem_name: Dict[str, str],
) -> Optional[str]:
    """Format a list of G.<n> targets into a `∵ rule_name <G.n>` justification argument."""
    if not just_targets:
        return None
    rule_names = [g_to_sem_name.get(t, t) for t in just_targets]
    rules_str = ", ".join(rule_names)
    targets_str = ", ".join(just_targets)
    return f"∵ {rules_str} <{targets_str}>"


def _build_signature_block(
    canonical_ref: str,
    node_type: str,
    subtype: Optional[str],
    g_name: str,
    sem_name: str,
    given_steps: List[str],
    goal_clauses: List[str],
    conclude_body: Optional[str],
    construct_steps: List[str],
) -> str:
    """Build a `.. signature::` RST block for a G-node."""
    fn_self = f":fn:`{sem_name} <{g_name}>`" if g_name else f"**{sem_name}**"

    # Special foundational construction postulates
    if canonical_ref == "I.post.1":
        return (
            f".. signature:: postulate\n\n"
            f"   | {fn_self}\\ (A, B) → / A B /\n"
            f"   | **given** A, B\n"
            f"   | **construct** / A B /"
        )
    if canonical_ref == "I.post.2":
        return (
            f".. signature:: postulate\n\n"
            f"   | {fn_self}\\ (/ A B /) → / B C /\n"
            f"   | **given** / A B /\n"
            f"   | **construct** / B C /"
        )
    if canonical_ref == "I.post.3":
        return (
            f".. signature:: postulate\n\n"
            f"   | {fn_self}\\ (A, / A B /) → ( B C D )\n"
            f"   | **given** A, / A B /\n"
            f"   | **construct** ( B C D )"
        )

    if node_type in ("def", "post", "cn"):
        sig_kind = "rule" if node_type in ("cn", "post") else "def"
        return f".. signature:: {sig_kind}\n\n   | {fn_self}"

    sig_kind = subtype if subtype in ("problem", "theorem") else "prop"
    given_text = "; ".join(given_steps).strip()

    # Extract distinct :g: roles from given_text
    given_roles: List[str] = []
    given_targets: set[str] = set()
    for m in re.finditer(r":g:`([^`]+?)\s+<([^`]+)>`", given_text):
        t = m.group(2).strip()
        if t not in given_targets:
            given_targets.add(t)
            given_roles.append(m.group(0))

    cleaned_conclude = ""
    if conclude_body:
        cleaned_conclude = re.sub(
            r"^(?:Therefore,?\s*(?:given\s+.+?,\s*(?=from\b|at\b|on\b|in\b|to\b))?|Thus\s+|Hence\s+|So\s+that\s+)",
            "",
            conclude_body.strip(),
            flags=re.IGNORECASE,
        ).strip()
        cleaned_conclude = re.sub(
            r",?\s*and\s+it\s+has\s+been\s+constructed.*$",
            "",
            cleaned_conclude,
            flags=re.IGNORECASE,
        ).rstrip(".")

    # Determine return symbol(s) and goal text for problems vs theorems
    ret_roles: List[str] = []
    if sig_kind == "problem":
        # Prefer conclude_body (or goal_clauses with :eq:) for extracting constructed return symbols
        sources = [cleaned_conclude, "; ".join(goal_clauses)]
        seen_ret: set[str] = set()
        for src in sources:
            if not src:
                continue
            for m in re.finditer(r":g:`([^`]+?)\s+<([^`]+)>`", src):
                t = m.group(2).strip()
                if t not in given_targets and t not in seen_ret:
                    seen_ret.add(t)
                    ret_roles.append(m.group(0))
            if ret_roles:
                break
        if not ret_roles and construct_steps:
            m_arrow = re.search(r"→\s*(:g:`[^`]+`)", construct_steps[-1])
            if m_arrow:
                ret_roles.append(m_arrow.group(1))

        # Prefer a goal_clause that already has :eq: or constructed symbols, else cleaned_conclude
        eq_goals = [g for g in goal_clauses if ":eq:`" in g]
        if eq_goals:
            goal_text = "; ".join(eq_goals).strip()
        elif cleaned_conclude:
            goal_text = cleaned_conclude
        else:
            goal_text = "; ".join(goal_clauses).strip()
    else:
        goal_text = "; ".join(goal_clauses).strip() or cleaned_conclude

    args_str = ", ".join(given_roles[:4]) if given_roles else ""
    if sig_kind == "problem" and ret_roles:
        header_line = f"{fn_self}\\ ({args_str}) → {', '.join(ret_roles[:2])}"
    else:
        header_line = f"{fn_self}\\ ({args_str})"

    lines = [f".. signature:: {sig_kind}", "", f"   | {header_line}"]
    if given_text:
        lines.append(f"   | **given** {given_text}")
    if goal_text:
        contract_kw = "construct" if sig_kind == "problem" else "prove"
        lines.append(f"   | **{contract_kw}** {goal_text}")
    return "\n".join(lines)


def generate_pseudocode_rst(
    heath_content_rst: str,
    canonical_ref: str,
    node_type: str,
    g_name: str = "",
    subtype: Optional[str] = None,
    id_map: Optional[Dict[str, str]] = None,
    g_to_sem_name: Optional[Dict[str, str]] = None,
) -> str:
    """Transform a Heath RST body (with G-Index roles/justifications) into Track 1 Pseudocode RST."""
    id_map = id_map or {}
    g_to_sem_name = g_to_sem_name or {}

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
            sem_name = g_to_sem_name.get(g_name) or get_semantic_name(
                canonical_ref, node_type, subtype, tight_enun
            )
            sig_block = _build_signature_block(
                canonical_ref, node_type, subtype, g_name, sem_name, [], [], None, []
            )
            indented = "\n".join(f"   {line}" for line in tight_enun.splitlines())
            out = f".. enunciation::\n\n{indented}\n\n{sig_block}"
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

    enun_block: Optional[str] = None
    raw_enun_parts: List[str] = []
    picture_blocks: List[str] = []
    step_items: List[Tuple[str, List[str], str]] = []  # (kind, just_targets, body)
    footer_blocks: List[str] = []
    given_clauses: List[str] = []
    goal_clauses: List[str] = []
    pending_premise: Optional[str] = None
    pending_just_targets: List[str] = []
    last_constructed_seg: Optional[str] = None
    constructed_circles: List[str] = []
    tight_enun_text = ""

    def _update_last_seg(body_text: str) -> None:
        nonlocal last_constructed_seg
        for m_seg in re.finditer(r":g:`/\s*[A-Za-z0-9_]+\s+[A-Za-z0-9_]+\s*/\s*<[^>]+>`", body_text):
            last_constructed_seg = m_seg.group(0)

    for b in blocks:
        b_strip = b.strip()
        if b_strip.startswith(".. enunciation::"):
            if not step_items and not picture_blocks and not given_clauses and not goal_clauses:
                b_lines = b_strip.splitlines()
                raw_enun = "\n".join(l.strip() for l in b_lines[1:] if l.strip())
                raw_enun_parts.append(raw_enun)
                merged_raw_enun = re.sub(r"(\w)-\s+(\w)", r"\1\2", " ".join(raw_enun_parts))
                tight_enun_text = tighten_enunciation_text(merged_raw_enun, canonical_ref)
                enun_block = f".. enunciation::\n\n   {tight_enun_text}"
            else:
                footer_blocks.append(b_strip)
            continue

        if b_strip.startswith(".. picture::"):
            picture_blocks.append(b_strip)
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
            dir_just_raw = (m_dir.group(2) or "").strip() or None
            dir_body = " ".join(l.strip() for l in m_dir.group(3).splitlines() if l.strip())
            dir_body, inline_just_raw = _extract_inline_justifications(dir_body)
            j_targets = (
                _parse_just_targets(dir_just_raw)
                or _parse_just_targets(inline_just_raw)
                or list(pending_just_targets)
            )
            pending_just_targets = []

            # Check if this .. assertion:: block in Heath is actually a construction step (like in G.17 / G.20)
            if not pending_premise:
                rewritten_dir = _rewrite_clause_to_pseudocode(
                    dir_body,
                    is_first_step=(len(step_items) == 0),
                    id_map=id_map,
                    last_constructed_seg=last_constructed_seg,
                    constructed_circles=constructed_circles,
                )
                if rewritten_dir and rewritten_dir[0] in ("construct", "intersect", "intersect_and_join"):
                    r_kind, r_text, used_fn = rewritten_dir
                    _update_last_seg(r_text)
                    if r_kind == "intersect_and_join":
                        int_text, join_text = r_text.split("|||", 1)
                        step_items.append(("intersect", [], int_text))
                        step_items.append(("construct", [], join_text))
                    else:
                        if not used_fn and j_targets and r_kind == "construct":
                            fn_t = j_targets[0]
                            fn_n = g_to_sem_name.get(fn_t, fn_t)
                            r_text = f"{_fn_tag(fn_n, fn_t).rstrip('\\ ')}: {r_text}"
                        step_items.append((r_kind, [], r_text))
                    continue

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
            if not j_targets and re.search(r"\bis\s+the\s+(?:centre|center)\s+of\b", cleaned, re.IGNORECASE):
                j_targets = [id_map.get("I.def.15", "G.2")]
            step_items.append(("assert", j_targets, cleaned))
            continue

        clauses = _split_clauses_preserving_roles(b_strip)
        for c in clauses:
            c_clean, c_just_raw = _extract_inline_justifications(c)
            c_targets = _parse_just_targets(c_just_raw)
            if c_clean.endswith(",") and re.match(
                r"^(?:Now,\s*|Again,\s*|Then,\s*|For,\s*|Since\b|And\s+since\b)",
                c_clean,
                re.IGNORECASE,
            ):
                pending_premise = _strip_redundant_type_nouns(c_clean)
                if c_targets:
                    pending_just_targets = c_targets
                continue

            if re.match(r"^And\s+things\s+which\s+are\s+equal\b", c_clean, re.IGNORECASE) and c_targets:
                pending_just_targets = c_targets
                continue

            rewritten = _rewrite_clause_to_pseudocode(
                c_clean,
                is_first_step=(len(step_items) == 0),
                id_map=id_map,
                last_constructed_seg=last_constructed_seg,
                constructed_circles=constructed_circles,
            )
            if not rewritten:
                continue

            kind, text, used_fn = rewritten
            if kind == "goal":
                goal_clauses.append(text)
                continue

            j_targets = c_targets or list(pending_just_targets)
            pending_just_targets = []
            if pending_premise:
                text = f"{pending_premise.rstrip(',; ')} → {text}"
                pending_premise = None

            _update_last_seg(text)

            if kind == "given":
                given_clauses.append(text)
                step_items.append(("given", [], text))
            elif kind == "intersect_and_join":
                int_text, join_text = text.split("|||", 1)
                step_items.append(("intersect", [], int_text))
                step_items.append(("construct", [], join_text))
            elif kind == "construct":
                # If a general construct step has a justification target not yet embedded as :fn:, embed it!
                if not used_fn and j_targets and ":fn:`" not in text:
                    fn_t = j_targets[0]
                    fn_n = g_to_sem_name.get(fn_t, fn_t)
                    text = f"{_fn_tag(fn_n, fn_t).rstrip('\\ ')}: {text}"
                step_items.append(("construct", [], text))
            else:
                if not j_targets and used_fn:
                    j_targets = [used_fn]
                elif not j_targets and re.search(r"\bis\s+the\s+(?:centre|center)\s+of\b", text, re.IGNORECASE):
                    j_targets = [id_map.get("I.def.15", "G.2")]
                step_items.append((kind, j_targets, text))

    # Promote final step to `conclude`, or append a `conclude` step from goal_clauses if missing
    conclude_body: Optional[str] = None
    if step_items:
        last_kind, last_targets, last_body = step_items[-1]
        if last_kind == "assert":
            step_items[-1] = ("conclude", last_targets, last_body)
            conclude_body = last_body
        elif last_kind == "conclude":
            conclude_body = last_body
    if not conclude_body and goal_clauses:
        conclude_body = "; ".join(goal_clauses)
        step_items.append(("conclude", [], conclude_body))

    sem_name = g_to_sem_name.get(g_name) or get_semantic_name(
        canonical_ref, node_type, subtype, tight_enun_text
    )
    construct_bodies = [b for k, _, b in step_items if k == "construct"]
    sig_block = _build_signature_block(
        canonical_ref,
        node_type,
        subtype,
        g_name,
        sem_name,
        given_clauses,
        goal_clauses,
        conclude_body,
        construct_bodies,
    )

    header_blocks: List[str] = []
    if enun_block:
        header_blocks.append(enun_block)
    header_blocks.append(sig_block)
    header_blocks.extend(picture_blocks)

    rendered_steps: List[str] = []
    for kind, j_targets, body in step_items:
        just_str = _format_rule_justification(j_targets, g_to_sem_name) if j_targets else None
        arg_str = f"{kind} {just_str}" if just_str else kind
        clean_body = " ".join(l.strip() for l in body.splitlines() if l.strip())
        rendered_steps.append(f".. step:: {arg_str}\n\n   {clean_body}")

    all_parts = header_blocks + rendered_steps + footer_blocks
    return "\n\n".join(all_parts)
