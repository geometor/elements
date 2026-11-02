:order: 422
:number: 422
:canonical_id: G.422
:original_id: X.def.ii.1
:title: G.422 first binomial
:volume: III
:book: X
:type: def
:categories: definition, incommensurables, magnitudes
:category: definition, incommensurables, magnitudes
:tags: book-x, rational, straight-line, square, commensurable, first-binomial-straight-line, binomial
:dependencies: G.4, G.63, G.372, G.391
:excerpt: Given arationalsegment and a binomial, divided into its terms, such that thesquare on the greater term is greater than the square on the lesser by the square on a segmentcommensurable in length with the greater, then, if the greater term be commensurable in length with the rational segment set out, let the whole be called afirst binomial segment;

.. _G.422:
.. _X.def.ii.1:

G.422 first binomial
====================

.. rubric:: `X.def.ii.1 <https://geometor.github.io/euclid/heath/volume_III/book_x/definitions_ii/#x-def-ii-1>`_

.. enunciation::

   Given a:term:`rational <G.392>`:term:`segment <G.4>` and a binomial, divided into its terms, such that the:term:`square <G.63>` on the greater term is greater than the square on the lesser by the square on a segment:term:`commensurable <G.372>` in length with the greater, then, if the greater term be commensurable in length with the :term:`rational <G.391>` segment set out, let the whole be called a:term:`**first binomial segment** <first-binomial-straight-line>`;

.. signature:: def

   | :fn:`rational_segment_binomial_def <G.422>`

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
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.372" [label="G.372", tooltip="G.372 (X.def.1): Those magnitudes are said to becommensurable which aremeasured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.372/index.html", target="_top"];
     "G.391" [label="G.391", tooltip="G.391 (X.def.3): With these hypotheses, it is proved that there existsegments infinite in multitude which arecommensurable and incommensurable respectively, some in length only, and others in squar...", fillcolor="#224422", URL="../G.391/index.html", target="_top"];
     "G.422" [label="G.422", tooltip="G.422 (X.def.ii.1): Given arationalsegment and a binomial, divided into its terms, such that thesquare on the greater term is greater than the square on the lesser by the square on a segmentcommensura...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.11" -> "G.4";
     "G.22" -> "G.4";
     "G.391" -> "G.4";
     "G.422" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.12" -> "G.11";
     "G.63" -> "G.11";
     "G.63" -> "G.12";
     "G.63" -> "G.22";
     "G.422" -> "G.63";
     "G.372" -> "G.169";
     "G.391" -> "G.372";
     "G.422" -> "G.372";
     "G.422" -> "G.391";
   }

Required for
------------

:ref:`G.423 <G.423>`, :ref:`G.434 <G.434>`, :ref:`G.440 <G.440>`, :ref:`G.446 <G.446>`, :ref:`G.451 <G.451>`, :ref:`G.497 <G.497>`

.. toctree::
   :hidden:

   heath
