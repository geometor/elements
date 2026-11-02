:canonical_id: G.567
:original_id: XI.def.22
:title: G.567 axis of a cylinder
:volume: III
:book: XI
:type: def

G.567 axis of a cylinder — Heath
================================

.. rubric:: `XI.def.22 <https://geometor.github.io/euclid/heath/volume_III/book_xi/definitions/#xi-def-22>`_

.. enunciation::

   The :term:`**axis of the cylinder** <axis-of-cylinder>` is the :term:`straight line <G.4>` which remains fixed and about which the parallelogram is turned.

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
     "G.567" [label="G.567", tooltip="G.567 (XI.def.22): Theaxis of the cylinder is thesegment which remains fixed and about which the parallelogram is turned.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.4" -> "G.3";
     "G.567" -> "G.4";
   }

Required for
------------

:ref:`G.569 <G.569>`, :ref:`G.570 <G.570>`
