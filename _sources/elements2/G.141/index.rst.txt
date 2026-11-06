:order: 141
:number: 141
:canonical_id: G.141
:original_id: III.33
:title: G.141 construct a circle segment on a chord admitting a given angle
:volume: II
:book: III
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles
:category: problem, construction, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, straight-line, segment-of-circle, plane-angle, rectilineal-angle, acute-angle, obtuse-angle, figure, right-angle, centre, extremity, diameter, tangent-to-circle, angle-in-segment, plane, equality
:dependencies: G.4, G.14, G.15, G.16, G.22, G.24, G.30, G.32, G.34, G.48, G.76, G.118, G.126, G.139, G.140
:excerpt: On a given segment, construct a segment of a circle admitting an angle equal to a given rectilineal angle.

.. _G.141:
.. _III.33:

G.141 construct a circle segment on a chord admitting a given angle
===================================================================

.. rubric:: `III.33 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/33/>`_

.. enunciation::

   On a given :term:`segment <G.4>`, construct a :term:`segment of a circle <G.126>` admitting an :term:`angle <G.22>` equal to a given :term:`rectilineal angle <G.30>`.

.. signature:: problem

   | :fn:`circle_segment_with_angle <G.141>`\ (:g:`/ A B / <g1:/ A B />`, :g:`< C ) <g1:< C )>`) → :g:`( A E B ) <g1:( A E B )>`
   | **given** :g:`/ A B / <g1:/ A B />`, :g:`< C ) <g1:< C )>`
   | **construct** :g:`< A E B ) <g1:< A E B )>` in segment :g:`( A E B ) <g1:( A E B )>` on :g:`/ A B / <g1:/ A B />` :eq:`= <g1:< A E B ) = g1:< C )>` :g:`< C ) <g1:< C )>`

.. picture:: g1.svg
   :alt: Proposition 33 first figure: acute angle case

.. picture:: g2.svg
   :alt: Proposition 33 second figure: right angle case

.. picture:: g3.svg
   :alt: Proposition 33 third figure: obtuse angle case

.. step:: given ∵ segment_def, rectilineal_angle_def, segment_circle_figure_def <G.4, G.30, G.126>

   :g:`/ A B / <g1:/ A B />`, rectilineal angle :g:`< C ) <g1:< C )>`

.. step:: construct ∵ copy_angle, perpendicular_at, bisect_segment, segment <G.48, G.34, G.32, G.14>

   :fn:`copy_angle <G.48>`\ (:g:`/ A B / <g1:/ A B />`, :g:`A <g1:A>`, :g:`< C ) <g1:< C )>`) → :g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< C )>` :g:`< C ) <g1:< C )>`, :fn:`perpendicular_at <G.34>`\ (:g:`/ D A / <g1:/ D A />`, :g:`A <g1:A>`) → :g:`/ A E / <g1:/ A E />` ⊥ :g:`/ D A / <g1:/ D A />`, :fn:`bisect_segment <G.32>`\ (:g:`/ A B / <g1:/ A B />`) → :g:`F <g1:F>`, :fn:`perpendicular_at <G.34>`\ (:g:`/ A B / <g1:/ A B />`, :g:`F <g1:F>`) → :g:`/ F G / <g1:/ F G />` ⊥ :g:`/ A B / <g1:/ A B />`, :fn:`segment <G.14>`\ (:g:`G <g1:G>`, :g:`B <g1:B>`) → :g:`/ G B / <g1:/ G B />`

.. step:: construct ∵ sas_congruence, circle, segment <G.24, G.15, G.14>

   :g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`, :g:`< A F G ) <g1:< A F G )>` :eq:`= <g1:< A F G ) = g1:< B F G )>` :g:`< B F G ) <g1:< B F G )>` → :g:`/ A G / <g1:/ A G />` :eq:`= <g1:/ A G / = g1:/ G B />` :g:`/ G B / <g1:/ G B />`; :fn:`circle <G.15>`\ (:g:`G <g1:G>`, :g:`A <g1:A>`) → :g:`( A B E ) <g1:( A B E )>`, :fn:`segment <G.14>`\ (:g:`E <g1:E>`, :g:`B <g1:B>`) → :g:`/ E B / <g1:/ E B />`

.. step:: assert ∵ perpendicular_at_diameter_extremity_tangent <G.118>

   :g:`/ A D / <g1:/ A D />` ⊥ diameter :g:`/ A E / <g1:/ A E />` at :g:`A <g1:A>` → :g:`/ A D / <g1:/ A D />` touches :g:`( A B E ) <g1:( A B E )>` at :g:`A <g1:A>`

.. step:: assert ∵ alternate_segment_theorem <G.140>

   tangent :g:`/ A D / <g1:/ A D />` and chord :g:`/ A B / <g1:/ A B />` at :g:`A <g1:A>` → :g:`< D A B ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< A E B )>` :g:`< A E B ) <g1:< A E B )>` in alternate segment :g:`( A E B ) <g1:( A E B )>`

.. step:: conclude ∵ equal_transitive, thales_semicircle_theorem <G.16, G.139>

   :g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< C )>` :g:`< C ) <g1:< C )>` → :g:`< A E B ) <g1:< A E B )>` :eq:`= <g1:< A E B ) = g1:< C )>` :g:`< C ) <g1:< C )>` in segment :g:`( A E B ) <g1:( A E B )>` on :g:`/ A B / <g1:/ A B />`

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
     "G.40" [label="G.40", tooltip="G.40 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
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
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.def.2): Asegment is said totouch a circle which, meeting thecircle and being produced, does not cut the circle.", fillcolor="#224422", URL="../G.111/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.117/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (III.16): The line drawn at right angles to the diameter of a circle from its extremity falls outside the circle, no other line can be interposed between it and the arc, and the angle of the...", fillcolor="#222244", URL="../G.118/index.html", target="_top"];
     "G.120" [label="G.120", tooltip="G.120 (III.18): If a line touches a circle, the segment joined from the center to the point of contact is perpendicular to the tangent.", fillcolor="#222244", URL="../G.120/index.html", target="_top"];
     "G.121" [label="G.121", tooltip="G.121 (III.19): If a line touches a circle, the line drawn at right angles to the tangent from the point of contact passes through the center of the circle.", fillcolor="#222244", URL="../G.121/index.html", target="_top"];
     "G.122" [label="G.122", tooltip="G.122 (III.def.10): Asector of a circle is thefigure which, when anangle is constructed at thecenter of thecircle, is contained by thesegments containing the angle and the arc cut off by them.", fillcolor="#224422", URL="../G.122/index.html", target="_top"];
     "G.123" [label="G.123", tooltip="G.123 (III.20): In a circle, the angle at the center is double the angle at the circumference when the angles have the same arc as base.", fillcolor="#222244", URL="../G.123/index.html", target="_top"];
     "G.124" [label="G.124", tooltip="G.124 (III.21): In a circle, angles in the same segment are equal to one another.", fillcolor="#222244", URL="../G.124/index.html", target="_top"];
     "G.125" [label="G.125", tooltip="G.125 (III.22): The opposite angles of any quadrilateral inscribed in a circle sum to two right angles.", fillcolor="#222244", URL="../G.125/index.html", target="_top"];
     "G.126" [label="G.126", tooltip="G.126 (III.def.6): Asegment of a circle is thefigure contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.126/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (III.def.8): Anangle in a segment is theangle which, when apoint is taken on the arc of the segment andsegments are joined from it to theextremities of the segment which is thebase of the segme...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (III.31): In a circle, the angle in a semicircle is right, the angle in a greater segment is acute, and the angle in a lesser segment is obtuse.", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.140" [label="G.140", tooltip="G.140 (III.32): If a line touches a circle and a chord is drawn from the point of contact, the angles which the chord makes with the tangent equal the angles in the alternate segments of the circl...", fillcolor="#222244", URL="../G.140/index.html", target="_top"];
     "G.141" [label="G.141", tooltip="G.141 (III.33): On a given segment, construct a segment of a circle admitting an angle equal to a given rectilineal angle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.40" -> "G.1";
     "G.45" -> "G.1";
     "G.47" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.59" -> "G.1";
     "G.120" -> "G.1";
     "G.121" -> "G.1";
     "G.138" -> "G.1";
     "G.140" -> "G.1";
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
     "G.40" -> "G.2";
     "G.48" -> "G.2";
     "G.52" -> "G.2";
     "G.53" -> "G.2";
     "G.55" -> "G.2";
     "G.56" -> "G.2";
     "G.58" -> "G.2";
     "G.118" -> "G.2";
     "G.120" -> "G.2";
     "G.121" -> "G.2";
     "G.140" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.118" -> "G.3";
     "G.138" -> "G.3";
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
     "G.61" -> "G.4";
     "G.98" -> "G.4";
     "G.111" -> "G.4";
     "G.117" -> "G.4";
     "G.118" -> "G.4";
     "G.120" -> "G.4";
     "G.121" -> "G.4";
     "G.122" -> "G.4";
     "G.124" -> "G.4";
     "G.126" -> "G.4";
     "G.138" -> "G.4";
     "G.139" -> "G.4";
     "G.140" -> "G.4";
     "G.141" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.138" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.96" -> "G.9";
     "G.122" -> "G.9";
     "G.126" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.96" -> "G.10";
     "G.98" -> "G.10";
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.120" -> "G.10";
     "G.121" -> "G.10";
     "G.122" -> "G.10";
     "G.123" -> "G.10";
     "G.124" -> "G.10";
     "G.125" -> "G.10";
     "G.126" -> "G.10";
     "G.139" -> "G.10";
     "G.140" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
     "G.96" -> "G.11";
     "G.98" -> "G.11";
     "G.120" -> "G.11";
     "G.121" -> "G.11";
     "G.122" -> "G.11";
     "G.123" -> "G.11";
     "G.13" -> "G.12";
     "G.17" -> "G.12";
     "G.20" -> "G.12";
     "G.24" -> "G.12";
     "G.25" -> "G.12";
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
     "G.53" -> "G.12";
     "G.59" -> "G.12";
     "G.125" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.34" -> "G.14";
     "G.41" -> "G.14";
     "G.43" -> "G.14";
     "G.45" -> "G.14";
     "G.47" -> "G.14";
     "G.48" -> "G.14";
     "G.58" -> "G.14";
     "G.98" -> "G.14";
     "G.118" -> "G.14";
     "G.121" -> "G.14";
     "G.123" -> "G.14";
     "G.124" -> "G.14";
     "G.125" -> "G.14";
     "G.139" -> "G.14";
     "G.140" -> "G.14";
     "G.141" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.47" -> "G.15";
     "G.141" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.40" -> "G.16";
     "G.47" -> "G.16";
     "G.56" -> "G.16";
     "G.59" -> "G.16";
     "G.124" -> "G.16";
     "G.125" -> "G.16";
     "G.139" -> "G.16";
     "G.141" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.42" -> "G.18";
     "G.45" -> "G.18";
     "G.53" -> "G.18";
     "G.58" -> "G.18";
     "G.59" -> "G.18";
     "G.123" -> "G.18";
     "G.139" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.40" -> "G.19";
     "G.123" -> "G.19";
     "G.140" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.45" -> "G.21";
     "G.47" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.30" -> "G.22";
     "G.31" -> "G.22";
     "G.32" -> "G.22";
     "G.33" -> "G.22";
     "G.34" -> "G.22";
     "G.37" -> "G.22";
     "G.40" -> "G.22";
     "G.41" -> "G.22";
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.45" -> "G.22";
     "G.48" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.58" -> "G.22";
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
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.141" -> "G.24";
     "G.28" -> "G.25";
     "G.43" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.118" -> "G.25";
     "G.123" -> "G.25";
     "G.139" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.43" -> "G.26";
     "G.45" -> "G.26";
     "G.98" -> "G.26";
     "G.120" -> "G.26";
     "G.121" -> "G.26";
     "G.139" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.48" -> "G.29";
     "G.98" -> "G.29";
     "G.31" -> "G.30";
     "G.48" -> "G.30";
     "G.118" -> "G.30";
     "G.141" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.98" -> "G.32";
     "G.141" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.40" -> "G.33";
     "G.42" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.59" -> "G.33";
     "G.76" -> "G.33";
     "G.77" -> "G.33";
     "G.98" -> "G.33";
     "G.118" -> "G.33";
     "G.120" -> "G.33";
     "G.121" -> "G.33";
     "G.125" -> "G.33";
     "G.139" -> "G.33";
     "G.37" -> "G.34";
     "G.98" -> "G.34";
     "G.140" -> "G.34";
     "G.141" -> "G.34";
     "G.37" -> "G.36";
     "G.42" -> "G.36";
     "G.56" -> "G.36";
     "G.59" -> "G.36";
     "G.123" -> "G.36";
     "G.125" -> "G.36";
     "G.139" -> "G.36";
     "G.40" -> "G.37";
     "G.42" -> "G.37";
     "G.56" -> "G.37";
     "G.59" -> "G.37";
     "G.140" -> "G.37";
     "G.40" -> "G.38";
     "G.121" -> "G.38";
     "G.41" -> "G.40";
     "G.56" -> "G.40";
     "G.42" -> "G.41";
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
     "G.141" -> "G.48";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.59" -> "G.52";
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
     "G.139" -> "G.76";
     "G.141" -> "G.76";
     "G.118" -> "G.77";
     "G.120" -> "G.77";
     "G.139" -> "G.77";
     "G.118" -> "G.96";
     "G.139" -> "G.96";
     "G.124" -> "G.98";
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
