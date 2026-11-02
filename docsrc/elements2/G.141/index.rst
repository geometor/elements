:order: 141
:number: 141
:canonical_id: G.141
:original_id: III.33
:title: G.141 describe on a given segment a segment of
:volume: II
:book: III
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles
:category: problem, construction, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, straight-line, segment-of-circle, plane-angle, rectilineal-angle, acute-angle, obtuse-angle, figure, right-angle, centre, extremity, diameter, tangent-to-circle, angle-in-segment, plane, equality
:dependencies: G.4, G.22, G.24, G.29, G.76, G.118, G.126, G.139, G.140
:excerpt: Describe on a given segment a segment of a circle admitting an angle equal to a given angle.

.. _G.141:
.. _III.33:

G.141 describe on a given segment a segment of
==============================================

.. rubric:: `III.33 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/33/>`_

.. enunciation::

   Describe on a given :term:`segment <G.4>` a :term:`segment of a circle <G.126>` admitting an :term:`angle <G.22>` equal to a given angle.

.. signature:: problem

   | :fn:`describe_segment_segment <G.141>`\ (:g:`/ A B / <g1:/ A B />`, :g:`< C ) <g1:< C )>`) → :g:`/ A B / <g3:/ A B />`, :g:`( A H B ) <g3:( A H B )>`
   | **given** :g:`/ A B / <g1:/ A B />`, the angle at :g:`< C ) <g1:< C )>`
   | **construct** on :g:`/ A B / <g3:/ A B />` the segment :g:`( A H B ) <g3:( A H B )>` of a circle has been described admitting an angle equal to the angle at :g:`< C ) <g3:< C )>`

.. picture:: g1.svg
   :alt: Proposition 33 first figure: acute angle case

.. picture:: g2.svg
   :alt: Proposition 33 second figure: right angle case

.. picture:: g3.svg
   :alt: Proposition 33 third figure: obtuse angle case

.. step:: given

   :g:`/ A B / <g1:/ A B />`, the angle at :g:`< C ) <g1:< C )>`

.. step:: assert

   The angle at :g:`< C ) <g1:< C )>` is then :term:`acute <G.77>`, or right, or :term:`obtuse <G.76>`.

.. step:: construct

   First let it be acute, and, as in the first :term:`figure <G.9>`, on :g:`/ A B / <g1:/ A B />`, and at :g:`A <g1:A>`, let :g:`< B A D ) <g1:< B A D )>` be constructed :eq:`equal <g1:< B A D ) = g1:< C )>` to the angle at :g:`< C ) <g1:< C )>`

.. step:: assert

   Therefore :g:`< B A D ) <g1:< B A D )>` is also acute.

.. step:: construct

   :fn:`perpendicular_at <G.33>`\ (:g:`/ D A / <g1:/ D A />`) → :g:`/ A E / <g1:/ A E />`

.. step:: construct

   :fn:`bisect_segment <G.31>`\ (:g:`/ A B / <g1:/ A B />`) → :g:`F <g1:F>` (bisected)

.. step:: construct

   :fn:`perpendicular_at <G.33>`\ (:g:`/ A B / <g1:/ A B />`, :g:`F <g1:F>`) → :g:`/ F G / <g1:/ F G />`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`G <g1:G>`, :g:`B <g1:B>`) → :g:`/ G B / <g1:/ G B />`

.. step:: assert

   Since :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`, and :g:`/ F G / <g1:/ F G />` is common → the two sides :g:`/ A F / <g1:/ A F />`, :g:`/ F G / <g1:/ F G />` are :eq:`equal <g1:/ A F / = g1:/ B F /; g1:/ F G / = g1:/ F G />` to the two sides :g:`/ B F / <g1:/ B F />`, :g:`/ F G / <g1:/ F G />`;

.. step:: assert

   And :g:`< A F G ) <g1:< A F G )>` is :eq:`equal <g1:< A F G ) = g1:< B F G )>` to :g:`< B F G ) <g1:< B F G )>`

.. step:: assert ∵ sas_congruence <G.24>

   Therefore the base :g:`/ A G / <g1:/ A G />` is :eq:`equal <g1:/ A G / = g1:/ B G />` to the base :g:`/ B G / <g1:/ B G />`.

.. step:: assert

   Therefore the :term:`circle <G.10>` described with :term:`center <G.14>` :g:`G <g1:G>` and distance :g:`/ G A / <g1:/ G A />` will pass through :g:`B <g1:B>` also.

.. step:: construct

   Let it be drawn

.. step:: assert

   Let it be :g:`( A B E ) <g1:( A B E )>`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`E <g1:E>`, :g:`B <g1:B>`) → :g:`/ E B / <g1:/ E B />`

.. step:: assert ∵ segment_drawn_right <G.118>

   Since :g:`/ A D / <g1:/ A D />` is drawn from :g:`A <g1:A>`, the :term:`extremity <G.3>` of the :term:`diameter <G.61>` :g:`/ A E / <g1:/ A E />`, :term:`at right angles <G.32>` to :g:`/ A E / <g1:/ A E />` → therefore :g:`/ A D / <g1:/ A D />` touches :g:`( A B E ) <g1:( A B E )>`.

.. step:: assert ∵ segment_touch_circle_iii_32 <G.140>

   Since then a segment :g:`/ A D / <g1:/ A D />` touches :g:`( A B E ) <g1:( A B E )>`, and from the :term:`point <G.1>` of contact at :g:`A <g1:A>` a segment :g:`/ A B / <g1:/ A B />` is drawn across in :g:`( A B E ) <g1:( A B E )>`, :g:`< D A B ) <g1:< D A B )>` is :eq:`equal <g1:< D A B ) = g1:< A E B )>` to :g:`< A E B ) <g1:< A E B )>` in the alternate segment of the circle.

.. step:: assert

   :g:`< D A B ) <g1:< D A B )>` is :eq:`equal <g1:< D A B ) = g1:< C )>` to the angle at :g:`< C ) <g1:< C )>`

.. step:: assert

   Therefore the angle at :g:`< C ) <g1:< C )>` is also :eq:`equal <g1:< C ) = g1:< A E B )>` to :g:`< A E B ) <g1:< A E B )>`.

.. step:: assert

   Therefore on :g:`/ A B / <g1:/ A B />` the segment :g:`( A E B ) <g1:( A E B )>` of a circle has been described admitting :g:`< A E B ) <g1:< A E B )>` :eq:`equal <g1:< A E B ) = g1:< C )>` to the given angle, the angle at :g:`< C ) <g1:< C )>`.

.. step:: assert

   Next let the angle at :g:`< C ) <g2:< C )>` be right

.. step:: assert

   And let it be again required to describe on :g:`/ A B / <g2:/ A B />` a segment of a circle admitting an angle equal to the right angle at :g:`< C ) <g2:< C )>`.

.. step:: construct

   Let :g:`< B A D ) <g2:< B A D )>` be constructed :eq:`equal <g2:< B A D ) = g2:< C )>` to the right angle at :g:`< C ) <g2:< C )>`, as is the case in the second figure

.. step:: construct

   :fn:`bisect_segment <G.31>`\ (:g:`/ A B / <g2:/ A B />`) → :g:`F <g2:F>` (bisected)

.. step:: construct

   With center :g:`F <g2:F>` and distance either :g:`/ F A / <g2:/ F A />` or :g:`/ F B / <g2:/ F B />` let :g:`( A E B ) <g2:( A E B )>` be described.

.. step:: assert ∵ segment_drawn_right <G.118>

   Therefore :g:`/ A D / <g2:/ A D />` touches :g:`( A B E ) <g2:( A B E )>`, because the angle at :g:`< A ) <g2:< A )>` is right.

.. step:: assert ∵ thales_semicircle_theorem <G.139>

   :g:`< B A D ) <g2:< B A D )>` is equal to the angle in the segment :g:`( A E B ) <g2:( A E B )>`, for the latter too is itself a right angle, being an angle in a semicircle.

.. step:: assert

   :g:`< B A D ) <g2:< B A D )>` is also :eq:`equal <g2:< B A D ) = g2:< C )>` to the angle at :g:`< C ) <g2:< C )>`.

.. step:: assert

   Therefore :g:`< A E B ) <g2:< A E B )>` is also :eq:`equal <g2:< A E B ) = g2:< C )>` to the angle at :g:`< C ) <g2:< C )>`.

.. step:: assert

   Therefore again the segment :g:`( A E B ) <g2:( A E B )>` of a circle has been described on :g:`/ A B / <g2:/ A B />` admitting an angle equal to the angle at :g:`< C ) <g2:< C )>`.

.. step:: assert

   Next, let the angle at :g:`< C ) <g3:< C )>` be obtuse

.. step:: construct

   And on :g:`/ A B / <g3:/ A B />`, and at :g:`A <g3:A>`, let :g:`< B A D ) <g3:< B A D )>` be constructed :eq:`equal <g3:< B A D ) = g3:< C )>` to it, as is the case in the third figure

.. step:: construct

   :fn:`perpendicular_at <G.33>`\ (:g:`/ A D / <g3:/ A D />`) → :g:`/ A E / <g3:/ A E />`

.. step:: construct

   Let :g:`/ A B / <g3:/ A B />` be again bisected at :g:`F <g3:F>`, let :g:`/ F G / <g3:/ F G />` be drawn at right angles to :g:`/ A B / <g3:/ A B />`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`G <g3:G>`, :g:`B <g3:B>`) → :g:`/ G B / <g3:/ G B />`

.. step:: assert

   Since :g:`/ A F / <g3:/ A F />` is again :eq:`equal <g3:/ A F / = g3:/ F B />` to :g:`/ F B / <g3:/ F B />`, and :g:`/ F G / <g3:/ F G />` is common → the two sides :g:`/ A F / <g3:/ A F />`, :g:`/ F G / <g3:/ F G />` are :eq:`equal <g3:/ A F / = g3:/ B F /; g3:/ F G / = g3:/ F G />` to the two sides :g:`/ B F / <g3:/ B F />`, :g:`/ F G / <g3:/ F G />`;

.. step:: assert

   And :g:`< A F G ) <g3:< A F G )>` is :eq:`equal <g3:< A F G ) = g3:< B F G )>` to :g:`< B F G ) <g3:< B F G )>`

.. step:: assert ∵ sas_congruence <G.24>

   Therefore the base :g:`/ A G / <g3:/ A G />` is :eq:`equal <g3:/ A G / = g3:/ B G />` to the base :g:`/ B G / <g3:/ B G />`.

.. step:: assert

   Therefore the circle described with center :g:`G <g3:G>` and distance :g:`/ G A / <g3:/ G A />` will pass through :g:`B <g3:B>` also

.. step:: assert

   Let it so pass, as :g:`( A E B ) <g3:( A E B )>`.

.. step:: assert ∵ segment_drawn_right <G.118>

   Since :g:`/ A D / <g3:/ A D />` is drawn at right angles to the diameter :g:`/ A E / <g3:/ A E />` from its extremity → :g:`/ A D / <g3:/ A D />` touches :g:`( A E B ) <g3:( A E B )>`.

.. step:: assert

   :g:`/ A B / <g3:/ A B />` has been drawn across from the point of contact at :g:`A <g3:A>`

.. step:: assert ∵ segment_touch_circle_iii_32 <G.140>

   Therefore :g:`< B A D ) <g3:< B A D )>` is equal to the angle constructed in the alternate segment :g:`( A H B ) <g3:( A H B )>` of the circle

.. step:: assert

   :g:`< B A D ) <g3:< B A D )>` is :eq:`equal <g3:< B A D ) = g3:< C )>` to the angle at :g:`< C ) <g3:< C )>`.

.. step:: assert

   Therefore the :term:`angle in the segment <G.138>` :g:`( A H B ) <g3:( A H B )>` is also equal to the angle at :g:`< C ) <g3:< C )>`.

.. step:: conclude

   Therefore on :g:`/ A B / <g3:/ A B />` the segment :g:`( A H B ) <g3:( A H B )>` of a circle has been described admitting an angle equal to the angle at :g:`< C ) <g3:< C )>`.

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
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.13/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.14/index.html", target="_top"];
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
     "G.27" [label="G.27", tooltip="G.27 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.37/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (I.def.11): An obtuse angle is greater than a right angle.", fillcolor="#224422", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.96" [label="G.96", tooltip="G.96 (I.def.18): A semicircle is the figure contained by a diameter and the arc cut off by it.", fillcolor="#224422", URL="../G.96/index.html", target="_top"];
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
     "G.138" [label="G.138", tooltip="G.138 (III.def.8): Anangle in a segment is theangle which, when apoint is taken on the arc of the segment andsegments are joined from it to theextremities of the segment which is thebase of the segme...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.140" [label="G.140", tooltip="G.140 (III.32): If a segment touch a circle, and from the point of contact there be drawn across, in the circle, a segment cutting the circle, the angles which it makes with the tangent will equal...", fillcolor="#222244", URL="../G.140/index.html", target="_top"];
     "G.141" [label="G.141", tooltip="G.141 (III.33): Describe on a given segment a segment of a circle admitting an angle equal to a given angle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.120" -> "G.1";
     "G.121" -> "G.1";
     "G.138" -> "G.1";
     "G.140" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.118" -> "G.3";
     "G.138" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.13" -> "G.4";
     "G.17" -> "G.4";
     "G.18" -> "G.4";
     "G.20" -> "G.4";
     "G.21" -> "G.4";
     "G.22" -> "G.4";
     "G.24" -> "G.4";
     "G.25" -> "G.4";
     "G.27" -> "G.4";
     "G.28" -> "G.4";
     "G.31" -> "G.4";
     "G.32" -> "G.4";
     "G.33" -> "G.4";
     "G.36" -> "G.4";
     "G.39" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.58" -> "G.4";
     "G.61" -> "G.4";
     "G.111" -> "G.4";
     "G.117" -> "G.4";
     "G.118" -> "G.4";
     "G.120" -> "G.4";
     "G.121" -> "G.4";
     "G.122" -> "G.4";
     "G.126" -> "G.4";
     "G.138" -> "G.4";
     "G.140" -> "G.4";
     "G.141" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.96" -> "G.9";
     "G.122" -> "G.9";
     "G.126" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.96" -> "G.10";
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.121" -> "G.10";
     "G.122" -> "G.10";
     "G.123" -> "G.10";
     "G.124" -> "G.10";
     "G.125" -> "G.10";
     "G.126" -> "G.10";
     "G.139" -> "G.10";
     "G.140" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.42" -> "G.11";
     "G.43" -> "G.11";
     "G.44" -> "G.11";
     "G.45" -> "G.11";
     "G.47" -> "G.11";
     "G.59" -> "G.11";
     "G.125" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.61" -> "G.14";
     "G.96" -> "G.14";
     "G.120" -> "G.14";
     "G.121" -> "G.14";
     "G.122" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.36" -> "G.16";
     "G.39" -> "G.16";
     "G.56" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.33" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.42" -> "G.18";
     "G.20" -> "G.19";
     "G.39" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.30" -> "G.21";
     "G.33" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.47" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.32" -> "G.22";
     "G.36" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.59" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.118" -> "G.22";
     "G.122" -> "G.22";
     "G.123" -> "G.22";
     "G.124" -> "G.22";
     "G.125" -> "G.22";
     "G.138" -> "G.22";
     "G.139" -> "G.22";
     "G.140" -> "G.22";
     "G.141" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.141" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.118" -> "G.25";
     "G.123" -> "G.25";
     "G.139" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.48" -> "G.28";
     "G.30" -> "G.29";
     "G.48" -> "G.29";
     "G.118" -> "G.29";
     "G.141" -> "G.29";
     "G.31" -> "G.30";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.42" -> "G.32";
     "G.55" -> "G.32";
     "G.56" -> "G.32";
     "G.59" -> "G.32";
     "G.76" -> "G.32";
     "G.77" -> "G.32";
     "G.118" -> "G.32";
     "G.120" -> "G.32";
     "G.121" -> "G.32";
     "G.125" -> "G.32";
     "G.139" -> "G.32";
     "G.36" -> "G.33";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.39" -> "G.36";
     "G.42" -> "G.36";
     "G.56" -> "G.36";
     "G.59" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.56" -> "G.39";
     "G.41" -> "G.40";
     "G.45" -> "G.40";
     "G.43" -> "G.41";
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
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.59" -> "G.56";
     "G.59" -> "G.58";
     "G.123" -> "G.59";
     "G.125" -> "G.59";
     "G.139" -> "G.59";
     "G.140" -> "G.59";
     "G.96" -> "G.61";
     "G.118" -> "G.61";
     "G.139" -> "G.61";
     "G.141" -> "G.76";
     "G.118" -> "G.77";
     "G.120" -> "G.77";
     "G.139" -> "G.96";
     "G.118" -> "G.111";
     "G.120" -> "G.111";
     "G.121" -> "G.111";
     "G.140" -> "G.111";
     "G.118" -> "G.117";
     "G.141" -> "G.118";
     "G.121" -> "G.120";
     "G.140" -> "G.121";
     "G.123" -> "G.122";
     "G.124" -> "G.123";
     "G.125" -> "G.124";
     "G.139" -> "G.125";
     "G.140" -> "G.125";
     "G.140" -> "G.126";
     "G.141" -> "G.126";
     "G.139" -> "G.138";
     "G.140" -> "G.139";
     "G.141" -> "G.139";
     "G.141" -> "G.140";
   }

.. toctree::
   :hidden:

   code
   heath
