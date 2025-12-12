.. _elements2-design:

Elements 2.0 Design
===================

This document outlines the design for the new reStructuredText (RST) structure and the XML parsing process for Euclid's Elements. The goal is to create a semantically consistent, machine-readable, and easily navigable documentation of the Elements, departing from the traditional numbered hierarchy.

1.  **Overall Structure and Naming Conventions**
    *   **File Organization**: Each element (definition, postulate, proposition, common notion) will reside in its own RST file. Files will be organized within subdirectories corresponding to books.
    *   **Semantic Naming**: File names and RST labels will use semantic phrases instead of traditional numbering (e.g., `book1/equilateral-triangle.rst` instead of `book1/prop1.rst`). This will also form the basis for predictable URLs and cross-references.
    *   **Title Format**: Each RST file will have a clear, succinct title reflecting the element's content.

2.  **XML Parsing Strategy**
    *   **Source**: The XML content from `resources/xml/` will be the primary source.
    *   **Parsing Tool**: A Python script will be developed to parse the XML.
    *   **Extraction**: The script will extract the element type (definition, postulate, proposition, common notion), the statement, and any associated proof or explanation.
    *   **Image Integration**: Images from `resources/images/` will be linked to the corresponding RST files. A consistent naming convention for images (e.g., `elem.<book>.<type>.<number>.jpg`) will be assumed or established.

3.  **RST Content Generation**
    *   **Standard Directives**: Use standard Sphinx/RST directives for definitions, propositions, and proofs.
    *   **Cross-referencing**: Implement a robust cross-referencing system using Sphinx's `ref` and `term` roles, linking to other elements, definitions, and glossary terms.
    *   **Glossary Integration**: Key terms will be linked to a central glossary.

4.  **Formalization and Dependency Mapping**
    *   **Metadata**: Each RST file will include metadata (e.g., using Sphinx's `meta` directive or custom fields) to capture the element type, original book/number, and semantic tags.
    *   **Dependency Links**: Within the RST content, explicit links or a custom Sphinx directive will be used to denote dependencies on other definitions, postulates, or propositions. This will facilitate the creation of a dependency graph.

5.  **Canonical Consistency**
    *   **URL Structure**: URLs will be derived directly from the semantic file paths (e.g., `/elements2/book1/equilateral-triangle.html`).
    *   **Labeling**: Consistent RST labels will ensure reliable cross-referencing throughout the documentation.

6.  **Development Workflow**
    *   **Iterative Parsing**: Develop the parsing script iteratively, starting with Book 1 and gradually extending to other books.
    *   **Testing**: Implement unit tests for the parsing script to ensure correct XML extraction and RST generation.
    *   **Build Verification**: Regularly build the Sphinx documentation to verify the generated RST content and resolve any rendering issues.

This design aims to create a flexible and powerful framework for exploring Euclid's Elements, enabling deeper analysis of its logical structure and dependencies.