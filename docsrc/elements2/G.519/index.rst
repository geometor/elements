:order: 519
:number: 519
:canonical_id: G.519
:original_id: XIII.12
:volume: III
:book: XIII
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry, regular-solids
:category: theorem, proof, solid-geometry, regular-solids
:tags: book-xiii, point, segment, circle, triangle, separando, equilateral, square, inscribed, equality
:dependencies: G.60, G.110, G.133
:excerpt: *If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.*

.. _G.519:
.. _XIII.12:

G.519
=====

.. rubric:: `XIII.12 <https://geometor.github.io/euclid/heath/volume_III/book_xiii/propositions/12/>`_

.. enunciation::

   *If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.*

Let :g:`( A B C ) <0471.g1:( A B C )>` be a circle, and let the :eq:`equilateral <0471.g1:/ A B / = 0471.g1:/ B C / = 0471.g1:/ C A />` triangle :g:`< A B C > <0471.g1:< A B C >>` be inscribed in it; I say that the square on one side of the triangle :g:`< A B C > <0471.g1:< A B C >>` is triple of the square on the radius of the circle.

.. picture:: 0471.g1.svg
   :alt: Proposition 12 Diagram

For let the centre :g:`D <0471.g1:D>` of the circle :g:`( A B C ) <0471.g1:( A B C )>` be taken, let :g:`/ A D / <0471.g1:/ A D />` be joined and carried through to :g:`E <0471.g1:E>`, and let :g:`/ B E / <0471.g1:/ B E />` be joined.

.. subclause::

   Then, since the triangle :g:`< A B C > <0471.g1:< A B C >>` is :eq:`equilateral <0471.g1:/ A B / = 0471.g1:/ B C / = 0471.g1:/ C A />`,

.. assertion::

   therefore the circumference :g:`( B E C ) <0471.g1:( B E C )>` is a third part of the circumference of the circle :g:`( A B C ) <0471.g1:( A B C )>`.

.. assertion::

   Therefore the circumference :g:`( B E ) <0471.g1:( B E )>` is a sixth part of the circumference of the circle; therefore the straight line :g:`/ B E / <0471.g1:/ B E />` belongs to a hexagon; therefore it is :eq:`equal <0471.g1:/ B E / = 0471.g1:/ D E />` to the radius :g:`/ D E / <0471.g1:/ D E />`. :just:`[G.133] <G.133>`

.. subclause::

   And, since :g:`/ A E / <0471.g1:/ A E />` is double of :g:`/ D E / <0471.g1:/ D E />`,

.. assertion::

   the square on :g:`/ A E / <0471.g1:/ A E />` is quadruple of the square on :g:`/ E D / <0471.g1:/ E D />`, that is, of the square on :g:`/ B E / <0471.g1:/ B E />`.

.. subclause::

   But the square on :g:`/ A E / <0471.g1:/ A E />` is equal to the squares on :g:`/ A B / <0471.g1:/ A B />`, :g:`/ B E / <0471.g1:/ B E />`; :just:`[G.110, G.60] <G.110, G.60>`

.. assertion::

   therefore the squares on :g:`/ A B / <0471.g1:/ A B />`, :g:`/ B E / <0471.g1:/ B E />` are quadruple of the square on :g:`/ B E / <0471.g1:/ B E />`.

.. assertion::

   Therefore, :term:`*separando* <separando>`, the square on :g:`/ A B / <0471.g1:/ A B />` is triple of the square on :g:`/ B E / <0471.g1:/ B E />`.

.. subclause::

   But :g:`/ B E / <0471.g1:/ B E />` is :eq:`equal <0471.g1:/ B E / = 0471.g1:/ D E />` to :g:`/ D E / <0471.g1:/ D E />`;

.. assertion::

   therefore the square on :g:`/ A B / <0471.g1:/ A B />` is triple of the square on :g:`/ D E / <0471.g1:/ D E />`.

.. assertion::

   Therefore the square on the side of the triangle is triple of the square on the radius.

.. qed::

   :just:`Q. E. D.`

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
     "G.24" [label="G.24", tooltip="G.24 (I.14): If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in...", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): If two straight lines cut one another, they make the vertical angles equal to one another.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): [8] 5. The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle two angles taken together in any manner are less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle two sides taken together in any manner are greater than the remaining one.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manne...", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of...", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet ...", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior an...", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Through a given point to draw a straight line parallel to a given straight line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.32): In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to tw...", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms which are on the same base and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles which are on the same base and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): On a given straight line to describe a square.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.47): In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): To find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.85/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.20): In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.99" [label="G.99", tooltip="G.99 (III.21): In a circle the angles in the same segment are equal to one another.", fillcolor="#222244", URL="../G.99/index.html", target="_top"];
     "G.100" [label="G.100", tooltip="G.100 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.100/index.html", target="_top"];
     "G.101" [label="G.101", tooltip="G.101 (III.def.11): Similar segments of circles are those which admit equal angles, or in which the angles are equal to one another.", fillcolor="#224422", URL="../G.101/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.24): Similar segments of circles on equal straight lines are equal to one another.", fillcolor="#222244", URL="../G.103/index.html", target="_top"];
     "G.105" [label="G.105", tooltip="G.105 (III.26): In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.105/index.html", target="_top"];
     "G.106" [label="G.106", tooltip="G.106 (III.27): In equal circles angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.106/index.html", target="_top"];
     "G.108" [label="G.108", tooltip="G.108 (III.29): In equal circles equal circumferences are subtended by equal straight lines.", fillcolor="#222244", URL="../G.108/index.html", target="_top"];
     "G.110" [label="G.110", tooltip="G.110 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.110/index.html", target="_top"];
     "G.133" [label="G.133", tooltip="G.133 (IV.15): In a given circle to inscribe an equilateral and equiangular hexagon.", fillcolor="#222244", URL="../G.133/index.html", target="_top"];
     "G.519" [label="G.519", tooltip="G.519 (XIII.12): *If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.*", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.80" -> "G.2";
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
     "G.24" -> "G.6";
     "G.25" -> "G.6";
     "G.48" -> "G.6";
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
     "G.37" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.105" -> "G.11";
     "G.108" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.98" -> "G.12";
     "G.110" -> "G.12";
     "G.133" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.76" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.76" -> "G.18";
     "G.110" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.60" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.60" -> "G.24";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.133" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.110" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.106" -> "G.34";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.45" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.45" -> "G.44";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.98" -> "G.45";
     "G.100" -> "G.45";
     "G.110" -> "G.45";
     "G.133" -> "G.45";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.50" -> "G.48";
     "G.54" -> "G.50";
     "G.60" -> "G.54";
     "G.60" -> "G.59";
     "G.519" -> "G.60";
     "G.85" -> "G.76";
     "G.85" -> "G.80";
     "G.103" -> "G.85";
     "G.99" -> "G.98";
     "G.106" -> "G.98";
     "G.100" -> "G.99";
     "G.110" -> "G.100";
     "G.105" -> "G.101";
     "G.105" -> "G.103";
     "G.106" -> "G.105";
     "G.133" -> "G.105";
     "G.108" -> "G.106";
     "G.133" -> "G.106";
     "G.133" -> "G.108";
     "G.519" -> "G.110";
     "G.519" -> "G.133";
   }

Required for
------------

:ref:`G.520 <G.520>`, :ref:`G.525 <G.525>`
