import networkx as nx
import re
from pathlib import Path
import shutil
import json
from geometor.elements.graph import build_graph

def generate_g_index(output_dir=None):
    if output_dir is None:
        # Default to project root elements2
        current_file = Path(__file__)
        project_root = current_file.parent.parent.parent.parent
        output_dir = project_root / "elements2"
    
    print("Building dependency graph...")
    G, all_books_data = build_graph()
    
    # Identify "Goal" nodes: Propositions in original book order
    goals = []
    for book in all_books_data:
        for section in book["sections"]:
            # We treat all entries in the book as potential goals, 
            # but we prioritize preserving the order of the book.
            # However, we primarily want to drive this by Propositions.
            # Definitions and Postulates are usually dependencies.
            # If we include Definitions in the goal list, they will be emitted 
            # when encountered if not already emitted.
            # But the user wants "push off definitions etc until we need them".
            # So we should ONLY use Propositions (and maybe Porisms/Lemmas) as goals.
            
            # Let's look at section types.
            # 'prop' is the main one.
            if section['type_canonical'] == 'prop':
                for entry in section['entries']:
                    if entry['canonical_ref']:
                        goals.append(entry['canonical_ref'])
    
    visited = set()
    g_sequence = []
    recursion_stack = set()

    def visit(node):
        if node in visited:
            return
        if node in recursion_stack:
            print(f"Warning: Cycle detected involving {node}")
            return
        
        recursion_stack.add(node)
        
        # If node is not in graph (e.g. external ref), skip or handle
        if node in G:
            # Visit dependencies first
            # Sort dependencies to ensure deterministic order (e.g. by canonical ref)
            dependencies = sorted(list(G.successors(node)))
            for dep in dependencies:
                visit(dep)
            
            g_sequence.append(node)
            visited.add(node)
        else:
            # print(f"Warning: Node {node} not found in graph")
            pass
            
        recursion_stack.remove(node)

    print(f"Processing {len(goals)} goal propositions...")
    for goal in goals:
        visit(goal)

    # Check for orphans (nodes in G but not in g_sequence)
    orphans = []
    for node in G.nodes():
        if node not in visited:
            orphans.append(node)
    
    if orphans:
        print(f"Found {len(orphans)} orphan nodes (unused definitions/postulates/etc):")
        for orphan in sorted(orphans):
            print(f" - {orphan}")
        # Optional: Append orphans at the end? 
        # For now, we leave them out as per "Just In Time" philosophy.
        # But maybe we should list them in a separate index or appendix.

    # Generate Output
    output_path = Path(output_dir)
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Build ID Map
    id_map = {}
    for i, node_ref in enumerate(g_sequence):
        g_id = i + 1
        g_name = f"G.{g_id}"
        id_map[node_ref] = g_name

    # Helper function to generate RST for a node
    def generate_node_rst(node_ref, node_dir, title, id_map, G, g_id, project_root):
        node_data = G.nodes[node_ref]
        node_dir.mkdir(parents=True, exist_ok=True)
        filepath = node_dir / "index.rst"
        
        rst_content = [
            f":order: {g_id}",
            f":original_id: {node_ref}",
            f":type: {node_data.get('type', 'unknown')}",
        ]
        
        if node_data.get('dependencies'):
            deps_list = []
            for dep in sorted(list(set(node_data['dependencies']))):
                if dep in id_map:
                    deps_list.append(id_map[dep])
                else:
                    deps_list.append(dep)
            deps_str = ', '.join(deps_list)
            rst_content.append(f":dependencies: {deps_str}")
            
        rst_content.append("")
        
        # Ref link - use the title as the label if it's a G-node, else the node_ref
        label = title if title.startswith("G.") else node_ref
        rst_content.append(f".. _{label}:")
        rst_content.append("")
        
        # Title
        display_title = title
        rst_content.append(display_title)
        rst_content.append("=" * len(display_title))
        rst_content.append("")
        
        if title.startswith("G."):
            rst_content.append(f"**Heath ID:** :ref:`{node_ref}`")
            rst_content.append("")
        
        content = node_data.get('content_rst', '')
        
        def replace_ref(match):
            content = match.group(1)
            if '<' in content:
                # Format: Label <Target>
                label, target = content.split('<')
                target = target.strip(' >')
                label = label.strip()
                
                new_target = target
                if target in id_map:
                    new_target = id_map[target]
                
                new_label = label
                if label in id_map:
                    new_label = id_map[label]
                
                if new_target != target or new_label != label:
                    if new_label == new_target:
                        return f":ref:`{new_target}`"
                    return f":ref:`{new_label} <{new_target}>`"
            else:
                # Format: Target
                target = content
                if target in id_map:
                    return f":ref:`{id_map[target]}`"
            return match.group(0)
            
        content = re.sub(r":ref:`([^`]+)`", replace_ref, content)
        
        # Copy images
        canonical_images_dir = project_root / "resources/canonical_images"
        
        if canonical_images_dir.exists():
            image_stem = node_ref
            for img in canonical_images_dir.glob(f"{image_stem}*.jpg"):
                shutil.copy(img, node_dir)
        
        # Graphic from docsrc/heath
        parts = node_ref.split('.')
        if len(parts) >= 2:
            book = parts[0]
            remainder = '.'.join(parts[1:])
            
            # Source path: docsrc/heath/{book}/{remainder}/{node_ref}.graphic.inverted.png
            graphic_source_dir = project_root / "docsrc/heath" / book / remainder
            graphic_file = graphic_source_dir / f"{node_ref}.graphic.inverted.png"
            
            if graphic_file.exists():
                # Rename to match G-node ID (e.g., g.1.png)
                new_graphic_name = f"{title}.png"
                shutil.copy(graphic_file, node_dir / new_graphic_name)
                
                # Update content to reference new image name
                # The original content likely has: .. figure:: I.1.graphic.inverted.png
                # Or maybe just I.1.graphic.png if that's what was in the RST?
                # Let's assume the RST might reference the inverted one or the standard one.
                # We'll replace both potential patterns to be safe, or just the one we know exists.
                content = content.replace(f"{node_ref}.graphic.inverted.png", new_graphic_name)
                content = content.replace(f"{node_ref}.graphic.png", new_graphic_name)
        
        rst_content.append(content)
        
        # Dependency Graph
        descendants = nx.descendants(G, node_ref)
        if descendants:
            rst_content.append("\n\nDependency Graph")
            rst_content.append("----------------")
            rst_content.append("")
            
            nodes_in_chain = descendants.union({node_ref})
            dot_lines = [
                "digraph {",
                '  bgcolor="black";',
                '  node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];',
                '  edge [color="white", fontcolor="white"];',
                '  rankdir="TB";',
            ]
            
            for node in nodes_in_chain:
                attrs = []
                label = id_map.get(node, node)
                if label.startswith("g."):
                    label = label.replace("g.", "G.")
                attrs.append(f'label="{label}"')
                
                # Determine node type for styling
                node_data_item = G.nodes[node]
                node_type = node_data_item.get('type', 'unknown')
                
                fillcolor = "#333333" # Default dark gray
                if node == node_ref:
                    # Current node
                    attrs.append('penwidth=3')
                    attrs.append('color="white"')
                    fillcolor = "#555555"
                else:
                    if node_type == 'def':
                        fillcolor = "#224422" # Dark Green
                    elif node_type == 'prop':
                        fillcolor = "#222244" # Dark Blue
                    elif node_type == 'cn':
                        fillcolor = "#442222" # Dark Red
                    elif node_type == 'post':
                        fillcolor = "#444422" # Dark Olive
                
                attrs.append(f'fillcolor="{fillcolor}"')
                
                if node in id_map:
                    url = f"/elements2/{id_map[node]}/"
                    attrs.append(f'URL="{url}"')
                    attrs.append('target="_top"')
                
                attr_str = ", ".join(attrs)
                node_id = label
                dot_lines.append(f'  "{node_id}" [{attr_str}];')
            
            for node in nodes_in_chain:
                src_label = id_map.get(node, node)
                if src_label.startswith("g."):
                    src_label = src_label.replace("g.", "G.")
                
                for pred in G.predecessors(node):
                    if pred in nodes_in_chain:
                        pred_label = id_map.get(pred, pred)
                        if pred_label.startswith("g."):
                            pred_label = pred_label.replace("g.", "G.")
                        dot_lines.append(f'  "{pred_label}" -> "{src_label}";')
            
            dot_lines.append("}")
            dot_content = "\n".join(dot_lines)
            
            rst_content.append(".. graphviz::")
            rst_content.append("")
            for line in dot_content.splitlines():
                rst_content.append(f"   {line}")
            rst_content.append("")

        # Required for
        ancestors = sorted(list(nx.ancestors(G, node_ref)))
        if ancestors:
            rst_content.append("\n\nRequired for")
            rst_content.append("------------")
            rst_content.append("")
            ref_list = []
            for ancestor in ancestors:
                if ancestor in id_map:
                    ref_list.append(f":ref:`{id_map[ancestor]}`")
                else:
                    ref_list.append(ancestor)
            rst_content.append(', '.join(ref_list))
            rst_content.append("")
        
        with open(filepath, "w") as f:
            f.write("\n".join(rst_content))

    # 2. Generate RST files for G-nodes
    print("Generating RST files for G-nodes...")
    for i, node_ref in enumerate(g_sequence):
        g_id = i + 1
        g_name = f"G.{g_id}"
        node_dir = output_path / g_name
        generate_node_rst(node_ref, node_dir, g_name, id_map, G, g_id, project_root)

    # 3. Generate Orphans
    if orphans:
        print(f"Generating orphans page for {len(orphans)} orphans...")
        orphans_file = output_path / "orphans.rst"
        
        orphans_content = [
            ":navigation: header",
            ":order: 99",
            "",
            "Orphans",
            "=======",
            "",
            "The following nodes were identified as orphans (not referenced by the main sequence).",
            "",
        ]
        
        ROMAN_TO_INT = {
            'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
            'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
            'XI': 11, 'XII': 12, 'XIII': 13
        }

        SECTION_TYPE_ORDER = {
            'def': 1,
            'post': 2,
            'cn': 3,
            'prop': 4
        }

        def canonical_sort_key(ref_id):
            parts = ref_id.split('.')
            if not parts:
                return (0, 0, 0)
            
            # Book Number
            book_num = 0
            if parts[0] in ROMAN_TO_INT:
                book_num = ROMAN_TO_INT[parts[0]]
            
            # Section Type
            type_order = 99
            if len(parts) > 1:
                type_order = SECTION_TYPE_ORDER.get(parts[1], 99)
            
            # Item Number
            item_num = 0
            if len(parts) > 2:
                try:
                    item_num = int(parts[2])
                except ValueError:
                    pass # Keep 0 if not an integer
            
            return (book_num, type_order, item_num)

        for orphan in sorted(orphans, key=canonical_sort_key):
            node_data = G.nodes[orphan]
            

            
            # Title
            orphans_content.append(orphan)
            orphans_content.append("-" * len(orphan))
            orphans_content.append("")
            
            # Content
            content = node_data.get('content_rst', '')
            
            # Replace refs
            def replace_ref(match):
                content = match.group(1)
                if '<' in content:
                    # Format: Label <Target>
                    label, target = content.split('<')
                    target = target.strip(' >')
                    label = label.strip()
                    
                    new_target = target
                    if target in id_map:
                        new_target = id_map[target]
                    
                    new_label = label
                    if label in id_map:
                        new_label = id_map[label]
                    
                    if new_target != target or new_label != label:
                        if new_label == new_target:
                            return f":ref:`{new_target}`"
                        return f":ref:`{new_label} <{new_target}>`"
                else:
                    # Format: Target
                    target = content
                    if target in id_map:
                        return f":ref:`{id_map[target]}`"
                return match.group(0)
                
            content = re.sub(r":ref:`([^`]+)`", replace_ref, content)
            
            # Copy images to output_dir (root of elements2)
            canonical_images_dir = project_root / "resources/canonical_images"
            
            if canonical_images_dir.exists():
                image_stem = orphan
                for img in canonical_images_dir.glob(f"{image_stem}*.jpg"):
                    shutil.copy(img, output_path)
            
            # Graphic from docsrc/heath
            parts = orphan.split('.')
            if len(parts) >= 2:
                book = parts[0]
                remainder = '.'.join(parts[1:])
                
                # Source path: docsrc/heath/{book}/{remainder}/{orphan}.graphic.inverted.png
                graphic_source_dir = project_root / "docsrc/heath" / book / remainder
                graphic_file = graphic_source_dir / f"{orphan}.graphic.inverted.png"
                
                if graphic_file.exists():
                    # For orphans, we keep the original name or maybe orphan name?
                    # Let's keep it simple and use orphan name but maybe .png?
                    # The user didn't specify renaming for orphans, but consistency is good.
                    # However, orphans don't have a G-ID.
                    # Let's just copy it as {orphan}.png to be cleaner than .graphic.inverted.png
                    new_graphic_name = f"{orphan}.png"
                    shutil.copy(graphic_file, output_path / new_graphic_name)
                    
                    content = content.replace(f"{orphan}.graphic.inverted.png", new_graphic_name)
                    content = content.replace(f"{orphan}.graphic.png", new_graphic_name)

            orphans_content.append(content)
            orphans_content.append("")
            orphans_content.append(".. raw:: html")
            orphans_content.append("")
            orphans_content.append("   <hr>")
            orphans_content.append("")

        with open(orphans_file, "w") as f:
            f.write("\n".join(orphans_content))

    # Generate Map JSON
    with open(output_path / "map.json", "w") as f:
        json.dump(id_map, f, indent=2)

    # Generate Main Index
    index_content = [
        ":navigation: header",
        ":order: 3",
        "",
        "Elements 2.0 (G Index)",
        "======================",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :caption: Contents",
        "",
        "   orphans" if orphans else "",
        "",
        ".. collection::",
        "   :type: g_node",
        "   :sort: order",
        "",
    ]
    
    # Remove empty lines if orphans is empty
    index_content = [line for line in index_content if line or line == ""]
    
    with open(output_path / "index.rst", "w") as f:
        f.write("\n".join(index_content))

    print(f"Generated {len(g_sequence)} G-nodes and {len(orphans)} orphans in {output_dir}")

if __name__ == "__main__":
    generate_g_index()
