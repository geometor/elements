:order: 115
:number: 115
:canonical_id: G.115
:original_id: III.def.5
:title: G.115 chord at greater distance from the center
:volume: II
:book: III
:type: def
:categories: definition, plane-geometry, circles
:category: definition, plane-geometry, circles
:tags: book-iii, straight-line, greater-distance-from-centre, perpendicular
:dependencies: G.4, G.32
:excerpt: And thatsegment is said to beat a greater distance on which the greaterperpendicular falls.

.. _G.115:
.. _III.def.5:

G.115 chord at greater distance from the center
===============================================

.. rubric:: `III.def.5 <https://geometor.github.io/euclid/heath/volume_II/book_iii/definitions/#iii-def-5>`_

.. enunciation::

   And that:term:`segment <G.4>` is said to be:term:`**at a greater distance** <greater-distance-from-center>` on which the greater:term:`perpendicular <G.32>` falls.

.. signature:: def

   | :fn:`segment_said_greater_def <G.115>`

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
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.115" [label="G.115", tooltip="G.115 (III.def.5): And thatsegment is said to beat a greater distance on which the greaterperpendicular falls.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.22" -> "G.4";
     "G.32" -> "G.4";
     "G.115" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.32" -> "G.22";
     "G.115" -> "G.32";
   }

Required for
------------

:ref:`G.116 <G.116>`

.. toctree::
   :hidden:

   heath
