GEOMETOR • elements
===================

.. image:: https://img.shields.io/github/license/geometor/elements.svg
   :target: https://github.com/geometor/elements/blob/main/LICENSE

Codifying the logic of Euclid's Elements.

Overview
--------

**geometor.elements** is a project to reconstruct Euclid's *Elements* as a structured, digital knowledge base. We are transforming the classical text and diagrams (based on the Heath edition) into a format that allows for deep analysis, cross-referencing, and visualization.

Our goal is not just to digitize the text, but to model the **dependency chain** of geometric logic—tracing how definitions, postulates, and propositions build upon one another.

Key Features
------------

- **Digital Reconstruction**: Parsing and normalizing text from the Heath edition.
- **Dependency Mapping**: Explicitly modeling the logical dependencies between propositions.
- **Diagram Extraction**: Processing and cleaning original diagrams for high-quality display.
- **Sphinx Integration**: Generating rich, cross-linked documentation.

Workflow
--------

The project employs a multi-stage pipeline:

1.  **Ingestion**: Extracting text and images from PDF sources.
2.  **Refinement**: Cropping diagrams, normalizing text, and identifying logical units.
3.  **Transformation**: Converting structured data into reStructuredText for Sphinx.
4.  **Publishing**: Building the static site for exploration.

Resources
---------

- **Source Code**: https://github.com/geometor/elements
- **Issues**: https://github.com/geometor/elements/issues

Related Projects
----------------

- `GEOMETOR Model <https://github.com/geometor/model>`_: The symbolic engine used to verify constructions.
