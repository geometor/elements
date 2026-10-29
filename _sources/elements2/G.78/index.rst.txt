:order: 78
:number: 78
:canonical_id: G.78
:original_id: III.3
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, triangle, right-angle, bisect, equality
:dependencies: G.12, G.15, G.18, G.37
:excerpt: If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

.. _G.78:
.. _III.3:

G.78
====

.. rubric:: `III.3 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/03/>`_

.. enunciation::

   If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

Let :g:`( A B C ) <0016.g1:( A B C )>` be a circle, and in it let a straight line :g:`/ C D / <0016.g1:/ C D />` through the centre :eq:`bisect <0016.g1:/ A F / = 0016.g1:/ F B />` a straight line :g:`/ A B / <0016.g1:/ A B />` not through the centre at the point :g:`F <0016.g1:F>`;

I say that it also cuts it at :eq:`right angles <0016.g1:< A F E ) = 0016.g1:< B F E )>`.

.. picture:: 0016.g1.svg
   :alt: Proposition 3

For let the centre of the circle :g:`( A B C ) <0016.g1:( A B C )>` be taken, and let it be :g:`E <0016.g1:E>`; let :g:`/ E A / <0016.g1:/ E A />`, :g:`/ E B / <0016.g1:/ E B />` be joined.

Then, since :g:`/ A F / <0016.g1:/ A F />` is :eq:`equal <0016.g1:/ A F / = 0016.g1:/ F B />` to :g:`/ F B / <0016.g1:/ F B />`, and :g:`/ F E / <0016.g1:/ F E />` is common,

.. subclause::

   two sides are :eq:`equal <0016.g1:/ A F / = 0016.g1:/ F B />` to two sides;

and the base :g:`/ E A / <0016.g1:/ E A />` is :eq:`equal <0016.g1:/ E A / = 0016.g1:/ E B />` to the base :g:`/ E B / <0016.g1:/ E B />`;

.. assertion:: [G.15] <G.15>

   therefore the angle :g:`< A F E ) <0016.g1:< A F E )>` is :eq:`equal <0016.g1:< A F E ) = 0016.g1:< B F E )>` to the angle :g:`< B F E ) <0016.g1:< B F E )>`.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; :just:`[G.18] <G.18>`

.. assertion::

   therefore each of the angles :g:`< A F E ) <0016.g1:< A F E )>`, :g:`< B F E ) <0016.g1:< B F E )>` is :eq:`right <0016.g1:< A F E ) = 0016.g1:< B F E )>`.

.. assertion::

   Therefore :g:`/ C D / <0016.g1:/ C D />`, which is through the centre, and :eq:`bisects <0016.g1:/ A F / = 0016.g1:/ F B />` :g:`/ A B / <0016.g1:/ A B />` which is not through the centre, also cuts it at :eq:`right angles <0016.g1:< A F E ) = 0016.g1:< B F E )>`.

Again, let :g:`/ C D / <0016.g1:/ C D />` cut :g:`/ A B / <0016.g1:/ A B />` at :eq:`right angles <0016.g1:< A F E ) = 0016.g1:< B F E )>`;

I say that it also :eq:`bisects <0016.g1:/ A F / = 0016.g1:/ F B />` it, that is, that :g:`/ A F / <0016.g1:/ A F />` is :eq:`equal <0016.g1:/ A F / = 0016.g1:/ F B />` to :g:`/ F B / <0016.g1:/ F B />`.

For, with the same construction,

.. subclause::

   since :g:`/ E A / <0016.g1:/ E A />` is :eq:`equal <0016.g1:/ E A / = 0016.g1:/ E B />` to :g:`/ E B / <0016.g1:/ E B />`,

the angle :g:`< E A F ) <0016.g1:< E A F )>` is also :eq:`equal <0016.g1:< E A F ) = 0016.g1:< E B F )>` to the angle :g:`< E B F ) <0016.g1:< E B F )>`. :just:`[G.12] <G.12>`

But the right angle :g:`< A F E ) <0016.g1:< A F E )>` is :eq:`equal <0016.g1:< A F E ) = 0016.g1:< B F E )>` to the right angle :g:`< B F E ) <0016.g1:< B F E )>`, therefore :g:`< E A F > <0016.g1:< E A F >>`, :g:`< E B F > <0016.g1:< E B F >>` are two triangles having two angles :eq:`equal <0016.g1:< E A F ) = 0016.g1:< E B F ); 0016.g1:< A F E ) = 0016.g1:< B F E )>` to two angles and one side equal to one side, namely :g:`/ E F / <0016.g1:/ E F />`, which is common to them, and subtends one of the :eq:`equal <0016.g1:< E A F ) = 0016.g1:< E B F )>` angles; therefore they will also have the remaining sides :eq:`equal <0016.g1:/ A F / = 0016.g1:/ F B /; 0016.g1:/ E A / = 0016.g1:/ E B />` to the remaining sides; :just:`[G.37] <G.37>`

.. assertion::

   therefore :g:`/ A F / <0016.g1:/ A F />` is :eq:`equal <0016.g1:/ A F / = 0016.g1:/ F B />` to :g:`/ F B / <0016.g1:/ F B />`.

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
     "G.16" [label="G.16", tooltip="G.16 (I.9): To bisect a given rectilineal angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): To bisect a given finite straight line.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is cal...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): To draw a straight line at right angles to a given straight line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals be added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): That all right angles are equal to one another.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): If two straight lines cut one another, they make the vertical angles equal to one another.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): [8] 5. The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of...", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
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
