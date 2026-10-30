:navigation: header
:order: 20

=====
usage
=====

``geometor.elements`` crawls the composed Heath Edition in ``../euclid/docsrc/heath/``, builds a ``networkx.DiGraph`` of every definition, postulate, common notion, and proposition, and compiles the 3-track **G-Index** Book Codex (``docsrc/elements2/``).

CLI Usage
---------

.. code-block:: bash

   # Generate the G-Index Book Codex for Book I (default)
   python3 -m geometor.elements --books 1 --output-dir docsrc/elements2

   # Generate across multiple books
   python3 -m geometor.elements --books 1 2 --output-dir docsrc/elements2

   # Build the Sphinx HTML documentation
   publish build

Three-Track Architecture
------------------------

Each ``G.<n>`` folder in ``docsrc/elements2/`` contains:

1. **Pseudocode** (``index.rst``): Concise fact enunciation, formal ``.. signature::`` block (``given`` / ``construct`` / ``prove``), ``g1.svg`` figure, and ``.. step::`` deductive sequence with ``∵ G.<k>`` justifications.
2. **Code** (``code.rst``): Standalone ``geometor.model`` construction script (``g1.py``) and Graphviz dependency tree.
3. **Heath** (``heath.rst``): Verbatim historical translation and proposition cross-links from ``geometor.euclid``.
