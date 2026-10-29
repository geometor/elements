:order: 20
:number: 20
:canonical_id: G.20
:original_id: I.12
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, line, circle, angle, perpendicular, equality
:dependencies: G.3, G.4, G.15, G.17, G.18
:excerpt: To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

.. _G.20:
.. _I.12:

G.20
====

.. rubric:: `I.12 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/12/>`_

.. enunciation::

   To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

Let :g:`[ A B ] <0285.g1:[ A B ]>` be the given infinite straight line, and :g:`C <0285.g1:C>` the given point which is not on it;

.. picture:: 0285.g1.svg
   :alt: Proposition 12 figure

thus it is required to draw to the given infinite straight line :g:`[ A B ] <0285.g1:[ A B ]>`, from the given point :g:`C <0285.g1:C>` which is not on it, a perpendicular straight line.

For let a point :g:`D <0285.g1:D>` be taken at random on the other side of the straight line :g:`[ A B ] <0285.g1:[ A B ]>`, and with centre :g:`C <0285.g1:C>` and distance :g:`/ C D / <0285.g1:/ C D />` let the circle :g:`( C D ) <0285.g1:( C D )>` be described; :just:`[G.4] <G.4>`

let the straight line :g:`/ E G / <0285.g1:/ E G />` be :eq:`bisected <0285.g1:/ G H / = 0285.g1:/ H E />` at :g:`H <0285.g1:H>`, :just:`[G.17] <G.17>`

and let the straight lines :g:`/ C G / <0285.g1:/ C G />`, :g:`/ C H / <0285.g1:/ C H />`, :g:`/ C E / <0285.g1:/ C E />` be joined. :just:`[G.3] <G.3>`

I say that :g:`/ C H / <0285.g1:/ C H />` has been drawn :eq:`perpendicular <0285.g1:< C H G ) = 0285.g1:< E H C )>` to the given infinite straight line :g:`[ A B ] <0285.g1:[ A B ]>` from the given point :g:`C <0285.g1:C>` which is not on it.

For, since :g:`/ G H / <0285.g1:/ G H />` is :eq:`equal <0285.g1:/ G H / = 0285.g1:/ H E />` to :g:`/ H E / <0285.g1:/ H E />`, and :g:`/ H C / <0285.g1:/ H C />` is common,

.. assertion::

   the two sides :g:`/ G H / <0285.g1:/ G H />`, :g:`/ H C / <0285.g1:/ H C />` are :eq:`equal <0285.g1:/ G H / = 0285.g1:/ E H />` to the two sides :g:`/ E H / <0285.g1:/ E H />`, :g:`/ H C / <0285.g1:/ H C />` respectively;

and the base :g:`/ C G / <0285.g1:/ C G />` is :eq:`equal <0285.g1:/ C G / = 0285.g1:/ C E />` to the base :g:`/ C E / <0285.g1:/ C E />`;

.. assertion:: [G.15] <G.15>

   therefore the angle :g:`< C H G ) <0285.g1:< C H G )>` is :eq:`equal <0285.g1:< C H G ) = 0285.g1:< E H C )>` to the angle :g:`< E H C ) <0285.g1:< E H C )>`.

And they are adjacent angles.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is called a perpendicular to that on which it stands. :just:`[G.18] <G.18>`

Therefore :g:`/ C H / <0285.g1:/ C H />` has been drawn :eq:`perpendicular <0285.g1:< C H G ) = 0285.g1:< E H C )>` to the given infinite straight line :g:`[ A B ] <0285.g1:[ A B ]>` from the given point :g:`C <0285.g1:C>` which is not on it.

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
     "G.16" [label="G.16", tooltip="G.16 (I.9): To bisect a given rectilineal angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): To bisect a given finite straight line.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is cal...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.20" [label="G.20", tooltip="G.20 (I.12): To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.20" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.20" -> "G.4";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.20" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.17";
     "G.20" -> "G.18";
   }

Required for
------------

:ref:`G.454 <G.454>`, :ref:`G.455 <G.455>`, :ref:`G.459 <G.459>`, :ref:`G.468 <G.468>`, :ref:`G.471 <G.471>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.520 <G.520>`, :ref:`G.521 <G.521>`, :ref:`G.525 <G.525>`
