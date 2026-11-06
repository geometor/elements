:order: 97
:number: 97
:canonical_id: G.97
:original_id: II.14
:title: G.97 construct a square equal to a polygon
:volume: I
:book: II
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, geometric-algebra
:category: problem, construction, plane-geometry, geometric-algebra
:tags: book-ii, point, segment, line, circle, quadrilateral, square, rectilineal-figure, contained-rectangle, straight-line, centre, semicircle, equality
:dependencies: G.10, G.12, G.14, G.16, G.18, G.19, G.21, G.32, G.63, G.74, G.75, G.79, G.81, G.87, G.96
:excerpt: Construct a square equal in area to a given rectilineal figure.

.. _G.97:
.. _II.14:

G.97 construct a square equal to a polygon
==========================================

.. rubric:: `II.14 <https://geometor.github.io/euclid/heath/volume_I/book_ii/propositions/14/>`_

.. enunciation::

   Construct a :term:`square <G.63>` equal in area to a given :term:`rectilineal figure <G.12>`.

.. signature:: problem

   | :fn:`square_from_polygon <G.97>`\ (:g:`A <g1:A>`) → :g:`/ E H / <g1:/ E H />`
   | **given** :g:`A <g1:A>`
   | **construct** :fn:`square_on_segment <G.75>`\ (:g:`/ E H / <g1:/ E H />`) :eq:`= <g1:/ E H / = g1:A>` :g:`A <g1:A>`

.. picture:: g1.svg
   :alt: Diagram

.. step:: given

   :g:`A <g1:A>`

.. step:: construct ∵ parallelogram_from_polygon, extend, cut_equal_segment <G.74, G.18, G.21>

   :fn:`parallelogram_from_polygon <G.74>`\ (:g:`A <g1:A>`) → :g:`< B D E C > <g1:< B D E C >>` (:eq:`= <g1:< B D E C > = g1:A>` :g:`A <g1:A>`), ? ¬(:g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ E D />` :g:`/ E D / <g1:/ E D />`) → :fn:`extend <G.18>`\ (:g:`/ B E / <g1:/ B E />`) → :g:`[ B F ] <g1:[ B E ]>`, :fn:`cut_equal_segment <G.21>`\ (:g:`[ B F ] <g1:[ B E ]>`, :g:`/ E D / <g1:/ E D />`) → :g:`/ E F / <g1:/ E F />` (:eq:`= <g1:/ E F / = g1:/ E D />` :g:`/ E D / <g1:/ E D />`)

.. step:: construct ∵ bisect_segment, semicircle_def, extend, segment <G.32, G.96, G.18, G.14>

   :fn:`bisect_segment <G.32>`\ (:g:`/ B F / <g1:/ B F />`) → :g:`G <g1:G>` (:g:`/ G B / <g1:/ G B />` :eq:`= <g1:/ G B / = g1:/ G F />` :g:`/ G F / <g1:/ G F />`), :fn:`semicircle_def <G.96>`\ (:g:`G <g1:G>`, :g:`/ G B / <g1:/ G B />`) → :g:`( B H F ) <g1:( B H F )>`, :fn:`extend <G.18>`\ (:g:`/ D E / <g1:/ E D />`) ∩ :g:`( B H F ) <g1:( B H F )>` → :g:`H <g1:H>`, :fn:`segment <G.14>`\ (:g:`G <g1:G>`, :g:`H <g1:H>`) → :g:`/ G H / <g1:/ G H />`

.. step:: assert ∵ difference_of_squares_equal_unequal, circle_radii <G.87, G.10>

   :g:`/ G B / <g1:/ G B />` :eq:`= <g1:/ G B / = g1:/ G F />` :g:`/ G F / <g1:/ G F />` → :fn:`rectangular_parallelogram_said_def <G.81>`\ (:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) + :fn:`square_on_segment <G.75>`\ (:g:`/ E G / <g1:/ E G />`) = :fn:`square_on_segment <G.75>`\ (:g:`/ G F / <g1:/ G F />`), :g:`/ G F / <g1:/ G F />` :eq:`= <g1:/ G F / = g1:/ G H />` :g:`/ G H / <g1:/ G H />` → :fn:`rectangular_parallelogram_said_def <G.81>`\ (:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) + :fn:`square_on_segment <G.75>`\ (:g:`/ E G / <g1:/ E G />`) = :fn:`square_on_segment <G.75>`\ (:g:`/ G H / <g1:/ G H />`)

.. step:: assert ∵ pythagorean_theorem, equal_transitive, subtract_equals <G.79, G.16, G.19>

   :fn:`square_on_segment <G.75>`\ (:g:`/ E H / <g1:/ E H />`) + :fn:`square_on_segment <G.75>`\ (:g:`/ E G / <g1:/ E G />`) = :fn:`square_on_segment <G.75>`\ (:g:`/ G H / <g1:/ G H />`) → :fn:`rectangular_parallelogram_said_def <G.81>`\ (:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) + :fn:`square_on_segment <G.75>`\ (:g:`/ E G / <g1:/ E G />`) = :fn:`square_on_segment <G.75>`\ (:g:`/ E H / <g1:/ E H />`) + :fn:`square_on_segment <G.75>`\ (:g:`/ E G / <g1:/ E G />`) → :fn:`rectangular_parallelogram_said_def <G.81>`\ (:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) = :fn:`square_on_segment <G.75>`\ (:g:`/ E H / <g1:/ E H />`)

.. step:: conclude ∵ rectangular_parallelogram_said_def, equal_transitive <G.81, G.16>

   :g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ E D />` :g:`/ E D / <g1:/ E D />` → :g:`< B D E C > <g1:< B D E C >>` = :fn:`rectangular_parallelogram_said_def <G.81>`\ (:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) = :fn:`square_on_segment <G.75>`\ (:g:`/ E H / <g1:/ E H />`), :g:`< B D E C > <g1:< B D E C >>` :eq:`= <g1:< B D E C > = g1:A>` :g:`A <g1:A>` → :fn:`square_on_segment <G.75>`\ (:g:`/ E H / <g1:/ E H />`) :eq:`= <g1:/ E H / = g1:A>` :g:`A <g1:A>`

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
     "G.39" [label="G.39", tooltip="G.39 (I.14): If two segments at a point on a line on opposite sides make adjacent angles summing to two right angles, the two segments are collinear.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
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
     "G.57" [label="G.57", tooltip="G.57 (I.30): Lines parallel to the same line are parallel to one another.", fillcolor="#222244", URL="../G.57/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.64" [label="G.64", tooltip="G.64 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.64/index.html", target="_top"];
     "G.65" [label="G.65", tooltip="G.65 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.65/index.html", target="_top"];
     "G.66" [label="G.66", tooltip="G.66 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.66/index.html", target="_top"];
     "G.67" [label="G.67", tooltip="G.67 (I.38): Triangles on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.67/index.html", target="_top"];
     "G.70" [label="G.70", tooltip="G.70 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.70/index.html", target="_top"];
     "G.71" [label="G.71", tooltip="G.71 (I.42): Construct, in a given angle, a parallelogram equal in area to a given triangle.", fillcolor="#222244", URL="../G.71/index.html", target="_top"];
     "G.72" [label="G.72", tooltip="G.72 (I.43): In any parallelogram, the complements of the parallelograms about the diagonal are equal in area.", fillcolor="#222244", URL="../G.72/index.html", target="_top"];
     "G.73" [label="G.73", tooltip="G.73 (I.44): Apply to a given segment, in a given angle, a parallelogram equal in area to a given triangle.", fillcolor="#222244", URL="../G.73/index.html", target="_top"];
     "G.74" [label="G.74", tooltip="G.74 (I.45): Construct, in a given angle, a parallelogram equal in area to a given polygon.", fillcolor="#222244", URL="../G.74/index.html", target="_top"];
     "G.75" [label="G.75", tooltip="G.75 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.75/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (I.def.11): An obtuse angle is greater than a right angle.", fillcolor="#224422", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (I.def.21): A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.", fillcolor="#224422", URL="../G.78/index.html", target="_top"];
     "G.79" [label="G.79", tooltip="G.79 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.79/index.html", target="_top"];
     "G.81" [label="G.81", tooltip="G.81 (II.def.1): Any rectangular parallelogram is said to becontained by the twosegments containing theright angle.", fillcolor="#224422", URL="../G.81/index.html", target="_top"];
     "G.86" [label="G.86", tooltip="G.86 (II.def.2): And in any parallelogrammic area let any one whatever of the parallelograms about itsdiameter with the two complements be called agnomon.", fillcolor="#224422", URL="../G.86/index.html", target="_top"];
     "G.87" [label="G.87", tooltip="G.87 (II.5): If a segment is cut into equal and unequal parts, the rectangle contained by the unequal parts together with the square on the segment between the points of section equals the squa...", fillcolor="#222244", URL="../G.87/index.html", target="_top"];
     "G.96" [label="G.96", tooltip="G.96 (I.def.18): A semicircle is the figure contained by a diameter and the arc cut off by it.", fillcolor="#224422", URL="../G.96/index.html", target="_top"];
     "G.97" [label="G.97", tooltip="G.97 (II.14): Construct a square equal in area to a given rectilineal figure.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.71" -> "G.1";
     "G.73" -> "G.1";
     "G.74" -> "G.1";
     "G.75" -> "G.1";
     "G.79" -> "G.1";
     "G.87" -> "G.1";
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
     "G.57" -> "G.2";
     "G.58" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.60" -> "G.3";
     "G.65" -> "G.3";
     "G.74" -> "G.3";
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
     "G.57" -> "G.4";
     "G.58" -> "G.4";
     "G.60" -> "G.4";
     "G.61" -> "G.4";
     "G.62" -> "G.4";
     "G.65" -> "G.4";
     "G.71" -> "G.4";
     "G.73" -> "G.4";
     "G.74" -> "G.4";
     "G.75" -> "G.4";
     "G.79" -> "G.4";
     "G.81" -> "G.4";
     "G.87" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.66" -> "G.9";
     "G.67" -> "G.9";
     "G.96" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.96" -> "G.10";
     "G.97" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
     "G.96" -> "G.11";
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
     "G.43" -> "G.12";
     "G.44" -> "G.12";
     "G.45" -> "G.12";
     "G.47" -> "G.12";
     "G.48" -> "G.12";
     "G.51" -> "G.12";
     "G.53" -> "G.12";
     "G.60" -> "G.12";
     "G.62" -> "G.12";
     "G.63" -> "G.12";
     "G.64" -> "G.12";
     "G.66" -> "G.12";
     "G.67" -> "G.12";
     "G.70" -> "G.12";
     "G.71" -> "G.12";
     "G.72" -> "G.12";
     "G.73" -> "G.12";
     "G.74" -> "G.12";
     "G.78" -> "G.12";
     "G.79" -> "G.12";
     "G.97" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.63" -> "G.13";
     "G.75" -> "G.13";
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
     "G.51" -> "G.14";
     "G.58" -> "G.14";
     "G.60" -> "G.14";
     "G.65" -> "G.14";
     "G.70" -> "G.14";
     "G.71" -> "G.14";
     "G.73" -> "G.14";
     "G.74" -> "G.14";
     "G.79" -> "G.14";
     "G.87" -> "G.14";
     "G.97" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.47" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.39" -> "G.16";
     "G.40" -> "G.16";
     "G.47" -> "G.16";
     "G.56" -> "G.16";
     "G.57" -> "G.16";
     "G.64" -> "G.16";
     "G.65" -> "G.16";
     "G.66" -> "G.16";
     "G.67" -> "G.16";
     "G.70" -> "G.16";
     "G.71" -> "G.16";
     "G.73" -> "G.16";
     "G.74" -> "G.16";
     "G.75" -> "G.16";
     "G.87" -> "G.16";
     "G.97" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.39" -> "G.18";
     "G.41" -> "G.18";
     "G.45" -> "G.18";
     "G.53" -> "G.18";
     "G.58" -> "G.18";
     "G.66" -> "G.18";
     "G.67" -> "G.18";
     "G.73" -> "G.18";
     "G.97" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.39" -> "G.19";
     "G.40" -> "G.19";
     "G.64" -> "G.19";
     "G.72" -> "G.19";
     "G.97" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.45" -> "G.21";
     "G.47" -> "G.21";
     "G.51" -> "G.21";
     "G.75" -> "G.21";
     "G.97" -> "G.21";
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
     "G.39" -> "G.22";
     "G.40" -> "G.22";
     "G.41" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.45" -> "G.22";
     "G.48" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.57" -> "G.22";
     "G.58" -> "G.22";
     "G.60" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.64" -> "G.22";
     "G.71" -> "G.22";
     "G.73" -> "G.22";
     "G.74" -> "G.22";
     "G.75" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.78" -> "G.22";
     "G.79" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.60" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.79" -> "G.24";
     "G.28" -> "G.25";
     "G.43" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.28" -> "G.26";
     "G.39" -> "G.26";
     "G.41" -> "G.26";
     "G.43" -> "G.26";
     "G.45" -> "G.26";
     "G.51" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.48" -> "G.29";
     "G.31" -> "G.30";
     "G.48" -> "G.30";
     "G.71" -> "G.30";
     "G.73" -> "G.30";
     "G.74" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.71" -> "G.32";
     "G.97" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.39" -> "G.33";
     "G.40" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.73" -> "G.33";
     "G.74" -> "G.33";
     "G.75" -> "G.33";
     "G.76" -> "G.33";
     "G.77" -> "G.33";
     "G.78" -> "G.33";
     "G.79" -> "G.33";
     "G.81" -> "G.33";
     "G.37" -> "G.34";
     "G.75" -> "G.34";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.62" -> "G.36";
     "G.64" -> "G.36";
     "G.72" -> "G.36";
     "G.74" -> "G.36";
     "G.79" -> "G.36";
     "G.87" -> "G.36";
     "G.39" -> "G.37";
     "G.40" -> "G.37";
     "G.56" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.38";
     "G.74" -> "G.39";
     "G.79" -> "G.39";
     "G.41" -> "G.40";
     "G.56" -> "G.40";
     "G.73" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.71" -> "G.48";
     "G.62" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.57" -> "G.52";
     "G.58" -> "G.52";
     "G.60" -> "G.52";
     "G.62" -> "G.52";
     "G.64" -> "G.52";
     "G.65" -> "G.52";
     "G.66" -> "G.52";
     "G.67" -> "G.52";
     "G.70" -> "G.52";
     "G.71" -> "G.52";
     "G.73" -> "G.52";
     "G.74" -> "G.52";
     "G.75" -> "G.52";
     "G.79" -> "G.52";
     "G.57" -> "G.53";
     "G.58" -> "G.53";
     "G.60" -> "G.53";
     "G.56" -> "G.55";
     "G.73" -> "G.55";
     "G.57" -> "G.56";
     "G.60" -> "G.56";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.73" -> "G.56";
     "G.74" -> "G.56";
     "G.75" -> "G.56";
     "G.74" -> "G.57";
     "G.66" -> "G.58";
     "G.67" -> "G.58";
     "G.71" -> "G.58";
     "G.73" -> "G.58";
     "G.75" -> "G.58";
     "G.79" -> "G.58";
     "G.87" -> "G.58";
     "G.65" -> "G.60";
     "G.74" -> "G.60";
     "G.62" -> "G.61";
     "G.66" -> "G.61";
     "G.67" -> "G.61";
     "G.70" -> "G.61";
     "G.72" -> "G.61";
     "G.73" -> "G.61";
     "G.86" -> "G.61";
     "G.96" -> "G.61";
     "G.64" -> "G.62";
     "G.65" -> "G.62";
     "G.66" -> "G.62";
     "G.67" -> "G.62";
     "G.70" -> "G.62";
     "G.72" -> "G.62";
     "G.74" -> "G.62";
     "G.75" -> "G.62";
     "G.64" -> "G.63";
     "G.75" -> "G.63";
     "G.79" -> "G.63";
     "G.87" -> "G.63";
     "G.97" -> "G.63";
     "G.65" -> "G.64";
     "G.66" -> "G.64";
     "G.67" -> "G.65";
     "G.87" -> "G.65";
     "G.70" -> "G.66";
     "G.71" -> "G.67";
     "G.71" -> "G.70";
     "G.79" -> "G.70";
     "G.73" -> "G.71";
     "G.74" -> "G.71";
     "G.73" -> "G.72";
     "G.87" -> "G.72";
     "G.74" -> "G.73";
     "G.97" -> "G.74";
     "G.79" -> "G.75";
     "G.87" -> "G.75";
     "G.97" -> "G.75";
     "G.78" -> "G.76";
     "G.78" -> "G.77";
     "G.79" -> "G.78";
     "G.97" -> "G.79";
     "G.87" -> "G.81";
     "G.97" -> "G.81";
     "G.87" -> "G.86";
     "G.97" -> "G.87";
     "G.97" -> "G.96";
   }

Required for
------------

:ref:`G.434 <G.434>`, :ref:`G.451 <G.451>`

.. toctree::
   :hidden:

   code
   heath
