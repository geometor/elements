:canonical_id: G.152
:original_id: IV.def.1
:title: G.152 polygon inscribed in a polygon
:volume: II
:book: IV
:type: def

G.152 polygon inscribed in a polygon — Heath
============================================

.. rubric:: `IV.def.1 <https://geometor.github.io/euclid/heath/volume_II/book_iv/definitions/#iv-def-1>`_

.. enunciation::

   A :term:`rectilineal figure <G.11>` is said to be :term:`**inscribed in a rectilineal figure** <inscribed-in-rectilineal-figure>` when the respective :term:`angles <G.22>` of the inscribed :term:`figure <G.9>` lie on the respective sides of that in which it is inscribed.

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
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (IV.def.1): Apolygon is said to beinscribed in a polygon when the respectiveangles of the inscribedfigure lie on the respective sides of that in which it is inscribed.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.11" -> "G.4";
     "G.22" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.152" -> "G.9";
     "G.152" -> "G.11";
     "G.152" -> "G.22";
   }

Required for
------------

:ref:`G.154 <G.154>`, :ref:`G.160 <G.160>`
