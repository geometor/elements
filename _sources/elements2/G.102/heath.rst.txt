:canonical_id: G.102
:original_id: III.5
:title: G.102 intersecting circles have distinct centers
:volume: II
:book: III
:type: prop

G.102 intersecting circles have distinct centers — Heath
========================================================

.. rubric:: `III.5 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/05/>`_

.. enunciation::

   If two :term:`circles <G.10>` cut one another, they will not have the same :term:`centre <G.11>`.

For let the circles :g:`( A B C ) <g1:( A B C )>`, :g:`( C D G ) <g1:( C D G )>` cut one another at the :term:`points <G.1>` :g:`B <g1:B>`, :g:`C <g1:C>`;

I say that they will not have the same centre.

.. picture:: g1.svg
   :alt: Proposition 5 Diagram

For, if possible, let it be :g:`E <g1:E>`; let :g:`/ E C / <g1:/ E C />` be joined, and let :g:`/ E F G / <g1:/ E F G />` be drawn through at random.

Then, since the point :g:`E <g1:E>` is the centre of the circle :g:`( A B C ) <g1:( A B C )>`,

.. assertion:: [G.10] <G.10>

   :g:`/ E C / <g1:/ E C />` is :eq:`equal <g1:/ E C / = g1:/ E F />` to :g:`/ E F / <g1:/ E F />`.

Again, since the point :g:`E <g1:E>` is the centre of the circle :g:`( C D G ) <g1:( C D G )>`,

.. assertion::

   :g:`/ E C / <g1:/ E C />` is :eq:`equal <g1:/ E C / = g1:/ E G />` to :g:`/ E G / <g1:/ E G />`.

But :g:`/ E C / <g1:/ E C />` was proved :eq:`equal <g1:/ E C / = g1:/ E F />` to :g:`/ E F / <g1:/ E F />` also; therefore :g:`/ E F / <g1:/ E F />` is also :eq:`equal <g1:/ E F / = g1:/ E G />` to :g:`/ E G / <g1:/ E G />`, the less to the greater: which is impossible.

.. assertion::

   Therefore the point :g:`E <g1:E>` is not the centre of the circles :g:`( A B C ) <g1:( A B C )>`, :g:`( C D G ) <g1:( C D G )>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

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
     "G.14" [label="G.14", tooltip="G.14 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.14/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.16/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.102" [label="G.102", tooltip="G.102 (III.5): Two intersecting circles do not have the same center.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.14" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.11" -> "G.10";
     "G.102" -> "G.10";
     "G.102" -> "G.11";
     "G.102" -> "G.14";
     "G.102" -> "G.16";
     "G.102" -> "G.26";
   }

Required for
------------

:ref:`G.108 <G.108>`, :ref:`G.129 <G.129>`, :ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.135 <G.135>`, :ref:`G.136 <G.136>`, :ref:`G.137 <G.137>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.167 <G.167>`, :ref:`G.168 <G.168>`, :ref:`G.246 <G.246>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.590 <G.590>`, :ref:`G.592 <G.592>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`
