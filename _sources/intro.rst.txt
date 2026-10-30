**Symbolic dependency mapping, formal pseudocode, and G-Index generation (`G.1`–`G.525`) for Euclid's *Elements*.**

The **G-Index** is a symbolic and logical codification of Euclid's *Elements*. While the sister repository `GEOMETOR • euclid <https://geometor.github.io/euclid>`_ compiles the 3-volume Heath Edition and critical commentary, ``geometor.elements`` sequences the definitions, postulates, common notions, and propositions into a computable directed acyclic dependency graph (`G.1` through `G.525`) rendered as a 3-track **Book Codex** via ``photon-platform/publish``.

----

Codex Architecture
------------------

* :doc:`Elements 2.0 — The G-Index (G.1–G.525) <elements2/index>` — Every element is presented in three synchronized companion tracks:

  1. **Pseudocode Track (`index.rst`)**: Concise ``.. enunciation::``, interactive SVG figure with step-by-step construction playback, formal ``.. signature::`` block (`given` / `construct` / `prove`), and ``.. step::`` sequences using composable ``:fn:`` calls, explicit GEOMETOR symbolic indications (``/ A B /``, ``[ A B ]``, ``( A B C )``, ``< B A C )``, ``< A B C >``, ``A``), ``:eq:`` equality tick-mark assertions, and semantic rule justifications (``∵ equal_things (G.1)``).
  2. **Code Track (`code.rst`)**: Callable ``.. function::`` definition, executable ``geometor.model`` construction script (`g1.py`), and interactive Graphviz dependency graph.
  3. **Heath Track (`heath.rst`)**: Classical Heath translation rewritten with GEOMETOR symbolic indications and ``G.<k>`` justification pills, linked via ``intersphinx`` to the full Heath Edition in `GEOMETOR • euclid <https://geometor.github.io/euclid>`_.

* :doc:`Design & Symbolic Grammar <design>` — Specification of GEOMETOR symbolic indications, step kinds, signatures, and composable geometric functions.
* :doc:`Book Notes <book-notes>` — Structural overview and dependency notes across Books I–XIII.
