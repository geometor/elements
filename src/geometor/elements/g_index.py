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
        print(f"Found {len(orphans)} orphan nodes (unused definitions/postulates/etc).")
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
        g_name = f"g.{g_id}"
        id_map[node_ref] = g_name

    # 2. Generate RST files
    print("Generating RST files...")
    for i, node_ref in enumerate(g_sequence):
        g_id = i + 1
        g_name = f"g.{g_id}"
        
        node_data = G.nodes[node_ref]
        
        # Create directory for the G-node
        node_dir = output_path / g_name
        node_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = node_dir / "index.rst"
        
        # Construct RST content
        rst_content = [
            f":order: {g_id}",
            f":original_id: {node_ref}",
            f":type: {node_data.get('type', 'unknown')}",
        ]
        
        # Add dependencies if available
        if node_data.get('dependencies'):
            # Replace dependency refs with G-refs
            deps_list = []
            for dep in sorted(list(set(node_data['dependencies']))):
                if dep in id_map:
                    deps_list.append(id_map[dep])
                else:
                    deps_list.append(dep) # Keep original if not in map
            deps_str = ', '.join(deps_list)
            rst_content.append(f":dependencies: {deps_str}")
            
        rst_content.append("")
        
        # Ref link
        rst_content.append(f".. _{g_name}:")
        rst_content.append("")
        
        # Title
        title = f"G.{g_id}"
        rst_content.append(title)
        rst_content.append("=" * len(title))
        rst_content.append("")
        
        # Link back to Heath
        rst_content.append(f"**Heath ID:** :ref:`{node_ref}`")
        rst_content.append("")
        
        # Original Content
        # We need to be careful about relative links or images in the original content.
        # The original content was designed for a specific folder structure.
        # We are flattening it.
        # Images: 'figure:: I.1.png' -> we need to copy images to this new dir.
        
        content = node_data.get('content_rst', '')
        
        # Replace refs in content
        def replace_ref(match):
            ref_key = match.group(1)
            if ref_key in id_map:
                return f":ref:`{id_map[ref_key]}`"
            return match.group(0)
            
        content = re.sub(r":ref:`([^`]+)`", replace_ref, content)
        
        # Let's copy images.
        canonical_images_dir = Path("resources/canonical_images")
        heath_propositions_dir = Path("resources/heath/propositions")
        
        if canonical_images_dir.exists():
            image_stem = node_ref
            # Copy all matching images
            for img in canonical_images_dir.glob(f"{image_stem}*.jpg"):
                shutil.copy(img, node_dir)
        
        if heath_propositions_dir.exists():
            graphic_stem = node_ref
            graphic_file = heath_propositions_dir / f"{graphic_stem}.graphic.png"
            if graphic_file.exists():
                # We might need to invert it again if we don't have the inverted one handy.
                # Or we can just copy it. transform.py inverted it.
                # Let's just copy the graphic for now.
                shutil.copy(graphic_file, node_dir / f"{graphic_stem}.graphic.png")
                # If we want the inverted one, we should probably do that image processing here too
                # or assume it's done.
        
        rst_content.append(content)
        
        with open(filepath, "w") as f:
            f.write("\n".join(rst_content))

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
        ".. collection::",
        "   :type: g_node",
        "   :sort: order",
        "",
    ]
    
    with open(output_path / "index.rst", "w") as f:
        f.write("\n".join(index_content))

    print(f"Generated {len(g_sequence)} G-nodes in {output_dir}")

if __name__ == "__main__":
    generate_g_index()
