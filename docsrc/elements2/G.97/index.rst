:order: 97
:number: 97
:canonical_id: G.97
:original_id: III.19
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, right-angle, tangent, equality, reductio-ad-absurdum
:dependencies: G.96
:excerpt: If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle is on the straight line so drawn.

.. _G.97:
.. _III.19:

G.97
====

.. rubric:: `III.19 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/19/>`_

.. enunciation::

   If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle is on the straight line so drawn.

.. signature:: theorem

   | :fn:`straight_line_touch_iii_19 <G.97>`\ ()
   | **prove** the center of the circle is on :g:`/ A C / <g1:/ A C />`

.. picture:: g1.svg
   :alt: Diagram for Proposition 19

.. step:: construct

   Let a straight line :g:`/ D E / <g1:/ D E />` touch :g:`( A B C ) <g1:( A B C )>` at :g:`C <g1:C>`, and from :g:`C <g1:C>` let :g:`/ C A / <g1:/ C A />` be drawn at right angles to :g:`/ D E / <g1:/ D E />`

.. step:: construct

   Suppose it is not, but, if possible, let :g:`F <g1:F>` be the center, and let :g:`/ C F / <g1:/ C F />` be joined.

.. step:: assert ∵ straight_line_touch <G.96>

   Since a straight line :g:`/ D E / <g1:/ D E />` touches :g:`( A B C ) <g1:( A B C )>`, and :g:`/ F C / <g1:/ F C />` has been joined from the center to the point of contact → :g:`/ F C / <g1:/ F C />` is perpendicular to :g:`/ D E / <g1:/ D E />`; therefore :g:`< F C E ) <g1:< F C E )>` is right.

.. step:: assert

   :g:`< A C E ) <g1:< A C E )>` is also right

.. step:: assert

   Therefore :g:`< F C E ) <g1:< F C E )>` is :eq:`equal <g1:< F C E ) = g1:< A C E )>` to :g:`< A C E ) <g1:< A C E )>`, the less to the greater: which is impossible.

.. step:: assert

   Therefore :g:`F <g1:F>` is not the center of :g:`( A B C ) <g1:( A B C )>`.

.. step:: conclude

   Similarly we can prove that neither is any other point except a point on :g:`/ A C / <g1:/ A C />`.

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
     "G.19" [label="G.19", tooltip="G.19 (I.11): Construct a line at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.96" [label="G.96", tooltip="G.96 (III.18): If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined is perpendicular to the tangent.", fillcolor="#222244", URL="../G.96/index.html", target="_top"];
     "G.97" [label="G.97", tooltip="G.97 (III.19): If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle is on the straight line so drawn.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.27" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.8" -> "G.6";
     "G.25" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.27" -> "G.7";
     "G.28" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.27" -> "G.9";
     "G.29" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.29" -> "G.27";
     "G.96" -> "G.28";
     "G.30" -> "G.29";
     "G.96" -> "G.30";
     "G.97" -> "G.96";
   }

Required for
------------

:ref:`G.111 <G.111>`, :ref:`G.112 <G.112>`, :ref:`G.113 <G.113>`, :ref:`G.118 <G.118>`, :ref:`G.128 <G.128>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.520 <G.520>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
