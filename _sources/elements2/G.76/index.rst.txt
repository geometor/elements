:order: 76
:number: 76
:canonical_id: G.76
:original_id: III.1
:volume: II
:book: III
:type: prop
:subtype: problem
:categories: problem, finding, plane-geometry, circles
:category: problem, finding, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, equality, reductio-ad-absurdum, porism
:dependencies: G.15, G.18
:excerpt: Find the centre of a given circle.

.. _G.76:
.. _III.1:

G.76
====

.. rubric:: `III.1 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/01/>`_

.. enunciation::

   Find the centre of a given circle.

.. signature:: problem

   | :fn:`find_circle_center <G.76>`\ (:g:`( A B C ) <g1:( A B C )>`) → :g:`F <g1:F>`
   | **given** :g:`( A B C ) <g1:( A B C )>`
   | **construct** :g:`F <g1:F>` is the center of :g:`( A B C ) <g1:( A B C )>`

.. picture:: g1.svg
   :alt: Proposition 1

.. step:: given

   :g:`( A B C ) <g1:( A B C )>`

.. step:: construct

   Let a straight line :g:`/ A B / <g1:/ A B />` be drawn through it at random

.. step:: assert

   Let it be :eq:`bisected <g1:/ A D / = g1:/ D B />` at :g:`D <g1:D>`

.. step:: construct

   From :g:`D <g1:D>` let :g:`/ D C / <g1:/ D C />` be drawn at right angles to :g:`/ A B / <g1:/ A B />` and let it be drawn through to :g:`E <g1:E>`

.. step:: construct

   :fn:`bisect_segment <G.17>`\ (:g:`/ C E / <g1:/ C E />`) → :g:`F <g1:F>` (:eq:`bisected <g1:/ C F / = g1:/ F E />`)

.. step:: construct

   Suppose it is not, but, if possible, let :g:`G <g1:G>` be the center, and let :g:`/ G A / <g1:/ G A />`, :g:`/ G D / <g1:/ G D />`, :g:`/ G B / <g1:/ G B />` be joined.

.. step:: assert

   Since :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ D B />` to :g:`/ D B / <g1:/ D B />`, and :g:`/ D G / <g1:/ D G />` is common → the two sides :g:`/ A D / <g1:/ A D />`, :g:`/ D G / <g1:/ D G />` are :eq:`equal <g1:/ A D / = g1:/ B D />` to the two sides :g:`/ B D / <g1:/ B D />`, :g:`/ D G / <g1:/ D G />` respectively;

.. step:: assert

   And the base :g:`/ G A / <g1:/ G A />` is :eq:`equal <g1:/ G A / = g1:/ G B />` to the base :g:`/ G B / <g1:/ G B />`, for they are radii

.. step:: assert ∵ sss_congruence <G.15>

   Therefore :g:`< A D G ) <g1:< A D G )>` is :eq:`equal <g1:< A D G ) = g1:< G D B )>` to :g:`< G D B ) <g1:< G D B )>`.

.. step:: assert ∵ right_angle_perpendicular <G.18>

   But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right

.. step:: assert

   Therefore :g:`< G D B ) <g1:< G D B )>` is right.

.. step:: assert

   :g:`< F D B ) <g1:< F D B )>` is also right

.. step:: assert

   Therefore :g:`< F D B ) <g1:< F D B )>` is :eq:`equal <g1:< F D B ) = g1:< G D B )>` to :g:`< G D B ) <g1:< G D B )>`, the greater to the less: which is impossible.

.. step:: assert

   Therefore :g:`G <g1:G>` is not the center of :g:`( A B C ) <g1:( A B C )>`.

.. step:: assert

   Similarly we can prove that neither is any other point except :g:`F <g1:F>`.

.. step:: conclude ∵ circle_radii <G.2>

   Therefore :g:`F <g1:F>` is the center of :g:`( A B C ) <g1:( A B C )>`.

.. enunciation::

   PORISM. From this it is manifest that, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line.

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
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.76" -> "G.18";
   }

Required for
------------

:ref:`G.77 <G.77>`, :ref:`G.79 <G.79>`, :ref:`G.83 <G.83>`, :ref:`G.84 <G.84>`, :ref:`G.85 <G.85>`, :ref:`G.89 <G.89>`, :ref:`G.91 <G.91>`, :ref:`G.93 <G.93>`, :ref:`G.95 <G.95>`, :ref:`G.103 <G.103>`, :ref:`G.104 <G.104>`, :ref:`G.105 <G.105>`, :ref:`G.106 <G.106>`, :ref:`G.107 <G.107>`, :ref:`G.108 <G.108>`, :ref:`G.109 <G.109>`, :ref:`G.119 <G.119>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.198 <G.198>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.519 <G.519>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
