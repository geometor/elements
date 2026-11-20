:site_title: Constructive Elements

.. container:: author-overline

   semantic digital archive • mathematical catalog

=====================
Constructive Elements
=====================

.. image:: _static/medallion.svg
   :alt: Constructive Elements Medallion
   :class: repo-medallion-hero

**Elements 2.0** reorganizes all thirteen books of Euclid's *Elements* into the **G-Index** (``G.1``–``G.601``)—a computable directed acyclic graph (DAG) where every definition, postulate, common notion, and proposition links explicitly to its logical ancestors. Each node pairs tightened mathematical pseudocode, step-by-step ``∵ G.<k>`` proof justifications, interactive vector diagrams, construction videos, and executable SymPy Python scripts alongside Sir Thomas Little Heath's classic English translation.

Catalog & Interactive Reader
----------------------------

.. container:: home-book-hero

   .. container:: home-book-thumb

      .. image:: elements2/G.17/g1.svg
         :alt: G.17 (Euclid I.1) Equilateral Triangle Construction Diagram
         :target: elements2/index.html

   .. container:: home-book-body

      .. rubric:: Constructive Canon · Books I–XIII · G.1–G.601

      **Elements 2.0 (The Constructive G-Index)** — Browse all 601 Euclidean axioms and propositions ordered by constructive dependency, from the first point definition (``G.1``) and equilateral triangle construction (``G.17`` / I.1) through Book XIII's Platonic solids, complete with ancestor graphs and interactive ``.euclid-graphic`` diagrams.

      .. container:: home-actions

         * :doc:`Explore the G-Index → <elements2/index>`
         * :doc:`Start at G.17 (Euclid I.1) → <elements2/G.17/index>`
         * :doc:`Begin at G.1 (Point) → <elements2/G.1/index>`

.. container:: home-book-hero

   .. container:: home-book-thumb

      .. image:: elements2/G.79/g1.svg
         :alt: G.79 (Euclid I.47) Pythagorean Theorem Diagram
         :target: usage/index.html

   .. container:: home-book-body

      .. rubric:: Four-Track Reader & Python Construction Engine

      **Synchronized Tracks & SymPy Modeling** — Every proposition offers four synchronized views—*Pseudocode*, *Video*, *Code*, and *Heath*—backed by the ``geometor.elements`` Python engine, exact ``geometor.model`` construction scripts, and Graphviz dependency subgraphs.

      .. container:: home-actions

         * :doc:`Reader's & Developer Guide → <usage/index>`
         * :doc:`Inspect G.79 (Pythagorean Theorem) → <elements2/G.79/index>`
         * :doc:`Python API Reference → <modules/index>`

Key Features
------------

.. container:: home-feature-grid

   .. container:: home-feature-card

      **Computable Dependency DAG**

      Trace every theorem backwards through its exact prerequisite definitions, postulates, and lemmas via ``∵ G.<k>`` links and per-proposition dependency graphs.

   .. container:: home-feature-card

      **Interactive ``:g:`` & ``:eq:`` Figures**

      Hover or click points, segments, circles, and triangles in the prose to highlight them directly on calibrated dark-and-light adaptive SVG plates.

   .. container:: home-feature-card

      **Executable SymPy Constructions**

      Run standalone ``geometor.model`` scripts for constructive propositions with zero floating-point approximation.

Reference & Project
-------------------

.. container:: home-columns

   .. container:: home-col

      .. rubric:: Scholarly Apparatus

      * :doc:`People <people/index>` — Profiles of Euclid, Sir Thomas Heath, Johan Ludvig Heiberg, Proclus, Pappus, and ancient commentators
      * :doc:`Bibliography <bibliography>` — Critical Greek editions, manuscript witnesses, and historical translations
      * :doc:`Orphaned Axioms <elements2/orphans>` — Classical definitions, postulates, and common notions outside the main proof DAG

   .. container:: home-col

      .. rubric:: About This Project

      * :doc:`About This Edition <about/index>` — Architectural overview of the G-Index and its links to ``geometor.euclid`` and ``geometor.divine``
      * :doc:`Using This Edition <usage/index>` — Guide to the four reading tracks, interactive highlighting, CLI tools, and Python API
      * :doc:`Research Log <log/index>` & :doc:`Python Modules <modules/index>` — Compilation notes and package reference

.. toctree::
   :maxdepth: 2
   :hidden:

   about/index
   elements2/index
   people/index
   bibliography
   usage/index
   log/index
   modules/index
