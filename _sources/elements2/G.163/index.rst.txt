:order: 163
:number: 163
:canonical_id: G.163
:original_id: IV.11
:title: G.163 inscribe pentagon in circle
:volume: II
:book: IV
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles, polygons
:category: problem, construction, plane-geometry, circles, polygons
:tags: book-iv, segment, circle, angle, triangle, polygon, equilateral-triangle, inscribed-in-circle, plane-angle, trilateral, straight-line, stand-upon-circumference, line, equilateral, inscribed, pentagon, equality
:dependencies: G.4, G.10, G.13, G.14, G.22, G.31, G.133, G.134, G.136, G.148, G.149, G.162
:excerpt: Inscribe in a given circle an equilateral and equiangular pentagon.

.. _G.163:
.. _IV.11:

G.163 inscribe pentagon in circle
=================================

.. rubric:: `IV.11 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/11/>`_

.. enunciation::

   :term:`Inscribe in a given circle <G.148>` an :term:`equilateral <G.13>` and equiangular pentagon.

.. signature:: problem

   | :fn:`inscribe_pentagon_in_circle <G.163>`\ (:g:`( A B C D E ) <g1:( A B C D E )>`)
   | **given** :g:`( A B C D E ) <g1:( A B C D E )>`
   | **construct** It was also proved :eq:`equilateral <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E A />`

.. picture:: g1.svg
   :alt: Proposition 11 diagram

.. step:: given

   :g:`( A B C D E ) <g1:( A B C D E )>`

.. step:: assert ∵ golden_isosceles_triangle <G.162>

   Let the isosceles triangle :g:`< F G H > <g1:< F G H >>` be set out having each of the :term:`angles <G.22>` at :g:`< F G H ) <g1:< F G H )>`, :g:`< F H G ) <g1:< F H G )>` double of the angle at :g:`< G F H ) <g1:< G F H )>`

.. step:: construct

   :fn:`inscribe_triangle_in_circle <G.149>`: Let there be inscribed in :g:`( A B C D E ) <g1:( A B C D E )>` :g:`< A C D > <g1:< A C D >>` :eq:`equiangular <g1:< C A D ) = g1:< G F H ); g1:< A C D ) = g1:< F G H ); g1:< C D A ) = g1:< F H G )>` with :g:`< F G H > <g1:< F G H >>`, so that :g:`< C A D ) <g1:< C A D )>` is :eq:`equal <g1:< C A D ) = g1:< G F H )>` to the angle at :g:`< G F H ) <g1:< G F H )>` and the angles at :g:`< F G H ) <g1:< F G H )>`, :g:`< F H G ) <g1:< F H G )>` respectively :eq:`equal <g1:< F G H ) = g1:< A C D ); g1:< F H G ) = g1:< C D A )>` to :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`

.. step:: assert

   each of :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>` is also double of :g:`< C A D ) <g1:< C A D )>`

.. step:: construct

   :fn:`segment <G.14>`\ () → :g:`< A C D ) <g1:< A C D )>`, :fn:`segment <G.14>`\ () → :g:`< C D A ) <g1:< C D A )>`, :fn:`segment <G.14>`\ (:g:`C <g1:C>`, :g:`E <g1:E>`) → :g:`/ C E / <g1:/ C E />`, :fn:`segment <G.14>`\ (:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`, :fn:`segment <G.14>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`, :fn:`segment <G.14>`\ (:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`, :fn:`segment <G.14>`\ (:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`/ D E / <g1:/ D E />`, :fn:`segment <G.14>`\ (:g:`E <g1:E>`, :g:`A <g1:A>`) → :g:`/ E A / <g1:/ E A />`

.. step:: assert

   each of :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>` is double of :g:`< C A D ) <g1:< C A D )>`, and they have been :eq:`bisected <g1:< A C E ) = g1:< E C D ); g1:< C D B ) = g1:< B D A )>` by :g:`/ C E / <g1:/ C E />`, :g:`/ D B / <g1:/ D B />` → therefore the five angles :g:`< D A C ) <g1:< D A C )>`, :g:`< A C E ) <g1:< A C E )>`, :g:`< E C D ) <g1:< E C D )>`, :g:`< C D B ) <g1:< C D B )>`, :g:`< B D A ) <g1:< B D A )>` :eq:`= <g1:< D A C ) = g1:< A C E ) = g1:< E C D ) = g1:< C D B ) = g1:< B D A )>`

.. step:: assert ∵ equal_circles_equal <G.133>

   Equal angles stand on equal arcs

.. step:: assert

   the five arcs :g:`( A B ) <g1:( A B )>`, :g:`( B C ) <g1:( B C )>`, :g:`( C D ) <g1:( C D )>`, :g:`( D E ) <g1:( D E )>`, :g:`( E A ) <g1:( E A )>` :eq:`= <g1:( A B ) = g1:( B C ) = g1:( C D ) = g1:( D E ) = g1:( E A )>`

.. step:: assert ∵ equal_circles_equal_iii_29 <G.136>

   Equal arcs are subtended by equal :term:`segments <G.4>`

.. step:: assert

   the five segments :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E A />`

.. step:: assert

   the pentagon :g:`< A B C D E > <g1:< A B C D E >>` is :eq:`equilateral <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E A />`

.. step:: assert

   I say next that it is also :eq:`equiangular <g1:< B A E ) = g1:< A B C ) = g1:< B C D ) = g1:< C D E ) = g1:< A E D )>`

.. step:: construct

   Since the arc :g:`( A B ) <g1:( A B )>` is :eq:`equal <g1:( A B ) = g1:( D E )>` to the arc :g:`( D E ) <g1:( D E )>`, let :g:`( B C D ) <g1:( B C D )>` be added to each

.. step:: assert

   the whole arc :g:`( A B C D ) <g1:( A B C D )>` :eq:`= <g1:( A B C D ) = g1:( E D C B )>` the whole arc :g:`( E D C B ) <g1:( E D C B )>`

.. step:: assert

   :g:`< A E D ) <g1:< A E D )>` stands on the arc :g:`( A B C D ) <g1:( A B C D )>`, and :g:`< B A E ) <g1:< B A E )>` on the arc :g:`( E D C B ) <g1:( E D C B )>`

.. step:: assert ∵ equal_circles_angles <G.134>

   :g:`< B A E ) <g1:< B A E )>` :eq:`= <g1:< B A E ) = g1:< A E D )>` :g:`< A E D ) <g1:< A E D )>`

.. step:: assert

   The same reason each of :g:`< A B C ) <g1:< A B C )>`, :g:`< B C D ) <g1:< B C D )>`, :g:`< C D E ) <g1:< C D E )>` :eq:`= <g1:< A B C ) = g1:< B C D ) = g1:< C D E ) = g1:< B A E ) = g1:< A E D )>` each of :g:`< B A E ) <g1:< B A E )>`, :g:`< A E D ) <g1:< A E D )>`

.. step:: assert

   the pentagon :g:`< A B C D E > <g1:< A B C D E >>` is :eq:`equiangular <g1:< B A E ) = g1:< A B C ) = g1:< B C D ) = g1:< C D E ) = g1:< A E D )>`

.. step:: conclude

   It was also proved :eq:`equilateral <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E A />`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.def.6): The extremities of a surface are lines or arcs.", fillcolor="#224422", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.def.15): A circle ( A B ) is a plane figure contained by one arc defined by a center A and a point B establishing its defining radius / A B /, such that all segments / A B /, / A C /, / A D...", fillcolor="#224422", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.13/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.post.3): Construct a circle ( A B ) with center A and defining radius point B.", fillcolor="#444422", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.1): Construct an equilateral triangle on a given segment.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.post.2): Extend a segment / A B / continuously along a line [ A B ] to / B C /.", fillcolor="#444422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.cn.3): If equals are subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.19/index.html", target="_top"];
     "G.20" [label="G.20", tooltip="G.20 (I.2): Construct at a given point a segment equal to a given segment.", fillcolor="#222244", URL="../G.20/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.3): Cut off from the greater of two unequal segments a segment equal to the less.", fillcolor="#222244", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.cn.4): Things / A B /, / D E / that coincide with one another are equal to one another.", fillcolor="#442222", URL="../G.23/index.html", target="_top"];
     "G.24" [label="G.24", tooltip="G.24 (I.4): Triangles with two sides and the included angle equal are congruent (SAS).", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.5): In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.14): If two segments at a point on a line on opposite sides make adjacent angles summing to two right angles, the two segments are collinear.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.64" [label="G.64", tooltip="G.64 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.64/index.html", target="_top"];
     "G.65" [label="G.65", tooltip="G.65 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.65/index.html", target="_top"];
     "G.66" [label="G.66", tooltip="G.66 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.66/index.html", target="_top"];
     "G.70" [label="G.70", tooltip="G.70 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.70/index.html", target="_top"];
     "G.72" [label="G.72", tooltip="G.72 (I.43): In any parallelogram, the complements of the parallelograms about the diagonal are equal in area.", fillcolor="#222244", URL="../G.72/index.html", target="_top"];
     "G.75" [label="G.75", tooltip="G.75 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.75/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (I.def.11): An obtuse angle is greater than a right angle.", fillcolor="#224422", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (I.def.21): A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.", fillcolor="#224422", URL="../G.78/index.html", target="_top"];
     "G.79" [label="G.79", tooltip="G.79 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.79/index.html", target="_top"];
     "G.81" [label="G.81", tooltip="G.81 (II.def.1): Any rectangular parallelogram is said to becontained by the twosegments containing theright angle.", fillcolor="#224422", URL="../G.81/index.html", target="_top"];
     "G.86" [label="G.86", tooltip="G.86 (II.def.2): And in any parallelogrammic area let any one whatever of the parallelograms about itsdiameter with the two complements be called agnomon.", fillcolor="#224422", URL="../G.86/index.html", target="_top"];
     "G.88" [label="G.88", tooltip="G.88 (II.6): If a segment be bisected and a segment be added to it in a segment, the rectangle contained by the whole with the added segment and the added segment together with the square on th...", fillcolor="#222244", URL="../G.88/index.html", target="_top"];
     "G.93" [label="G.93", tooltip="G.93 (II.11): Cut a given segment so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment.", fillcolor="#222244", URL="../G.93/index.html", target="_top"];
     "G.96" [label="G.96", tooltip="G.96 (I.def.18): A semicircle is the figure contained by a diameter and the arc cut off by it.", fillcolor="#224422", URL="../G.96/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.100" [label="G.100", tooltip="G.100 (III.3): If in a circle a segment through the center bisect a segment not through the center, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.", fillcolor="#222244", URL="../G.100/index.html", target="_top"];
     "G.102" [label="G.102", tooltip="G.102 (III.5): If two circles cut one another, they will not have the same center.", fillcolor="#222244", URL="../G.102/index.html", target="_top"];
     "G.108" [label="G.108", tooltip="G.108 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.108/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.def.2): Asegment is said totouch a circle which, meeting thecircle and being produced, does not cut the circle.", fillcolor="#224422", URL="../G.111/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.117/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (III.16): The segment drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the segment and the arc another segment ca...", fillcolor="#222244", URL="../G.118/index.html", target="_top"];
     "G.120" [label="G.120", tooltip="G.120 (III.18): If a segment touch a circle, and a segment be joined from the center to the point of contact, the segment so joined is perpendicular to the tangent.", fillcolor="#222244", URL="../G.120/index.html", target="_top"];
     "G.121" [label="G.121", tooltip="G.121 (III.19): If a segment touch a circle, and from the point of contact a segment be drawn at right angles to the tangent, the center of the circle is on the segment so drawn.", fillcolor="#222244", URL="../G.121/index.html", target="_top"];
     "G.122" [label="G.122", tooltip="G.122 (III.def.10): Asector of a circle is thefigure which, when anangle is constructed at thecenter of thecircle, is contained by thesegments containing the angle and the arc cut off by them.", fillcolor="#224422", URL="../G.122/index.html", target="_top"];
     "G.123" [label="G.123", tooltip="G.123 (III.20): In a circle the angle at the center is double of the angle at the arc, when the angles have the same arc as base.", fillcolor="#222244", URL="../G.123/index.html", target="_top"];
     "G.124" [label="G.124", tooltip="G.124 (III.21): In a circle the angles in the same segment are equal.", fillcolor="#222244", URL="../G.124/index.html", target="_top"];
     "G.125" [label="G.125", tooltip="G.125 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.125/index.html", target="_top"];
     "G.126" [label="G.126", tooltip="G.126 (III.def.6): Asegment of a circle is thefigure contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.126/index.html", target="_top"];
     "G.127" [label="G.127", tooltip="G.127 (III.def.11): Similar segments of circles are those which admit equalangles, or in which the angles are equal.", fillcolor="#224422", URL="../G.127/index.html", target="_top"];
     "G.129" [label="G.129", tooltip="G.129 (III.24): Similar segments of circles on equal segments are equal.", fillcolor="#222244", URL="../G.129/index.html", target="_top"];
     "G.131" [label="G.131", tooltip="G.131 (III.def.1): Equal circles are those thediameters of which are equal, or the radii of which are equal.", fillcolor="#224422", URL="../G.131/index.html", target="_top"];
     "G.132" [label="G.132", tooltip="G.132 (III.def.9): And, when thesegments containing theangle cut off a arc, the angle is said tostand upon that arc.", fillcolor="#224422", URL="../G.132/index.html", target="_top"];
     "G.133" [label="G.133", tooltip="G.133 (III.26): In equal circles equal angles stand on equal arcs, whether they stand at the centres or at the arcs.", fillcolor="#222244", URL="../G.133/index.html", target="_top"];
     "G.134" [label="G.134", tooltip="G.134 (III.27): In equal circles angles standing on equal arcs are equal, whether they stand at the centres or at the arcs.", fillcolor="#222244", URL="../G.134/index.html", target="_top"];
     "G.136" [label="G.136", tooltip="G.136 (III.29): In equal circles equal arcs are subtended by equal segments.", fillcolor="#222244", URL="../G.136/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (III.def.8): Anangle in a segment is theangle which, when apoint is taken on the arc of the segment andsegments are joined from it to theextremities of the segment which is thebase of the segme...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.140" [label="G.140", tooltip="G.140 (III.32): If a segment touch a circle, and from the point of contact there be drawn across, in the circle, a segment cutting the circle, the angles which it makes with the tangent will equal...", fillcolor="#222244", URL="../G.140/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (III.36): If a point be taken outside a circle and from it there fall on the circle two segments, and if one of them cut the circle and the other touch it, the rectangle contained by the who...", fillcolor="#222244", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (III.37): If a point be taken outside a circle and from the point there fall on the circle two segments, if one of them cut the circle, and the other fall on it, and if further the rectangle...", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (IV.def.7): Asegment is said to befitted into a circle when itsextremities are on the arc of thecircle.", fillcolor="#224422", URL="../G.146/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (IV.1): Into a given circle to fit a segment equal to a given segment which is not greater than the diameter of the circle.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (IV.def.3): Apolygon is said to beinscribed in a circle when eachangle of the inscribedfigure lies on the arc of thecircle.", fillcolor="#224422", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (IV.2): Inscribe in a given circle a triangle equiangular with a given triangle.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.155" [label="G.155", tooltip="G.155 (IV.def.2): Similarly afigure is said to becircumscribed about a figure when the respective sides of the circumscribed figure pass through the respectiveangles of that about which it is circum...", fillcolor="#224422", URL="../G.155/index.html", target="_top"];
     "G.156" [label="G.156", tooltip="G.156 (IV.def.6): Acircle is said to becircumscribed about a figure when the arc of the circle passes through eachangle of thefigure about which it is circumscribed.", fillcolor="#224422", URL="../G.156/index.html", target="_top"];
     "G.157" [label="G.157", tooltip="G.157 (IV.5): Circumscribe about a given triangle a circle.", fillcolor="#222244", URL="../G.157/index.html", target="_top"];
     "G.162" [label="G.162", tooltip="G.162 (IV.10): Construct an isosceles triangle having each of the angles at the base double of the remaining one.", fillcolor="#222244", URL="../G.162/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (IV.11): Inscribe in a given circle an equilateral and equiangular pentagon.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.11" -> "G.1";
     "G.14" -> "G.1";
     "G.15" -> "G.1";
     "G.17" -> "G.1";
     "G.20" -> "G.1";
     "G.21" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.28" -> "G.1";
     "G.29" -> "G.1";
     "G.31" -> "G.1";
     "G.32" -> "G.1";
     "G.34" -> "G.1";
     "G.37" -> "G.1";
     "G.39" -> "G.1";
     "G.40" -> "G.1";
     "G.45" -> "G.1";
     "G.47" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.59" -> "G.1";
     "G.75" -> "G.1";
     "G.79" -> "G.1";
     "G.98" -> "G.1";
     "G.108" -> "G.1";
     "G.120" -> "G.1";
     "G.121" -> "G.1";
     "G.129" -> "G.1";
     "G.138" -> "G.1";
     "G.140" -> "G.1";
     "G.144" -> "G.1";
     "G.145" -> "G.1";
     "G.149" -> "G.1";
     "G.157" -> "G.1";
     "G.162" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.18" -> "G.2";
     "G.22" -> "G.2";
     "G.30" -> "G.2";
     "G.33" -> "G.2";
     "G.34" -> "G.2";
     "G.37" -> "G.2";
     "G.39" -> "G.2";
     "G.40" -> "G.2";
     "G.48" -> "G.2";
     "G.52" -> "G.2";
     "G.53" -> "G.2";
     "G.55" -> "G.2";
     "G.56" -> "G.2";
     "G.58" -> "G.2";
     "G.65" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.60" -> "G.3";
     "G.65" -> "G.3";
     "G.118" -> "G.3";
     "G.138" -> "G.3";
     "G.145" -> "G.3";
     "G.146" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.12" -> "G.4";
     "G.14" -> "G.4";
     "G.17" -> "G.4";
     "G.18" -> "G.4";
     "G.20" -> "G.4";
     "G.21" -> "G.4";
     "G.22" -> "G.4";
     "G.24" -> "G.4";
     "G.25" -> "G.4";
     "G.28" -> "G.4";
     "G.29" -> "G.4";
     "G.30" -> "G.4";
     "G.31" -> "G.4";
     "G.32" -> "G.4";
     "G.33" -> "G.4";
     "G.34" -> "G.4";
     "G.37" -> "G.4";
     "G.39" -> "G.4";
     "G.40" -> "G.4";
     "G.41" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.58" -> "G.4";
     "G.59" -> "G.4";
     "G.60" -> "G.4";
     "G.61" -> "G.4";
     "G.62" -> "G.4";
     "G.65" -> "G.4";
     "G.75" -> "G.4";
     "G.79" -> "G.4";
     "G.81" -> "G.4";
     "G.88" -> "G.4";
     "G.93" -> "G.4";
     "G.98" -> "G.4";
     "G.100" -> "G.4";
     "G.108" -> "G.4";
     "G.111" -> "G.4";
     "G.117" -> "G.4";
     "G.118" -> "G.4";
     "G.120" -> "G.4";
     "G.121" -> "G.4";
     "G.122" -> "G.4";
     "G.123" -> "G.4";
     "G.124" -> "G.4";
     "G.126" -> "G.4";
     "G.129" -> "G.4";
     "G.132" -> "G.4";
     "G.133" -> "G.4";
     "G.136" -> "G.4";
     "G.138" -> "G.4";
     "G.139" -> "G.4";
     "G.140" -> "G.4";
     "G.144" -> "G.4";
     "G.145" -> "G.4";
     "G.146" -> "G.4";
     "G.147" -> "G.4";
     "G.149" -> "G.4";
     "G.157" -> "G.4";
     "G.163" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.138" -> "G.6";
     "G.146" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.66" -> "G.9";
     "G.96" -> "G.9";
     "G.122" -> "G.9";
     "G.126" -> "G.9";
     "G.148" -> "G.9";
     "G.155" -> "G.9";
     "G.156" -> "G.9";
     "G.157" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.96" -> "G.10";
     "G.98" -> "G.10";
     "G.100" -> "G.10";
     "G.102" -> "G.10";
     "G.108" -> "G.10";
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.121" -> "G.10";
     "G.122" -> "G.10";
     "G.123" -> "G.10";
     "G.124" -> "G.10";
     "G.125" -> "G.10";
     "G.126" -> "G.10";
     "G.129" -> "G.10";
     "G.133" -> "G.10";
     "G.134" -> "G.10";
     "G.136" -> "G.10";
     "G.139" -> "G.10";
     "G.140" -> "G.10";
     "G.144" -> "G.10";
     "G.145" -> "G.10";
     "G.146" -> "G.10";
     "G.147" -> "G.10";
     "G.148" -> "G.10";
     "G.149" -> "G.10";
     "G.156" -> "G.10";
     "G.157" -> "G.10";
     "G.163" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
     "G.96" -> "G.11";
     "G.98" -> "G.11";
     "G.100" -> "G.11";
     "G.102" -> "G.11";
     "G.108" -> "G.11";
     "G.120" -> "G.11";
     "G.121" -> "G.11";
     "G.122" -> "G.11";
     "G.123" -> "G.11";
     "G.124" -> "G.11";
     "G.133" -> "G.11";
     "G.134" -> "G.11";
     "G.136" -> "G.11";
     "G.140" -> "G.11";
     "G.144" -> "G.11";
     "G.145" -> "G.11";
     "G.157" -> "G.11";
     "G.13" -> "G.12";
     "G.17" -> "G.12";
     "G.20" -> "G.12";
     "G.24" -> "G.12";
     "G.25" -> "G.12";
     "G.27" -> "G.12";
     "G.28" -> "G.12";
     "G.29" -> "G.12";
     "G.31" -> "G.12";
     "G.32" -> "G.12";
     "G.34" -> "G.12";
     "G.41" -> "G.12";
     "G.42" -> "G.12";
     "G.43" -> "G.12";
     "G.44" -> "G.12";
     "G.45" -> "G.12";
     "G.47" -> "G.12";
     "G.48" -> "G.12";
     "G.51" -> "G.12";
     "G.53" -> "G.12";
     "G.59" -> "G.12";
     "G.60" -> "G.12";
     "G.62" -> "G.12";
     "G.63" -> "G.12";
     "G.64" -> "G.12";
     "G.66" -> "G.12";
     "G.70" -> "G.12";
     "G.72" -> "G.12";
     "G.78" -> "G.12";
     "G.79" -> "G.12";
     "G.100" -> "G.12";
     "G.125" -> "G.12";
     "G.139" -> "G.12";
     "G.140" -> "G.12";
     "G.148" -> "G.12";
     "G.149" -> "G.12";
     "G.157" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.63" -> "G.13";
     "G.75" -> "G.13";
     "G.162" -> "G.13";
     "G.163" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.27" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.34" -> "G.14";
     "G.41" -> "G.14";
     "G.43" -> "G.14";
     "G.45" -> "G.14";
     "G.47" -> "G.14";
     "G.51" -> "G.14";
     "G.58" -> "G.14";
     "G.60" -> "G.14";
     "G.65" -> "G.14";
     "G.70" -> "G.14";
     "G.79" -> "G.14";
     "G.88" -> "G.14";
     "G.93" -> "G.14";
     "G.100" -> "G.14";
     "G.102" -> "G.14";
     "G.123" -> "G.14";
     "G.124" -> "G.14";
     "G.125" -> "G.14";
     "G.133" -> "G.14";
     "G.136" -> "G.14";
     "G.139" -> "G.14";
     "G.140" -> "G.14";
     "G.144" -> "G.14";
     "G.145" -> "G.14";
     "G.147" -> "G.14";
     "G.149" -> "G.14";
     "G.157" -> "G.14";
     "G.162" -> "G.14";
     "G.163" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.47" -> "G.15";
     "G.147" -> "G.15";
     "G.162" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.39" -> "G.16";
     "G.40" -> "G.16";
     "G.56" -> "G.16";
     "G.64" -> "G.16";
     "G.65" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.42" -> "G.18";
     "G.45" -> "G.18";
     "G.58" -> "G.18";
     "G.59" -> "G.18";
     "G.66" -> "G.18";
     "G.93" -> "G.18";
     "G.123" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.39" -> "G.19";
     "G.40" -> "G.19";
     "G.64" -> "G.19";
     "G.72" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.27" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.45" -> "G.21";
     "G.47" -> "G.21";
     "G.75" -> "G.21";
     "G.93" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.27" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.30" -> "G.22";
     "G.31" -> "G.22";
     "G.32" -> "G.22";
     "G.33" -> "G.22";
     "G.34" -> "G.22";
     "G.37" -> "G.22";
     "G.39" -> "G.22";
     "G.40" -> "G.22";
     "G.41" -> "G.22";
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.45" -> "G.22";
     "G.48" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.58" -> "G.22";
     "G.59" -> "G.22";
     "G.60" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.64" -> "G.22";
     "G.75" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.78" -> "G.22";
     "G.79" -> "G.22";
     "G.93" -> "G.22";
     "G.98" -> "G.22";
     "G.100" -> "G.22";
     "G.118" -> "G.22";
     "G.120" -> "G.22";
     "G.122" -> "G.22";
     "G.123" -> "G.22";
     "G.124" -> "G.22";
     "G.125" -> "G.22";
     "G.127" -> "G.22";
     "G.132" -> "G.22";
     "G.133" -> "G.22";
     "G.134" -> "G.22";
     "G.136" -> "G.22";
     "G.138" -> "G.22";
     "G.139" -> "G.22";
     "G.140" -> "G.22";
     "G.148" -> "G.22";
     "G.155" -> "G.22";
     "G.156" -> "G.22";
     "G.162" -> "G.22";
     "G.163" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.27" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.60" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.79" -> "G.24";
     "G.133" -> "G.24";
     "G.136" -> "G.24";
     "G.157" -> "G.24";
     "G.28" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.100" -> "G.25";
     "G.118" -> "G.25";
     "G.123" -> "G.25";
     "G.139" -> "G.25";
     "G.162" -> "G.25";
     "G.27" -> "G.26";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.45" -> "G.26";
     "G.162" -> "G.27";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.48" -> "G.29";
     "G.98" -> "G.29";
     "G.100" -> "G.29";
     "G.145" -> "G.29";
     "G.31" -> "G.30";
     "G.48" -> "G.30";
     "G.118" -> "G.30";
     "G.32" -> "G.31";
     "G.163" -> "G.31";
     "G.41" -> "G.32";
     "G.98" -> "G.32";
     "G.157" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.39" -> "G.33";
     "G.40" -> "G.33";
     "G.42" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.59" -> "G.33";
     "G.75" -> "G.33";
     "G.76" -> "G.33";
     "G.77" -> "G.33";
     "G.78" -> "G.33";
     "G.79" -> "G.33";
     "G.81" -> "G.33";
     "G.98" -> "G.33";
     "G.100" -> "G.33";
     "G.108" -> "G.33";
     "G.118" -> "G.33";
     "G.120" -> "G.33";
     "G.121" -> "G.33";
     "G.125" -> "G.33";
     "G.139" -> "G.33";
     "G.140" -> "G.33";
     "G.144" -> "G.33";
     "G.145" -> "G.33";
     "G.157" -> "G.33";
     "G.37" -> "G.34";
     "G.75" -> "G.34";
     "G.140" -> "G.34";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.62" -> "G.36";
     "G.64" -> "G.36";
     "G.72" -> "G.36";
     "G.79" -> "G.36";
     "G.39" -> "G.37";
     "G.40" -> "G.37";
     "G.42" -> "G.37";
     "G.56" -> "G.37";
     "G.59" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.38";
     "G.79" -> "G.39";
     "G.41" -> "G.40";
     "G.56" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.118" -> "G.42";
     "G.120" -> "G.42";
     "G.139" -> "G.42";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.118" -> "G.44";
     "G.120" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.134" -> "G.48";
     "G.149" -> "G.48";
     "G.62" -> "G.51";
     "G.100" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.59" -> "G.52";
     "G.60" -> "G.52";
     "G.62" -> "G.52";
     "G.64" -> "G.52";
     "G.65" -> "G.52";
     "G.66" -> "G.52";
     "G.70" -> "G.52";
     "G.75" -> "G.52";
     "G.79" -> "G.52";
     "G.58" -> "G.53";
     "G.60" -> "G.53";
     "G.56" -> "G.55";
     "G.59" -> "G.56";
     "G.60" -> "G.56";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.75" -> "G.56";
     "G.59" -> "G.58";
     "G.66" -> "G.58";
     "G.75" -> "G.58";
     "G.79" -> "G.58";
     "G.88" -> "G.58";
     "G.123" -> "G.59";
     "G.125" -> "G.59";
     "G.139" -> "G.59";
     "G.140" -> "G.59";
     "G.149" -> "G.59";
     "G.162" -> "G.59";
     "G.65" -> "G.60";
     "G.62" -> "G.61";
     "G.66" -> "G.61";
     "G.70" -> "G.61";
     "G.72" -> "G.61";
     "G.86" -> "G.61";
     "G.96" -> "G.61";
     "G.118" -> "G.61";
     "G.131" -> "G.61";
     "G.139" -> "G.61";
     "G.145" -> "G.61";
     "G.147" -> "G.61";
     "G.162" -> "G.61";
     "G.64" -> "G.62";
     "G.65" -> "G.62";
     "G.66" -> "G.62";
     "G.70" -> "G.62";
     "G.72" -> "G.62";
     "G.75" -> "G.62";
     "G.64" -> "G.63";
     "G.75" -> "G.63";
     "G.79" -> "G.63";
     "G.88" -> "G.63";
     "G.93" -> "G.63";
     "G.144" -> "G.63";
     "G.145" -> "G.63";
     "G.162" -> "G.63";
     "G.65" -> "G.64";
     "G.66" -> "G.64";
     "G.88" -> "G.65";
     "G.70" -> "G.66";
     "G.79" -> "G.70";
     "G.88" -> "G.72";
     "G.79" -> "G.75";
     "G.88" -> "G.75";
     "G.93" -> "G.75";
     "G.78" -> "G.76";
     "G.78" -> "G.77";
     "G.118" -> "G.77";
     "G.120" -> "G.77";
     "G.79" -> "G.78";
     "G.93" -> "G.79";
     "G.144" -> "G.79";
     "G.88" -> "G.81";
     "G.93" -> "G.81";
     "G.144" -> "G.81";
     "G.145" -> "G.81";
     "G.162" -> "G.81";
     "G.88" -> "G.86";
     "G.93" -> "G.88";
     "G.144" -> "G.88";
     "G.162" -> "G.93";
     "G.139" -> "G.96";
     "G.157" -> "G.96";
     "G.108" -> "G.98";
     "G.144" -> "G.100";
     "G.108" -> "G.102";
     "G.129" -> "G.108";
     "G.118" -> "G.111";
     "G.120" -> "G.111";
     "G.121" -> "G.111";
     "G.140" -> "G.111";
     "G.145" -> "G.111";
     "G.118" -> "G.117";
     "G.145" -> "G.118";
     "G.149" -> "G.118";
     "G.121" -> "G.120";
     "G.144" -> "G.120";
     "G.145" -> "G.120";
     "G.140" -> "G.121";
     "G.123" -> "G.122";
     "G.124" -> "G.123";
     "G.134" -> "G.123";
     "G.125" -> "G.124";
     "G.139" -> "G.125";
     "G.140" -> "G.125";
     "G.140" -> "G.126";
     "G.149" -> "G.126";
     "G.162" -> "G.126";
     "G.129" -> "G.127";
     "G.133" -> "G.127";
     "G.133" -> "G.129";
     "G.133" -> "G.131";
     "G.134" -> "G.131";
     "G.136" -> "G.131";
     "G.133" -> "G.132";
     "G.134" -> "G.132";
     "G.134" -> "G.133";
     "G.163" -> "G.133";
     "G.136" -> "G.134";
     "G.163" -> "G.134";
     "G.163" -> "G.136";
     "G.139" -> "G.138";
     "G.140" -> "G.139";
     "G.157" -> "G.139";
     "G.149" -> "G.140";
     "G.162" -> "G.140";
     "G.145" -> "G.144";
     "G.162" -> "G.145";
     "G.147" -> "G.146";
     "G.162" -> "G.147";
     "G.149" -> "G.148";
     "G.163" -> "G.148";
     "G.163" -> "G.149";
     "G.156" -> "G.155";
     "G.157" -> "G.155";
     "G.157" -> "G.156";
     "G.162" -> "G.157";
     "G.163" -> "G.162";
   }

Required for
------------

:ref:`G.164 <G.164>`

.. toctree::
   :hidden:

   code
   heath
