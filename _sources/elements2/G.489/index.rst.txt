:order: 489
:number: 489
:canonical_id: G.489
:original_id: XII.3
:volume: III
:book: XII
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry, method-of-exhaustion
:category: theorem, proof, solid-geometry, method-of-exhaustion
:tags: book-xii, point, segment, angle, triangle, quadrilateral, similar, prism, pyramid, equality
:dependencies: G.11, G.42, G.47, G.164, G.170, G.453, G.474, G.486
:excerpt: Any pyramid which has a triangular base is divided into two pyramids equal and similar to one another, similar to the whole and having triangular bases, and into two equal prisms; and the two prisms are greater than the half of the whole pyramid.

.. _G.489:
.. _XII.3:

G.489
=====

.. rubric:: `XII.3 <https://geometor.github.io/euclid/heath/volume_III/book_xii/propositions/03/>`_

.. enunciation::

   Any pyramid which has a triangular base is divided into two pyramids equal and similar to one another, similar to the whole and having triangular bases, and into two equal prisms; and the two prisms are greater than the half of the whole pyramid.

.. signature:: theorem

   | :fn:`pyramid_triangular_base <G.489>`\ (:g:`< A B C > <g1:< A B C >>`, :g:`D <g1:D>`)
   | **given** there be a pyramid of which :g:`< A B C > <g1:< A B C >>` is the base and :g:`D <g1:D>` the vertex
   | **prove** the pyramid :g:`< A B C D > <g1:< A B C D >>` is divided into two pyramids equal to one another, having triangular bases and similar to the whole pyramid, and into two equal prisms

.. picture:: g1.svg
   :alt: Pyramid divided into two pyramids and two prisms

.. step:: given

   there be a pyramid of which :g:`< A B C > <g1:< A B C >>` is the base and :g:`D <g1:D>` the vertex

.. step:: assert

   And the two prisms are greater than the half of the whole pyramid.

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`, :fn:`segment <G.3>`\ (:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`, :fn:`segment <G.3>`\ (:g:`C <g1:C>`, :g:`A <g1:A>`) → :g:`/ C A / <g1:/ C A />`, :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`D <g1:D>`) → :g:`/ A D / <g1:/ A D />`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`C <g1:C>`) → :g:`/ D C / <g1:/ D C />`, :fn:`segment <G.3>`\ () → :g:`E <g1:E>`, :fn:`segment <G.3>`\ () → :g:`F <g1:F>`, :fn:`segment <G.3>`\ () → :g:`G <g1:G>`, :fn:`segment <G.3>`\ () → :g:`H <g1:H>`, :fn:`segment <G.3>`\ () → :g:`K <g1:K>`, :fn:`segment <G.3>`\ () → :g:`L <g1:L>`, :fn:`segment <G.3>`\ (:g:`H <g1:H>`, :g:`E <g1:E>`) → :g:`/ H E / <g1:/ H E />`, :fn:`segment <G.3>`\ (:g:`E <g1:E>`, :g:`G <g1:G>`) → :g:`/ E G / <g1:/ E G />`, :fn:`segment <G.3>`\ (:g:`G <g1:G>`, :g:`H <g1:H>`) → :g:`/ G H / <g1:/ G H />`, :fn:`segment <G.3>`\ (:g:`H <g1:H>`, :g:`K <g1:K>`) → :g:`/ H K / <g1:/ H K />`, :fn:`segment <G.3>`\ (:g:`K <g1:K>`, :g:`L <g1:L>`) → :g:`/ K L / <g1:/ K L />`, :fn:`segment <G.3>`\ (:g:`L <g1:L>`, :g:`H <g1:H>`) → :g:`/ L H / <g1:/ L H />`, :fn:`segment <G.3>`\ (:g:`K <g1:K>`, :g:`F <g1:F>`) → :g:`/ K F / <g1:/ K F />`, :fn:`segment <G.3>`\ (:g:`F <g1:F>`, :g:`G <g1:G>`) → :g:`/ F G / <g1:/ F G />`

.. step:: assert

   Since :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ E B /; g1:/ A H / = g1:/ D H />` to :g:`/ E B / <g1:/ E B />`, and :g:`/ A H / <g1:/ A H />` to :g:`/ D H / <g1:/ D H />`,

.. step:: assert ∵ straight_line_drawn_vi_2 <G.164>

   Therefore :g:`/ E H / <g1:/ E H />` is parallel to :g:`/ D B / <g1:/ D B />`.

.. step:: assert

   For the same reason :g:`/ H K / <g1:/ H K />` is also parallel to :g:`/ A B / <g1:/ A B />`.

.. step:: assert ∵ parallelogram_properties <G.47>

   Therefore :g:`< H E B K > <g1:< H E B K >>` is a parallelogram; therefore :g:`/ H K / <g1:/ H K />` is :eq:`equal <g1:/ H K / = g1:/ E B />` to :g:`/ E B / <g1:/ E B />`.

.. step:: assert

   :g:`/ E B / <g1:/ E B />` is :eq:`equal <g1:/ E B / = g1:/ E A />` to :g:`/ E A / <g1:/ E A />`;

.. step:: assert

   Therefore :g:`/ A E / <g1:/ A E />` is also :eq:`equal <g1:/ A E / = g1:/ H K />` to :g:`/ H K / <g1:/ H K />`.

.. step:: assert

   :g:`/ A H / <g1:/ A H />` is also :eq:`equal <g1:/ A H / = g1:/ H D />` to :g:`/ H D / <g1:/ H D />`;

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the two sides :g:`/ E A / <g1:/ E A />`, :g:`/ A H / <g1:/ A H />` are :eq:`equal <g1:/ E A / = g1:/ K H /; g1:/ A H / = g1:/ H D />` to the two sides :g:`/ K H / <g1:/ K H />`, :g:`/ H D / <g1:/ H D />` respectively, and :g:`< E A H ) <g1:< E A H )>` is :eq:`equal <g1:< E A H ) = g1:< K H D )>` to :g:`< K H D ) <g1:< K H D )>`; therefore the base :g:`/ E H / <g1:/ E H />` is :eq:`equal <g1:/ E H / = g1:/ K D />` to the base :g:`/ K D / <g1:/ K D />`.

.. step:: assert

   Therefore :g:`< A E H > <g1:< A E H >>` is :eq:`equal <g1:< A E H > = g1:< H K D >>` and similar to :g:`< H K D > <g1:< H K D >>`.

.. step:: assert

   For the same reason :g:`< A H G > <g1:< A H G >>` is also :eq:`equal <g1:< A H G > = g1:< H L D >>` and similar to :g:`< H L D > <g1:< H L D >>`.

.. step:: assert ∵ straight_lines_meeting <G.453>

   Since two straight lines :g:`/ E H / <g1:/ E H />`, :g:`/ H G / <g1:/ H G />` meeting one another are parallel to two straight lines :g:`/ K D / <g1:/ K D />`, :g:`/ D L / <g1:/ D L />` meeting one another, and are not in the same plane, they will contain equal angles.

.. step:: assert

   Therefore :g:`< E H G ) <g1:< E H G )>` is :eq:`equal <g1:< E H G ) = g1:< K D L )>` to :g:`< K D L ) <g1:< K D L )>`.

.. step:: assert

   And, since :g:`/ E H / <g1:/ E H />`, :g:`/ H G / <g1:/ H G />` are :eq:`equal <g1:/ E H / = g1:/ K D /; g1:/ H G / = g1:/ D L />` to the two :g:`/ K D / <g1:/ K D />`, :g:`/ D L / <g1:/ D L />` respectively, and :g:`< E H G ) <g1:< E H G )>` is :eq:`equal <g1:< E H G ) = g1:< K D L )>` to :g:`< K D L ) <g1:< K D L )>`,

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ E G / <g1:/ E G />` is :eq:`equal <g1:/ E G / = g1:/ K L />` to the base :g:`/ K L / <g1:/ K L />`; therefore :g:`< E H G > <g1:< E H G >>` is :eq:`equal <g1:< E H G > = g1:< K D L >>` and similar to :g:`< K D L > <g1:< K D L >>`.

.. step:: assert

   For the same reason :g:`< A E G > <g1:< A E G >>` is also :eq:`equal <g1:< A E G > = g1:< H K L >>` and similar to :g:`< H K L > <g1:< H K L >>`.

.. step:: assert ∵ equal_similar_solid_def <G.474>

   Therefore the pyramid of which :g:`< A E G > <g1:< A E G >>` is the base and :g:`H <g1:H>` the vertex is :eq:`equal <g1:< A E G H > = g1:< H K L D >>` and similar to the pyramid of which :g:`< H K L > <g1:< H K L >>` is the base and :g:`D <g1:D>` the vertex.

.. step:: assert

   And, since :g:`/ H K / <g1:/ H K />` has been drawn parallel to :g:`/ A B / <g1:/ A B />`, one of the sides of :g:`< A D B > <g1:< A D B >>`,

.. step:: assert ∵ parallel_transversal_angles, similar_polygons_angles_def <G.42, G.170>

   :g:`< A D B > <g1:< A D B >>` is equiangular to :g:`< D H K > <g1:< D H K >>`, and they have their sides proportional; therefore :g:`< A D B > <g1:< A D B >>` is similar to :g:`< D H K > <g1:< D H K >>`.

.. step:: assert

   For the same reason :g:`< D B C > <g1:< D B C >>` is also similar to :g:`< D K L > <g1:< D K L >>`, and :g:`< A D C > <g1:< A D C >>` to :g:`< D L H > <g1:< D L H >>`.

.. step:: assert ∵ straight_lines_meeting <G.453>

   Since :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />` meeting one another are parallel to :g:`/ K H / <g1:/ K H />`, :g:`/ H L / <g1:/ H L />` meeting one another, not in the same plane, they will contain equal angles.

.. step:: assert

   Therefore :g:`< B A C ) <g1:< B A C )>` is :eq:`equal <g1:< B A C ) = g1:< K H L )>` to :g:`< K H L ) <g1:< K H L )>`.

.. step:: assert

   And, as :g:`/ B A / <g1:/ B A />` is to :g:`/ A C / <g1:/ A C />`, so is :g:`/ K H / <g1:/ K H />` to :g:`/ H L / <g1:/ H L />`;

.. step:: assert

   Therefore :g:`< A B C > <g1:< A B C >>` is similar to :g:`< H K L > <g1:< H K L >>`.

.. step:: assert

   Therefore also the pyramid of which :g:`< A B C > <g1:< A B C >>` is the base and :g:`D <g1:D>` the vertex is similar to the pyramid of which :g:`< H K L > <g1:< H K L >>` is the base and :g:`D <g1:D>` the vertex.

.. step:: assert

   The pyramid of which :g:`< H K L > <g1:< H K L >>` is the base and :g:`D <g1:D>` the vertex was proved similar to the pyramid of which :g:`< A E G > <g1:< A E G >>` is the base and :g:`H <g1:H>` the vertex.

.. step:: assert

   Therefore each of the pyramids :g:`< A E G H > <g1:< A E G H >>`, :g:`< H K L D > <g1:< H K L D >>` is similar to the whole pyramid :g:`< A B C D > <g1:< A B C D >>`.

.. step:: assert

   Next, since :g:`/ B F / <g1:/ B F />` is :eq:`equal <g1:/ B F / = g1:/ F C />` to :g:`/ F C / <g1:/ F C />`,

.. step:: assert

   The parallelogram :g:`< E B F G > <g1:< E B F G >>` is double of :g:`< G F C > <g1:< G F C >>`.

.. step:: assert ∵ there_prisms_equal <G.486>

   Since, if there be two prisms of equal height, and one have a parallelogram as base, and the other a triangle, and if the parallelogram be double of the triangle, the prisms are equal.

.. step:: assert

   Therefore the prism contained by the two triangles :g:`< B K F > <g1:< B K F >>`, :g:`< E H G > <g1:< E H G >>`, and the three parallelograms :g:`< E B F G > <g1:< E B F G >>`, :g:`< E B K H > <g1:< E B K H >>`, :g:`< H K F G > <g1:< H K F G >>` is :eq:`equal <g1:< H G E K F B > = g1:< G C F H L K >>` to the prism contained by the two triangles :g:`< G F C > <g1:< G F C >>`, :g:`< H K L > <g1:< H K L >>` and the three parallelograms :g:`< K F C L > <g1:< K F C L >>`, :g:`< L C G H > <g1:< L C G H >>`, :g:`< H K F G > <g1:< H K F G >>`.

.. step:: assert

   It is manifest that each of the prisms, namely that in which the parallelogram :g:`< E B F G > <g1:< E B F G >>` is the base and :g:`/ H K / <g1:/ H K />` is its opposite, and that in which :g:`< G F C > <g1:< G F C >>` is the base and :g:`< H K L > <g1:< H K L >>` its opposite, is greater than each of the pyramids of which :g:`< A E G > <g1:< A E G >>`, :g:`< H K L > <g1:< H K L >>` are the bases and :g:`H <g1:H>`, :g:`D <g1:D>` the vertices,

.. step:: assert

   Inasmuch as, if we join :g:`/ E F / <g1:/ E F />`, :g:`/ E K / <g1:/ E K />`, the prism in which the parallelogram :g:`< E B F G > <g1:< E B F G >>` is the base and :g:`/ H K / <g1:/ H K />` its opposite is greater than the pyramid of which :g:`< E B F > <g1:< E B F >>` is the base and :g:`K <g1:K>` the vertex.

.. step:: assert

   The pyramid of which :g:`< E B F > <g1:< E B F >>` is the base and :g:`K <g1:K>` the vertex is :eq:`equal <g1:< K E F B > = g1:< A E G H >>` to the pyramid of which :g:`< A E G > <g1:< A E G >>` is the base and :g:`H <g1:H>` the vertex; for they are contained by equal and similar planes.

.. step:: assert

   Hence also the prism in which the parallelogram :g:`< E B F G > <g1:< E B F G >>` is the base and :g:`/ H K / <g1:/ H K />` its opposite is greater than the pyramid of which :g:`< A E G > <g1:< A E G >>` is the base and :g:`H <g1:H>` the vertex.

.. step:: assert

   The prism in which the parallelogram :g:`< E B F G > <g1:< E B F G >>` is the base and :g:`/ H K / <g1:/ H K />` its opposite is :eq:`equal <g1:< H G E K F B > = g1:< G C F H L K >>` to the prism in which :g:`< G F C > <g1:< G F C >>` is the base and :g:`< H K L > <g1:< H K L >>` its opposite, and the pyramid of which :g:`< A E G > <g1:< A E G >>` is the base and :g:`H <g1:H>` the vertex is :eq:`equal <g1:< A E G H > = g1:< H K L D >>` to the pyramid of which :g:`< H K L > <g1:< H K L >>` is the base and :g:`D <g1:D>` the vertex.

.. step:: assert

   Therefore the said two prisms are greater than the said two pyramids of which :g:`< A E G > <g1:< A E G >>`, :g:`< H K L > <g1:< H K L >>` are the bases and :g:`H <g1:H>`, :g:`D <g1:D>` the vertices.

.. step:: conclude

   Therefore the whole pyramid, of which :g:`< A B C > <g1:< A B C >>` is the base and :g:`D <g1:D>` the vertex, has been divided into two pyramids :eq:`equal <g1:< A E G H > = g1:< H K L D >>` to one another and into two :eq:`equal <g1:< H G E K F B > = g1:< G C F H L K >>` prisms, and the two prisms are greater than the half of the whole pyramid.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all segments falling upon it from its center are equal.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1): Construct a segment between any two points.", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3): Construct a circle with any center and radius.", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1): Construct an equilateral triangle on a given finite segment.", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3): If equals are subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2): Extend a finite segment continuously in a straight line.", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2): Construct at a given point a segment equal to a given segment.", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3): Cut off from the greater of two unequal segments a segment equal to the less.", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4): Things that coincide with one another are equal.", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4): Triangles with two sides and the included angle equal are congruent (SAS).", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5): In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): Bisect a given finite segment.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line standing on a straight line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing line is perpendicular to that on which...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): Construct a line at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.38): Triangles on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.39): Equal triangles on the same base and on the same side lie in the same parallels.", fillcolor="#222244", URL="../G.52/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.146/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.152/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.164" [label="G.164", tooltip="G.164 (VI.2): If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionall...", fillcolor="#222244", URL="../G.164/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (VI.def.1): Similar polygons are such as have their angles severally equal and the sides about the equal angles proportional.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.448" [label="G.448", tooltip="G.448 (XI.5): If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.", fillcolor="#222244", URL="../G.448/index.html", target="_top"];
     "G.449" [label="G.449", tooltip="G.449 (XI.6): If two straight lines be at right angles to the same plane, the straight lines is parallel.", fillcolor="#222244", URL="../G.449/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.452" [label="G.452", tooltip="G.452 (XI.9): Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.", fillcolor="#222244", URL="../G.452/index.html", target="_top"];
     "G.453" [label="G.453", tooltip="G.453 (XI.10): If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.", fillcolor="#222244", URL="../G.453/index.html", target="_top"];
     "G.460" [label="G.460", tooltip="G.460 (XI.16): If two parallel planes be cut by any plane, their common sections are parallel.", fillcolor="#222244", URL="../G.460/index.html", target="_top"];
     "G.469" [label="G.469", tooltip="G.469 (XI.24): If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.", fillcolor="#222244", URL="../G.469/index.html", target="_top"];
     "G.470" [label="G.470", tooltip="G.470 (XI.25): If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.", fillcolor="#222244", URL="../G.470/index.html", target="_top"];
     "G.474" [label="G.474", tooltip="G.474 (XI.def.10): Equal and similar solid figures are those contained by similar planes equal in multitude and in magnitude.", fillcolor="#224422", URL="../G.474/index.html", target="_top"];
     "G.475" [label="G.475", tooltip="G.475 (XI.28): If a parallelepipedal solid be cut by a plane through the diagonals of the opposite planes, the solid is bisected by the plane.", fillcolor="#222244", URL="../G.475/index.html", target="_top"];
     "G.476" [label="G.476", tooltip="G.476 (XI.29): Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal.", fillcolor="#222244", URL="../G.476/index.html", target="_top"];
     "G.477" [label="G.477", tooltip="G.477 (XI.30): Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal.", fillcolor="#222244", URL="../G.477/index.html", target="_top"];
     "G.478" [label="G.478", tooltip="G.478 (XI.31): Parallelepipedal solids which are on equal bases and of the same height are equal.", fillcolor="#222244", URL="../G.478/index.html", target="_top"];
     "G.486" [label="G.486", tooltip="G.486 (XI.39): If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms is equal.", fillcolor="#222244", URL="../G.486/index.html", target="_top"];
     "G.489" [label="G.489", tooltip="G.489 (XII.3): Any pyramid which has a triangular base is divided into two pyramids equal and similar to one another, similar to the whole and having triangular bases, and into two equal prisms; ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.52" -> "G.1";
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
     "G.447" -> "G.11";
     "G.449" -> "G.11";
     "G.469" -> "G.11";
     "G.476" -> "G.11";
     "G.489" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.447" -> "G.15";
     "G.449" -> "G.15";
     "G.453" -> "G.15";
     "G.476" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.25" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.447" -> "G.25";
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
     "G.478" -> "G.34";
     "G.47" -> "G.37";
     "G.447" -> "G.37";
     "G.39" -> "G.38";
     "G.460" -> "G.38";
     "G.40" -> "G.39";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.449" -> "G.40";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.451" -> "G.42";
     "G.489" -> "G.42";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.52" -> "G.44";
     "G.49" -> "G.46";
     "G.453" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.469" -> "G.47";
     "G.475" -> "G.47";
     "G.476" -> "G.47";
     "G.486" -> "G.47";
     "G.489" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.478" -> "G.48";
     "G.51" -> "G.49";
     "G.476" -> "G.49";
     "G.52" -> "G.50";
     "G.54" -> "G.50";
     "G.163" -> "G.51";
     "G.164" -> "G.51";
     "G.164" -> "G.52";
     "G.163" -> "G.54";
     "G.145" -> "G.135";
     "G.149" -> "G.135";
     "G.142" -> "G.138";
     "G.149" -> "G.138";
     "G.163" -> "G.138";
     "G.470" -> "G.138";
     "G.152" -> "G.142";
     "G.164" -> "G.142";
     "G.478" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.146" -> "G.145";
     "G.164" -> "G.146";
     "G.478" -> "G.146";
     "G.163" -> "G.148";
     "G.164" -> "G.148";
     "G.478" -> "G.148";
     "G.152" -> "G.149";
     "G.163" -> "G.152";
     "G.164" -> "G.163";
     "G.489" -> "G.164";
     "G.489" -> "G.170";
     "G.444" -> "G.443";
     "G.460" -> "G.443";
     "G.449" -> "G.444";
     "G.451" -> "G.444";
     "G.448" -> "G.445";
     "G.450" -> "G.445";
     "G.447" -> "G.446";
     "G.448" -> "G.446";
     "G.449" -> "G.446";
     "G.451" -> "G.446";
     "G.448" -> "G.447";
     "G.451" -> "G.447";
     "G.452" -> "G.447";
     "G.449" -> "G.448";
     "G.452" -> "G.449";
     "G.451" -> "G.450";
     "G.452" -> "G.451";
     "G.453" -> "G.452";
     "G.469" -> "G.453";
     "G.489" -> "G.453";
     "G.469" -> "G.460";
     "G.470" -> "G.469";
     "G.478" -> "G.469";
     "G.478" -> "G.470";
     "G.475" -> "G.474";
     "G.478" -> "G.474";
     "G.489" -> "G.474";
     "G.486" -> "G.475";
     "G.477" -> "G.476";
     "G.478" -> "G.476";
     "G.478" -> "G.477";
     "G.486" -> "G.478";
     "G.489" -> "G.486";
   }

Required for
------------

:ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`

.. toctree::
   :hidden:

   code
   heath
