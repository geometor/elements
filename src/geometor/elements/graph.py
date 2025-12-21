"""
Graph manipulation utilities (RST version).

This module is responsible for crawling the Euclid source documentation
(sourced from the Heath edition in the sibling `geometor-euclid` project)
to build a NetworkX dependency graph and extract metadata for G-Index generation.
"""

from __future__ import annotations
import networkx as nx
import re
from pathlib import Path

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

# Reverse mapping for sorting
ROMAN_TO_INT = {v: int(k) for k, v in ROMAN_NUMERALS.items()}

def parse_rst_file(file_path: Path) -> dict:
    """Parse an RST file to extract metadata and content.

    Identifies metadata fields at the beginning of the file, strips standard
    Euclid header blocks and picture directives, and returns the structured
    components.

    Args:
        file_path (Path): Path to the RST file.

    Returns:
        dict: A dictionary containing 'metadata', 'image', and 'content'.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    metadata = {}
    content_lines = []
    is_metadata = True
    
    # Simple state machine
    # 1. Parsing Metadata (lines starting with :)
    # 2. Parsing Content
    
    for line in lines:
        stripped = line.strip()
        if is_metadata:
            if stripped.startswith(":") and ":" in stripped[1:]:
                # Parse metadata field
                parts = stripped[1:].split(":", 1)
                key = parts[0].strip()
                value = parts[1].strip()
                metadata[key] = value
            elif not stripped:
                continue # Skip empty lines between metadata
            else:
                is_metadata = False
                content_lines.append(line)
        else:
            content_lines.append(line)

    content = "".join(content_lines)
    
    # Remove the standard Euclid header block:
    header_pattern = r"\.\. _[^:]+:\s+\n\n?[^\n]+\n=+\n"
    content = re.sub(header_pattern, "", content, count=1)

    # Extract Main Image
    # Look for .. picture:: FILENAME or .. figure:: FILENAME
    # We want to extract it and remove it from the content so we can place it manually
    image_pattern = r"(\.\. (picture|figure):: [^\n]+)\n"
    match = re.search(image_pattern, content)
    main_image = None
    if match:
        main_image = match.group(1).split("::")[1].strip()
        # Remove the image line from content
        content = re.sub(image_pattern, "", content, count=1)

    # refined metadata
    if "dependencies" in metadata:
        deps = [d.strip() for d in metadata["dependencies"].split(",")]
        metadata["dependencies"] = [d for d in deps if d]
    else:
        metadata["dependencies"] = []
        
    return {
        "metadata": metadata,
        "image": main_image,
        "content": content.strip()
    }

def build_graph(source_dir: Path | None = None) -> tuple[nx.DiGraph, list[dict]]:
    """Build a NetworkX dependency graph from the RST source files.

    Scans the specified source directory (defaulting to the Euclid sibling
    project) for Euclid books and entries. Builds a directed graph representing
    the logical dependency flow.

    Args:
        source_dir (Path, optional): Directory containing the Euclid RST books.
            Defaults to '../euclid/docsrc/heath'.

    Returns:
        tuple[nx.DiGraph, list[dict]]: The dependency graph and a list of book data.
    """
    if source_dir is None:
        # Default to project root dependencies
        # Assuming we are in geometor/elements, we need to go to ../euclid/docsrc/heath
        current_file = Path(__file__)
        # src/geometor/elements/graph.py -> elements root
        project_root = current_file.parent.parent.parent.parent
        # Go up to PROJECTS/geometor and then into euclid
        source_dir = project_root.parent / "euclid" / "docsrc" / "heath"

    all_books_data = []
    G = nx.DiGraph()
    
    print(f"Scanning for books in {source_dir}...")
    
    # Iterate over books I to XIII - LIMIT to Book I for verification
    for book_num in range(1, 2):
        roman = ROMAN_NUMERALS[str(book_num)]
        book_dir = source_dir / roman
        
        if not book_dir.exists():
            print(f"Book {roman} not found at {book_dir}")
            continue

        print(f"Processing Book {roman}...")
        
        book_data = {
            "book_number_roman": roman,
            "book_number_arabic": str(book_num),
            "sections": []
        }
        
        # We need to collect entries. 
        # The structure is heath/{BOOK}/{ID}/index.rst
        # ID can be 1, 2... or def.1, cn.1, post.1 etc.
        # We should walk the directory or just list dirs
        
        # A section in xml structure grouped entries. Here entries are folders.
        # We can construct a synthetic "section" for compatibility or flat list.
        # Let's create one big section for the book.
        
        entries = []
        
        for entry_dir in book_dir.iterdir():
            if entry_dir.is_dir():
                index_file = entry_dir / "index.rst"
                if index_file.exists():
                    try:
                        parsed_data = parse_rst_file(index_file)
                        meta = parsed_data["metadata"]
                        content = parsed_data["content"]
                        image = parsed_data["image"]
                        
                        # Construct canonical ref
                        dir_name = entry_dir.name
                        canonical_ref = f"{roman}.{dir_name}"
                        
                        # The node metadata might have ID we can use to double check?
                        # Sample doesn't have explicit ID field, but has `I.1` as title underline.
                        
                        entry_data = {
                            "canonical_ref": canonical_ref,
                            "type": meta.get("type", "unknown"),
                            "dependencies": meta.get("dependencies", []),
                            "content_rst": content,
                            "image": image,
                            "order": meta.get("order", 0),
                            "metadata": meta
                        }
                        
                        entries.append(entry_data)
                        
                        # Add to Graph
                        G.add_node(canonical_ref, **entry_data)
                        for dep in entry_data["dependencies"]:
                            G.add_edge(canonical_ref, dep)
                            
                    except Exception as e:
                        print(f"Error parsing {index_file}: {e}")

        # Sort entries by order (if convertible to int) or name
        def sort_key(e):
            try:
                return int(e["order"])
            except:
                return 999
        
        entries.sort(key=sort_key)
        
        section_data = {
            "type_canonical": "prop", # Default? Or Mixed?
            "title": f"Book {roman}",
            "entries": entries
        }
        
        book_data["sections"].append(section_data)
        all_books_data.append(book_data)

    return G, all_books_data

