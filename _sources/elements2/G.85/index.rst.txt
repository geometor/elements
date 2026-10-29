:order: 85
:number: 85
:canonical_id: G.85
:original_id: III.10
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, equality, reductio-ad-absurdum
:dependencies: G.76, G.80
:excerpt: A circle does not cut a circle at more points than two.

.. _G.85:
.. _III.10:

G.85
====

.. rubric:: `III.10 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/10/>`_

.. enunciation::

   A circle does not cut a circle at more points than two.

.. picture:: g1.svg
   :alt: Diagram for Proposition 10

.. step:: assert

   If possible, let :g:`( A B C ) <g1:( A B C )>` cut :g:`( D E F ) <g1:( D E F )>` at more points than two, namely :g:`B <g1:B>`, :g:`G <g1:G>`, :g:`F <g1:F>`, :g:`H <g1:H>`

.. step:: construct

   Let :g:`/ B H / <g1:/ B H />`, :g:`/ B G / <g1:/ B G />` be joined and :eq:`bisected <g1:/ B K / = g1:/ K H /; g1:/ B L / = g1:/ L G />` at :g:`K <g1:K>`, :g:`L <g1:L>`

.. step:: construct

   From :g:`K <g1:K>`, :g:`L <g1:L>` let :g:`/ K C / <g1:/ K C />`, :g:`/ L M / <g1:/ L M />` be drawn at right angles to :g:`/ B H / <g1:/ B H />`, :g:`/ B G / <g1:/ B G />` and carried through to :g:`A <g1:A>`, :g:`E <g1:E>`.

.. step:: assert [G.76] <G.76>

   Since in :g:`( A B C ) <g1:( A B C )>` a straight line :g:`/ A C / <g1:/ A C />` cuts a straight line :g:`/ B H / <g1:/ B H />` into two :eq:`equal <g1:/ B K / = g1:/ K H />` parts and at right angles → the center of :g:`( A B C ) <g1:( A B C )>` is on :g:`/ A C / <g1:/ A C />`.

.. step:: assert

   Since in the same circle :g:`( A B C ) <g1:( A B C )>` a straight line :g:`/ N O / <g1:/ N O />` cuts a straight line :g:`/ B G / <g1:/ B G />` into two :eq:`equal <g1:/ B L / = g1:/ L G />` parts and at right angles → the center of :g:`( A B C ) <g1:( A B C )>` is on :g:`/ N O / <g1:/ N O />`.

.. step:: intersect

   It was also proved to be on :g:`/ A C / <g1:/ A C />`, and :g:`/ A C / <g1:/ A C />`, :g:`/ N O / <g1:/ N O />` meet at no point except at :g:`P <g1:P>`

.. step:: assert

   Therefore :g:`P <g1:P>` is the center of :g:`( A B C ) <g1:( A B C )>`.

.. step:: assert

   Similarly we can prove that :g:`P <g1:P>` is also the center of :g:`( D E F ) <g1:( D E F )>`

.. step:: conclude [G.80] <G.80>

   Therefore the two circles :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` which cut one another have the same center :g:`P <g1:P>`: which is impossible.

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
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.80" -> "G.2";
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
     "G.76" -> "G.18";
     "G.85" -> "G.76";
     "G.85" -> "G.80";
   }

Required for
------------

:ref:`G.103 <G.103>`, :ref:`G.105 <G.105>`, :ref:`G.106 <G.106>`, :ref:`G.107 <G.107>`, :ref:`G.108 <G.108>`, :ref:`G.109 <G.109>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.198 <G.198>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.519 <G.519>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
