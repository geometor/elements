:canonical_id: G.117
:original_id: III.def.7
:title: G.117 angle of a circle segment
:volume: II
:book: III
:type: def

G.117 angle of a circle segment — Heath
=======================================

.. rubric:: `III.def.7 <https://geometor.github.io/euclid/heath/volume_II/book_iii/definitions/#iii-def-7>`_

.. enunciation::

   An :term:`**angle of a segment** <angle-of-segment>` is that contained by a :term:`straight line <G.4>` and a circumference of a :term:`circle <G.10>`.

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
     "G.6" [label="G.6", tooltip="G.6 (I.def.6): The extremities of a surface are lines or arcs.", fillcolor="#224422", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.def.15): A circle ( A B ) is a plane figure contained by one arc defined by a center A and a point B establishing its defining radius / A B /, such that all segments / A B /, / A C /, / A D...", fillcolor="#224422", URL="../G.10/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.117" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.117" -> "G.10";
   }

Required for
------------

:ref:`G.118 <G.118>`, :ref:`G.119 <G.119>`, :ref:`G.141 <G.141>`, :ref:`G.145 <G.145>`, :ref:`G.149 <G.149>`, :ref:`G.151 <G.151>`, :ref:`G.154 <G.154>`, :ref:`G.159 <G.159>`, :ref:`G.160 <G.160>`, :ref:`G.162 <G.162>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.165 <G.165>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.574 <G.574>`, :ref:`G.592 <G.592>`, :ref:`G.601 <G.601>`
