:order: 132
:number: 132
:canonical_id: G.132
:original_id: III.def.9
:title: G.132 angle standing on an arc
:volume: II
:book: III
:type: def
:categories: definition, plane-geometry, circles
:category: definition, plane-geometry, circles
:tags: book-iii, straight-line, plane-angle, stand-upon-circumference, arc, plane
:dependencies: G.4, G.22
:excerpt: And, when thesegments containing theangle cut off a arc, the angle is said tostand upon that arc.

.. _G.132:
.. _III.def.9:

G.132 angle standing on an arc
==============================

.. rubric:: `III.def.9 <https://geometor.github.io/euclid/heath/volume_II/book_iii/definitions/#iii-def-9>`_

.. enunciation::

   And, when the:term:`segments <G.4>` containing the:term:`angle <G.22>` cut off a arc, the angle is said to:term:`**stand upon** <stand-upon-arc>` that arc.

.. signature:: def

   | :fn:`segments_containing_angle_def <G.132>`

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
     "G.132" [label="G.132", tooltip="G.132 (III.def.9): And, when thesegments containing theangle cut off a arc, the angle is said tostand upon that arc.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.22" -> "G.4";
     "G.132" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.132" -> "G.22";
   }

Required for
------------

:ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.135 <G.135>`, :ref:`G.136 <G.136>`, :ref:`G.137 <G.137>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.167 <G.167>`, :ref:`G.168 <G.168>`, :ref:`G.246 <G.246>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.590 <G.590>`, :ref:`G.592 <G.592>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   heath
