:canonical_id: G.503
:original_id: XI.2
:title: G.503 segments cut plane
:volume: III
:book: XI
:type: prop

G.503 segments cut plane — Heath
================================

.. rubric:: `XI.2 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/02/>`_

.. enunciation::

   If two :term:`straight lines <G.4>` cut one another, they are in one :term:`plane <G.7>`, and every :term:`triangle <G.12>` is in one plane.

For let the two straight lines :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` cut one another at the :term:`point <G.1>` :g:`E <g1:E>`; I say that :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are in one plane, and every triangle is in one plane.

.. picture:: g1.svg
   :alt: Book XI, Proposition 2

For let points :g:`F <g1:F>`, :g:`G <g1:G>` be taken at random on :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />`, let :g:`/ C B / <g1:/ C B />`, :g:`/ F G / <g1:/ F G />` be joined, and let :g:`/ F H / <g1:/ F H />`, :g:`/ G K / <g1:/ G K />` be drawn across; I say first that the triangle :g:`< E C B > <g1:< E C B >>` is in one plane.

.. subclause::

   For, if :term:`part of <G.253>` the triangle :g:`< E C B > <g1:< E C B >>`, either :g:`< F H C > <g1:< F H C >>` or :g:`< G B K > <g1:< G B K >>`, is in the plane of reference, and the rest in another,

.. assertion::

   a part also of one of the straight lines :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />` will be in the plane of reference, and a part in another.

.. subclause::

   But, if the part :g:`< F C B G > <g1:< F C B G >>` of the triangle :g:`< E C B > <g1:< E C B >>` be in the plane of reference, and the rest in another,

.. assertion::

   a part also of both the straight lines :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />` will be in the plane of reference and a part in another:

.. assertion:: [G.502] <G.502>

   which was proved absurd.

.. assertion::

   Therefore the triangle :g:`< E C B > <g1:< E C B >>` is in one plane.

.. subclause::

   But, in whatever plane the triangle :g:`< E C B > <g1:< E C B >>` is, in that plane also is each of the straight lines :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />`, and, in whatever plane each of the straight lines :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />` is, in that plane are :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` also. :just:`[G.502] <G.502>`

.. assertion::

   Therefore the straight lines :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are in one plane, and every triangle is in one plane.

.. qed::

   :just:`Q. E. D.`

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
     "G.11" [label="G.11", tooltip="G.11 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.14/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.502" [label="G.502", tooltip="G.502 (XI.1): A part of a segment cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.502/index.html", target="_top"];
     "G.503" [label="G.503", tooltip="G.503 (XI.2): If two segments cut one another, they are in one plane, and every triangle is in one plane.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.11" -> "G.1";
     "G.14" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.12" -> "G.4";
     "G.14" -> "G.4";
     "G.61" -> "G.4";
     "G.502" -> "G.4";
     "G.503" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.502" -> "G.7";
     "G.503" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.61" -> "G.10";
     "G.502" -> "G.10";
     "G.61" -> "G.11";
     "G.502" -> "G.11";
     "G.503" -> "G.12";
     "G.503" -> "G.14";
     "G.502" -> "G.61";
     "G.253" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.502" -> "G.253";
     "G.503" -> "G.253";
     "G.503" -> "G.502";
   }

Required for
------------

:ref:`G.508 <G.508>`, :ref:`G.510 <G.510>`, :ref:`G.511 <G.511>`, :ref:`G.512 <G.512>`, :ref:`G.513 <G.513>`, :ref:`G.514 <G.514>`, :ref:`G.518 <G.518>`, :ref:`G.522 <G.522>`, :ref:`G.528 <G.528>`, :ref:`G.530 <G.530>`, :ref:`G.531 <G.531>`, :ref:`G.532 <G.532>`, :ref:`G.541 <G.541>`, :ref:`G.542 <G.542>`, :ref:`G.543 <G.543>`, :ref:`G.544 <G.544>`, :ref:`G.545 <G.545>`, :ref:`G.546 <G.546>`, :ref:`G.547 <G.547>`, :ref:`G.549 <G.549>`, :ref:`G.550 <G.550>`, :ref:`G.554 <G.554>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.560 <G.560>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.592 <G.592>`, :ref:`G.594 <G.594>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`
