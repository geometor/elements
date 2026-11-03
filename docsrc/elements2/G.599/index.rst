:order: 599
:number: 599
:canonical_id: G.599
:original_id: XI.def.28
:title: G.599 dodecahedron
:volume: III
:book: XI
:type: def
:categories: definition, solid-geometry
:category: definition, solid-geometry
:tags: book-xi, dodecahedron, solid, equilateral-triangle, equilateral, pentagon
:dependencies: G.13, G.529
:excerpt: Adodecahedron is asolid figure contained by twelve equal,equilateral, and equiangular pentagons.

.. _G.599:
.. _XI.def.28:

G.599 dodecahedron
==================

.. rubric:: `XI.def.28 <https://geometor.github.io/euclid/heath/volume_III/book_xi/definitions/#xi-def-28>`_

.. enunciation::

   A:term:`**dodecahedron** <dodecahedron>` is a:term:`solid figure <G.529>` contained by twelve equal,:term:`equilateral <G.13>`, and equiangular pentagons.

.. signature:: def

   | :fn:`dodecahedron_solid_figure_def <G.599>`

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
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.13/index.html", target="_top"];
     "G.529" [label="G.529", tooltip="G.529 (XI.def.1): Asolid is that which has length, breadth, and depth.", fillcolor="#224422", URL="../G.529/index.html", target="_top"];
     "G.599" [label="G.599", tooltip="G.599 (XI.def.28): Adodecahedron is asolid figure contained by twelve equal,equilateral, and equiangular pentagons.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.4";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.13" -> "G.12";
     "G.599" -> "G.13";
     "G.599" -> "G.529";
   }

Required for
------------

:ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   heath
