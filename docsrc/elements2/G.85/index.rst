:order: 85
:number: 85
:canonical_id: G.85
:original_id: III.10
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, equality, reductio-ad-absurdum
:dependencies: G.76, G.80
:excerpt: A circle does not cut a circle at more points than two.

.. _G.85:
.. _III.10:

G.85
====

.. rubric:: `III.10 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/10/>`_

.. enunciation::

   A circle does not cut a circle at more points than two.

For, if possible, let the circle :g:`( A B C ) <0029.g1:( A B C )>` cut the circle :g:`( D E F ) <0029.g1:( D E F )>` at more points than two, namely :g:`B <0029.g1:B>`, :g:`G <0029.g1:G>`, :g:`F <0029.g1:F>`, :g:`H <0029.g1:H>`; let :g:`/ B H / <0029.g1:/ B H />`, :g:`/ B G / <0029.g1:/ B G />` be joined and :eq:`bisected <0029.g1:/ B K / = 0029.g1:/ K H /; 0029.g1:/ B L / = 0029.g1:/ L G />` at the points :g:`K <0029.g1:K>`, :g:`L <0029.g1:L>`, and from :g:`K <0029.g1:K>`, :g:`L <0029.g1:L>` let :g:`/ K C / <0029.g1:/ K C />`, :g:`/ L M / <0029.g1:/ L M />` be drawn at right angles to :g:`/ B H / <0029.g1:/ B H />`, :g:`/ B G / <0029.g1:/ B G />` and carried through to the points :g:`A <0029.g1:A>`, :g:`E <0029.g1:E>`.

.. picture:: 0029.g1.svg
   :alt: Diagram for Proposition 10

Then, since in the circle :g:`( A B C ) <0029.g1:( A B C )>` a straight line :g:`/ A C / <0029.g1:/ A C />` cuts a straight line :g:`/ B H / <0029.g1:/ B H />` into two :eq:`equal <0029.g1:/ B K / = 0029.g1:/ K H />` parts and at right angles,

.. assertion:: [G.76] <G.76>

   the centre of the circle :g:`( A B C ) <0029.g1:( A B C )>` is on :g:`/ A C / <0029.g1:/ A C />`.

Again, since in the same circle :g:`( A B C ) <0029.g1:( A B C )>` a straight line :g:`/ N O / <0029.g1:/ N O />` cuts a straight line :g:`/ B G / <0029.g1:/ B G />` into two :eq:`equal <0029.g1:/ B L / = 0029.g1:/ L G />` parts and at right angles,

.. assertion::

   the centre of the circle :g:`( A B C ) <0029.g1:( A B C )>` is on :g:`/ N O / <0029.g1:/ N O />`.

But it was also proved to be on :g:`/ A C / <0029.g1:/ A C />`, and the straight lines :g:`/ A C / <0029.g1:/ A C />`, :g:`/ N O / <0029.g1:/ N O />` meet at no point except at :g:`P <0029.g1:P>`;

.. assertion::

   therefore the point :g:`P <0029.g1:P>` is the centre of the circle :g:`( A B C ) <0029.g1:( A B C )>`.

Similarly we can prove that :g:`P <0029.g1:P>` is also the centre of the circle :g:`( D E F ) <0029.g1:( D E F )>`;

.. assertion::

   therefore the two circles :g:`( A B C ) <0029.g1:( A B C )>`, :g:`( D E F ) <0029.g1:( D E F )>` which cut one another have the same centre :g:`P <0029.g1:P>`: which is impossible. :just:`[G.80] <G.80>`

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
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.76" -> "G.15";
     "G.76" -> "G.18";
     "G.85" -> "G.76";
     "G.85" -> "G.80";
   }

Required for
------------

:ref:`G.103 <G.103>`, :ref:`G.105 <G.105>`, :ref:`G.106 <G.106>`, :ref:`G.107 <G.107>`, :ref:`G.108 <G.108>`, :ref:`G.109 <G.109>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.198 <G.198>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.519 <G.519>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`
