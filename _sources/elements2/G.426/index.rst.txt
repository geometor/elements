:order: 426
:number: 426
:canonical_id: G.426
:original_id: X.def.ii.3
:title: G.426 third binomial
:volume: III
:book: X
:type: def
:categories: definition, incommensurables, magnitudes
:category: definition, incommensurables, magnitudes
:tags: book-x, commensurable, rational, straight-line, third-binomial, binomial
:dependencies: G.4, G.372, G.391
:excerpt: And if neither of the terms becommensurable in length with therationalsegment set out, let the whole be called athird binomial.

.. _G.426:
.. _X.def.ii.3:

G.426 third binomial
====================

.. rubric:: `X.def.ii.3 <https://geometor.github.io/euclid/heath/volume_III/book_x/definitions_ii/#x-def-ii-3>`_

.. enunciation::

   And if neither of the terms be:term:`commensurable <G.372>` in length with the:term:`rational <G.392>`:term:`segment <G.4>` set out, let the whole be called a:term:`**third binomial** <third-binomial>`.

.. signature:: def

   | :fn:`terms_commensurable_length_def <G.426>`

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
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.372" [label="G.372", tooltip="G.372 (X.def.1): Those magnitudes are said to becommensurable which aremeasured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.372/index.html", target="_top"];
     "G.391" [label="G.391", tooltip="G.391 (X.def.3): With these hypotheses, it is proved that there existsegments infinite in multitude which arecommensurable and incommensurable respectively, some in length only, and others in squar...", fillcolor="#224422", URL="../G.391/index.html", target="_top"];
     "G.426" [label="G.426", tooltip="G.426 (X.def.ii.3): And if neither of the terms becommensurable in length with therationalsegment set out, let the whole be called athird binomial.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.4" -> "G.3";
     "G.391" -> "G.4";
     "G.426" -> "G.4";
     "G.372" -> "G.169";
     "G.391" -> "G.372";
     "G.426" -> "G.372";
     "G.426" -> "G.391";
   }

Required for
------------

:ref:`G.427 <G.427>`, :ref:`G.436 <G.436>`, :ref:`G.442 <G.442>`, :ref:`G.446 <G.446>`, :ref:`G.452 <G.452>`

.. toctree::
   :hidden:

   heath
