:order: 553
:number: 553
:canonical_id: G.553
:original_id: XI.def.12
:title: G.553 pyramid
:volume: III
:book: XI
:type: def
:categories: definition, solid-geometry
:category: definition, solid-geometry
:tags: book-xi, pyramid, solid, plane-surface, point, plane
:dependencies: G.1, G.7, G.529
:excerpt: Apyramid is asolid figure, contained byplanes, which is constructed from one plane to onepoint.

.. _G.553:
.. _XI.def.12:

G.553 pyramid
=============

.. rubric:: `XI.def.12 <https://geometor.github.io/euclid/heath/volume_III/book_xi/definitions/#xi-def-12>`_

.. enunciation::

   A:term:`**pyramid** <pyramid>` is a:term:`solid figure <G.529>`, contained by:term:`planes <G.7>`, which is constructed from one plane to one:term:`point <G.1>`.

.. signature:: def

   | :fn:`pyramid_solid_figure_def <G.553>`

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
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.529" [label="G.529", tooltip="G.529 (XI.def.1): Asolid is that which has length, breadth, and depth.", fillcolor="#224422", URL="../G.529/index.html", target="_top"];
     "G.553" [label="G.553", tooltip="G.553 (XI.def.12): Apyramid is asolid figure, contained byplanes, which is constructed from one plane to onepoint.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.553" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.7" -> "G.5";
     "G.553" -> "G.7";
     "G.553" -> "G.529";
   }

Required for
------------

:ref:`G.554 <G.554>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.560 <G.560>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.592 <G.592>`, :ref:`G.595 <G.595>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   heath
