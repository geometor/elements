:order: 114
:number: 114
:canonical_id: G.114
:original_id: III.14
:title: G.114 circle equal segments
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, straight-line, equally-distant-from-centre, line, centre, perpendicular, square, plane-angle, equality
:dependencies: G.4, G.10, G.79, G.98, G.100, G.113
:excerpt: In a circle equal segments are equally distant from the center, and those which are equally distant from the center are equal.

.. _G.114:
.. _III.14:

G.114 circle equal segments
===========================

.. rubric:: `III.14 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/14/>`_

.. enunciation::

   In a :term:`circle <G.10>` equal :term:`segments <G.4>` are :term:`equally distant <G.113>` from the :term:`center <G.14>`, and those which are equally distant from the center are equal.

.. signature:: theorem

   | :fn:`circle_equal_segments <G.114>`\ (:g:`( A B D C ) <g1:( A B D C )>`, :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`)
   | **given** :g:`( A B D C ) <g1:( A B D C )>` be a circle, let :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` be :eq:`equal <g1:/ A B / = g1:/ C D />` segments in it
   | **prove** :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are equally distant from the center; :g:`/ A B / <g1:/ A B />` is also :eq:`equal <g1:/ A B / = g1:/ C D />` to :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Proposition 14 diagram

.. step:: given

   :g:`( A B D C ) <g1:( A B D C )>` be a circle, let :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` be :eq:`equal <g1:/ A B / = g1:/ C D />` segments in it

.. step:: construct

   :fn:`find_circle_center <G.98>`: Let the center of :g:`( A B D C ) <g1:( A B D C )>` be taken

.. step:: assert

   Let it be :g:`E <g1:E>`

.. step:: construct

   From :g:`E <g1:E>` let :g:`/ E F / <g1:/ E F />`, :g:`/ E G / <g1:/ E G />` be drawn :term:`perpendicular <G.32>` to :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, and let :g:`/ A E / <g1:/ A E />`, :g:`/ E C / <g1:/ E C />` be joined.

.. step:: assert ∵ circle_segment_center <G.100>

   Since a segment :g:`/ E F / <g1:/ E F />` through the center cuts a segment :g:`/ A B / <g1:/ A B />` not through the center at right angles, it also :eq:`bisects <g1:/ A F / = g1:/ F B />` it.

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`; therefore :g:`/ A B / <g1:/ A B />` is :eq:`double <g1:/ A F / = g1:/ F B />` of :g:`/ A F / <g1:/ A F />`.

.. step:: assert

   The same reason

.. step:: assert

   :g:`/ C D / <g1:/ C D />` is also :eq:`double <g1:/ C G / = g1:/ G D />` of :g:`/ C G / <g1:/ C G />`;

.. step:: assert

   And :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g1:/ C D />` to :g:`/ C D / <g1:/ C D />`

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` is also :eq:`equal <g1:/ A F / = g1:/ C G />` to :g:`/ C G / <g1:/ C G />`.

.. step:: assert

   And, since :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ E C />` to :g:`/ E C / <g1:/ E C />`,

.. step:: assert

   The :term:`square <G.63>` on :g:`/ A E / <g1:/ A E />` is also :eq:`equal <g1:/ A E / = g1:/ E C />` to the square on :g:`/ E C / <g1:/ E C />`.

.. step:: assert

   The squares on :g:`/ A F / <g1:/ A F />`, :g:`/ E F / <g1:/ E F />` are equal to the square on :g:`/ A E / <g1:/ A E />`, for the :term:`angle <G.22>` at :g:`< E F A ) <g1:< E F A )>` is right

.. step:: assert ∵ pythagorean_theorem <G.79>

   And the squares on :g:`/ E G / <g1:/ E G />`, :g:`/ G C / <g1:/ G C />` are equal to the square on :g:`/ E C / <g1:/ E C />`, for the angle at :g:`< E G C ) <g1:< E G C )>` is right

.. step:: assert

   Therefore the squares on :g:`/ A F / <g1:/ A F />`, :g:`/ F E / <g1:/ F E />` are equal to the squares on :g:`/ C G / <g1:/ C G />`, :g:`/ G E / <g1:/ G E />`,

.. step:: assert

   Of which the square on :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ C G />` to the square on :g:`/ C G / <g1:/ C G />`, for :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ C G />` to :g:`/ C G / <g1:/ C G />`

.. step:: assert

   Therefore the square on :g:`/ F E / <g1:/ F E />` which remains is :eq:`equal <g1:/ F E / = g1:/ E G />` to the square on :g:`/ E G / <g1:/ E G />`,

.. step:: assert

   Therefore :g:`/ E F / <g1:/ E F />` is :eq:`equal <g1:/ E F / = g1:/ E G />` to :g:`/ E G / <g1:/ E G />`.

.. step:: assert ∵ circle_segments_said_def <G.113>

   In a :term:`circle segments <G.126>` are said to be equally distant from the center when the perpendiculars drawn to them from the center are equal

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are equally distant from the center.

.. step:: assert

   Next, let :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` be equally distant from the center

.. step:: assert

   That is, let :g:`/ E F / <g1:/ E F />` be :eq:`equal <g1:/ E F / = g1:/ E G />` to :g:`/ E G / <g1:/ E G />`.

.. step:: assert

   With the same construction, we can prove, similarly, that :g:`/ A B / <g1:/ A B />` is :eq:`double <g1:/ A F / = g1:/ F B /; g1:/ C G / = g1:/ G D />` of :g:`/ A F / <g1:/ A F />`, and :g:`/ C D / <g1:/ C D />` of :g:`/ C G / <g1:/ C G />`.

.. step:: assert

   And, since :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ C E />` to :g:`/ C E / <g1:/ C E />`,

.. step:: assert

   The square on :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ C E />` to the square on :g:`/ C E / <g1:/ C E />`.

.. step:: assert ∵ pythagorean_theorem <G.79>

   The squares on :g:`/ E F / <g1:/ E F />`, :g:`/ F A / <g1:/ F A />` are equal to the square on :g:`/ A E / <g1:/ A E />`, and the squares on :g:`/ E G / <g1:/ E G />`, :g:`/ G C / <g1:/ G C />` equal to the square on :g:`/ C E / <g1:/ C E />`

.. step:: assert

   Therefore the squares on :g:`/ E F / <g1:/ E F />`, :g:`/ F A / <g1:/ F A />` are equal to the squares on :g:`/ E G / <g1:/ E G />`, :g:`/ G C / <g1:/ G C />`, of which the square on :g:`/ E F / <g1:/ E F />` is :eq:`equal <g1:/ E F / = g1:/ E G />` to the square on :g:`/ E G / <g1:/ E G />`, for :g:`/ E F / <g1:/ E F />` is :eq:`equal <g1:/ E F / = g1:/ E G />` to :g:`/ E G / <g1:/ E G />`

.. step:: assert

   Therefore the square on :g:`/ A F / <g1:/ A F />` which remains is :eq:`equal <g1:/ A F / = g1:/ C G />` to the square on :g:`/ C G / <g1:/ C G />`

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ C G />` to :g:`/ C G / <g1:/ C G />`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is :eq:`double <g1:/ A F / = g1:/ F B />` of :g:`/ A F / <g1:/ A F />`, and :g:`/ C D / <g1:/ C D />` :eq:`double <g1:/ C G / = g1:/ G D />` of :g:`/ C G / <g1:/ C G />`

.. step:: conclude

   Therefore :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g1:/ C D />` to :g:`/ C D / <g1:/ C D />`.

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
     "G.38" [label="G.38", tooltip="G.38 (I.14): If two segments at a point on a line on opposite sides make adjacent angles summing to two right angles, the two segments are collinear.", fillcolor="#222244", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.40/index.html", target="_top"];
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
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.64" [label="G.64", tooltip="G.64 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.64/index.html", target="_top"];
     "G.66" [label="G.66", tooltip="G.66 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.66/index.html", target="_top"];
     "G.70" [label="G.70", tooltip="G.70 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.70/index.html", target="_top"];
     "G.75" [label="G.75", tooltip="G.75 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.75/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (I.def.11): An obtuse angle is greater than a right angle.", fillcolor="#224422", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (I.def.21): A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.", fillcolor="#224422", URL="../G.78/index.html", target="_top"];
     "G.79" [label="G.79", tooltip="G.79 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.79/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.100" [label="G.100", tooltip="G.100 (III.3): If in a circle a segment through the center bisect a segment not through the center, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.", fillcolor="#222244", URL="../G.100/index.html", target="_top"];
     "G.113" [label="G.113", tooltip="G.113 (III.def.4): In acirclesegments are said to beequally distant from the center when theperpendiculars drawn to them from thecenter are equal.", fillcolor="#224422", URL="../G.113/index.html", target="_top"];
     "G.114" [label="G.114", tooltip="G.114 (III.14): In a circle equal segments are equally distant from the center, and those which are equally distant from the center are equal.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.38" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
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
     "G.38" -> "G.4";
     "G.39" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.58" -> "G.4";
     "G.61" -> "G.4";
     "G.75" -> "G.4";
     "G.100" -> "G.4";
     "G.113" -> "G.4";
     "G.114" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.98" -> "G.10";
     "G.100" -> "G.10";
     "G.113" -> "G.10";
     "G.114" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.43" -> "G.11";
     "G.44" -> "G.11";
     "G.45" -> "G.11";
     "G.47" -> "G.11";
     "G.51" -> "G.11";
     "G.63" -> "G.11";
     "G.66" -> "G.11";
     "G.70" -> "G.11";
     "G.78" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.63" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.61" -> "G.14";
     "G.98" -> "G.14";
     "G.100" -> "G.14";
     "G.113" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.36" -> "G.16";
     "G.38" -> "G.16";
     "G.39" -> "G.16";
     "G.56" -> "G.16";
     "G.64" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.33" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.20" -> "G.19";
     "G.38" -> "G.19";
     "G.39" -> "G.19";
     "G.64" -> "G.19";
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
     "G.38" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.78" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.79" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.100" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.48" -> "G.28";
     "G.98" -> "G.28";
     "G.100" -> "G.28";
     "G.30" -> "G.29";
     "G.48" -> "G.29";
     "G.31" -> "G.30";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.38" -> "G.32";
     "G.55" -> "G.32";
     "G.56" -> "G.32";
     "G.76" -> "G.32";
     "G.77" -> "G.32";
     "G.78" -> "G.32";
     "G.79" -> "G.32";
     "G.98" -> "G.32";
     "G.100" -> "G.32";
     "G.113" -> "G.32";
     "G.36" -> "G.33";
     "G.75" -> "G.33";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.62" -> "G.35";
     "G.64" -> "G.35";
     "G.79" -> "G.35";
     "G.38" -> "G.36";
     "G.39" -> "G.36";
     "G.56" -> "G.36";
     "G.38" -> "G.37";
     "G.39" -> "G.37";
     "G.79" -> "G.38";
     "G.41" -> "G.39";
     "G.56" -> "G.39";
     "G.41" -> "G.40";
     "G.45" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.62" -> "G.51";
     "G.100" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.64" -> "G.52";
     "G.66" -> "G.52";
     "G.70" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.75" -> "G.56";
     "G.66" -> "G.58";
     "G.75" -> "G.58";
     "G.62" -> "G.61";
     "G.64" -> "G.62";
     "G.66" -> "G.62";
     "G.70" -> "G.62";
     "G.75" -> "G.62";
     "G.64" -> "G.63";
     "G.75" -> "G.63";
     "G.79" -> "G.63";
     "G.66" -> "G.64";
     "G.70" -> "G.66";
     "G.79" -> "G.70";
     "G.79" -> "G.75";
     "G.78" -> "G.76";
     "G.78" -> "G.77";
     "G.79" -> "G.78";
     "G.114" -> "G.79";
     "G.114" -> "G.98";
     "G.114" -> "G.100";
     "G.114" -> "G.113";
   }

Required for
------------

:ref:`G.116 <G.116>`

.. toctree::
   :hidden:

   code
   heath
