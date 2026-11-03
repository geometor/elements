:order: 534
:number: 534
:canonical_id: G.534
:original_id: XI.def.9
:title: G.534 similar solid figures
:volume: III
:book: XI
:type: def
:categories: definition, solid-geometry
:category: definition, solid-geometry
:tags: book-xi, similar-solid-figures, surface, similar, plane
:dependencies: G.533
:excerpt: Similar solid figures are thosecontained by similar planes equal in multitude.

.. _G.534:
.. _XI.def.9:

G.534 similar solid figures
===========================

.. rubric:: `XI.def.9 <https://geometor.github.io/euclid/heath/volume_III/book_xi/definitions/#xi-def-9>`_

.. enunciation::

   :term:`**Similar solid figures** <similar-solid-figures>` are those:term:`contained by similar planes <G.533>` equal in multitude.

.. signature:: def

   | :fn:`similar_solid_figures_def <G.534>`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.def.6): The extremities of a surface are lines or arcs.", fillcolor="#224422", URL="../G.6/index.html", target="_top"];
     "G.529" [label="G.529", tooltip="G.529 (XI.def.1): Asolid is that which has length, breadth, and depth.", fillcolor="#224422", URL="../G.529/index.html", target="_top"];
     "G.533" [label="G.533", tooltip="G.533 (XI.def.2): Anextremity of asolid is asurface.", fillcolor="#224422", URL="../G.533/index.html", target="_top"];
     "G.534" [label="G.534", tooltip="G.534 (XI.def.9): Similar solid figures are thosecontained by similar planes equal in multitude.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.3" -> "G.2";
     "G.6" -> "G.2";
     "G.6" -> "G.3";
     "G.533" -> "G.3";
     "G.6" -> "G.5";
     "G.533" -> "G.6";
     "G.533" -> "G.529";
     "G.534" -> "G.533";
   }

Required for
------------

:ref:`G.536 <G.536>`, :ref:`G.559 <G.559>`, :ref:`G.570 <G.570>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`

.. toctree::
   :hidden:

   heath
