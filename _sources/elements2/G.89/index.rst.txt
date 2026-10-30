:order: 89
:number: 89
:canonical_id: G.89
:original_id: III.13
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, tangent, equality, reductio-ad-absurdum
:dependencies: G.77, G.86, G.88
:excerpt: A circle does not touch a circle at more points than one, whether it touch it internally or externally.

.. _G.89:
.. _III.13:

G.89
====

.. rubric:: `III.13 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/13/>`_

.. enunciation::

   A circle does not touch a circle at more points than one, whether it touch it internally or externally.

.. signature:: theorem

   | :fn:`circle_touch_circle <G.89>`\ ()
   | **prove** It was proved that neither does it so touch it internally

.. picture:: g1.svg
   :alt: Proposition 13 diagram

.. step:: assert

   If possible, let :g:`( A B D C ) <g1:( A B D C )>` touch :g:`( E B F D ) <g1:( E B F D )>`, first internally, at more points than one, namely :g:`D <g1:D>`, :g:`B <g1:B>`.

.. step:: construct

   Let the center :g:`G <g1:G>` of :g:`( A B D C ) <g1:( A B D C )>`, and the center :g:`H <g1:H>` of :g:`( E B F D ) <g1:( E B F D )>`, be taken.

.. step:: assert ∵ circles_touch_internally <G.86>

   Therefore the straight line joined from :g:`G <g1:G>` to :g:`H <g1:H>` will fall on :g:`B <g1:B>`, :g:`D <g1:D>`.

.. step:: assert

   Let it so fall, as :g:`/ B G H D / <g1:/ B G H D />`.

.. step:: assert ∵ circle_radii <G.2>

   Since :g:`G <g1:G>` is the center of :g:`( A B C D ) <g1:( A B C D )>` → :g:`/ B G / <g1:/ B G />` is :eq:`equal <g1:/ B G / = g1:/ G D />` to :g:`/ G D / <g1:/ G D />`;

.. step:: assert

   Therefore :g:`/ B G / <g1:/ B G />` is greater than :g:`/ H D / <g1:/ H D />`;

.. step:: assert

   Therefore :g:`/ B H / <g1:/ B H />` is much greater than :g:`/ H D / <g1:/ H D />`.

.. step:: assert ∵ circle_radii <G.2>

   Since :g:`H <g1:H>` is the center of :g:`( E B F D ) <g1:( E B F D )>` → :g:`/ B H / <g1:/ B H />` is :eq:`equal <g1:/ B H / = g1:/ H D />` to :g:`/ H D / <g1:/ H D />`;

.. step:: assert

   But it was also proved much greater than it: which is impossible.

.. step:: assert

   Therefore a circle does not touch a circle internally at more points than one.

.. step:: assert

   I say further that neither does it so touch it externally.

.. step:: construct

   If possible, let :g:`( A C K ) <g1:( A C K )>` touch :g:`( A B D C ) <g1:( A B D C )>` at more points than one, namely :g:`A <g1:A>`, :g:`C <g1:C>`, and let :g:`/ A C / <g1:/ A C />` be joined.

.. step:: assert ∵ circumference_circle_points <G.77>

   Since on the circumference of each of :g:`( A B D C ) <g1:( A B D C )>`, :g:`( A C K ) <g1:( A C K )>` two points :g:`A <g1:A>`, :g:`C <g1:C>` have been taken at random, the straight line joining the points will fall within each circle

.. step:: assert ∵ circles_said_touch_def <G.88>

   But it fell within :g:`( A B C D ) <g1:( A B C D )>` and outside :g:`( A C K ) <g1:( A C K )>`: which is absurd.

.. step:: assert

   Therefore a circle does not touch a circle externally at more points than one.

.. step:: conclude

   It was proved that neither does it so touch it internally.

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
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (III.2): If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.", fillcolor="#222244", URL="../G.77/index.html", target="_top"];
     "G.86" [label="G.86", tooltip="G.86 (III.11): If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the c...", fillcolor="#222244", URL="../G.86/index.html", target="_top"];
     "G.88" [label="G.88", tooltip="G.88 (III.def.3): **Circles** are said totouch one another which, meeting one another, do not cut one another.", fillcolor="#224422", URL="../G.88/index.html", target="_top"];
     "G.89" [label="G.89", tooltip="G.89 (III.13): A circle does not touch a circle at more points than one, whether it touch it internally or externally.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.77" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.76" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.76" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.29" -> "G.27";
     "G.77" -> "G.27";
     "G.30" -> "G.29";
     "G.77" -> "G.30";
     "G.77" -> "G.76";
     "G.89" -> "G.77";
     "G.89" -> "G.86";
     "G.89" -> "G.88";
   }

.. toctree::
   :hidden:

   code
   heath
