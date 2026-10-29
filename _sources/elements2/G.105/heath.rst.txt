:canonical_id: G.105
:original_id: III.26
:volume: II
:book: III
:type: prop

G.105 — Heath
=============

.. rubric:: `III.26 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/26/>`_

.. enunciation::

   In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.

Let :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` be :eq:`equal <g1:( A B C ) = g1:( D E F )>` circles, and in them let there
be :eq:`equal <g1:< B G C ) = g1:< E H F ); g1:< B A C ) = g1:< E D F )>` angles, namely at the centres the angles :g:`< B G C ) <g1:< B G C )>`,
:g:`< E H F ) <g1:< E H F )>`, and at the circumferences the angles :g:`< B A C ) <g1:< B A C )>`, :g:`< E D F ) <g1:< E D F )>`;
I say that the circumference :g:`( B K C ) <g1:( B K C )>` is :eq:`equal <g1:( B K C ) = g1:( E L F )>` to the circumference
:g:`( E L F ) <g1:( E L F )>`.

.. picture:: g1.svg
   :alt: Diagram

For let :g:`/ B C / <g1:/ B C />`, :g:`/ E F / <g1:/ E F />` be joined.

Now, since the circles :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` are :eq:`equal <g1:( A B C ) = g1:( D E F )>`,

.. assertion::

   the radii are :eq:`equal <g1:/ B G / = g1:/ G C / = g1:/ E H / = g1:/ H F />`.

Thus the two straight lines :g:`/ B G / <g1:/ B G />`, :g:`/ G C / <g1:/ G C />` are :eq:`equal <g1:/ B G / = g1:/ E H /; g1:/ G C / = g1:/ H F />` to the
two straight lines :g:`/ E H / <g1:/ E H />`, :g:`/ H F / <g1:/ H F />`;

.. subclause::

   and the angle at :g:`G <g1:G>` is :eq:`equal <g1:< B G C ) = g1:< E H F )>` to the angle at :g:`H <g1:H>`;

.. assertion:: [G.11] <G.11>

   therefore the base :g:`/ B C / <g1:/ B C />` is :eq:`equal <g1:/ B C / = g1:/ E F />` to the base :g:`/ E F / <g1:/ E F />`.

And, since the angle at :g:`A <g1:A>` is :eq:`equal <g1:< B A C ) = g1:< E D F )>` to the angle at :g:`D <g1:D>`,

.. assertion:: [G.101] <G.101>

   the segment :g:`( B A C ) <g1:( B A C )>` is similar to the segment :g:`( E D F ) <g1:( E D F )>`;

and they are upon :eq:`equal <g1:/ B C / = g1:/ E F />` straight lines.

But similar segments of circles on equal straight lines are
equal to one another; :just:`[G.103] <G.103>`

.. assertion::

   therefore the segment :g:`( B A C ) <g1:( B A C )>` is :eq:`equal <g1:( B A C ) = g1:( E D F )>` to :g:`( E D F ) <g1:( E D F )>`.

But the whole circle :g:`( A B C ) <g1:( A B C )>` is also :eq:`equal <g1:( A B C ) = g1:( D E F )>` to the whole circle
:g:`( D E F ) <g1:( D E F )>`;
therefore the circumference :g:`( B K C ) <g1:( B K C )>` which remains is :eq:`equal <g1:( B K C ) = g1:( E L F )>` to
the circumference :g:`( E L F ) <g1:( E L F )>`.

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
     "G.105" [label="G.105", tooltip="G.105 (III.26): In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.76" -> "G.15";
     "G.76" -> "G.18";
     "G.85" -> "G.76";
     "G.85" -> "G.80";
     "G.103" -> "G.85";
     "G.105" -> "G.101";
     "G.105" -> "G.103";
   }

Required for
------------

:ref:`G.106 <G.106>`, :ref:`G.107 <G.107>`, :ref:`G.108 <G.108>`, :ref:`G.109 <G.109>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.198 <G.198>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.519 <G.519>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`
