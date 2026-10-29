:canonical_id: G.78
:original_id: III.3
:volume: II
:book: III
:type: prop

G.78 — Heath
============

.. rubric:: `III.3 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/03/>`_

.. enunciation::

   If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

Let :g:`( A B C ) <g1:( A B C )>` be a circle, and in it let a straight line :g:`/ C D / <g1:/ C D />` through the centre :eq:`bisect <g1:/ A F / = g1:/ F B />` a straight line :g:`/ A B / <g1:/ A B />` not through the centre at the point :g:`F <g1:F>`;

I say that it also cuts it at :eq:`right angles <g1:< A F E ) = g1:< B F E )>`.

.. picture:: g1.svg
   :alt: Proposition 3

For let the centre of the circle :g:`( A B C ) <g1:( A B C )>` be taken, and let it be :g:`E <g1:E>`; let :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />` be joined.

Then, since :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`, and :g:`/ F E / <g1:/ F E />` is common,

.. subclause::

   two sides are :eq:`equal <g1:/ A F / = g1:/ F B />` to two sides;

and the base :g:`/ E A / <g1:/ E A />` is :eq:`equal <g1:/ E A / = g1:/ E B />` to the base :g:`/ E B / <g1:/ E B />`;

.. assertion:: [G.15] <G.15>

   therefore the angle :g:`< A F E ) <g1:< A F E )>` is :eq:`equal <g1:< A F E ) = g1:< B F E )>` to the angle :g:`< B F E ) <g1:< B F E )>`.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; :just:`[G.18] <G.18>`

.. assertion::

   therefore each of the angles :g:`< A F E ) <g1:< A F E )>`, :g:`< B F E ) <g1:< B F E )>` is :eq:`right <g1:< A F E ) = g1:< B F E )>`.

.. assertion::

   Therefore :g:`/ C D / <g1:/ C D />`, which is through the centre, and :eq:`bisects <g1:/ A F / = g1:/ F B />` :g:`/ A B / <g1:/ A B />` which is not through the centre, also cuts it at :eq:`right angles <g1:< A F E ) = g1:< B F E )>`.

Again, let :g:`/ C D / <g1:/ C D />` cut :g:`/ A B / <g1:/ A B />` at :eq:`right angles <g1:< A F E ) = g1:< B F E )>`;

I say that it also :eq:`bisects <g1:/ A F / = g1:/ F B />` it, that is, that :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`.

For, with the same construction,

.. subclause::

   since :g:`/ E A / <g1:/ E A />` is :eq:`equal <g1:/ E A / = g1:/ E B />` to :g:`/ E B / <g1:/ E B />`,

the angle :g:`< E A F ) <g1:< E A F )>` is also :eq:`equal <g1:< E A F ) = g1:< E B F )>` to the angle :g:`< E B F ) <g1:< E B F )>`. :just:`[G.12] <G.12>`

But the right angle :g:`< A F E ) <g1:< A F E )>` is :eq:`equal <g1:< A F E ) = g1:< B F E )>` to the right angle :g:`< B F E ) <g1:< B F E )>`, therefore :g:`< E A F > <g1:< E A F >>`, :g:`< E B F > <g1:< E B F >>` are two triangles having two angles :eq:`equal <g1:< E A F ) = g1:< E B F ); g1:< A F E ) = g1:< B F E )>` to two angles and one side equal to one side, namely :g:`/ E F / <g1:/ E F />`, which is common to them, and subtends one of the :eq:`equal <g1:< E A F ) = g1:< E B F )>` angles; therefore they will also have the remaining sides :eq:`equal <g1:/ A F / = g1:/ F B /; g1:/ E A / = g1:/ E B />` to the remaining sides; :just:`[G.37] <G.37>`

.. assertion::

   therefore :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`.

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
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (III.3): If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.14" -> "G.12";
     "G.78" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.78" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.78" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.37" -> "G.27";
     "G.78" -> "G.37";
   }

Required for
------------

:ref:`G.79 <G.79>`, :ref:`G.91 <G.91>`, :ref:`G.93 <G.93>`, :ref:`G.114 <G.114>`, :ref:`G.115 <G.115>`, :ref:`G.116 <G.116>`, :ref:`G.128 <G.128>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.503 <G.503>`
