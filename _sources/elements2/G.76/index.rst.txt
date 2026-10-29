:order: 76
:number: 76
:canonical_id: G.76
:original_id: III.1
:volume: II
:book: III
:type: prop
:subtype: problem
:categories: problem, finding, plane-geometry, circles
:category: problem, finding, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, equality, reductio-ad-absurdum, porism
:dependencies: G.15, G.18
:excerpt: To find the centre of a given circle.

.. _G.76:
.. _III.1:

G.76
====

.. rubric:: `III.1 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/01/>`_

.. enunciation::

   To find the centre of a given circle.

Let :g:`( A B C ) <0012.g1:( A B C )>` be the given circle;

thus it is required to find the centre of the circle :g:`( A B C ) <0012.g1:( A B C )>`.

Let a straight line :g:`/ A B / <0012.g1:/ A B />` be drawn through it at random, and let it be :eq:`bisected <0012.g1:/ A D / = 0012.g1:/ D B />` at the point :g:`D <0012.g1:D>`; from :g:`D <0012.g1:D>` let :g:`/ D C / <0012.g1:/ D C />` be drawn at right angles to :g:`/ A B / <0012.g1:/ A B />` and let it be drawn through to :g:`E <0012.g1:E>`; let :g:`/ C E / <0012.g1:/ C E />` be :eq:`bisected <0012.g1:/ C F / = 0012.g1:/ F E />` at :g:`F <0012.g1:F>`;

I say that :g:`F <0012.g1:F>` is the centre of the circle :g:`( A B C ) <0012.g1:( A B C )>`.

.. picture:: 0012.g1.svg
   :alt: Proposition 1

For suppose it is not, but, if possible, let :g:`G <0012.g1:G>` be the centre, and let :g:`/ G A / <0012.g1:/ G A />`, :g:`/ G D / <0012.g1:/ G D />`, :g:`/ G B / <0012.g1:/ G B />` be joined.

Then, since :g:`/ A D / <0012.g1:/ A D />` is :eq:`equal <0012.g1:/ A D / = 0012.g1:/ D B />` to :g:`/ D B / <0012.g1:/ D B />`, and :g:`/ D G / <0012.g1:/ D G />` is common,

.. subclause::

   the two sides :g:`/ A D / <0012.g1:/ A D />`, :g:`/ D G / <0012.g1:/ D G />` are :eq:`equal <0012.g1:/ A D / = 0012.g1:/ B D />` to the two sides :g:`/ B D / <0012.g1:/ B D />`, :g:`/ D G / <0012.g1:/ D G />` respectively;

and the base :g:`/ G A / <0012.g1:/ G A />` is :eq:`equal <0012.g1:/ G A / = 0012.g1:/ G B />` to the base :g:`/ G B / <0012.g1:/ G B />`, for they are radii;

.. assertion:: [G.15] <G.15>

   therefore the angle :g:`< A D G ) <0012.g1:< A D G )>` is :eq:`equal <0012.g1:< A D G ) = 0012.g1:< G D B )>` to the angle :g:`< G D B ) <0012.g1:< G D B )>`.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; :just:`[G.18] <G.18>`

.. assertion::

   therefore the angle :g:`< G D B ) <0012.g1:< G D B )>` is right.

But the angle :g:`< F D B ) <0012.g1:< F D B )>` is also right; therefore the angle :g:`< F D B ) <0012.g1:< F D B )>` is :eq:`equal <0012.g1:< F D B ) = 0012.g1:< G D B )>` to the angle :g:`< G D B ) <0012.g1:< G D B )>`, the greater to the less: which is impossible.

.. assertion::

   Therefore :g:`G <0012.g1:G>` is not the centre of the circle :g:`( A B C ) <0012.g1:( A B C )>`.

Similarly we can prove that neither is any other point except :g:`F <0012.g1:F>`.

.. assertion::

   Therefore the point :g:`F <0012.g1:F>` is the centre of the circle :g:`( A B C ) <0012.g1:( A B C )>`.

.. enunciation::

   PORISM. From this it is manifest that, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line.

.. qed::

   Q. E. F.

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
     "G.76" [label="G.76", tooltip="G.76 (III.1): To find the centre of a given circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.76" -> "G.18";
   }

Required for
------------

:ref:`G.77 <G.77>`, :ref:`G.79 <G.79>`, :ref:`G.83 <G.83>`, :ref:`G.84 <G.84>`, :ref:`G.85 <G.85>`, :ref:`G.89 <G.89>`, :ref:`G.91 <G.91>`, :ref:`G.93 <G.93>`, :ref:`G.95 <G.95>`, :ref:`G.103 <G.103>`, :ref:`G.104 <G.104>`, :ref:`G.105 <G.105>`, :ref:`G.106 <G.106>`, :ref:`G.107 <G.107>`, :ref:`G.108 <G.108>`, :ref:`G.109 <G.109>`, :ref:`G.119 <G.119>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.198 <G.198>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.519 <G.519>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`
