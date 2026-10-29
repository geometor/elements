:order: 67
:number: 67
:canonical_id: G.67
:original_id: II.6
:volume: I
:book: II
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, geometric-algebra
:category: theorem, proof, plane-geometry, geometric-algebra
:tags: book-ii, point, segment, triangle, quadrilateral, polygon, square, rectangle, bisect, equality
:dependencies: G.44, G.49, G.56, G.59
:excerpt: If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line together with the square on the half is equal to the square on the straight line made up of the half and the added straight line.

.. _G.67:
.. _II.6:

G.67
====

.. rubric:: `II.6 <https://geometor.github.io/euclid/heath/volume_I/book_ii/propositions/06/>`_

.. enunciation::

   If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line together with the square on the half is equal to the square on the straight line made up of the half and the added straight line.

For let a straight line :g:`/ A B / <0400.g1:/ A B />` be :eq:`bisected <0400.g1:/ A C / = 0400.g1:/ C B />` at the point :g:`C <0400.g1:C>`, and let a straight line :g:`/ B D / <0400.g1:/ B D />` be added to it in a straight line;

I say that the rectangle contained by :g:`/ A D / <0400.g1:/ A D />`, :g:`/ D B / <0400.g1:/ D B />` together with the square on :g:`/ C B / <0400.g1:/ C B />` is equal to the square on :g:`/ C D / <0400.g1:/ C D />`.

For let the square :g:`< C E F D > <0400.g1:< C E F D >>` be described on :g:`/ C D / <0400.g1:/ C D />`, :just:`[G.59] <G.59>`

and let :g:`/ D E / <0400.g1:/ D E />` be joined;

through the point :g:`B <0400.g1:B>` let :g:`/ B G / <0400.g1:/ B G />` be drawn parallel to either :g:`/ E C / <0400.g1:/ E C />` or :g:`/ D F / <0400.g1:/ D F />`,
through the point :g:`H <0400.g1:H>` let :g:`/ K M / <0400.g1:/ K M />` be drawn parallel to either :g:`/ A B / <0400.g1:/ A B />` or :g:`/ E F / <0400.g1:/ E F />`, and further through :g:`A <0400.g1:A>` let :g:`/ A K / <0400.g1:/ A K />` be drawn parallel to either :g:`/ C L / <0400.g1:/ C L />` or :g:`/ D M / <0400.g1:/ D M />`. :just:`[G.44] <G.44>`

.. picture:: 0400.g1.svg
   :alt: Diagram

Then, since :g:`/ A C / <0400.g1:/ A C />` is :eq:`equal <0400.g1:/ A C / = 0400.g1:/ C B />` to :g:`/ C B / <0400.g1:/ C B />`,

.. assertion:: [G.49] <G.49>

   :g:`< A L > <0400.g1:< A L >>` is also :eq:`equal <0400.g1:< A L > = 0400.g1:< C H >>` to :g:`< C H > <0400.g1:< C H >>`.

But :g:`< C H > <0400.g1:< C H >>` is :eq:`equal <0400.g1:< C H > = 0400.g1:< H F >>` to :g:`< H F > <0400.g1:< H F >>`. :just:`[G.56] <G.56>`

.. assertion::

   Therefore :g:`< A L > <0400.g1:< A L >>` is also :eq:`equal <0400.g1:< A L > = 0400.g1:< H F >>` to :g:`< H F > <0400.g1:< H F >>`.

Let :g:`< C M > <0400.g1:< C M >>` be added to each;

.. assertion::

   therefore the whole :g:`< A M > <0400.g1:< A M >>` is :eq:`equal <0400.g1:< A M > = 0400.g1:< N O P >>` to the gnomon :g:`< N O P > <0400.g1:< N O P >>`.

But :g:`< A M > <0400.g1:< A M >>` is the rectangle :g:`/ A D / <0400.g1:/ A D />`, :g:`/ D B / <0400.g1:/ D B />`, for :g:`/ D M / <0400.g1:/ D M />` is :eq:`equal <0400.g1:/ D M / = 0400.g1:/ D B />` to :g:`/ D B / <0400.g1:/ D B />`;

.. assertion::

   therefore the gnomon :g:`< N O P > <0400.g1:< N O P >>` is also equal to the rectangle :g:`/ A D / <0400.g1:/ A D />`, :g:`/ D B / <0400.g1:/ D B />`.

Let :g:`< L G > <0400.g1:< L G >>`, which is equal to the square on :g:`/ B C / <0400.g1:/ B C />`, be added to each;

.. assertion::

   therefore the rectangle contained by :g:`/ A D / <0400.g1:/ A D />`, :g:`/ D B / <0400.g1:/ D B />` together with the square on :g:`/ C B / <0400.g1:/ C B />` is equal to the gnomon :g:`< N O P > <0400.g1:< N O P >>` and :g:`< L G > <0400.g1:< L G >>`.

But the gnomon :g:`< N O P > <0400.g1:< N O P >>` and :g:`< L G > <0400.g1:< L G >>` are the whole square :g:`< C E F D > <0400.g1:< C E F D >>`, which is described on :g:`/ C D / <0400.g1:/ C D />`;

.. assertion::

   therefore the rectangle contained by :g:`/ A D / <0400.g1:/ A D />`, :g:`/ D B / <0400.g1:/ D B />` together with the square on :g:`/ C B / <0400.g1:/ C B />` is equal to the square on :g:`/ C D / <0400.g1:/ C D />`.

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
     "G.37" [label="G.37", tooltip="G.37 (I.26): If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of...", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet ...", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior an...", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Through a given point to draw a straight line parallel to a given straight line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms which are on the same base and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms which are on equal bases and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.43): In any parallelogram the complements of the parallelograms about the diameter are equal to one another.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): On a given straight line to describe a square.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.67" [label="G.67", tooltip="G.67 (II.6): If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
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
     "G.48" -> "G.6";
     "G.56" -> "G.6";
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
     "G.37" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.56" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.59" -> "G.44";
     "G.67" -> "G.44";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.56" -> "G.47";
     "G.59" -> "G.47";
     "G.49" -> "G.48";
     "G.67" -> "G.49";
     "G.67" -> "G.56";
     "G.67" -> "G.59";
   }

Required for
------------

:ref:`G.72 <G.72>`, :ref:`G.115 <G.115>`, :ref:`G.116 <G.116>`, :ref:`G.128 <G.128>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`
