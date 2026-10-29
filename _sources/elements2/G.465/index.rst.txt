:order: 465
:number: 465
:canonical_id: G.465
:original_id: XI.20
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, plane, solid-angle, equality
:dependencies: G.11, G.31, G.36
:excerpt: If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

.. _G.465:
.. _XI.20:

G.465
=====

.. rubric:: `XI.20 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/20/>`_

.. enunciation::

   If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

For let the solid angle at :g:`A <0311.g3:A>` be contained by the three plane angles :g:`< B A C ) <0311.g3:< B A C )>`, :g:`< C A D ) <0311.g3:< C A D )>`, :g:`< D A B ) <0311.g3:< D A B )>`; I say that any two of the angles :g:`< B A C ) <0311.g3:< B A C )>`, :g:`< C A D ) <0311.g3:< C A D )>`, :g:`< D A B ) <0311.g3:< D A B )>`, taken together in any manner, are greater than the remaining one.

.. picture:: 0311.g3.svg
   :alt: Book XI, Proposition 20

.. subclause::

   If now the angles :g:`< B A C ) <0311.g3:< B A C )>`, :g:`< C A D ) <0311.g3:< C A D )>`, :g:`< D A B ) <0311.g3:< D A B )>` are :eq:`equal <0311.g3:< B A C ) = 0311.g3:< C A D ) = 0311.g3:< D A B )>` to one another,

.. assertion::

   it is manifest that any two are greater than the remaining one.

.. subclause::

   But, if not, let :g:`< B A C ) <0311.g3:< B A C )>` be greater,

and on the straight line :g:`/ A B / <0311.g3:/ A B />`, and at the point :g:`A <0311.g3:A>` on it, let the
angle :g:`< B A E ) <0311.g3:< B A E )>` be constructed, in the plane through :g:`/ B A / <0311.g3:/ B A />`, :g:`/ A C / <0311.g3:/ A C />`, :eq:`equal <0311.g3:< B A E ) = 0311.g3:< D A B )>` to the angle :g:`< D A B ) <0311.g3:< D A B )>`; let :g:`/ A E / <0311.g3:/ A E />` be made :eq:`equal <0311.g3:/ A E / = 0311.g3:/ A D />` to :g:`/ A D / <0311.g3:/ A D />`, and let :g:`/ B E C / <0311.g3:/ B E C />`, drawn across through the point :g:`E <0311.g3:E>`, cut the straight lines :g:`/ A B / <0311.g3:/ A B />`, :g:`/ A C / <0311.g3:/ A C />` at the points :g:`B <0311.g3:B>`, :g:`C <0311.g3:C>`; let :g:`/ D B / <0311.g3:/ D B />`, :g:`/ D C / <0311.g3:/ D C />` be joined.

.. subclause::

   Now, since :g:`/ D A / <0311.g3:/ D A />` is :eq:`equal <0311.g3:/ D A / = 0311.g3:/ A E />` to :g:`/ A E / <0311.g3:/ A E />`, and :g:`/ A B / <0311.g3:/ A B />` is common, two sides are :eq:`equal <0311.g3:/ D A / = 0311.g3:/ A E />` to two sides ; and the angle :g:`< D A B ) <0311.g3:< D A B )>` is :eq:`equal <0311.g3:< D A B ) = 0311.g3:< B A E )>` to the angle :g:`< B A E ) <0311.g3:< B A E )>`;

.. assertion:: [G.11] <G.11>

   therefore the base :g:`/ D B / <0311.g3:/ D B />` is :eq:`equal <0311.g3:/ D B / = 0311.g3:/ B E />` to the base :g:`/ B E / <0311.g3:/ B E />`.

.. subclause::

   And, since the two sides :g:`/ B D / <0311.g3:/ B D />`, :g:`/ D C / <0311.g3:/ D C />` are greater than :g:`/ B C / <0311.g3:/ B C />`, :just:`[G.31] <G.31>` and of these :g:`/ D B / <0311.g3:/ D B />` was proved :eq:`equal <0311.g3:/ D B / = 0311.g3:/ B E />` to :g:`/ B E / <0311.g3:/ B E />`,

.. assertion::

   therefore the remainder :g:`/ D C / <0311.g3:/ D C />` is greater than the remainder :g:`/ E C / <0311.g3:/ E C />`.

.. subclause::

   Now, since :g:`/ D A / <0311.g3:/ D A />` is :eq:`equal <0311.g3:/ D A / = 0311.g3:/ A E />` to :g:`/ A E / <0311.g3:/ A E />`, and :g:`/ A C / <0311.g3:/ A C />` is common, and the base :g:`/ D C / <0311.g3:/ D C />` is greater than the base :g:`/ E C / <0311.g3:/ E C />`,

.. assertion::

   therefore the angle :g:`< D A C ) <0311.g3:< D A C )>` is greater than the angle :g:`< E A C ) <0311.g3:< E A C )>`. :just:`[G.36] <G.36>`

.. subclause::

   But the angle :g:`< D A B ) <0311.g3:< D A B )>` was also proved :eq:`equal <0311.g3:< D A B ) = 0311.g3:< B A E )>` to the angle :g:`< B A E ) <0311.g3:< B A E )>` ;

.. assertion::

   therefore the angles :g:`< D A B ) <0311.g3:< D A B )>`, :g:`< D A C ) <0311.g3:< D A C )>` are greater than the angle :g:`< B A C ) <0311.g3:< B A C )>`.

Similarly we can prove that the remaining angles also, taken together two and two, are greater than the remaining one.

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
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle two sides taken together in any manner are greater than the remaining one.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manne...", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.24): If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also hav...", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.25): If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal strai...", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.465" [label="G.465", tooltip="G.465 (XI.20): If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.29" -> "G.9";
     "G.33" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.35" -> "G.11";
     "G.36" -> "G.11";
     "G.465" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.35" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.35" -> "G.30";
     "G.33" -> "G.31";
     "G.465" -> "G.31";
     "G.34" -> "G.33";
     "G.35" -> "G.34";
     "G.36" -> "G.35";
     "G.465" -> "G.36";
   }

Required for
------------

:ref:`G.466 <G.466>`
