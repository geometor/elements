:order: 32
:number: 32
:canonical_id: G.32
:original_id: I.21
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, line, angle, triangle
:dependencies: G.27, G.31
:excerpt: If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greater angle.

.. _G.32:
.. _I.21:

G.32
====

.. rubric:: `I.21 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/21/>`_

.. enunciation::

   If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greater angle.

On :g:`/ B C / <0303.g1:/ B C />`, one of the sides of the triangle :g:`< A B C > <0303.g1:< A B C >>`, from its extremities :g:`B <0303.g1:B>`, :g:`C <0303.g1:C>`, let the two straight lines :g:`/ B D / <0303.g1:/ B D />`, :g:`/ D C / <0303.g1:/ D C />` be constructed meeting within the triangle;

I say that :g:`/ B D / <0303.g1:/ B D />`, :g:`/ D C / <0303.g1:/ D C />` are less than the remaining two sides of the triangle :g:`/ B A / <0303.g1:/ B A />`, :g:`/ A C / <0303.g1:/ A C />`, but contain an angle :g:`< B D C ) <0303.g1:< B D C )>` greater than the angle :g:`< B A C ) <0303.g1:< B A C )>`.

.. picture:: 0303.g1.svg
   :alt: Folio 0303 Figure 1 - Proposition 21

For let :g:`[ B D ] <0303.g1:[ B D ]>` be drawn through to :g:`E <0303.g1:E>`. Then, since in any triangle two sides are greater than the remaining one, :just:`[G.31] <G.31>`

.. assertion::

   therefore, in the triangle :g:`< A B E > <0303.g1:< A B E >>`, the two sides :g:`/ A B / <0303.g1:/ A B />`, :g:`/ A E / <0303.g1:/ A E />` are greater than :g:`/ B E / <0303.g1:/ B E />`.

.. subclause::

   Let :g:`/ E C / <0303.g1:/ E C />` be added to each;

.. assertion::

   therefore :g:`/ B A / <0303.g1:/ B A />`, :g:`/ A C / <0303.g1:/ A C />` are greater than :g:`/ B E / <0303.g1:/ B E />`, :g:`/ E C / <0303.g1:/ E C />`.

Again, since, in the triangle :g:`< C E D > <0303.g1:< C E D >>`,

.. assertion::

   the two sides :g:`/ C E / <0303.g1:/ C E />`, :g:`/ E D / <0303.g1:/ E D />` are greater than :g:`/ C D / <0303.g1:/ C D />`,

.. subclause::

   let :g:`/ D B / <0303.g1:/ D B />` be added to each;

.. assertion::

   therefore :g:`/ C E / <0303.g1:/ C E />`, :g:`/ E B / <0303.g1:/ E B />` are greater than :g:`/ C D / <0303.g1:/ C D />`, :g:`/ D B / <0303.g1:/ D B />`.

But :g:`/ B A / <0303.g1:/ B A />`, :g:`/ A C / <0303.g1:/ A C />` were proved greater than :g:`/ B E / <0303.g1:/ B E />`, :g:`/ E C / <0303.g1:/ E C />`;

.. assertion::

   therefore :g:`/ B A / <0303.g1:/ B A />`, :g:`/ A C / <0303.g1:/ A C />` are much greater than :g:`/ B D / <0303.g1:/ B D />`, :g:`/ D C / <0303.g1:/ D C />`.

Again, since in any triangle the exterior angle is greater than the interior and opposite angle, :just:`[G.27] <G.27>`

therefore, in the triangle :g:`< C D E > <0303.g1:< C D E >>`,

.. assertion::

   the exterior angle :g:`< B D C ) <0303.g1:< B D C )>` is greater than the angle :g:`< C E D ) <0303.g1:< C E D )>`.

For the same reason, moreover, in the triangle :g:`< A B E > <0303.g1:< A B E >>` also,

.. assertion::

   the exterior angle :g:`< C E B ) <0303.g1:< C E B )>` is greater than the angle :g:`< B A C ) <0303.g1:< B A C )>`.

But the angle :g:`< B D C ) <0303.g1:< B D C )>` was proved greater than the angle :g:`< C E B ) <0303.g1:< C E B )>`;

.. assertion::

   therefore the angle :g:`< B D C ) <0303.g1:< B D C )>` is much greater than the angle :g:`< B A C ) <0303.g1:< B A C )>`.

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
     "G.32" [label="G.32", tooltip="G.32 (I.21): If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
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
     "G.32" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.32" -> "G.31";
   }

Required for
------------

:ref:`G.83 <G.83>`
