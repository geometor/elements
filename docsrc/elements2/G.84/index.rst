:order: 84
:number: 84
:canonical_id: G.84
:original_id: III.9
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, equality
:dependencies: G.15, G.18, G.76
:excerpt: If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

.. _G.84:
.. _III.9:

G.84
====

.. rubric:: `III.9 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/09/>`_

.. enunciation::

   If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

.. picture:: g1.svg
   :alt: Diagram for Proposition 9

.. step:: given

   :g:`( A B C ) <g1:( A B C )>` be a circle and :g:`D <g1:D>` a point within it

.. step:: assert

   From :g:`D <g1:D>` let more than two :eq:`equal <g1:/ D A / = g1:/ D B / = g1:/ D C />` straight lines, namely :g:`/ D A / <g1:/ D A />`, :g:`/ D B / <g1:/ D B />`, :g:`/ D C / <g1:/ D C />`, fall on :g:`( A B C ) <g1:( A B C )>`

.. step:: construct

   For let :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` be joined and :eq:`bisected <g1:/ A E / = g1:/ E B /; g1:/ B F / = g1:/ F C />` at :g:`E <g1:E>`, :g:`F <g1:F>`

.. step:: construct

   Let :g:`/ E D / <g1:/ E D />`, :g:`/ F D / <g1:/ F D />` be joined and drawn through to :g:`G <g1:G>`, :g:`K <g1:K>`, :g:`H <g1:H>`, :g:`L <g1:L>`.

.. step:: assert

   Since :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ E B />` to :g:`/ E B / <g1:/ E B />`, and :g:`/ E D / <g1:/ E D />` is common → the two sides :g:`/ A E / <g1:/ A E />`, :g:`/ E D / <g1:/ E D />` are :eq:`equal <g1:/ A E / = g1:/ B E />` to the two sides :g:`/ B E / <g1:/ B E />`, :g:`/ E D / <g1:/ E D />`;

.. step:: assert

   And the base :g:`/ D A / <g1:/ D A />` is :eq:`equal <g1:/ D A / = g1:/ D B />` to the base :g:`/ D B / <g1:/ D B />`

.. step:: assert [G.15] <G.15>

   Therefore :g:`< A E D ) <g1:< A E D )>` is :eq:`equal <g1:< A E D ) = g1:< B E D )>` to :g:`< B E D ) <g1:< B E D )>`.

.. step:: assert [G.18] <G.18>

   Therefore each of :g:`< A E D ) <g1:< A E D )>`, :g:`< B E D ) <g1:< B E D )>` is :eq:`right <g1:< A E D ) = g1:< B E D )>`;

.. step:: assert

   Therefore :g:`/ G K / <g1:/ G K />` cuts :g:`/ A B / <g1:/ A B />` into two :eq:`equal <g1:/ A E / = g1:/ E B />` parts and at :eq:`right angles <g1:< A E D ) = g1:< B E D )>`.

.. step:: assert [G.76] <G.76>

   Since, if in a circle a straight line cut a straight line into two equal parts and at right angles, the center of the circle is on the cutting straight line.

.. step:: assert

   The center of the circle is on :g:`/ G K / <g1:/ G K />`.

.. step:: assert

   For the same reason

.. step:: assert

   The center of :g:`( A B C ) <g1:( A B C )>` is also on :g:`/ H L / <g1:/ H L />`.

.. step:: assert

   :g:`/ G K / <g1:/ G K />`, :g:`/ H L / <g1:/ H L />` have no other point common but :g:`D <g1:D>`

.. step:: conclude

   Therefore :g:`D <g1:D>` is the center of :g:`( A B C ) <g1:( A B C )>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all segments falling upon it from its center are equal.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1): Construct a segment between any two points.", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3): Construct a circle with any center and radius.", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1): Construct an equilateral triangle on a given finite segment.", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3): If equals are subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2): Extend a finite segment continuously in a straight line.", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2): Construct at a given point a segment equal to a given segment.", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3): Cut off from the greater of two unequal segments a segment equal to the less.", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4): Things that coincide with one another are equal.", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4): Triangles with two sides and the included angle equal are congruent (SAS).", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5): In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line standing on a straight line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing line is perpendicular to that on which...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.84" [label="G.84", tooltip="G.84 (III.9): If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.76" -> "G.15";
     "G.84" -> "G.15";
     "G.76" -> "G.18";
     "G.84" -> "G.18";
     "G.84" -> "G.76";
   }

Required for
------------

:ref:`G.104 <G.104>`

.. toctree::
   :hidden:

   code
   heath
