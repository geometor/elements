"""
Graph construction and semantic metadata extraction for GEOMETOR Elements.

Crawls the composed Heath Edition RST source in `../euclid/docsrc/heath/` across
all 3 volumes (Books I–XIII), extracting discrete nodes for definitions,
postulates, common notions, and propositions, along with their dependency edges,
interactive SVG diagrams, categories, and semantic tags.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import networkx as nx

ROMAN_NUMERALS = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
    "10": "X",
    "11": "XI",
    "12": "XII",
    "13": "XIII",
}

ROMAN_TO_INT = {v: int(k) for k, v in ROMAN_NUMERALS.items()}
VALID_BOOKS = set(ROMAN_NUMERALS.values())

BOOK_TO_VOLUME = {
    "I": "I",
    "II": "I",
    "III": "II",
    "IV": "II",
    "V": "II",
    "VI": "II",
    "VII": "II",
    "VIII": "II",
    "IX": "II",
    "X": "III",
    "XI": "III",
    "XII": "III",
    "XIII": "III",
}

BOOK_DOMAIN_CATEGORIES: Dict[str, List[str]] = {
    "I": ["plane-geometry"],
    "II": ["plane-geometry", "geometric-algebra"],
    "III": ["plane-geometry", "circles"],
    "IV": ["plane-geometry", "circles", "polygons"],
    "V": ["proportions", "magnitudes"],
    "VI": ["plane-geometry", "proportions", "similar-figures"],
    "VII": ["number-theory"],
    "VIII": ["number-theory", "proportions"],
    "IX": ["number-theory"],
    "X": ["incommensurables", "magnitudes"],
    "XI": ["solid-geometry"],
    "XII": ["solid-geometry", "method-of-exhaustion"],
    "XIII": ["solid-geometry", "regular-solids"],
}

SECTION_TYPE_ORDER = {
    "def": 1,
    "post": 2,
    "cn": 3,
    "prop": 4,
}

# For G-Index dependency traversal, preserve the classic Book I ordering (cn, def, post, prop)
G_DEP_TYPE_ORDER = {
    "cn": 1,
    "def": 2,
    "post": 3,
    "prop": 4,
}

_ITEM_LABEL_RE = re.compile(
    r"^\.\.\s+_((?:I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII)\.(?:def(?:\.(?:ii|iii))?|post|cn)\.\d+):\s*$",
    re.MULTILINE,
)

_FOLIO_BLOCK_RE = re.compile(
    r"(?:^\.\.\s+_folio-[^\n]+:\s*\n+)?^\.\.\s+folio::[^\n]*(?:\n|$)(?:[ \t]+:[^\n]*(?:\n|$))*\n*",
    re.MULTILINE,
)

_G_ROLE_RE = re.compile(r":g:`([^`]+)`")
_TERM_ROLE_RE = re.compile(r":term:`([^`]+)`")
_EQ_ROLE_RE = re.compile(r":eq:`([^`]+)`")
_JUST_ROLE_RE = re.compile(r":just:`([^`]+)`")
_DIR_JUST_RE = re.compile(
    r"^\.\.\s+(?:assertion|subclause|sub-clause)::[ \t]+([^\n]+)",
    re.MULTILINE,
)

CONCEPT_PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    (tag, re.compile(pat, re.IGNORECASE))
    for tag, pat in [
        ("equilateral", r"\bequilateral\b"),
        ("isosceles", r"\bisosceles\b"),
        ("scalene", r"\bscalene\b"),
        ("right-angle", r"\bright[- ]angled?\b|\bright angles?\b"),
        ("obtuse-angle", r"\bobtuse[- ]angled?\b|\bobtuse angles?\b"),
        ("acute-angle", r"\bacute[- ]angled?\b|\bacute angles?\b"),
        ("parallel", r"\bparallels?\b"),
        ("parallelogram", r"\bparallelograms?\b|\bparallelogrammic\b"),
        ("square", r"\bsquares?\b"),
        ("rectangle", r"\brectangles?\b|\brectangular\b"),
        ("gnomon", r"\bgnomons?\b"),
        ("bisect", r"\bbisect(?:ed|s|ing)?\b"),
        ("perpendicular", r"\bperpendicular(?:s|ly)?\b"),
        ("tangent", r"\btouch(?:es|ing)?\b|\btangent\b"),
        ("semicircle", r"\bsemicircles?\b"),
        ("arc", r"\bcircumferences?\b|\barcs?\b"),
        ("chord", r"\bchords?\b"),
        ("sector", r"\bsectors?\b"),
        ("inscribed", r"\binscribe[ds]?\b"),
        ("circumscribed", r"\bcircumscribe[ds]?\b"),
        ("pentagon", r"\bpentagons?\b"),
        ("hexagon", r"\bhexagons?\b"),
        ("fifteen-angled", r"\bfifteen[- ]angled\b"),
        ("extreme-and-mean-ratio", r"\bextreme and mean ratio\b"),
        ("ratio", r"\bratios?\b"),
        ("proportion", r"\bproportion(?:al|als)?\b"),
        ("duplicate-ratio", r"\bduplicate ratio\b"),
        ("triplicate-ratio", r"\btriplicate ratio\b"),
        ("mean-proportional", r"\bmean proportional\b"),
        ("similar", r"\bsimilar(?:ly)?\b"),
        ("commensurable", r"\bcommensurable\b"),
        ("incommensurable", r"\bincommensurable\b"),
        ("rational", r"\brational\b"),
        ("irrational", r"\birrational\b"),
        ("medial", r"\bmedial\b"),
        ("binomial", r"\bbinomials?\b"),
        ("apotome", r"\bapotomes?\b"),
        ("unit", r"\bunits?\b"),
        ("number", r"\bnumbers?\b"),
        ("prime", r"\bprime\b"),
        ("composite", r"\bcomposite\b"),
        ("greatest-common-measure", r"\bgreatest common measure\b"),
        ("least-common-multiple", r"\bleast number which they measure\b"),
        ("continued-proportion", r"\bcontinued proportion\b|\bcontinuously proportional\b"),
        ("plane-number", r"\bplane numbers?\b"),
        ("solid-number", r"\bsolid numbers?\b"),
        ("square-number", r"\bsquare numbers?\b"),
        ("cube-number", r"\bcube numbers?\b"),
        ("even-number", r"\beven\b"),
        ("odd-number", r"\bodd\b"),
        ("perfect-number", r"\bperfect numbers?\b"),
        ("plane", r"\bplanes?\b"),
        ("solid-angle", r"\bsolid angles?\b"),
        ("parallelepiped", r"\bparallelepipeds?\b|\bparallelepipedal\b"),
        ("prism", r"\bprisms?\b"),
        ("pyramid", r"\bpyramids?\b"),
        ("cone", r"\bcones?\b"),
        ("cylinder", r"\bcylinders?\b"),
        ("sphere", r"\bspheres?\b"),
        ("cube", r"\bcubes?\b"),
        ("octahedron", r"\boctahedrons?\b"),
        ("icosahedron", r"\bicosahedrons?\b"),
        ("dodecahedron", r"\bdodecahedrons?\b"),
    ]
]


def normalize_canonical_id(ref_id: str) -> str:
    """Normalize cross-book shared definition IDs (e.g. VIII.def.20 -> VII.def.20)."""
    s = (ref_id or "").strip()
    m = re.match(r"^(VIII|IX)\.(def\.\d+)$", s, re.IGNORECASE)
    if m:
        return f"VII.{m.group(2).lower()}"
    m_solid = re.match(r"^(XII|XIII)\.(def\.\d+)$", s, re.IGNORECASE)
    if m_solid:
        return f"XI.{m_solid.group(2).lower()}"
    return s


def get_node_type(ref_id: str) -> str:
    """Classify a canonical Euclid ID into 'prop', 'def', 'post', or 'cn'."""
    parts = ref_id.split(".")
    if len(parts) >= 2:
        sec = parts[1].lower()
        if sec in ("def", "post", "cn"):
            return sec
        if sec.isdigit():
            return "prop"
    return "unknown"


def canonical_sort_key(
    ref_id: str, type_order_map: Optional[Dict[str, int]] = None
) -> Tuple[int, int, int, int, str]:
    """Return a deterministic sort key for canonical Euclid IDs."""
    order_map = type_order_map or SECTION_TYPE_ORDER
    parts = ref_id.split(".")
    if not parts:
        return (999, 999, 0, 0, ref_id)

    book_num = ROMAN_TO_INT.get(parts[0].upper(), 999)
    if len(parts) == 2 and parts[1].isdigit():
        return (book_num, order_map.get("prop", 4), 0, int(parts[1]), ref_id)

    sec_type = parts[1].lower() if len(parts) > 1 else ""
    type_order = order_map.get(sec_type, 99)

    group_order = 0
    item_num = 0
    if len(parts) == 3 and parts[2].isdigit():
        item_num = int(parts[2])
    elif len(parts) == 4:
        sub_map = {"i": 1, "ii": 2, "iii": 3}
        group_order = sub_map.get(parts[2].lower(), 0)
        if parts[3].isdigit():
            item_num = int(parts[3])

    return (book_num, type_order, group_order, item_num, ref_id)


def g_dependency_sort_key(ref_id: str) -> Tuple[int, int, int, int, str]:
    """Sort key for G-Index dependency traversal (cn, def, post, prop)."""
    return canonical_sort_key(ref_id, type_order_map=G_DEP_TYPE_ORDER)


def infer_justification_target(
    display: str, current_book: Optional[str] = None
) -> Optional[str]:
    """Infer canonical target ID(s) from justification text when <target> is omitted."""
    s = (display or "").strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1].strip()
    if not s or re.match(
        r"^(?:Q\.\s*\$?E\$?\.|[*]?id[*]?\.|above|from above|Part\s+\d|First part|Prop\.\s*D|Simson|Pappus|\(\d+\))",
        s,
        re.IGNORECASE,
    ):
        return None

    m_deff = re.search(
        r"\b([IVXLCDM]+)\.\s*Deff?\.\s*(III|II)(?:\.\s*(\d+))?",
        s,
        re.IGNORECASE,
    )
    if m_deff and m_deff.group(1).upper() in VALID_BOOKS:
        bk = m_deff.group(1).upper()
        sub = m_deff.group(2).lower()
        num = m_deff.group(3)
        return f"{bk}.def.{sub}.{num}" if num else f"{bk}.def.{sub}"

    bk_default = (current_book or "I").upper()
    m_post = re.match(r"^Post\.\s*(\d+)\.?$", s, re.IGNORECASE)
    if m_post:
        return f"I.post.{m_post.group(1)}"
    m_cn = re.match(r"^C\.\s*N\.\s*(\d+)\.?$", s, re.IGNORECASE)
    if m_cn:
        return f"I.cn.{m_cn.group(1)}"
    m_def_bare = re.match(r"^Def\.\s*(\d+)\.?$", s, re.IGNORECASE)
    if m_def_bare:
        return normalize_canonical_id(f"{bk_default}.def.{m_def_bare.group(1)}")

    results: List[str] = []
    pat = re.compile(
        r"\b([IVXLCDM]+)\.\s*(?:(Def\.?)\s*(\d+)|(\d+)(?:\s*(?:,|and|or)\s*(\d+))?)",
        re.IGNORECASE,
    )
    for m in pat.finditer(s):
        bk = m.group(1).upper()
        if bk not in VALID_BOOKS:
            continue
        if m.group(2):
            results.append(normalize_canonical_id(f"{bk}.def.{m.group(3)}"))
        else:
            results.append(f"{bk}.{m.group(4)}")
            if m.group(5):
                results.append(f"{bk}.{m.group(5)}")
    if results:
        return ", ".join(dict.fromkeys(results))
    return None


def parse_justification_arg(
    raw_arg: str, current_book: Optional[str] = None
) -> Tuple[str, Optional[str]]:
    """Parse a justification string into (display_text, normalized_target_ids)."""
    text = (raw_arg or "").strip()
    if not text:
        return "", None

    match = re.match(r"^(.*?)\s*<([^>]+)>$", text)
    if match:
        display = match.group(1).strip()
        raw_target = match.group(2).strip()
        targets = [
            normalize_canonical_id(t.strip())
            for t in raw_target.split(",")
            if t.strip()
        ]
        target = ", ".join(dict.fromkeys(targets))
        if not display:
            display = f"[{target}]"
        return display, target

    if text.startswith("[") and text.endswith("]"):
        return text, infer_justification_target(text, current_book=current_book)

    if re.match(r"^[A-Za-z0-9_.-]+$", text) and "." in text:
        norm = normalize_canonical_id(text)
        return f"[{norm}]", norm

    return text, infer_justification_target(text, current_book=current_book)


def parse_metadata_and_body(rst_text: str) -> Tuple[Dict[str, str], str]:
    """Split an RST document into its leading field-list metadata dict and remaining body."""
    lines = rst_text.splitlines()
    metadata: Dict[str, str] = {}
    body_start = 0

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith(":") and ":" in stripped[1:]:
            key, val = stripped[1:].split(":", 1)
            metadata[key.strip()] = val.strip()
            body_start = idx + 1
        elif not stripped:
            body_start = idx + 1
        else:
            body_start = idx
            break

    body = "\n".join(lines[body_start:]).strip()
    return metadata, body


def strip_folio_milestones(rst_body: str) -> str:
    """Remove .. _folio-...: labels and .. folio:: directives from an RST body."""
    cleaned = _FOLIO_BLOCK_RE.sub("", rst_body)
    cleaned = re.sub(r"^\.\.\s+_folio-[^\n]+:\s*\n+", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def extract_primitive_tags(rst_body: str) -> List[str]:
    """Identify GEOMETOR geometric primitive tags from :g: role targets in rst_body."""
    found: Set[str] = set()
    for m in _G_ROLE_RE.finditer(rst_body):
        raw = m.group(1).strip()
        t_match = re.match(r"^.+?\s+<(.+)>$", raw)
        target = t_match.group(1).strip() if t_match else raw
        expr = target.split(":", 1)[-1].strip() if ":" in target else target

        if expr.startswith("/ ") and expr.endswith(" /"):
            found.add("segment")
        elif expr.startswith("[ ") and expr.endswith(" ]"):
            found.add("line")
        elif expr.startswith("( ") and expr.endswith(" )"):
            found.add("circle")
        elif expr.startswith("< ") and expr.endswith(" )"):
            found.add("angle")
        elif expr.startswith("< ") and expr.endswith(" >"):
            pts = expr[2:-2].strip().split()
            if len(pts) == 3:
                found.add("triangle")
            elif len(pts) == 4:
                found.add("quadrilateral")
            else:
                found.add("polygon")
        elif expr:
            found.add("point")

    ordered = [
        p
        for p in (
            "point",
            "segment",
            "line",
            "circle",
            "angle",
            "triangle",
            "quadrilateral",
            "polygon",
        )
        if p in found
    ]
    return ordered


def extract_taxonomy(
    node_ref: str,
    node_type: str,
    book_roman: str,
    rst_body: str,
) -> Tuple[List[str], List[str], Optional[str]]:
    """Derive (categories, tags, subtype) for a G-Index node from its content and structure."""
    body_no_fn = re.split(r"\n\.\.\s+\[#", rst_body, maxsplit=1)[0]
    enun_m = re.search(r"\.\.\s+enunciation::\n+(.*?)(?=\n\S|\Z)", body_no_fn, re.DOTALL)
    enun_text = enun_m.group(1).strip() if enun_m else body_no_fn
    qed_m = re.search(r"\.\.\s+qed::\n+(.*?)(?=\n\S|\Z)", body_no_fn, re.DOTALL)
    qed_text = qed_m.group(1).strip() if qed_m else ""

    categories: List[str] = []
    tags: List[str] = [f"book-{book_roman.lower()}"]
    subtype: Optional[str] = None

    # 1. Structural Role Categories
    if node_type == "def":
        categories.append("definition")
    elif node_type == "post":
        categories.append("postulate")
        if node_ref in ("I.post.1", "I.post.2", "I.post.3"):
            categories.append("construction")
    elif node_type == "cn":
        categories.extend(["common-notion", "equality"])
    elif node_type == "prop":
        is_problem = bool(
            re.search(
                r"required to do|Q\.\s*\$?E\$?\.\s*F\.|what it was required to construct",
                qed_text,
                re.IGNORECASE,
            )
            or re.search(
                r"\bto (?:construct|draw|cut|bisect|describe|apply|inscribe|circumscribe|find|set out|divide|make|produce)\b",
                enun_text,
                re.IGNORECASE,
            )
        )
        if is_problem:
            subtype = "problem"
            categories.append("problem")
            if re.search(r"\bto find\b", enun_text, re.IGNORECASE):
                categories.append("finding")
            else:
                categories.append("construction")
        else:
            subtype = "theorem"
            categories.extend(["theorem", "proof"])

    # 2. Book / Mathematical Domain Categories
    for dom_cat in BOOK_DOMAIN_CATEGORIES.get(book_roman, []):
        if dom_cat not in categories:
            categories.append(dom_cat)

    # 3. Primitive Element Tags from :g: roles
    for ptag in extract_primitive_tags(body_no_fn):
        if ptag not in tags:
            tags.append(ptag)

    # 4. Glossary :term: tags from body_no_fn
    for m_term in _TERM_ROLE_RE.finditer(body_no_fn):
        raw_t = m_term.group(1).strip()
        t_match = re.match(r"^.+?\s+<([^>]+)>$", raw_t)
        slug = t_match.group(1).strip() if t_match else re.sub(r"[^a-z0-9-]+", "-", raw_t.lower()).strip("-")
        if slug and slug not in tags:
            tags.append(slug)

    # 5. Mathematical Concept Tags from enunciation (or full statement for def/post/cn)
    scan_text = enun_text if node_type == "prop" else body_no_fn
    if node_ref == "XIII.18":
        scan_text = body_no_fn
    for concept_tag, pattern in CONCEPT_PATTERNS:
        if pattern.search(scan_text) and concept_tag not in tags:
            tags.append(concept_tag)

    # 6. Proof Structure & Method Tags
    if _EQ_ROLE_RE.search(body_no_fn) and "equality" not in tags:
        tags.append("equality")
    if re.search(
        r"\b(?:which is impossible|which is absurd|For, if possible|For, if not|contrary to the hypothesis)\b",
        body_no_fn,
    ):
        tags.append("reductio-ad-absurdum")
    if re.search(r"\.\.\s+porism::|^\s*\*?\*?PORISM", body_no_fn, re.MULTILINE | re.IGNORECASE):
        tags.append("porism")
    if re.search(r"\.\.\s+lemma::|^LEMMA\.", body_no_fn, re.MULTILINE | re.IGNORECASE):
        tags.append("lemma")

    return categories, tags, subtype


def parse_grouped_items_file(
    rst_path: Path, heath_root: Path
) -> List[Dict[str, Any]]:
    """Extract individual anchored items (definitions, postulates, common notions) from a grouped RST file."""
    raw_text = rst_path.read_text(encoding="utf-8")
    meta, body = parse_metadata_and_body(raw_text)

    # Strip trailing commentary divider and hidden toctree
    body = re.split(r"\n----\n|\n\.\.\s+toctree::", body, maxsplit=1)[0]

    book_roman = meta.get("book", "I").strip()
    volume_roman = meta.get("volume", BOOK_TO_VOLUME.get(book_roman, "I")).strip()
    rel_dir = rst_path.parent.relative_to(heath_root).as_posix()

    matches = list(_ITEM_LABEL_RE.finditer(body))
    items: List[Dict[str, Any]] = []

    for idx, match in enumerate(matches):
        item_id = match.group(1).strip()
        start_pos = match.end()
        end_pos = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)

        chunk = body[start_pos:end_pos].strip()
        chunk = strip_folio_milestones(chunk)
        # Strip leading item number (e.g. "15. " or "**1.** ")
        chunk = re.sub(r"^(?:\*\*\d+\.\*\*|\d+\.)\s+", "", chunk, count=1)

        node_type = get_node_type(item_id)
        anchor = re.sub(r"[^a-z0-9]+", "-", item_id.lower()).strip("-")
        heath_url = f"https://geometor.github.io/euclid/heath/{rel_dir}/#{anchor}"

        categories, tags, subtype = extract_taxonomy(
            item_id, node_type, book_roman, chunk
        )

        items.append(
            {
                "canonical_ref": item_id,
                "type": node_type,
                "subtype": subtype,
                "book": book_roman,
                "volume": volume_roman,
                "dependencies": [],
                "content_rst": chunk,
                "svg_files": [],
                "heath_url": heath_url,
                "categories": categories,
                "tags": tags,
                "metadata": meta,
            }
        )

    return items


def parse_proposition_file(
    rst_path: Path, heath_root: Path
) -> Dict[str, Any]:
    """Parse a composed proposition index.rst file from euclid/docsrc/heath/."""
    raw_text = rst_path.read_text(encoding="utf-8")
    meta, body = parse_metadata_and_body(raw_text)

    cid = meta.get("canonical_id", "").strip()
    book_roman = meta.get("book", cid.split(".")[0] if "." in cid else "I").strip()
    volume_roman = meta.get("volume", BOOK_TO_VOLUME.get(book_roman, "I")).strip()

    # Strip trailing Dependency Graph, Required for, commentary link, and hidden toctree
    body = re.split(
        r"\n*Dependency Graph\n----------------|\n*Required for\n------------|\n----\n|\n\.\.\s+toctree::",
        body,
        maxsplit=1,
    )[0].strip()

    # Strip explicit canonical label (`.. _I.1:`), folio milestones, and `PROPOSITION N.\n===` heading
    body = re.sub(r"^\.\.\s+_[^:\n]+:\s*\n+", "", body, flags=re.MULTILINE)
    body = strip_folio_milestones(body)
    body = re.sub(
        r"^PROPOSITION\s+\d+\.?\s*\n=+\s*\n+",
        "",
        body,
        count=1,
        flags=re.IGNORECASE,
    ).strip()

    # Extract and normalize dependencies
    deps_raw = meta.get("dependencies", "")
    deps: List[str] = []
    if deps_raw:
        for d in deps_raw.split(","):
            norm_d = normalize_canonical_id(d.strip())
            if norm_d and norm_d != cid and norm_d not in deps:
                deps.append(norm_d)

    svg_files = sorted(rst_path.parent.glob("*.svg"))
    rel_dir = rst_path.parent.relative_to(heath_root).as_posix()
    heath_url = f"https://geometor.github.io/euclid/heath/{rel_dir}/"

    categories, tags, subtype = extract_taxonomy(cid, "prop", book_roman, body)

    return {
        "canonical_ref": cid,
        "type": "prop",
        "subtype": subtype,
        "book": book_roman,
        "volume": volume_roman,
        "dependencies": deps,
        "content_rst": body,
        "svg_files": svg_files,
        "heath_url": heath_url,
        "categories": categories,
        "tags": tags,
        "metadata": meta,
    }


def build_graph(
    source_dir: Optional[Path] = None,
    books: Optional[List[str]] = None,
) -> Tuple[nx.DiGraph, List[Dict[str, Any]]]:
    """Build the complete NetworkX dependency graph from ../euclid/docsrc/heath/.

    Args:
        source_dir: Path to `euclid/docsrc/heath`. Defaults to sibling repo.
        books: Optional list of Roman book numerals to include (defaults to I..XIII).

    Returns:
        Tuple of (DiGraph, all_books_data).
    """
    if source_dir is None:
        current_file = Path(__file__)
        project_root = current_file.parent.parent.parent.parent
        source_dir = project_root.parent / "euclid" / "docsrc" / "heath"

    source_dir = Path(source_dir)
    target_books = books or [ROMAN_NUMERALS[str(i)] for i in range(1, 14)]

    all_books_data: List[Dict[str, Any]] = []
    G = nx.DiGraph()

    print(f"Scanning composed Euclid source in {source_dir}...")

    for roman in target_books:
        vol = BOOK_TO_VOLUME.get(roman, "I")
        book_dir = source_dir / f"volume_{vol}" / f"book_{roman.lower()}"
        if not book_dir.exists():
            print(f"Warning: Book {roman} directory not found at {book_dir}")
            continue

        entries: List[Dict[str, Any]] = []

        # 1. Definitions, Postulates, Common Notions
        for sec_dir_name in (
            "definitions",
            "definitions_ii",
            "definitions_iii",
            "postulates",
            "common_notions",
        ):
            sec_index = book_dir / sec_dir_name / "index.rst"
            if sec_index.is_file():
                items = parse_grouped_items_file(sec_index, source_dir)
                for item in items:
                    entries.append(item)
                    G.add_node(item["canonical_ref"], **item)

        # 2. Propositions
        props_dir = book_dir / "propositions"
        if props_dir.is_dir():
            for prop_index in sorted(props_dir.glob("*/index.rst")):
                prop_data = parse_proposition_file(prop_index, source_dir)
                cid = prop_data["canonical_ref"]
                entries.append(prop_data)
                G.add_node(cid, **prop_data)
                for dep in prop_data["dependencies"]:
                    G.add_edge(cid, dep)

        entries.sort(key=lambda e: canonical_sort_key(e["canonical_ref"]))

        book_data = {
            "book_number_roman": roman,
            "book_number_arabic": str(ROMAN_TO_INT[roman]),
            "volume": vol,
            "sections": [
                {
                    "type_canonical": "mixed",
                    "title": f"Book {roman}",
                    "entries": entries,
                }
            ],
        }
        all_books_data.append(book_data)

    return G, all_books_data
