:order: 84
:number: 84
:canonical_id: G.84
:original_id: III.9
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, equality
:dependencies: G.15, G.18, G.76
:excerpt: If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

.. _G.84:
.. _III.9:

G.84
====

.. rubric:: `III.9 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/09/>`_

.. enunciation::

   If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

Let :g:`( A B C ) <0027.g1:( A B C )>` be a circle and :g:`D <0027.g1:D>` a point within it, and from :g:`D <0027.g1:D>` let more than two :eq:`equal <0027.g1:/ D A / = 0027.g1:/ D B / = 0027.g1:/ D C />` straight lines, namely :g:`/ D A / <0027.g1:/ D A />`, :g:`/ D B / <0027.g1:/ D B />`, :g:`/ D C / <0027.g1:/ D C />`, fall on the circle :g:`( A B C ) <0027.g1:( A B C )>`;

I say that the point :g:`D <0027.g1:D>` is the centre of the circle :g:`( A B C ) <0027.g1:( A B C )>`.

.. picture:: 0027.g1.svg
   :alt: Diagram for Proposition 9

For let :g:`/ A B / <0027.g1:/ A B />`, :g:`/ B C / <0027.g1:/ B C />` be joined and :eq:`bisected <0027.g1:/ A E / = 0027.g1:/ E B /; 0027.g1:/ B F / = 0027.g1:/ F C />` at the points :g:`E <0027.g1:E>`, :g:`F <0027.g1:F>`, and let :g:`/ E D / <0027.g1:/ E D />`, :g:`/ F D / <0027.g1:/ F D />` be joined and drawn through to the points :g:`G <0027.g1:G>`, :g:`K <0027.g1:K>`, :g:`H <0027.g1:H>`, :g:`L <0027.g1:L>`.

Then, since :g:`/ A E / <0027.g1:/ A E />` is :eq:`equal <0027.g1:/ A E / = 0027.g1:/ E B />` to :g:`/ E B / <0027.g1:/ E B />`, and :g:`/ E D / <0027.g1:/ E D />` is common,

.. subclause::

   the two sides :g:`/ A E / <0027.g1:/ A E />`, :g:`/ E D / <0027.g1:/ E D />` are :eq:`equal <0027.g1:/ A E / = 0027.g1:/ B E />` to the two sides :g:`/ B E / <0027.g1:/ B E />`, :g:`/ E D / <0027.g1:/ E D />`;

and the base :g:`/ D A / <0027.g1:/ D A />` is :eq:`equal <0027.g1:/ D A / = 0027.g1:/ D B />` to the base :g:`/ D B / <0027.g1:/ D B />`;

.. assertion:: [G.15] <G.15>

   therefore the angle :g:`< A E D ) <0027.g1:< A E D )>` is :eq:`equal <0027.g1:< A E D ) = 0027.g1:< B E D )>` to the angle :g:`< B E D ) <0027.g1:< B E D )>`.

.. assertion:: [G.18] <G.18>

   Therefore each of the angles :g:`< A E D ) <0027.g1:< A E D )>`, :g:`< B E D ) <0027.g1:< B E D )>` is :eq:`right <0027.g1:< A E D ) = 0027.g1:< B E D )>`;

therefore :g:`/ G K / <0027.g1:/ G K />` cuts :g:`/ A B / <0027.g1:/ A B />` into two :eq:`equal <0027.g1:/ A E / = 0027.g1:/ E B />` parts and at :eq:`right angles <0027.g1:< A E D ) = 0027.g1:< B E D )>`.

And since, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line, :just:`[G.76] <G.76>`

.. assertion::

   the centre of the circle is on :g:`/ G K / <0027.g1:/ G K />`.

For the same reason

.. assertion::

   the centre of the circle :g:`( A B C ) <0027.g1:( A B C )>` is also on :g:`/ H L / <0027.g1:/ H L />`.

And the straight lines :g:`/ G K / <0027.g1:/ G K />`, :g:`/ H L / <0027.g1:/ H L />` have no other point common but the point :g:`D <0027.g1:D>`;

.. assertion::

   therefore the point :g:`D <0027.g1:D>` is the centre of the circle :g:`( A B C ) <0027.g1:( A B C )>`.

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
     "G.76" [label="G.76", tooltip="G.76 (III.1): To find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.84" [label="G.84", tooltip="G.84 (III.9): If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.84" -> "G.15";
     "G.76" -> "G.18";
     "G.84" -> "G.18";
     "G.84" -> "G.76";
   }

Required for
------------

:ref:`G.104 <G.104>`
