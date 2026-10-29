:order: 20
:number: 20
:canonical_id: G.20
:original_id: I.12
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, line, circle, angle, perpendicular, equality
:dependencies: G.3, G.4, G.15, G.17, G.18
:excerpt: Construct a perpendicular to a given infinite line from a given point not on it.

.. _G.20:
.. _I.12:

G.20
====

.. rubric:: `I.12 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/12/>`_

.. enunciation::

   Construct a perpendicular to a given infinite line from a given point not on it.

.. picture:: g1.svg
   :alt: Proposition 12 figure

.. step:: given

   :g:`[ A B ] <g1:[ A B ]>` be the given infinite straight line, :g:`C <g1:C>` the given point which is not on it

.. step:: construct

   For let a point :g:`D <g1:D>` be taken at random on the other side of :g:`[ A B ] <g1:[ A B ]>`

.. step:: construct [G.4] <G.4>

   **circle** :g:`( C D ) <g1:( C D )>` with center :g:`C <g1:C>` and radius :g:`/ C D / <g1:/ C D />`

.. step:: assert [G.17] <G.17>

   Let :g:`/ E G / <g1:/ E G />` be :eq:`bisected <g1:/ G H / = g1:/ H E />` at :g:`H <g1:H>`.

.. step:: construct [G.3] <G.3>

   **segment** :g:`/ C G / <g1:/ C G />`, :g:`/ C H / <g1:/ C H />`, :g:`/ C E / <g1:/ C E />`

.. step:: assert

   :g:`/ C H / <g1:/ C H />` has been drawn :eq:`perpendicular <g1:< C H G ) = g1:< E H C )>` to the given infinite straight line :g:`[ A B ] <g1:[ A B ]>` from :g:`C <g1:C>` which is not on it.

.. step:: assert

   Since :g:`/ G H / <g1:/ G H />` is :eq:`equal <g1:/ G H / = g1:/ H E />` to :g:`/ H E / <g1:/ H E />`, and :g:`/ H C / <g1:/ H C />` is common → the two sides :g:`/ G H / <g1:/ G H />`, :g:`/ H C / <g1:/ H C />` are :eq:`equal <g1:/ G H / = g1:/ E H />` to the two sides :g:`/ E H / <g1:/ E H />`, :g:`/ H C / <g1:/ H C />` respectively;

.. step:: assert

   And the base :g:`/ C G / <g1:/ C G />` is :eq:`equal <g1:/ C G / = g1:/ C E />` to the base :g:`/ C E / <g1:/ C E />`

.. step:: assert [G.15] <G.15>

   Therefore :g:`< C H G ) <g1:< C H G )>` is :eq:`equal <g1:< C H G ) = g1:< E H C )>` to :g:`< E H C ) <g1:< E H C )>`.

.. step:: assert

   They are adjacent angles.

.. step:: assert [G.18] <G.18>

   But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is called a perpendicular to that on which it stands.

.. step:: conclude

   Therefore :g:`/ C H / <g1:/ C H />` has been drawn :eq:`perpendicular <g1:< C H G ) = g1:< E H C )>` to the given infinite straight line :g:`[ A B ] <g1:[ A B ]>` from :g:`C <g1:C>` which is not on it.

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
     "G.16" [label="G.16", tooltip="G.16 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): Bisect a given finite segment.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line standing on a straight line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing line is perpendicular to that on which...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.20" [label="G.20", tooltip="G.20 (I.12): Construct a perpendicular to a given infinite line from a given point not on it.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.20" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.20" -> "G.4";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.20" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.17";
     "G.20" -> "G.18";
   }

Required for
------------

:ref:`G.454 <G.454>`, :ref:`G.455 <G.455>`, :ref:`G.459 <G.459>`, :ref:`G.468 <G.468>`, :ref:`G.471 <G.471>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.520 <G.520>`, :ref:`G.521 <G.521>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
