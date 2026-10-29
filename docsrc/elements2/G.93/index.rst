:order: 93
:number: 93
:canonical_id: G.93
:original_id: III.15
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, equality
:dependencies: G.31, G.35, G.91, G.92
:excerpt: Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

.. _G.93:
.. _III.15:

G.93
====

.. rubric:: `III.15 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/15/>`_

.. enunciation::

   Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

Let :g:`( A B C D ) <0042.g1:( A B C D )>` be a circle, let :g:`/ A D / <0042.g1:/ A D />` be its diameter and :g:`E <0042.g1:E>`
the centre; and let :g:`/ B C / <0042.g1:/ B C />` be nearer to the
diameter :g:`/ A D / <0042.g1:/ A D />`, and :g:`/ F G / <0042.g1:/ F G />` more remote;
I say that :g:`/ A D / <0042.g1:/ A D />` is greatest and :g:`/ B C / <0042.g1:/ B C />`
greater than :g:`/ F G / <0042.g1:/ F G />`.

.. picture:: 0042.g1.svg
   :alt: Diagram for Proposition 15

For from the centre :g:`E <0042.g1:E>` let :g:`/ E H / <0042.g1:/ E H />`, :g:`/ E K / <0042.g1:/ E K />`
be drawn perpendicular to :g:`/ B C / <0042.g1:/ B C />`, :g:`/ F G / <0042.g1:/ F G />`.

Then, since :g:`/ B C / <0042.g1:/ B C />` is nearer to the
centre and :g:`/ F G / <0042.g1:/ F G />` more remote, :g:`/ E K / <0042.g1:/ E K />` is
greater than :g:`/ E H / <0042.g1:/ E H />`. :just:`[G.92] <G.92>`

Let :g:`/ E L / <0042.g1:/ E L />` be made :eq:`equal <0042.g1:/ E L / = 0042.g1:/ E H />` to :g:`/ E H / <0042.g1:/ E H />`,
through :g:`L <0042.g1:L>` let :g:`/ L M / <0042.g1:/ L M />` be drawn at right
angles to :g:`/ E K / <0042.g1:/ E K />` and carried through to :g:`N <0042.g1:N>`, and let :g:`/ M E / <0042.g1:/ M E />`, :g:`/ E N / <0042.g1:/ E N />`,
:g:`/ F E / <0042.g1:/ F E />`, :g:`/ E G / <0042.g1:/ E G />` be joined.

Then, since :g:`/ E H / <0042.g1:/ E H />` is :eq:`equal <0042.g1:/ E H / = 0042.g1:/ E L />` to :g:`/ E L / <0042.g1:/ E L />`,

.. assertion:: [G.91] <G.91>

   :g:`/ B C / <0042.g1:/ B C />` is also :eq:`equal <0042.g1:/ B C / = 0042.g1:/ M N />` to :g:`/ M N / <0042.g1:/ M N />`.

Again, since :g:`/ A E / <0042.g1:/ A E />` is :eq:`equal <0042.g1:/ A E / = 0042.g1:/ E M /; 0042.g1:/ E D / = 0042.g1:/ E N />` to :g:`/ E M / <0042.g1:/ E M />`, and :g:`/ E D / <0042.g1:/ E D />` to :g:`/ E N / <0042.g1:/ E N />`,

.. assertion::

   :g:`/ A D / <0042.g1:/ A D />` is equal to :g:`/ M E / <0042.g1:/ M E />`, :g:`/ E N / <0042.g1:/ E N />`.

But :g:`/ M E / <0042.g1:/ M E />`, :g:`/ E N / <0042.g1:/ E N />` are greater than :g:`/ M N / <0042.g1:/ M N />`, :just:`[G.31] <G.31>`
and :g:`/ M N / <0042.g1:/ M N />` is :eq:`equal <0042.g1:/ M N / = 0042.g1:/ B C />` to :g:`/ B C / <0042.g1:/ B C />`;

.. assertion::

   therefore :g:`/ A D / <0042.g1:/ A D />` is greater than :g:`/ B C / <0042.g1:/ B C />`.

And, since the two sides :g:`/ M E / <0042.g1:/ M E />`, :g:`/ E N / <0042.g1:/ E N />` are :eq:`equal <0042.g1:/ M E / = 0042.g1:/ F E /; 0042.g1:/ E N / = 0042.g1:/ E G />` to the two
sides :g:`/ F E / <0042.g1:/ F E />`, :g:`/ E G / <0042.g1:/ E G />`,
and the angle :g:`< M E N ) <0042.g1:< M E N )>` greater than the angle :g:`< F E G ) <0042.g1:< F E G )>`,
therefore the base :g:`/ M N / <0042.g1:/ M N />` is greater than the base :g:`/ F G / <0042.g1:/ F G />`. :just:`[G.35] <G.35>`

But :g:`/ M N / <0042.g1:/ M N />` was proved :eq:`equal <0042.g1:/ M N / = 0042.g1:/ B C />` to :g:`/ B C / <0042.g1:/ B C />`.
Therefore the diameter :g:`/ A D / <0042.g1:/ A D />` is greatest and :g:`/ B C / <0042.g1:/ B C />` greater
than :g:`/ F G / <0042.g1:/ F G />`.

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
     "G.24" [label="G.24", tooltip="G.24 (I.14): If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in...", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): If two straight lines cut one another, they make the vertical angles equal to one another.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): [8] 5. The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle two sides taken together in any manner are greater than the remaining one.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manne...", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.24): If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also hav...", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of...", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet ...", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior an...", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Through a given point to draw a straight line parallel to a given straight line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms which are on the same base and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles which are on the same base and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): On a given straight line to describe a square.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.47): In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): To find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (III.3): If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects ...", fillcolor="#222244", URL="../G.78/index.html", target="_top"];
     "G.90" [label="G.90", tooltip="G.90 (III.def.4): In a circle straight lines are said to be equally distant from the centre when the perpendiculars drawn to them from the centre are equal.", fillcolor="#224422", URL="../G.90/index.html", target="_top"];
     "G.91" [label="G.91", tooltip="G.91 (III.14): In a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal to one another.", fillcolor="#222244", URL="../G.91/index.html", target="_top"];
     "G.92" [label="G.92", tooltip="G.92 (III.def.5): And that straight line is said to be at a greater distance on which the greater perpendicular falls.", fillcolor="#224422", URL="../G.92/index.html", target="_top"];
     "G.93" [label="G.93", tooltip="G.93 (III.15): Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.35" -> "G.11";
     "G.37" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.35" -> "G.12";
     "G.78" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.76" -> "G.15";
     "G.78" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.76" -> "G.18";
     "G.78" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.60" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.60" -> "G.24";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.35" -> "G.30";
     "G.33" -> "G.31";
     "G.93" -> "G.31";
     "G.34" -> "G.33";
     "G.35" -> "G.34";
     "G.44" -> "G.34";
     "G.93" -> "G.35";
     "G.47" -> "G.37";
     "G.78" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.50" -> "G.48";
     "G.54" -> "G.50";
     "G.60" -> "G.54";
     "G.60" -> "G.59";
     "G.91" -> "G.60";
     "G.91" -> "G.76";
     "G.91" -> "G.78";
     "G.91" -> "G.90";
     "G.93" -> "G.91";
     "G.93" -> "G.92";
   }
