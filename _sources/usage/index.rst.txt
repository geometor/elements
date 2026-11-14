:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Reader's Guide & Developer Documentation for Elements 2.0

``geometor.elements`` re-architects Euclid's *Elements* into a computable directed acyclic graph (DAG) of constructive dependencies (the **G-Index**, `G.1`–`G.601`). This guide outlines the interactive reading features of the digital edition and details command-line compilation and Python scripting.

Reader's Guide
==============

1. Synchronized Reading Tracks
------------------------------

Every G-Index node (`G.1` through `G.601`) is presented across four synchronized companion tracks accessible from the track switcher in the codex header bar:

* **Pseudocode (`index.rst`)**: Tightened, fact-oriented mathematical enunciation (``.. enunciation::``), formal input/output signature block (``given`` / ``construct`` / ``prove``), interactive construction figure, and formal step sequence (``.. step::``) with composable geometric operations (``:fn:``) and symbolic indication roles.
* **Video (`video.rst`)**: High-definition animated construction video synchronized with Heath's traditional proof steps and geometric figures.
* **Code (`code.rst`)**: Standalone, executable Python construction scripts using ``geometor.model``, complete with interactive Graphviz dependency graphs and reproducible algebraic coordinates.
* **Heath (`heath.rst`)**: The classical English translation and critical commentary of Sir Thomas Little Heath, enriched with GEOMETOR symbolic notation and direct hyperlinks to foundational definitions and prior propositions.

2. Interactive Diagrams & Deductive Links
-----------------------------------------

* **Geometric Elements (``:g:``)**: Hovering or clicking a geometric label—such as point :g:`A <g1:A>`, line :g:`[ A B ] <g1:[ A B ]>`, segment :g:`/ A B / <g1:/ A B />`, circle :g:`( A B ) <g1:( B C D )>`, or triangle :g:`< A B C > <g1:< A B C >>`—highlights the corresponding element in the vector diagram.
* **Equality Assertions (``:eq:``)**: Explicit tick-mark assertions visually correlate congruent segments and equal angles across figures.
* **Justification Links (``∵ G.<k>``)**: Every deductive step links directly to its ancestor prerequisite in the G-Index dependency chain, enabling instant navigation backwards through the logical derivation.

3. Archival Cross-References & Heath Milestones
-----------------------------------------------

Propositions and definitions maintain bi-directional links to the historical three-volume Heath critical edition hosted in `GEOMETOR • euclid <https://geometor.github.io/euclid>`_, allowing readers to cross-examine Greek textual apparatus, variant manuscript readings (such as *Codex Vaticanus Graecus 190*), and ancient scholia.

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

The global documentation search indexes all 600+ G-nodes, definitions, postulates, and scholarly notes. Selecting any search result loads the page with search queries highlighted in-context via URL parameters (``?highlight=``), making it effortless to pinpoint specific constructions and mathematical lemmas.

5. Taxonomy, Document Types & Collection Views
----------------------------------------------

The G-Index collection page provides responsive viewing modes and taxonomy facets:

* **View Toggles**: Switch effortlessly between **Cards** (visual grid with thumbnails and excerpts), **Banners** (wide summary cards with badges), and **List** (compact index table) layouts.
* **Facets**: Filter elements by mathematical type (propositions, definitions, postulates, common notions, or orphans), Book (Books I through XIII), and construction tags.

6. People, Bibliography & Glossary Tooltips
-------------------------------------------

* **Person Badges (``:person:``)**: Hovering over cited geometers, commentators, and editors reveals biographical cards summarizing their eras, major works, and historical roles.
* **Citations (``:cite:``)**: Direct cross-references to the critical apparatus and primary literature.
* **Light / Dark Themes**: Toggle between light and dark display modes tailored for daytime study or night-time coding.

Developer & CLI Guide
=====================

Command-Line Interface
----------------------

``geometor.elements`` provides a command-line tool to crawl the composed Heath Edition, build the dependency graph, and compile the multi-track G-Index Book Codex:

.. code-block:: bash

   # Generate the G-Index Book Codex for Book I (default)
   python3 -m geometor.elements --books 1 --output-dir docsrc/elements2

   # Generate across multiple books (e.g. Books I and II)
   python3 -m geometor.elements --books 1 2 --output-dir docsrc/elements2

   # Build the Sphinx HTML documentation site
   publish build

Python API & Graph Traversal
----------------------------

You can traverse and analyze Euclid's dependency structure programmatically using NetworkX:

.. code-block:: python

   from geometor.elements.graph import build_graph

   # Build directed dependency graph for Book I
   G, books_data = build_graph(books=["I"])

   # Query prerequisites for Proposition I.1
   prereqs = list(G.predecessors("I.1"))
   print("Prerequisites for I.1:", prereqs)

   # Query propositions depending on Postulate 1
   dependents = list(G.successors("I.post.1"))
   print("Elements depending on Postulate 1:", len(dependents))
