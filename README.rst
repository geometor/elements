GEOMETOR • elements
===================

.. image:: https://img.shields.io/github/license/geometor/elements.svg
   :target: https://github.com/geometor/elements/blob/main/LICENSE

**Symbolic dependency mapping and G-Index generation for Euclid's Elements.**


Overview
--------

**geometor.elements** transforms the processed Euclid text into a structured G-Index. While the sister project `geometor.euclid` focuses on semantic discovery and text normalization, **elements** is responsible for:

- **Logic Mapping**: Creating the G-Index (G.1, G.2...) to trace the strict logical genealogy of propositions.
- **Dependency Analysis**: Modeling the relationships between definitions, postulates, and propositions as a directed acyclic graph (DAG).
- **Symbolic Integration**: Preparing the foundations for symbolic modeling in `geometor.model`.

Key Features
------------

- **G-Index Generation**: Automating the creation of a cross-referenced index of all elements.
- **Dependency Graphs**: Visualizing the proof chain for every proposition using Graphviz.
- **Clean RST Injection**: Generating optimized documentation with clean enunciation blockquotes and integrated diagrams.
- **Intersphinx Integration**: Seamlessly linking back to the canonical Euclid source.

Usage
-----

To generate the G-Index:

.. code-block:: bash

    python -m geometor.elements

Resources
---------

- **Source Code**: https://github.com/geometor/elements
- **Issues**: https://github.com/geometor/elements/issues

Related Projects
----------------

- `GEOMETOR Euclid <https://github.com/geometor/euclid>`_: Semantic discovery and source text.
- `GEOMETOR Model <https://github.com/geometor/model>`_: The symbolic engine.
