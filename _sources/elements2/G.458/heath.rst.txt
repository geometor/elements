:canonical_id: G.458
:original_id: XI.14
:volume: III
:book: XI
:type: prop

G.458 — Heath
=============

.. rubric:: `XI.14 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/14/>`_

.. enunciation::

   Planes to which the same straight line is at right angles will be parallel.

For let any straight line :g:`/ A B / <g1:/ A B />` be at right angles to each of the planes :g:`< C D > <g1:< C D >>`, :g:`< E F > <g1:< E F >>`; I say that the planes are parallel.

.. picture:: g1.svg
   :alt: Book XI, Proposition 14

For, if not, they will meet when produced. Let them meet; they will then make, as common section, a straight line. :just:`[G.445] <G.445>` Let them make :g:`/ G H / <g1:/ G H />`; let a point :g:`K <g1:K>` be taken at random on :g:`/ G H / <g1:/ G H />`, and let :g:`/ A K / <g1:/ A K />`, :g:`/ B K / <g1:/ B K />` be joined.

Now, since :g:`/ A B / <g1:/ A B />` is at right angles to the plane :g:`< E F > <g1:< E F >>`, therefore :g:`/ A B / <g1:/ A B />` is also at right angles to :g:`/ B K / <g1:/ B K />` which is a straight line in the plane :g:`< E F > <g1:< E F >>` produced; :just:`[G.446] <G.446>`

.. assertion::

   therefore the angle :g:`< A B K ) <g1:< A B K )>` is right.

.. subclause::

   For the same reason the angle :g:`< B A K ) <g1:< B A K )>` is also right.

Thus, in the triangle :g:`< A B K > <g1:< A B K >>`, the two angles :g:`< A B K ) <g1:< A B K )>`, :g:`< B A K ) <g1:< B A K )>` are equal to two right angles:

.. assertion:: [G.28] <G.28>

   which is impossible.

Therefore the planes :g:`< C D > <g1:< C D >>`, :g:`< E F > <g1:< E F >>` will not meet when produced;

.. assertion:: [G.457] <G.457>

   therefore the planes :g:`< C D > <g1:< C D >>`, :g:`< E F > <g1:< E F >>` are parallel.

.. assertion::

   Therefore planes to which the same straight line is at right angles are parallel.

.. qed::

   Q. E. D.

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
     "G.19" [label="G.19", tooltip="G.19 (I.11): Construct a line at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.457" [label="G.457", tooltip="G.457 (XI.def.8): Parallel planes are those which do not meet.", fillcolor="#224422", URL="../G.457/index.html", target="_top"];
     "G.458" [label="G.458", tooltip="G.458 (XI.14): Planes to which the same straight line is at right angles is parallel.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
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
     "G.19" -> "G.5";
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.28" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.19" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.19" -> "G.15";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.28" -> "G.22";
     "G.458" -> "G.28";
     "G.458" -> "G.445";
     "G.458" -> "G.446";
     "G.458" -> "G.457";
   }

Required for
------------

:ref:`G.459 <G.459>`
