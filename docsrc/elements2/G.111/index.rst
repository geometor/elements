:order: 111
:number: 111
:canonical_id: G.111
:original_id: III.32
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, quadrilateral, tangent, equality
:dependencies: G.45, G.97, G.100, G.110
:excerpt: If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

.. _G.111:
.. _III.32:

G.111
=====

.. rubric:: `III.32 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/32/>`_

.. enunciation::

   If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

For let a straight line :g:`/ E F / <0072.g1:/ E F />` touch the circle :g:`( A B C D ) <0072.g1:( A B C D )>` at
the point :g:`B <0072.g1:B>`, and from the point :g:`B <0072.g1:B>` let there be drawn across,
in the circle :g:`( A B C D ) <0072.g1:( A B C D )>`, a straight line :g:`/ B D / <0072.g1:/ B D />` cutting it;
I say that the angles which :g:`/ B D / <0072.g1:/ B D />` makes with the tangent :g:`/ E F / <0072.g1:/ E F />`
will be equal to the angles in the alternate segments of the
circle, that is, that the angle :g:`< F B D ) <0072.g1:< F B D )>` is equal to the angle
constructed in the segment :g:`( B A D ) <0072.g1:( B A D )>`, and the angle :g:`< E B D ) <0072.g1:< E B D )>` is
equal to the angle constructed in the
segment :g:`( D C B ) <0072.g1:( D C B )>`.

.. picture:: 0072.g1.svg
   :alt: Proposition 32 diagram

For let :g:`/ B A / <0072.g1:/ B A />` be drawn from :g:`B <0072.g1:B>` at
right angles to :g:`/ E F / <0072.g1:/ E F />`,
let a point :g:`C <0072.g1:C>` be taken at random on
the circumference :g:`( B D ) <0072.g1:( B D )>`,
and let :g:`/ A D / <0072.g1:/ A D />`, :g:`/ D C / <0072.g1:/ D C />`, :g:`/ C B / <0072.g1:/ C B />` be joined.

Then, since a straight line :g:`/ E F / <0072.g1:/ E F />`
touches the circle :g:`( A B C D ) <0072.g1:( A B C D )>` at :g:`B <0072.g1:B>`,
and :g:`/ B A / <0072.g1:/ B A />` has been drawn from the point
of contact at right angles to the tangent,
the centre of the circle :g:`( A B C D ) <0072.g1:( A B C D )>` is on :g:`/ B A / <0072.g1:/ B A />`. :just:`[G.97] <G.97>`

Therefore :g:`/ B A / <0072.g1:/ B A />` is a diameter of the circle :g:`( A B C D ) <0072.g1:( A B C D )>`;
therefore the angle :g:`< A D B ) <0072.g1:< A D B )>`, being an angle in a semicircle,
is right. :just:`[G.110] <G.110>`

Therefore the remaining angles :g:`< B A D ) <0072.g1:< B A D )>`, :g:`< A B D ) <0072.g1:< A B D )>` are equal to
one right angle. :just:`[G.45] <G.45>`

But the angle :g:`< A B F ) <0072.g1:< A B F )>` is also right;
therefore the angle :g:`< A B F ) <0072.g1:< A B F )>` is equal to the angles :g:`< B A D ) <0072.g1:< B A D )>`, :g:`< A B D ) <0072.g1:< A B D )>`.

Let the angle :g:`< A B D ) <0072.g1:< A B D )>` be subtracted from each;
therefore the angle :g:`< D B F ) <0072.g1:< D B F )>` which remains is :eq:`equal <0072.g1:< D B F ) = 0072.g1:< B A D )>` to the angle
:g:`< B A D ) <0072.g1:< B A D )>` in the alternate segment of the circle.

Next, since :g:`< A B C D > <0072.g1:< A B C D >>` is a quadrilateral in a circle,
its opposite angles are equal to two right angles. :just:`[G.100] <G.100>`

But the angles :g:`< D B F ) <0072.g1:< D B F )>`, :g:`< D B E ) <0072.g1:< D B E )>` are also equal to two right
angles;
therefore the angles :g:`< D B F ) <0072.g1:< D B F )>`, :g:`< D B E ) <0072.g1:< D B E )>` are equal to the angles
:g:`< B A D ) <0072.g1:< B A D )>`, :g:`< B C D ) <0072.g1:< B C D )>`,

.. subclause::

   of which the angle :g:`< B A D ) <0072.g1:< B A D )>` was proved :eq:`equal <0072.g1:< B A D ) = 0072.g1:< D B F )>` to the angle :g:`< D B F ) <0072.g1:< D B F )>`;

therefore the angle :g:`< D B E ) <0072.g1:< D B E )>` which remains is :eq:`equal <0072.g1:< D B E ) = 0072.g1:< D C B )>` to the
angle :g:`< D C B ) <0072.g1:< D C B )>` in the alternate segment :g:`( D C B ) <0072.g1:( D C B )>` of the circle.

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
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle two angles taken together in any manner are less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle two sides taken together in any manner are greater than the remaining one.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manne...", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet ...", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior an...", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Through a given point to draw a straight line parallel to a given straight line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.32): In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to tw...", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.96" [label="G.96", tooltip="G.96 (III.18): If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.", fillcolor="#222244", URL="../G.96/index.html", target="_top"];
     "G.97" [label="G.97", tooltip="G.97 (III.19): If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle will be on the straight line so d...", fillcolor="#222244", URL="../G.97/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.20): In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.99" [label="G.99", tooltip="G.99 (III.21): In a circle the angles in the same segment are equal to one another.", fillcolor="#222244", URL="../G.99/index.html", target="_top"];
     "G.100" [label="G.100", tooltip="G.100 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.100/index.html", target="_top"];
     "G.110" [label="G.110", tooltip="G.110 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.110/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.32): If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangen...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
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
     "G.28" -> "G.7";
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
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.98" -> "G.12";
     "G.110" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.110" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.39" -> "G.27";
     "G.96" -> "G.28";
     "G.110" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.96" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.45" -> "G.42";
     "G.45" -> "G.44";
     "G.98" -> "G.45";
     "G.100" -> "G.45";
     "G.110" -> "G.45";
     "G.111" -> "G.45";
     "G.97" -> "G.96";
     "G.111" -> "G.97";
     "G.99" -> "G.98";
     "G.100" -> "G.99";
     "G.110" -> "G.100";
     "G.111" -> "G.100";
     "G.111" -> "G.110";
   }

Required for
------------

:ref:`G.112 <G.112>`, :ref:`G.113 <G.113>`, :ref:`G.118 <G.118>`, :ref:`G.128 <G.128>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.520 <G.520>`, :ref:`G.525 <G.525>`
