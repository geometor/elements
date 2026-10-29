:order: 458
:number: 458
:canonical_id: G.458
:original_id: XI.14
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, triangle, polygon, right-angle, parallel, plane, reductio-ad-absurdum
:dependencies: G.28, G.445, G.446, G.457
:excerpt: Planes to which the same straight line is at right angles will be parallel.

.. _G.458:
.. _XI.14:

G.458
=====

.. rubric:: `XI.14 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/14/>`_

.. enunciation::

   Planes to which the same straight line is at right angles will be parallel.

For let any straight line :g:`/ A B / <0300.g1:/ A B />` be at right angles to each of the planes :g:`< C D > <0300.g1:< C D >>`, :g:`< E F > <0300.g1:< E F >>`; I say that the planes are parallel.

.. picture:: 0300.g1.svg
   :alt: Book XI, Proposition 14

For, if not, they will meet when produced. Let them meet; they will then make, as common section, a straight line. :just:`[G.445] <G.445>` Let them make :g:`/ G H / <0300.g1:/ G H />`; let a point :g:`K <0300.g1:K>` be taken at random on :g:`/ G H / <0300.g1:/ G H />`, and let :g:`/ A K / <0300.g1:/ A K />`, :g:`/ B K / <0300.g1:/ B K />` be joined.

Now, since :g:`/ A B / <0300.g1:/ A B />` is at right angles to the plane :g:`< E F > <0300.g1:< E F >>`, therefore :g:`/ A B / <0300.g1:/ A B />` is also at right angles to :g:`/ B K / <0300.g1:/ B K />` which is a straight line in the plane :g:`< E F > <0300.g1:< E F >>` produced; :just:`[G.446] <G.446>`

.. assertion::

   therefore the angle :g:`< A B K ) <0300.g1:< A B K )>` is right.

.. subclause::

   For the same reason the angle :g:`< B A K ) <0300.g1:< B A K )>` is also right.

Thus, in the triangle :g:`< A B K > <0300.g1:< A B K >>`, the two angles :g:`< A B K ) <0300.g1:< A B K )>`, :g:`< B A K ) <0300.g1:< B A K )>` are equal to two right angles:

.. assertion:: [G.28] <G.28>

   which is impossible.

Therefore the planes :g:`< C D > <0300.g1:< C D >>`, :g:`< E F > <0300.g1:< E F >>` will not meet when produced;

.. assertion:: [G.457] <G.457>

   therefore the planes :g:`< C D > <0300.g1:< C D >>`, :g:`< E F > <0300.g1:< E F >>` are parallel.

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
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1): Things which are equal to the same thing are also equal to one another.", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another ;", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1): To draw a straight line from any point to any point.", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3): To describe a circle with any centre and distance.", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1): On a given finite straight line to construct an equilateral triangle.", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3): If equals be subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2): To produce a finite straight line continuously in a straight line.", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2): To place at a given point (as an extremity) a straight line equal to a given straight line.", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3): Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4): [7] 4. Things which coincide with one another are equal to one another.", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4): If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base...", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5): In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another...", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7): Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities),...", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8): If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal...", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is cal...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): To draw a straight line at right angles to a given straight line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals be added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle two angles taken together in any manner are less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line is at right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.457" [label="G.457", tooltip="G.457 (XI.def.8): Parallel planes are those which do not meet.", fillcolor="#224422", URL="../G.457/index.html", target="_top"];
     "G.458" [label="G.458", tooltip="G.458 (XI.14): Planes to which the same straight line is at right angles will be parallel.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
