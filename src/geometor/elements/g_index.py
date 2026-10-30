"""
Generate the G-Index for Euclid's Elements.

Processes the composed Heath Edition in `../euclid/docsrc/heath/` to produce:
- Strictly numbered G-Index nodes (`G.1`, `G.2`, ...) in topological dependency order
- GEOMETOR symbolic element indications in `:g:` roles (`/ A B /`, `< A B C >`, `< B A C )`, `( B C D )`, `[ A B ]`, `A`)
- G-Index step justifications (`:just:`[G.4] <G.4>``, `.. assertion:: [G.2] <G.2>`)
- Interactive inline SVG figures copied per G-node
- Rich metadata (`:type:`, `:subtype:`, `:categories:`, `:tags:`, `:dependencies:`)
- Transitive Graphviz dependency graphs and `Required for` back-links
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import networkx as nx

from .graph import (
    build_graph,
    canonical_sort_key,
    g_dependency_sort_key,
    parse_justification_arg,
)
from .pseudocode import (
    generate_pseudocode_rst,
    get_semantic_name,
    tighten_enunciation_text,
)

_G_ROLE_RE = re.compile(r":g:`([^`]+)`")
_TERM_ROLE_RE = re.compile(r":term:`([^`]+)`")
_PERSON_ROLE_RE = re.compile(r":person:`([^`]+)`")
_CITE_ROLE_RE = re.compile(r":cite:`([^`]+)`")
_EQ_ROLE_RE = re.compile(r":eq:`([^`]+)`")
_COMBINED_JUST_RE = re.compile(
    r"(?P<role>:just:`(?P<role_arg>[^`]+)`)|(?P<dir>^(?P<dir_prefix>\.\.\s+(?:assertion|subclause|sub-clause)::)[ \t]+(?P<dir_arg>[^\n]+))",
    re.MULTILINE,
)


def g_num_sort_key(g_name: str) -> int:
    """Return integer index for a 'G.<n>' identifier."""
    if g_name.startswith("G.") and g_name[2:].isdigit():
        return int(g_name[2:])
    return 999999


def transform_geom_roles(rst_text: str) -> str:
    """Replace cryptic `$AB$` display labels in `:g:` roles with GEOMETOR symbolic indications.

    Examples:
    - ``:g:`$AB$ <0255.g1:/ A B />``` -> ``:g:`/ A B / <0255.g1:/ A B />```
    - ``:g:`$ABC$ <0255.g1:< A B C >>``` -> ``:g:`< A B C > <0255.g1:< A B C >>```
    - ``:g:`$BAC$ <0261.g1:< B A C )>``` -> ``:g:`< B A C ) <0261.g1:< B A C )>```
    - ``:g:`$BCD$ <0255.g1:( B C D )>``` -> ``:g:`( B C D ) <0255.g1:( B C D )>```
    - ``:g:`$A$ <0255.g1:A>``` -> ``:g:`A <0255.g1:A>```
    """

    def _repl(match: re.Match) -> str:
        raw = match.group(1).strip()
        m = re.match(r"^(.+?)\s+<(.+)>$", raw)
        if m:
            target = m.group(2).strip()
        else:
            target = raw
        expr = target.split(":", 1)[-1].strip() if ":" in target else target
        if not expr:
            return match.group(0)
        return f":g:`{expr} <{target}>`"

    return _G_ROLE_RE.sub(_repl, rst_text)


def transform_justifications(
    rst_text: str,
    current_book: str,
    id_map: Dict[str, str],
) -> str:
    """Rewrite `:just:` roles and `.. assertion::` / `.. subclause::` justifications to G-Index IDs."""
    last_g_targets: Optional[str] = None

    def _map_arg(raw_arg: str) -> Optional[str]:
        nonlocal last_g_targets
        s = raw_arg.strip()
        if re.match(r"^\[?\*?id\.?\*?\.?\]?$", s, re.IGNORECASE) and last_g_targets:
            return f"[{last_g_targets}] <{last_g_targets}>"

        _disp, target = parse_justification_arg(s, current_book=current_book)
        if not target:
            return None

        mapped_list: List[str] = []
        for part in target.split(","):
            p = part.strip()
            if not p:
                continue
            mapped = id_map.get(p, p)
            if mapped not in mapped_list:
                mapped_list.append(mapped)

        if not mapped_list:
            return None

        g_targets_str = ", ".join(mapped_list)
        last_g_targets = g_targets_str
        return f"[{g_targets_str}] <{g_targets_str}>"

    def _repl(match: re.Match) -> str:
        if match.group("role"):
            new_arg = _map_arg(match.group("role_arg"))
            if new_arg:
                return f":just:`{new_arg}`"
            return match.group(0)
        else:
            prefix = match.group("dir_prefix")
            new_arg = _map_arg(match.group("dir_arg"))
            if new_arg:
                return f"{prefix} {new_arg}"
            return match.group(0)

    return _COMBINED_JUST_RE.sub(_repl, rst_text)


def transform_refs(rst_text: str, id_map: Dict[str, str]) -> str:
    """Rewrite any `:ref:` roles whose target is in `id_map` to the corresponding G-ID."""

    def _replace_ref(match: re.Match) -> str:
        val = match.group(1).strip()
        if "<" in val and val.endswith(">"):
            lbl, target_part = val.rsplit("<", 1)
            target = target_part[:-1].strip()
            lbl = lbl.strip()
            new_target = id_map.get(target, target)
            new_lbl = id_map.get(lbl, lbl)
            if new_target != target or new_lbl != lbl:
                return f":ref:`{new_lbl} <{new_target}>`"
        else:
            if val in id_map:
                g_val = id_map[val]
                return f":ref:`{g_val} <{g_val}>`"
        return match.group(0)

    return re.sub(r":ref:`([^`]+)`", _replace_ref, rst_text)


def clean_plain_excerpt(rst_body: str) -> str:
    """Extract a clean one-line plain-text excerpt from the enunciation or first paragraph."""
    enun_m = re.search(
        r"\.\.\s+enunciation::\n+(.*?)(?=\n\S|\Z)", rst_body, re.DOTALL
    )
    raw = enun_m.group(1).strip() if enun_m else rst_body.split("\n\n", 1)[0].strip()

    # Strip footnote references (`\ [#f1]_` or `[#f1]_`)
    text = re.sub(r"\\?\s*\[#[^\]]+\]_", "", raw)

    # Unwrap roles (`:g:`, `:term:`, `:person:`, `:cite:`, `:eq:`, `:ref:`)
    def _unwrap_role(m: re.Match) -> str:
        inner = m.group(1).strip()
        m_disp = re.match(r"^(.+?)\s+<.+>$", inner)
        disp = m_disp.group(1).strip() if m_disp else inner
        return disp.replace("**", "").replace("*", "")

    text = re.sub(r":[A-Za-z0-9_.-]+:`([^`]+)`", _unwrap_role, text)
    text = " ".join(line.strip() for line in text.splitlines() if line.strip())
    return text


def wrap_as_enunciation(statement_rst: str) -> str:
    """Wrap a definition, postulate, or common notion statement in an `.. enunciation::` block."""
    stripped = statement_rst.strip()
    if stripped.startswith(".. enunciation::"):
        return stripped
    indented = "\n".join(
        f"   {line}" if line.strip() else "" for line in stripped.splitlines()
    )
    return f".. enunciation::\n\n{indented}"


def generate_g_dot(
    G: nx.DiGraph,
    node_ref: str,
    id_map: Dict[str, str],
) -> str:
    """Generate a Graphviz DOT string for the transitive proof chain of `node_ref` using G-IDs."""
    descendants = nx.descendants(G, node_ref)
    if not descendants:
        return ""

    nodes_in_chain = sorted(
        descendants.union({node_ref}),
        key=lambda n: g_num_sort_key(id_map.get(n, n)),
    )

    dot_lines = [
        "digraph {",
        '  bgcolor="transparent";',
        '  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];',
        '  edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];',
        '  rankdir="TB";',
    ]

    for node in nodes_in_chain:
        g_label = id_map.get(node, node)
        node_data = G.nodes[node]
        node_type = node_data.get("type", "unknown")
        excerpt = node_data.get("g_excerpt") or node_data.get("excerpt", "")
        if excerpt:
            short_excerpt = excerpt[:180] + ("..." if len(excerpt) > 180 else "")
            escaped_excerpt = short_excerpt.replace("\\", "\\\\").replace('"', '\\"')
            tooltip_str = f"{g_label} ({node}): {escaped_excerpt}"
        else:
            tooltip_str = f"{g_label} ({node})"

        fillcolor = "#333333"
        attrs = [
            f'label="{g_label}"',
            f'tooltip="{tooltip_str}"',
        ]
        if node == node_ref:
            attrs.append("penwidth=2.5")
            attrs.append('color="#e8b85a"')
            fillcolor = "#4a453b"
        else:
            if node_type == "def":
                fillcolor = "#224422"
            elif node_type == "prop":
                fillcolor = "#222244"
            elif node_type == "cn":
                fillcolor = "#442222"
            elif node_type == "post":
                fillcolor = "#444422"

        attrs.append(f'fillcolor="{fillcolor}"')
        if node == node_ref:
            attrs.append('URL="index.html"')
        elif node in id_map:
            attrs.append(f'URL="../{g_label}/index.html"')
        attrs.append('target="_top"')

        dot_lines.append(f'  "{g_label}" [{", ".join(attrs)}];')

    for node in nodes_in_chain:
        dst_label = id_map.get(node, node)
        preds = sorted(
            [p for p in G.predecessors(node) if p in nodes_in_chain],
            key=lambda n: g_num_sort_key(id_map.get(n, n)),
        )
        for pred in preds:
            src_label = id_map.get(pred, pred)
            dot_lines.append(f'  "{src_label}" -> "{dst_label}";')

    dot_lines.append("}")
    return "\n".join(dot_lines)


def sync_apparatus_resources(project_root: Path) -> None:
    """Copy glossary.json, persons.json, citations.json, and enunciations.json from euclid/resources/heath/ into elements/resources/."""
    euclid_res = project_root.parent / "euclid" / "resources" / "heath"
    target_res = project_root / "resources"
    if not euclid_res.is_dir():
        return
    target_res.mkdir(parents=True, exist_ok=True)
    for fname in ("glossary.json", "persons.json", "citations.json", "enunciations.json"):
        src_file = euclid_res / fname
        if src_file.is_file():
            shutil.copy2(src_file, target_res / fname)


def generate_g_index(
    output_dir: Optional[Path] = None,
    books: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Generate the complete G-Index RST structure from ../euclid/docsrc/heath/.

    Args:
        output_dir: Directory to write generated G-Index RST files (`docsrc/elements2`).
        books: Optional list of Roman book numerals to include (defaults to all 13 books).

    Returns:
        Summary statistics dictionary.
    """
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent.parent
    if output_dir is None:
        output_dir = project_root / "docsrc" / "elements2"

    sync_apparatus_resources(project_root)

    print("Building dependency graph from composed Euclid Heath edition...")
    G, all_books_data = build_graph(books=books)

    # Identify Goal nodes: Propositions in canonical book order
    goals: List[str] = []
    for book in all_books_data:
        for section in book["sections"]:
            for entry in section["entries"]:
                if entry.get("type") == "prop" and entry.get("canonical_ref"):
                    goals.append(entry["canonical_ref"])

    visited: Set[str] = set()
    g_sequence: List[str] = []
    recursion_stack: Set[str] = set()

    def visit(node: str) -> None:
        if node in visited:
            return
        if node in recursion_stack:
            print(f"Warning: Cycle detected involving {node}")
            return

        recursion_stack.add(node)
        if node in G:
            dependencies = sorted(
                list(G.successors(node)),
                key=g_dependency_sort_key,
            )
            for dep in dependencies:
                visit(dep)

            g_sequence.append(node)
            visited.add(node)
        recursion_stack.remove(node)

    print(f"Sequencing {len(goals)} propositions into G-Index...")
    for goal in goals:
        visit(goal)

    orphans = sorted(
        [node for node in G.nodes() if node not in visited],
        key=canonical_sort_key,
    )
    if orphans:
        print(f"Found {len(orphans)} orphan nodes (unreferenced definitions/postulates/common notions).")

    output_path = Path(output_dir)
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Build ID Map (Euclid Canonical ID -> G.<n>) and Semantic Function/Rule Name Map
    id_map: Dict[str, str] = {}
    g_to_sem_name: Dict[str, str] = {}
    used_sem_names: Set[str] = set()
    for i, node_ref in enumerate(g_sequence):
        g_label = f"G.{i + 1}"
        id_map[node_ref] = g_label
        nd = G.nodes[node_ref]
        raw_ex = nd.get("excerpt", "") or clean_plain_excerpt(nd.get("content_rst", ""))
        tight_ex = tighten_enunciation_text(raw_ex, node_ref)
        sem_name = get_semantic_name(
            node_ref,
            nd.get("type", "prop"),
            nd.get("subtype"),
            tight_ex,
        )
        if sem_name in used_sem_names:
            ref_suffix = re.sub(r"[^a-z0-9]+", "_", node_ref.lower()).strip("_")
            sem_name = f"{sem_name}_{ref_suffix}"
        used_sem_names.add(sem_name)
        g_to_sem_name[g_label] = sem_name

    # 2. Generate RST files for each G-node
    print(f"Generating RST files for {len(g_sequence)} G-nodes...")
    for i, node_ref in enumerate(g_sequence):
        g_id = i + 1
        g_name = f"G.{g_id}"
        node_dir = output_path / g_name
        node_dir.mkdir(parents=True, exist_ok=True)

        node_data = G.nodes[node_ref]
        node_type = node_data.get("type", "unknown")
        subtype = node_data.get("subtype")
        book_roman = node_data.get("book", "I")
        volume_roman = node_data.get("volume", "I")
        categories = node_data.get("categories", [])
        tags = node_data.get("tags", [])
        heath_url = node_data.get("heath_url", "")
        svg_files: List[Path] = node_data.get("svg_files", [])
        py_files: List[Path] = node_data.get("py_files", [])

        # Map original <folio>.g<k> stems to clean sequential g1, g2, ...
        gid_map: Dict[str, str] = {}
        local_svg_names: List[str] = []
        for idx, svg_path in enumerate(svg_files, start=1):
            new_gid = f"g{idx}"
            gid_map[svg_path.stem] = new_gid
            dest_svg_name = f"{new_gid}.svg"
            local_svg_names.append(dest_svg_name)
            if svg_path.is_file():
                svg_text = svg_path.read_text(encoding="utf-8")
                svg_text = re.sub(
                    r'\s+data-folio="[^"]*"', "", svg_text
                )
                svg_text = re.sub(
                    r'data-graphic-id="[^"]*"',
                    f'data-graphic-id="{new_gid}"',
                    svg_text,
                )
                svg_text = re.sub(
                    r'data-graphic="[^"]*"',
                    f'data-graphic="{new_gid}"',
                    svg_text,
                )
                (node_dir / dest_svg_name).write_text(svg_text, encoding="utf-8")

        local_py_names: List[str] = []
        for idx, py_path in enumerate(py_files, start=1):
            dest_py_name = f"g{idx}.py"
            local_py_names.append(dest_py_name)
            if py_path.is_file():
                shutil.copy2(py_path, node_dir / dest_py_name)

        # Map dependencies to G-IDs sorted in G-order
        deps_g: List[str] = []
        for dep in node_data.get("dependencies", []):
            mapped_dep = id_map.get(dep, dep)
            if mapped_dep not in deps_g:
                deps_g.append(mapped_dep)
        deps_g.sort(key=g_num_sort_key)
        deps_str = ", ".join(deps_g)

        # Transform content body (Heath edition with GEOMETOR roles and G.<n> justifications)
        raw_content = node_data.get("content_rst", "")
        for old_stem, new_gid in gid_map.items():
            raw_content = raw_content.replace(f"{old_stem}.svg", f"{new_gid}.svg")
            raw_content = raw_content.replace(f"{old_stem}:", f"{new_gid}:")
        raw_content = re.sub(r"\b\d{4}\.(g\d+):", r"\1:", raw_content)

        if node_type in ("def", "post", "cn"):
            raw_content = wrap_as_enunciation(raw_content)

        heath_content = transform_geom_roles(raw_content)
        heath_content = transform_justifications(heath_content, book_roman, id_map)
        heath_content = transform_refs(heath_content, id_map)

        # Generate Pseudocode track content with tightened enunciation, .. signature::, and .. step:: sequence
        pseudo_content = generate_pseudocode_rst(
            heath_content,
            node_ref,
            node_type,
            g_name=g_name,
            subtype=subtype,
            id_map=id_map,
            g_to_sem_name=g_to_sem_name,
        )

        excerpt = clean_plain_excerpt(pseudo_content)
        node_data["g_excerpt"] = excerpt

        # Metadata header for primary track (index.rst)
        meta_lines = [
            f":order: {g_id}",
            f":number: {g_id}",
            f":canonical_id: {g_name}",
            f":original_id: {node_ref}",
            f":volume: {volume_roman}",
            f":book: {book_roman}",
            f":type: {node_type}",
        ]
        if subtype:
            meta_lines.append(f":subtype: {subtype}")
        if categories:
            cats_str = ", ".join(categories)
            meta_lines.append(f":categories: {cats_str}")
            meta_lines.append(f":category: {cats_str}")
        if tags:
            meta_lines.append(f":tags: {', '.join(tags)}")
        meta_lines.append(f":dependencies: {deps_str}")
        if excerpt:
            meta_lines.append(f":excerpt: {excerpt}")

        heath_link = f"`{node_ref} <{heath_url}>`_" if heath_url else f"``{node_ref}``"
        title_underline = "=" * len(g_name)

        # Dependency Graph & Required For (shared by Pseudocode and Heath tracks)
        dot_str = generate_g_dot(G, node_ref, id_map)
        dep_graph_section = ""
        if dot_str:
            indented_dot = "\n".join(f"   {line}" for line in dot_str.splitlines())
            dep_graph_section = (
                f"Dependency Graph\n----------------\n\n.. graphviz::\n\n{indented_dot}"
            )

        ancestors = sorted(
            list(nx.ancestors(G, node_ref)),
            key=lambda a: g_num_sort_key(id_map.get(a, a)),
        )
        req_for_section = ""
        if ancestors:
            ref_links = [
                f":ref:`{id_map[a]} <{id_map[a]}>`" if a in id_map else a
                for a in ancestors
            ]
            req_for_section = f"Required for\n------------\n\n{', '.join(ref_links)}"

        # Companion track toctree (hidden)
        toctree_entries = []
        if local_py_names:
            toctree_entries.append("   code")
        toctree_entries.append("   heath")
        toctree_section = ".. toctree::\n   :hidden:\n\n" + "\n".join(toctree_entries)

        # Track 1: index.rst (Pseudocode)
        index_sections: List[str] = [
            "\n".join(meta_lines),
            f".. _{g_name}:\n.. _{node_ref}:\n\n{g_name}\n{title_underline}",
            f".. rubric:: {heath_link}",
            pseudo_content,
            dep_graph_section,
            req_for_section,
            toctree_section,
        ]
        rendered_index = "\n\n".join(s for s in index_sections if s).strip() + "\n"
        (node_dir / "index.rst").write_text(rendered_index, encoding="utf-8")

        # Auxiliary metadata header for Code and Heath tracks
        aux_meta = "\n".join(
            [
                f":canonical_id: {g_name}",
                f":original_id: {node_ref}",
                f":volume: {volume_roman}",
                f":book: {book_roman}",
                f":type: {node_type}",
            ]
        )

        # Track 2: code.rst (Code - only when .py construction scripts exist)
        if local_py_names:
            code_title = f"{g_name} — Code"
            code_sections: List[str] = [
                aux_meta,
                f"{code_title}\n{'=' * len(code_title)}",
                f".. rubric:: {heath_link}",
            ]
            enun_m = re.search(
                r"(\.\.\s+enunciation::\n+(?:[ \t]+[^\n]*\n+|\n)*)",
                pseudo_content,
            )
            if enun_m:
                code_sections.append(enun_m.group(1).strip())

            for idx, py_name in enumerate(local_py_names):
                if len(local_py_names) > 1:
                    code_sections.append(f".. rubric:: ``{py_name}``")
                if idx < len(local_svg_names):
                    code_sections.append(f".. picture:: {local_svg_names[idx]}")
                code_sections.append(
                    f".. literalinclude:: {py_name}\n   :language: python"
                )

            rendered_code = "\n\n".join(s for s in code_sections if s).strip() + "\n"
            (node_dir / "code.rst").write_text(rendered_code, encoding="utf-8")

        # Track 3: heath.rst (Heath)
        heath_title = f"{g_name} — Heath"
        heath_sections: List[str] = [
            aux_meta,
            f"{heath_title}\n{'=' * len(heath_title)}",
            f".. rubric:: {heath_link}",
            heath_content,
            dep_graph_section,
            req_for_section,
        ]
        rendered_heath = "\n\n".join(s for s in heath_sections if s).strip() + "\n"
        (node_dir / "heath.rst").write_text(rendered_heath, encoding="utf-8")

    # 3. Generate Orphans page
    if orphans:
        print(f"Generating orphans page for {len(orphans)} orphans...")
        orphans_lines = [
            ":order: 9999",
            ":type: orphans",
            ":excerpt: Definitions, postulates, and common notions not directly cited in the dependency sequence.",
            "",
            "Orphans",
            "=======",
            "",
            "The following definitions, postulates, and common notions are not directly cited by any proposition in the main dependency sequence.",
            "",
        ]
        for idx, orphan in enumerate(orphans):
            node_data = G.nodes[orphan]
            heath_url = node_data.get("heath_url", "")
            heading = orphan
            orphans_lines.append(f".. _{orphan}:")
            orphans_lines.append("")
            orphans_lines.append(heading)
            orphans_lines.append("-" * len(heading))
            orphans_lines.append("")
            if heath_url:
                orphans_lines.append(f"**Heath ID:** `{orphan} <{heath_url}>`_")
                orphans_lines.append("")
            body_txt = transform_geom_roles(node_data.get("content_rst", ""))
            body_txt = transform_refs(body_txt, id_map)
            orphans_lines.append(body_txt)
            orphans_lines.append("")
            if idx < len(orphans) - 1:
                orphans_lines.append("----")
                orphans_lines.append("")

        (output_path / "orphans.rst").write_text(
            "\n".join(orphans_lines).rstrip() + "\n", encoding="utf-8"
        )

    # 4. Write map.json and update resources/enunciations.json
    with open(output_path / "map.json", "w", encoding="utf-8") as f:
        json.dump(id_map, f, indent=2)

    enun_path = project_root / "resources" / "enunciations.json"
    enun_data: Dict[str, str] = {}
    if enun_path.is_file():
        try:
            enun_data = json.loads(enun_path.read_text(encoding="utf-8"))
        except Exception:
            enun_data = {}
    for node_ref in g_sequence:
        g_name = id_map[node_ref]
        ex = G.nodes[node_ref].get("g_excerpt") or G.nodes[node_ref].get("excerpt", "")
        if ex:
            enun_data[g_name] = ex
            enun_data[node_ref] = ex
    enun_path.parent.mkdir(parents=True, exist_ok=True)
    enun_path.write_text(
        json.dumps(enun_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # 5. Generate Main Index (docsrc/elements2/index.rst)
    index_lines = [
        ":navigation: header",
        ":order: 3",
        ":layout: book",
        ":book_title: Elements 2.0 (G Index)",
        "",
        "Elements 2.0 (G Index)",
        "======================",
        "",
        ".. collection::",
        "   :sort: order",
        "",
    ]
    (output_path / "index.rst").write_text("\n".join(index_lines), encoding="utf-8")

    stats = {
        "g_nodes": len(g_sequence),
        "orphans": len(orphans),
        "total_edges": G.number_of_edges(),
        "output_dir": str(output_path),
    }
    print(
        f"Generated {len(g_sequence)} G-nodes and {len(orphans)} orphans in {output_path}"
    )
    return stats


if __name__ == "__main__":
    generate_g_index()
