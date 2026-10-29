:order: 109
:number: 109
:canonical_id: G.109
:original_id: III.30
:volume: II
:book: III
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles
:category: problem, construction, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, bisect, arc, equality
:dependencies: G.11, G.107
:excerpt: Bisect a given circumference.

.. _G.109:
.. _III.30:

G.109
=====

.. rubric:: `III.30 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/30/>`_

.. enunciation::

   Bisect a given circumference.

.. picture:: g1.svg
   :alt: Diagram

.. step:: given

   :g:`( A D B ) <g1:( A D B )>` be the given circumference

.. step:: construct

   Let :g:`/ A B / <g1:/ A B />` be joined and bisected at :g:`C <g1:C>`

.. step:: construct

   From :g:`C <g1:C>` let :g:`/ C D / <g1:/ C D />` be drawn at right angles to :g:`/ A B / <g1:/ A B />`

.. step:: construct

   **segment** :g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />`

.. step:: assert

   Since :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ C B />` to :g:`/ C B / <g1:/ C B />`, and :g:`/ C D / <g1:/ C D />` is common, the two sides :g:`/ A C / <g1:/ A C />`, :g:`/ C D / <g1:/ C D />` are :eq:`equal <g1:/ A C / = g1:/ B C /; g1:/ C D / = g1:/ C D />` to the two sides :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`

.. step:: assert

   And :g:`< A C D ) <g1:< A C D )>` is :eq:`equal <g1:< A C D ) = g1:< B C D )>` to :g:`< B C D ) <g1:< B C D )>`, for each is right

.. step:: assert [G.11] <G.11>

   Therefore the base :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ D B />` to the base :g:`/ D B / <g1:/ D B />`.

.. step:: assert [G.107] <G.107>

   Equal straight lines cut off equal circumferences, the greater equal to the greater, and the less to the less

.. step:: assert

   And each of the circumferences :g:`( A D ) <g1:( A D )>`, :g:`( D B ) <g1:( D B )>` is less than a semicircle;

.. step:: assert

   Therefore the circumference :g:`( A D ) <g1:( A D )>` is :eq:`equal <g1:( A D ) = g1:( D B )>` to the circumference :g:`( D B ) <g1:( D B )>`.

.. step:: conclude

   Therefore the given circumference has been bisected at :g:`D <g1:D>`.

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
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.85/index.html", target="_top"];
     "G.101" [label="G.101", tooltip="G.101 (III.def.11): Similar segments of circles are those which admit equal angles, or in which the angles are equal.", fillcolor="#224422", URL="../G.101/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.24): Similar segments of circles on equal straight lines are equal.", fillcolor="#222244", URL="../G.103/index.html", target="_top"];
     "G.105" [label="G.105", tooltip="G.105 (III.26): In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.105/index.html", target="_top"];
     "G.107" [label="G.107", tooltip="G.107 (III.28): In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.", fillcolor="#222244", URL="../G.107/index.html", target="_top"];
     "G.109" [label="G.109", tooltip="G.109 (III.30): Bisect a given circumference.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.105" -> "G.11";
     "G.109" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.76" -> "G.15";
     "G.107" -> "G.15";
     "G.76" -> "G.18";
     "G.85" -> "G.76";
     "G.85" -> "G.80";
     "G.103" -> "G.85";
     "G.105" -> "G.101";
     "G.105" -> "G.103";
     "G.107" -> "G.105";
     "G.109" -> "G.107";
   }

Required for
------------

:ref:`G.134 <G.134>`

.. toctree::
   :hidden:

   code
   heath
