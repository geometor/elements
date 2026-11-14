**Symbolic dependency mapping, formal pseudocode, and G-Index generation (`G.1`–`G.601`) for Euclid's *Elements*.**

The **G-Index** is a symbolic and logical codification of Euclid's *Elements*. While the sister repository `GEOMETOR • euclid <https://geometor.github.io/euclid>`_ compiles the three-volume Heath Edition and critical apparatus, ``geometor.elements`` sequences the definitions, postulates, common notions, and propositions into a computable directed acyclic dependency graph (`G.1` through `G.601`) rendered as an interactive **Book Codex** via ``photon-platform/publish``.

----

Core Edition Gateways
---------------------

* :doc:`Elements 2.0 — The G-Index (G.1–G.601) <elements2/index>`: The complete computational dependency sequence across all thirteen books of the *Elements*, featuring synchronized reading tracks:
  
  1. **Pseudocode Track (`index.rst`)**: Tightened, fact-oriented enunciations, formal ``given`` / ``construct`` / ``prove`` signatures, interactive vector diagrams, and step-by-step deductive chains with ``∵ G.<k>`` justification links.
  2. **Video Track (`video.rst`)**: High-definition construction playback demonstrating geometric derivations.
  3. **Code Track (`code.rst`)**: Callable Python functions, standalone reproducible construction scripts using ``geometor.model``, and dependency DAG diagrams.
  4. **Heath Track (`heath.rst`)**: Sir Thomas Little Heath's classical English translation enriched with GEOMETOR symbolic indications and cross-links to `GEOMETOR • euclid <https://geometor.github.io/euclid>`_.

* :doc:`People <persons>`: Biographical register documenting primary authors, translators, and ancient/modern commentators, including :person:`Euclid of Alexandria <euclid>`, :person:`Sir Thomas Little Heath <heath>`, :person:`Proclus Diadochus <proclus>`, :person:`Pappus of Alexandria <pappus>`, :person:`Johan Ludvig Heiberg <heiberg>`, and :person:`phi ARCHITECT <phi-architect>`.
* :doc:`Bibliography <bibliography>`: Catalogue of Greek critical editions (Heiberg's Teubner text), English editions (Heath, Simson), archival manuscript witnesses (*Codex Vaticanus Graecus 190*, *Codex Bodleianus D'Orville 301*), and cited classical works.
* :doc:`Using This Edition (Reader's Guide) <usage/index>`: Detailed walkthrough of track switching, interactive diagram element highlighting, search with term highlighting, and Python API graph queries.
* :doc:`Design & Symbolic Grammar <design>`: Specification of GEOMETOR symbolic indications (segments, lines, circles, angles, polygons), step contracts, and composable functions.
* :doc:`Book Notes <book-notes>`: Structural overview and dependency notes across Books I–XIII.
