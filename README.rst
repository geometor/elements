GEOMETOR • elements
===================

.. image:: https://img.shields.io/github/license/geometor/elements.svg
   :target: https://github.com/geometor/elements/blob/main/LICENSE

**Symbolic dependency mapping, formal pseudocode, and G-Index generation (`G.1`–`G.525`) for Euclid's *Elements*.**

Overview
--------

``geometor.elements`` is the symbolic logic and serialization layer of the GEOMETOR Euclid project. While the sister repository `geometor/euclid <https://github.com/geometor/euclid>`_ focuses on semantic discovery and compiling the 3-volume Heath Edition, ``geometor.elements`` codifies the logical structure of the *Elements* into a computable directed acyclic dependency graph—the **G-Index** (`G.1` through `G.525`)—and renders a 3-track **Book Codex** powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_.

Process & Pipeline
------------------

1. **Graph Crawl & Atomic Splitting (``graph.py``)**:
   - Crawls the composed Heath Edition in ``../euclid/docsrc/heath/``, splitting definitions, postulates, common notions, and propositions into discrete anchored nodes in a ``networkx.DiGraph``.
   - Resolves explicit and implicit dependencies, attaches semantic categories and tags (`book-i`–`book-xiii`), copies recalibrated SVG diagrams, and pairs propositions with symbolic ``geometor.model`` construction scripts (`resources/constructions/<id>/g1.py`).

2. **Topological Sequencing & G-Index Assignment (``g_index.py``)**:
   - Sequences all 525 foundational rules and propositions into a strict dependency order (`G.1`–`G.525`) where every element depends only on preceding ``G.<k>`` elements, while tracking unreferenced definitions in ``docsrc/elements2/orphans.rst``.
   - Generates per-element Graphviz dependency trees showing immediate ancestors and descendants.

3. **Formal Pseudocode & Composable Functions (``pseudocode.py``)**:
   - Distills Heath's prose enunciations into concise symbolic fact statements (`resources/enunciations.json`).
   - Generates formal ``.. signature::`` blocks (`theorem`, `problem`, or `rule`) declaring ``given``, ``construct``, and ``prove`` parameters with `:sig:` type annotations (`segment`, `point`, `line`, `circle`, `angle`, `triangle`, `polygon`, `magnitude`, `number`, `ratio`).
   - Converts Euclidean constructions and proofs into structured ``.. step:: <kind>`` sequences (`given`, `construct` with composable ``:fn:`` calls such as `segment`, `circle`, `equilateral_triangle`, `bisect_angle`, `bisect_segment`, `perpendicular_at`, `perpendicular_from`, `copy_angle`, `parallel_line`, `square`, symbolic `intersect` with ``∩``, `assert`, and `conclude`) paired with semantic rule justifications (`∵ equal_things (G.1)`).

4. **3-Track Book Codex Generation (`docsrc/elements2/G.<n>/`)**:
   - **Pseudocode Track (`index.rst`)**: Formal ``.. enunciation::``, interactive SVG figure with step-by-step playback controls, ``.. signature::`` block, and symbolic ``.. step::`` sequence with explicit GEOMETOR indications (``/ A B /``, ``[ A B ]``, ``( A B C )``, ``< B A C )``, ``< A B C >``, ``A``) and ``:eq:`` equality tick-mark assertions.
   - **Code Track (`code.rst`)**: Callable ``.. function::`` header, executable ``geometor.model`` Python construction script (`g1.py`), and interactive dependency graph.
   - **Heath Track (`heath.rst`)**: Classical Heath prose translation with ``:g:`` symbolic indications and ``G.<k>`` justification pills, deep-linked via ``intersphinx`` to `geometor/euclid <https://geometor.github.io/euclid>`_.

Coordination with ``publish``
-----------------------------

- Uses ``:layout: book`` in `photon-platform/publish <https://github.com/photon-platform/publish>`_ to provide instant tab switching between **Pseudocode**, **Code**, and **Heath** tracks across all 525 G-Index elements.
- Leverages ``geometor_interactive.js`` so stepping through ``.. step::`` directives in the Pseudocode track progressively reveals the corresponding geometric primitives in the SVG diagram and highlights equal segments/angles with center tick marks.
- Exports `resources/enunciations.json` and `docs/objects.inv` for cross-repository tooltips and intersphinx references.

Usage
-----

.. code-block:: bash

   # Generate the complete G-Index (G.1..G.525) into docsrc/elements2/
   python3 -m geometor.elements

   # Build and serve the 3-track Book Codex locally
   publish test

Resources & Related Projects
----------------------------

- **Live Edition**: https://geometor.github.io/elements
- **Source Code**: https://github.com/geometor/elements
- `GEOMETOR • euclid <https://github.com/geometor/euclid>`_: 3-volume Heath Edition source text and commentary.
- `GEOMETOR • model <https://github.com/geometor/model>`_: Symbolic geometric construction engine.
- `PHOTON • publish <https://github.com/photon-platform/publish>`_: Sphinx Book Codex publishing engine and theme.
