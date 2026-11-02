:order: 166
:number: 166
:canonical_id: G.166
:original_id: IV.14
:title: G.166 pentagon equilateral equiangular
:volume: II
:book: IV
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles, polygons
:category: problem, construction, plane-geometry, circles, polygons
:tags: book-iv, point, segment, circle, angle, polygon, equilateral-triangle, plane-angle, straight-line, line, centre, equilateral, circumscribed, pentagon, equality
:dependencies: G.10, G.12, G.14, G.26, G.156
:excerpt: About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.

.. _G.166:
.. _IV.14:

G.166 pentagon equilateral equiangular
======================================

.. rubric:: `IV.14 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/14/>`_

.. enunciation::

   About a given pentagon, which is :term:`equilateral <G.12>` and equiangular, to circumscribe a :term:`circle <G.10>`.

.. signature:: problem

   | :fn:`pentagon_equilateral_equiangular_iv_14 <G.166>`\ (:g:`< A B C D E > <g1:< A B C D E >>`)
   | **given** :g:`< A B C D E > <g1:< A B C D E >>` be the given pentagon, which is equilateral and equiangular
   | **construct** circumscribe a circle about the pentagon :g:`< A B C D E > <g1:< A B C D E >>`

.. picture:: g1.svg
   :alt: Book IV Proposition 14: Circle circumscribed about regular pentagon ABCDE

.. step:: given

   :g:`< A B C D E > <g1:< A B C D E >>` be the given pentagon, which is equilateral and equiangular

.. step:: construct

   Let :g:`< B C D ) <g1:< B C D )>`, :g:`< C D E ) <g1:< C D E )>` be bisected by :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />` respectively, and from :g:`F <g1:F>`, at which the :term:`segments <G.4>` meet, let :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` be joined to :g:`B <g1:B>`, :g:`A <g1:A>`, :g:`E <g1:E>`.

.. step:: assert

   Then in manner similar to the preceding it can be proved that :g:`< C B A ) <g1:< C B A )>`, :g:`< B A E ) <g1:< B A E )>`, :g:`< A E D ) <g1:< A E D )>` have also been bisected by :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` respectively.

.. step:: assert

   Since :g:`< B C D ) <g1:< B C D )>` is :eq:`equal <g1:< B C D ) = g1:< C D E )>` to :g:`< C D E ) <g1:< C D E )>`, and :g:`< F C D ) <g1:< F C D )>` is half of :g:`< B C D ) <g1:< B C D )>`, and :g:`< C D F ) <g1:< C D F )>` half of :g:`< C D E ) <g1:< C D E )>` → therefore :g:`< F C D ) <g1:< F C D )>` is also :eq:`equal <g1:< F C D ) = g1:< C D F )>` to :g:`< C D F ) <g1:< C D F )>`,

.. step:: assert ∵ equal_angles_isosceles <G.26>

   So that the side :g:`/ F C / <g1:/ F C />` is also :eq:`equal <g1:/ F C / = g1:/ F D />` to the side :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   Similarly it can be proved that each of :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` is also :eq:`equal <g1:/ F B / = g1:/ F A / = g1:/ F E / = g1:/ F C / = g1:/ F D />` to each of :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />`

.. step:: assert

   Therefore the five segments :g:`/ F A / <g1:/ F A />`, :g:`/ F B / <g1:/ F B />`, :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />`, :g:`/ F E / <g1:/ F E />` are :eq:`equal <g1:/ F A / = g1:/ F B / = g1:/ F C / = g1:/ F D / = g1:/ F E />` to one another.

.. step:: assert

   Therefore the circle described with :term:`center <G.14>` :g:`F <g1:F>` and distance one of :g:`/ F A / <g1:/ F A />`, :g:`/ F B / <g1:/ F B />`, :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />`, :g:`/ F E / <g1:/ F E />` will pass also through the remaining :term:`points <G.1>`, and will have been circumscribed.

.. step:: construct

   Let it be circumscribed, and let it be :g:`( A B C D E ) <g1:( A B C D E )>`.

.. step:: conclude

   :term:`circumscribe a circle about <G.156>` the pentagon :g:`< A B C D E > <g1:< A B C D E >>`

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
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.14/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", fillcolor="#222244", URL="../G.26/index.html", target="_top"];
     "G.156" [label="G.156", tooltip="G.156 (IV.def.6): Acircle is said to becircumscribed about a figure when the arc of the circle passes through eachangle of thefigure about which it is circumscribed.", fillcolor="#224422", URL="../G.156/index.html", target="_top"];
     "G.166" [label="G.166", tooltip="G.166 (IV.14): About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.14" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.22" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.26" -> "G.9";
     "G.156" -> "G.9";
     "G.14" -> "G.10";
     "G.156" -> "G.10";
     "G.166" -> "G.10";
     "G.12" -> "G.11";
     "G.26" -> "G.11";
     "G.166" -> "G.12";
     "G.166" -> "G.14";
     "G.26" -> "G.22";
     "G.156" -> "G.22";
     "G.166" -> "G.26";
     "G.166" -> "G.156";
   }

Required for
------------

:ref:`G.586 <G.586>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
