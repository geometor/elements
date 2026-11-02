:order: 596
:number: 596
:canonical_id: G.596
:original_id: XI.def.27
:title: G.596 icosahedron
:volume: III
:book: XI
:type: def
:categories: definition, solid-geometry
:category: definition, solid-geometry
:tags: book-xi, icosahedron, solid, equilateral-triangle, equilateral
:dependencies: G.12, G.529
:excerpt: Anicosahedron is asolid figure contained by twenty equal andequilateral triangles.

.. _G.596:
.. _XI.def.27:

G.596 icosahedron
=================

.. rubric:: `XI.def.27 <https://geometor.github.io/euclid/heath/volume_III/book_xi/definitions/#xi-def-27>`_

.. enunciation::

   An:term:`**icosahedron** <icosahedron>` is a:term:`solid figure <G.529>` contained by twenty equal and:term:`equilateral triangles <G.12>`.

.. signature:: def

   | :fn:`icosahedron_solid_figure_def <G.596>`

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
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.529" [label="G.529", tooltip="G.529 (XI.def.1): Asolid is that which has length, breadth, and depth.", fillcolor="#224422", URL="../G.529/index.html", target="_top"];
     "G.596" [label="G.596", tooltip="G.596 (XI.def.27): Anicosahedron is asolid figure contained by twenty equal andequilateral triangles.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.4" -> "G.3";
     "G.11" -> "G.4";
     "G.12" -> "G.11";
     "G.596" -> "G.12";
     "G.596" -> "G.529";
   }

Required for
------------

:ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   heath
