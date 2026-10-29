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

- **G-Index Generation**: Automating the creation of a cross-referenced dependency index (`G.1`, `G.2`...) from the composed `geometor.euclid` Heath Edition.
- **GEOMETOR Symbolic Indications**: Transforming geometric references into explicit symbolic primitives (`/ A B /`, `< A B C >`, `< B A C )`, `( B C D )`, `[ A B ]`, `A`).
- **Interactive SVG & Dependency Graphs**: Embedding interactive SVG diagrams and Graphviz dependency trees for every element.
- **Taxonomy & Apparatus**: Extracting categories, semantic tags, and scholarly apparatus (`:term:`, `:person:`, `:cite:`).

Usage
-----

To generate the G-Index (optionally filtering by book):

.. code-block:: bash

    python3 -m geometor.elements --books I

Resources
---------

- **Source Code**: https://github.com/geometor/elements
- **Issues**: https://github.com/geometor/elements/issues

Related Projects
----------------

- `GEOMETOR Euclid <https://github.com/geometor/euclid>`_: Semantic discovery and source text.
- `GEOMETOR Model <https://github.com/geometor/model>`_: The symbolic engine.
