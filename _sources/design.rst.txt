.. _elements-design:

G-Index Design
==============

The G-Index is a symbolic and logical codification of Euclid's *Elements*. It transforms the semantic structure of the modernized text into a strictly numbered dependency graph.

1.  **G-Index Structure**
    -------------------

    Unlike the traditional book-based numbering (I.1, II.5), the **G-Index** uses a flat, incremental numbering system (**G.1**, **G.2**...) reflecting the order of introduction and the dependency chain.

    *   **G-Nodes**: Each entry (definition, postulate, common notion, or proposition) is treated as a node in a Directed Acyclic Graph (DAG).
    *   **Orphans**: Elements that are defined but not yet used as dependencies are tracked as orphans to ensure complete logical coverage.

2.  **Sourcing Strategy**
    -----------------

    `geometor.elements` sources its data from the sister project `geometor.euclid`.

    *   **RST Parsing**: Instead of raw XML, the system parses the processed reStructuredText files from `euclid/docsrc/heath`.
    *   **Metadata Extraction**: Dependency links are extracted from `:dependencies:` metadata fields in the source files.
    *   **Asset Management**: Diagrams and images are sourced from the corresponding Euclid folders and renamed to match the G-Index Identity (e.g., `G.1.png`).

3.  **Generation Pipeline**
    -------------------

    The generation process follows these steps:

    1.  **Graph Construction**: Use `networkx` to build a dependency graph by scanning all source files in the Euclid project.
    2.  **Topological Sort**: (Optional) Analysis of the graph to understand the "Genealogy of Truth."
    3.  **Templated RST Output**: Every G-Node is rendered using a standard template that includes:
        *   **Heath ID**: Link back to the canonical Euclid entry.
        *   **Enunciation**: Indented blockquote for the main statement.
        *   **Dependency Graph**: A Graphviz visualization of the node's relatives.
        *   **Required For**: A list of all future nodes that depend on this truth.

4.  **Formalization Goals**
    -------------------

    The ultimate goal of the G-Index is to serve as a bridge to formal symbolic logic:

    *   **Symbolic Tagging**: Mapping textual elements (e.g., "equilateral triangle") to symbolic types in `geometor.model`.
    *   **Construction Steps**: Future iterations will include the symbolic construction steps required to generate the diagrams programmatically.

5.  **Implementation Details**
    ----------------------

    *   `graph.py`: Handles the crawling of the Euclid source tree and the extraction of metadata/content using regular expressions.
    *   `g_index.py`: Manages the generation of the flat directory structure in `docsrc/elements2/` and the rendering of the templated RST.