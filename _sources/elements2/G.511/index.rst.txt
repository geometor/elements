:order: 511
:number: 511
:canonical_id: G.511
:original_id: XIII.4
:volume: III
:book: XIII
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry, regular-solids
:category: theorem, proof, solid-geometry, regular-solids
:tags: book-xiii, point, segment, triangle, quadrilateral, polygon, square, extreme-and-mean-ratio, ratio, equality
:dependencies: G.180, G.507
:excerpt: If a straight line be cut in extreme and mean ratio, the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.

.. _G.511:
.. _XIII.4:

G.511
=====

.. rubric:: `XIII.4 <https://geometor.github.io/euclid/heath/volume_III/book_xiii/propositions/04/>`_

.. enunciation::

   If a straight line be cut in extreme and mean ratio, the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.

Let :g:`/ A B / <0451.g2:/ A B />` be a straight line, let it be cut in extreme and mean ratio at :g:`C <0451.g2:C>`, and let :g:`/ A C / <0451.g2:/ A C />` be the greater segment; I say that the squares on :g:`/ A B / <0451.g2:/ A B />`, :g:`/ B C / <0451.g2:/ B C />` are triple of the square on :g:`/ C A / <0451.g2:/ C A />`.

.. picture:: 0451.g2.svg
   :alt: Book XIII, Proposition 4

For let the square :g:`< A D E B > <0451.g2:< A D E B >>` be described on :g:`/ A B / <0451.g2:/ A B />`, and let the figure be drawn.

.. subclause::

   Since then :g:`/ A B / <0451.g2:/ A B />` has been cut in extreme and mean ratio at :g:`C <0451.g2:C>`, and :g:`/ A C / <0451.g2:/ A C />` is the greater segment,

.. assertion::

   therefore the rectangle :g:`/ A B / <0451.g2:/ A B />`, :g:`/ B C / <0451.g2:/ B C />` is equal to the square on :g:`/ A C / <0451.g2:/ A C />`. :just:`[G.507, G.180] <G.507, G.180>`

.. assertion::

   And :g:`< A K > <0451.g2:< A K >>` is the rectangle :g:`/ A B / <0451.g2:/ A B />`, :g:`/ B C / <0451.g2:/ B C />`, and :g:`< H G > <0451.g2:< H G >>` the square on :g:`/ A C / <0451.g2:/ A C />`; therefore :g:`< A K > <0451.g2:< A K >>` is :eq:`equal <0451.g2:< A K > = 0451.g2:< H G >>` to :g:`< H G > <0451.g2:< H G >>`.

.. subclause::

   And, since :g:`< A F > <0451.g2:< A F >>` is :eq:`equal <0451.g2:< A F > = 0451.g2:< F E >>` to :g:`< F E > <0451.g2:< F E >>`, let :g:`< C K > <0451.g2:< C K >>` be added to each;

.. assertion::

   therefore the whole :g:`< A K > <0451.g2:< A K >>` is :eq:`equal <0451.g2:< A K > = 0451.g2:< C E >>` to the whole :g:`< C E > <0451.g2:< C E >>`; therefore :g:`< A K > <0451.g2:< A K >>`, :g:`< C E > <0451.g2:< C E >>` are double of :g:`< A K > <0451.g2:< A K >>`.

.. subclause::

   But :g:`< A K > <0451.g2:< A K >>`, :g:`< C E > <0451.g2:< C E >>` are the gnomon :g:`< L M N > <0451.g2:< L M N >>` and the square :g:`< C K > <0451.g2:< C K >>`;

.. assertion::

   therefore the gnomon :g:`< L M N > <0451.g2:< L M N >>` and the square :g:`< C K > <0451.g2:< C K >>` are double of :g:`< A K > <0451.g2:< A K >>`.

.. subclause::

   But, further, :g:`< A K > <0451.g2:< A K >>` was also proved :eq:`equal <0451.g2:< A K > = 0451.g2:< H G >>` to :g:`< H G > <0451.g2:< H G >>`;

.. assertion::

   therefore the gnomon :g:`< L M N > <0451.g2:< L M N >>` and the squares :g:`< C K > <0451.g2:< C K >>`, :g:`< H G > <0451.g2:< H G >>` are triple of the square :g:`< H G > <0451.g2:< H G >>`.

.. subclause::

   And the gnomon :g:`< L M N > <0451.g2:< L M N >>` and the squares :g:`< C K > <0451.g2:< C K >>`, :g:`< H G > <0451.g2:< H G >>` are the whole square :g:`< A E > <0451.g2:< A E >>` and :g:`< C K > <0451.g2:< C K >>`, which are the squares on :g:`/ A B / <0451.g2:/ A B />`, :g:`/ B C / <0451.g2:/ B C />`, while :g:`< H G > <0451.g2:< H G >>` is the square on :g:`/ A C / <0451.g2:/ A C />`.

.. assertion::

   Therefore the squares on :g:`/ A B / <0451.g2:/ A B />`, :g:`/ B C / <0451.g2:/ B C />` are triple of the square on :g:`/ A C / <0451.g2:/ A C />`.

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
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles which are on the same base and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.38): Triangles which are on equal bases and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said to be in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equim...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said to have a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (V.9): Magnitudes which have the same ratio to the same are equal to one another ; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.146/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.152/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.177" [label="G.177", tooltip="G.177 (VI.14): In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are...", fillcolor="#222244", URL="../G.177/index.html", target="_top"];
     "G.179" [label="G.179", tooltip="G.179 (VI.16): If four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes be...", fillcolor="#222244", URL="../G.179/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (VI.17): If three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes be equal to the...", fillcolor="#222244", URL="../G.180/index.html", target="_top"];
     "G.507" [label="G.507", tooltip="G.507 (VI.def.3): A straight line is said to have been cut in extreme and mean ratio when, as the whole line is to the greater segment, so is the greater to the less.", fillcolor="#224422", URL="../G.507/index.html", target="_top"];
     "G.511" [label="G.511", tooltip="G.511 (XIII.4): If a straight line be cut in extreme and mean ratio, the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
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
     "G.24" -> "G.6";
     "G.25" -> "G.6";
     "G.48" -> "G.6";
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
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.177" -> "G.24";
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
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.51" -> "G.49";
     "G.54" -> "G.50";
     "G.163" -> "G.51";
     "G.163" -> "G.54";
     "G.145" -> "G.135";
     "G.149" -> "G.135";
     "G.142" -> "G.138";
     "G.149" -> "G.138";
     "G.163" -> "G.138";
     "G.152" -> "G.142";
     "G.177" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.146" -> "G.145";
     "G.177" -> "G.146";
     "G.163" -> "G.148";
     "G.177" -> "G.148";
     "G.152" -> "G.149";
     "G.163" -> "G.152";
     "G.177" -> "G.163";
     "G.179" -> "G.177";
     "G.180" -> "G.179";
     "G.511" -> "G.180";
     "G.511" -> "G.507";
   }

Required for
------------

:ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`
