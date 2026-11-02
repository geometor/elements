:order: 594
:number: 594
:canonical_id: G.594
:original_id: XIII.14
:title: G.594 construct an octahedron and comprehend it in a
:volume: III
:book: XIII
:type: prop
:subtype: problem
:categories: problem, construction, solid-geometry, regular-solids
:category: problem, construction, solid-geometry, regular-solids
:tags: book-xiii, point, segment, circle, angle, triangle, quadrilateral, octahedron, sphere, square, diameter-of-sphere, diameter, semicircle, right-angle, straight-line, right-angles-to-plane, plane-surface, plane-angle, trilateral, axis-of-sphere, equality
:dependencies: G.24, G.63, G.79, G.139, G.514, G.575, G.576, G.591, G.593
:excerpt: Construct an octahedron and comprehend it in a sphere, as in the preceding case; and to prove that the square on the diameter of the sphere is double of the square on the side of the octahedron.

.. _G.594:
.. _XIII.14:

G.594 construct an octahedron and comprehend it in a
====================================================

.. rubric:: `XIII.14 <https://geometor.github.io/euclid/heath/volume_III/book_xiii/propositions/14/>`_

.. enunciation::

   Construct an :term:`octahedron <G.593>` and comprehend it in a :term:`sphere <G.575>`, as in the preceding case; and to prove that the :term:`square <G.63>` on the :term:`diameter of the sphere <G.576>` is double of the square on the side of the octahedron.

.. signature:: problem

   | :fn:`construct_octahedron_comprehend <G.594>`\ (:g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>`)
   | **given** the diameter :g:`/ A B / <g1:/ A B />` of the given sphere be set out, let it be :eq:`bisected <g1:/ A C / = g1:/ C B />` at :g:`C <g1:C>`
   | **construct** the octahedron has been comprehended in the given sphere, and it has been demonstrated at the same time that the square on the diameter of the sphere is double of the square on the side of the octahedron

.. picture:: g1.svg
   :alt: Proposition 14 Diagram

.. step:: given

   the :term:`diameter <G.61>` :g:`/ A B / <g1:/ A B />` of the given sphere be set out, let it be :eq:`bisected <g1:/ A C / = g1:/ C B />` at :g:`C <g1:C>`

.. step:: construct

   Let the :term:`semicircle <G.96>` :g:`( A D B ) <g1:( A D B )>` be described on :g:`/ A B / <g1:/ A B />`

.. step:: construct

   :fn:`perpendicular_at <G.33>`\ (:g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>`) → :g:`/ C D / <g1:/ C D />`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`

.. step:: construct

   :fn:`segment <G.13>`\ () → :g:`< E F G H > <g1:< E F G H >>`, :fn:`segment <G.13>`\ (:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`, :fn:`segment <G.13>`\ (:g:`H <g1:H>`, :g:`F <g1:F>`) → :g:`/ H F / <g1:/ H F />`, :fn:`segment <G.13>`\ (:g:`E <g1:E>`, :g:`G <g1:G>`) → :g:`/ E G / <g1:/ E G />`

.. step:: construct

   :fn:`set_segment_right <G.514>`: From :g:`K <g1:K>` let :g:`/ K L / <g1:/ K L />` be set up at right angles to the plane of the square :g:`< E F G H > <g1:< E F G H >>`, and let it be carried through to the other side of the plane, as :g:`/ K M / <g1:/ K M />`

.. step:: construct

   From :g:`/ K L / <g1:/ K L />`, :g:`/ K M / <g1:/ K M />` let :g:`/ K L / <g1:/ K L />`, :g:`/ K M / <g1:/ K M />` be respectively cut off :eq:`equal <g1:/ K L / = g1:/ K M / = g1:/ E K / = g1:/ F K / = g1:/ G K / = g1:/ H K />` to one of :g:`/ E K / <g1:/ E K />`, :g:`/ F K / <g1:/ F K />`, :g:`/ G K / <g1:/ G K />`, :g:`/ H K / <g1:/ H K />`, and let :g:`/ L E / <g1:/ L E />`, :g:`/ L F / <g1:/ L F />`, :g:`/ L G / <g1:/ L G />`, :g:`/ L H / <g1:/ L H />`, :g:`/ M E / <g1:/ M E />`, :g:`/ M F / <g1:/ M F />`, :g:`/ M G / <g1:/ M G />`, :g:`/ M H / <g1:/ M H />` be joined.

.. step:: assert ∵ pythagorean_theorem <G.79>

   Since :g:`/ K E / <g1:/ K E />` is :eq:`equal <g1:/ K E / = g1:/ K H />` to :g:`/ K H / <g1:/ K H />`, and :g:`< E K H ) <g1:< E K H )>` is right, therefore the square on :g:`/ H E / <g1:/ H E />` is double of the square on :g:`/ E K / <g1:/ E K />`.

.. step:: assert ∵ pythagorean_theorem <G.79>

   Since :g:`/ L K / <g1:/ L K />` is :eq:`equal <g1:/ L K / = g1:/ K E />` to :g:`/ K E / <g1:/ K E />`, and :g:`< L K E ) <g1:< L K E )>` is right, therefore the square on :g:`/ E L / <g1:/ E L />` is double of the square on :g:`/ E K / <g1:/ E K />`

.. step:: assert

   The square on :g:`/ H E / <g1:/ H E />` was also proved double of the square on :g:`/ E K / <g1:/ E K />`

.. step:: assert

   Therefore the square on :g:`/ L E / <g1:/ L E />` is :eq:`equal <g1:/ L E / = g1:/ E H />` to the square on :g:`/ E H / <g1:/ E H />`

.. step:: assert

   Therefore :g:`/ L E / <g1:/ L E />` is :eq:`equal <g1:/ L E / = g1:/ E H />` to :g:`/ E H / <g1:/ E H />`.

.. step:: assert

   The same reason :g:`/ L H / <g1:/ L H />` is also :eq:`equal <g1:/ L H / = g1:/ H E />` to :g:`/ H E / <g1:/ H E />`

.. step:: assert

   Therefore :g:`< L E H > <g1:< L E H >>` is :eq:`equilateral <g1:/ L E / = g1:/ E H / = g1:/ H L />`.

.. step:: assert

   Similarly we can prove that each of the remaining :term:`triangles <G.11>` of which the sides of the square :g:`< E F G H > <g1:< E F G H >>` are the bases, and :g:`L <g1:L>`, :g:`M <g1:M>` the vertices, is :eq:`equilateral <g1:/ E F / = g1:/ F G / = g1:/ G H / = g1:/ H E / = g1:/ L E / = g1:/ L F / = g1:/ L G / = g1:/ L H / = g1:/ M E / = g1:/ M F / = g1:/ M G / = g1:/ M H />`

.. step:: assert

   Therefore an octahedron has been constructed which is contained by eight :eq:`equilateral <g1:/ E F / = g1:/ F G / = g1:/ G H / = g1:/ H E / = g1:/ L E / = g1:/ L F / = g1:/ L G / = g1:/ L H / = g1:/ M E / = g1:/ M F / = g1:/ M G / = g1:/ M H />` triangles.

.. step:: assert

   It is next required to comprehend it in the given sphere, and to prove that the square on the diameter of the sphere is double of the square on the side of the octahedron.

.. step:: assert

   Since :g:`/ L K / <g1:/ L K />`, :g:`/ K M / <g1:/ K M />`, :g:`/ K E / <g1:/ K E />` are :eq:`equal <g1:/ L K / = g1:/ K M / = g1:/ K E />` to one another, therefore the semicircle described on :g:`/ L M / <g1:/ L M />` will also pass through :g:`E <g1:E>`.

.. step:: assert

   For the same reason, if, :g:`/ L M / <g1:/ L M />` remaining fixed, the :term:`semicircle be carried round <G.591>` and restored to the same position from which it began to be moved, it will also pass through :g:`F <g1:F>`, :g:`G <g1:G>`, :g:`H <g1:H>`, and the octahedron will have been comprehended in a sphere.

.. step:: assert

   I say next that it is also comprehended in the given sphere.

.. step:: assert ∵ sas_congruence <G.24>

   Since :g:`/ L K / <g1:/ L K />` is :eq:`equal <g1:/ L K / = g1:/ K M />` to :g:`/ K M / <g1:/ K M />`, while :g:`/ K E / <g1:/ K E />` is common, and they contain :term:`right angles <G.32>`, therefore the base :g:`/ L E / <g1:/ L E />` is :eq:`equal <g1:/ L E / = g1:/ E M />` to the base :g:`/ E M / <g1:/ E M />`.

.. step:: assert ∵ thales_semicircle_theorem, pythagorean_theorem <G.139, G.79>

   And, since :g:`< L E M ) <g1:< L E M )>` is right, for it is in a semicircle, therefore the square on :g:`/ L M / <g1:/ L M />` is double of the square on :g:`/ L E / <g1:/ L E />`.

.. step:: assert

   Since :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ C B />` to :g:`/ C B / <g1:/ C B />`, :g:`/ A B / <g1:/ A B />` is double of :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   But, as :g:`/ A B / <g1:/ A B />` is to :g:`/ B C / <g1:/ B C />`, so is the square on :g:`/ A B / <g1:/ A B />` to the square on :g:`/ B D / <g1:/ B D />`

.. step:: assert

   Therefore the square on :g:`/ A B / <g1:/ A B />` is double of the square on :g:`/ B D / <g1:/ B D />`.

.. step:: assert

   The square on :g:`/ L M / <g1:/ L M />` was also proved double of the square on :g:`/ L E / <g1:/ L E />`.

.. step:: assert

   The square on :g:`/ D B / <g1:/ D B />` is :eq:`equal <g1:/ D B / = g1:/ L E />` to the square on :g:`/ L E / <g1:/ L E />`, for :g:`/ E H / <g1:/ E H />` was made :eq:`equal <g1:/ E H / = g1:/ D B />` to :g:`/ D B / <g1:/ D B />`.

.. step:: assert

   Therefore the square on :g:`/ A B / <g1:/ A B />` is also :eq:`equal <g1:/ A B / = g1:/ L M />` to the square on :g:`/ L M / <g1:/ L M />`

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g1:/ L M />` to :g:`/ L M / <g1:/ L M />`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is the diameter of the given sphere

.. step:: assert

   Therefore :g:`/ L M / <g1:/ L M />` is :eq:`equal <g1:/ L M / = g1:/ A B />` to the diameter of the given sphere.

.. step:: conclude

   Therefore the octahedron has been comprehended in the given sphere, and it has been demonstrated at the same time that the square on the diameter of the sphere is double of the square on the side of the octahedron.

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
     "G.34" [label="G.34", tooltip="G.34 (I.12): Construct a perpendicular to a given line from a given point not on it.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.14): If two segments at a point on a line on opposite sides make adjacent angles summing to two right angles, the two segments are collinear.", fillcolor="#222244", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.40/index.html", target="_top"];
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
     "G.96" [label="G.96", tooltip="G.96 (I.def.18): A semicircle is the figure contained by a diameter and the arc cut off by it.", fillcolor="#224422", URL="../G.96/index.html", target="_top"];
     "G.122" [label="G.122", tooltip="G.122 (III.def.10): Asector of a circle is thefigure which, when anangle is constructed at thecenter of thecircle, is contained by thesegments containing the angle and the arc cut off by them.", fillcolor="#224422", URL="../G.122/index.html", target="_top"];
     "G.123" [label="G.123", tooltip="G.123 (III.20): In a circle the angle at the center is double of the angle at the arc, when the angles have the same arc as base.", fillcolor="#222244", URL="../G.123/index.html", target="_top"];
     "G.124" [label="G.124", tooltip="G.124 (III.21): In a circle the angles in the same segment are equal.", fillcolor="#222244", URL="../G.124/index.html", target="_top"];
     "G.125" [label="G.125", tooltip="G.125 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.125/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (III.def.8): Anangle in a segment is theangle which, when apoint is taken on the arc of the segment andsegments are joined from it to theextremities of the segment which is thebase of the segme...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.502" [label="G.502", tooltip="G.502 (XI.1): A part of a segment cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.502/index.html", target="_top"];
     "G.503" [label="G.503", tooltip="G.503 (XI.2): If two segments cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.503/index.html", target="_top"];
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", fillcolor="#222244", URL="../G.504/index.html", target="_top"];
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.506" [label="G.506", tooltip="G.506 (XI.4): If a segment be set up at right angles to two segments which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.506/index.html", target="_top"];
     "G.509" [label="G.509", tooltip="G.509 (XI.7): If two segments be parallel and points be taken at random on each of them, the segment joining the points is in the same plane with the parallel lines.", fillcolor="#222244", URL="../G.509/index.html", target="_top"];
     "G.510" [label="G.510", tooltip="G.510 (XI.8): If two segments be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.510/index.html", target="_top"];
     "G.513" [label="G.513", tooltip="G.513 (XI.11): From a given elevated point to draw a segment perpendicular to a given plane.", fillcolor="#222244", URL="../G.513/index.html", target="_top"];
     "G.514" [label="G.514", tooltip="G.514 (XI.12): To set up a segment at right angles to a given plane from a given point in it.", fillcolor="#222244", URL="../G.514/index.html", target="_top"];
     "G.529" [label="G.529", tooltip="G.529 (XI.def.1): Asolid is that which has length, breadth, and depth.", fillcolor="#224422", URL="../G.529/index.html", target="_top"];
     "G.575" [label="G.575", tooltip="G.575 (XI.def.14): When, thediameter of asemicircle remaining fixed, the semicircle is carried round and restored again to the same position from which it began to be moved, thefigure so comprehended...", fillcolor="#224422", URL="../G.575/index.html", target="_top"];
     "G.576" [label="G.576", tooltip="G.576 (XI.def.17): Adiameter of the sphere is anysegment drawn through thecenter and terminated in both directions by thesurface of thesphere.", fillcolor="#224422", URL="../G.576/index.html", target="_top"];
     "G.591" [label="G.591", tooltip="G.591 (XI.def.15): Theaxis of the sphere is thesegment which remains fixed and about which thesemicircle is turned.", fillcolor="#224422", URL="../G.591/index.html", target="_top"];
     "G.593" [label="G.593", tooltip="G.593 (XI.def.26): Anoctahedron is asolid figure contained by eight equal andequilateral triangles.", fillcolor="#224422", URL="../G.593/index.html", target="_top"];
     "G.594" [label="G.594", tooltip="G.594 (XIII.14): Construct an octahedron and comprehend it in a sphere, as in the preceding case; and to prove that the square on the diameter of the sphere is double of the square on the side of t...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.34" -> "G.1";
     "G.38" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.138" -> "G.1";
     "G.506" -> "G.1";
     "G.509" -> "G.1";
     "G.513" -> "G.1";
     "G.514" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
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
     "G.34" -> "G.4";
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
     "G.122" -> "G.4";
     "G.138" -> "G.4";
     "G.502" -> "G.4";
     "G.503" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.506" -> "G.4";
     "G.509" -> "G.4";
     "G.510" -> "G.4";
     "G.513" -> "G.4";
     "G.514" -> "G.4";
     "G.576" -> "G.4";
     "G.591" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.576" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.502" -> "G.7";
     "G.503" -> "G.7";
     "G.504" -> "G.7";
     "G.505" -> "G.7";
     "G.509" -> "G.7";
     "G.510" -> "G.7";
     "G.513" -> "G.7";
     "G.514" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.96" -> "G.9";
     "G.122" -> "G.9";
     "G.575" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.96" -> "G.10";
     "G.122" -> "G.10";
     "G.123" -> "G.10";
     "G.124" -> "G.10";
     "G.125" -> "G.10";
     "G.139" -> "G.10";
     "G.502" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.42" -> "G.11";
     "G.43" -> "G.11";
     "G.44" -> "G.11";
     "G.45" -> "G.11";
     "G.47" -> "G.11";
     "G.51" -> "G.11";
     "G.59" -> "G.11";
     "G.63" -> "G.11";
     "G.66" -> "G.11";
     "G.70" -> "G.11";
     "G.78" -> "G.11";
     "G.125" -> "G.11";
     "G.503" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.63" -> "G.12";
     "G.593" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.34" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.61" -> "G.14";
     "G.96" -> "G.14";
     "G.122" -> "G.14";
     "G.502" -> "G.14";
     "G.576" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.34" -> "G.15";
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
     "G.42" -> "G.18";
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
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.59" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.78" -> "G.22";
     "G.122" -> "G.22";
     "G.123" -> "G.22";
     "G.124" -> "G.22";
     "G.125" -> "G.22";
     "G.138" -> "G.22";
     "G.139" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.79" -> "G.24";
     "G.506" -> "G.24";
     "G.594" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.123" -> "G.25";
     "G.139" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.34" -> "G.28";
     "G.48" -> "G.28";
     "G.506" -> "G.28";
     "G.30" -> "G.29";
     "G.48" -> "G.29";
     "G.31" -> "G.30";
     "G.34" -> "G.31";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.34" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.38" -> "G.32";
     "G.42" -> "G.32";
     "G.55" -> "G.32";
     "G.56" -> "G.32";
     "G.59" -> "G.32";
     "G.76" -> "G.32";
     "G.77" -> "G.32";
     "G.78" -> "G.32";
     "G.79" -> "G.32";
     "G.125" -> "G.32";
     "G.139" -> "G.32";
     "G.505" -> "G.32";
     "G.506" -> "G.32";
     "G.510" -> "G.32";
     "G.513" -> "G.32";
     "G.514" -> "G.32";
     "G.36" -> "G.33";
     "G.75" -> "G.33";
     "G.513" -> "G.33";
     "G.513" -> "G.34";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.62" -> "G.35";
     "G.64" -> "G.35";
     "G.79" -> "G.35";
     "G.38" -> "G.36";
     "G.39" -> "G.36";
     "G.42" -> "G.36";
     "G.56" -> "G.36";
     "G.59" -> "G.36";
     "G.38" -> "G.37";
     "G.39" -> "G.37";
     "G.79" -> "G.38";
     "G.41" -> "G.39";
     "G.56" -> "G.39";
     "G.506" -> "G.39";
     "G.41" -> "G.40";
     "G.45" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.139" -> "G.42";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.62" -> "G.51";
     "G.506" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.64" -> "G.52";
     "G.66" -> "G.52";
     "G.70" -> "G.52";
     "G.509" -> "G.52";
     "G.510" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.59" -> "G.56";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.75" -> "G.56";
     "G.510" -> "G.56";
     "G.59" -> "G.58";
     "G.66" -> "G.58";
     "G.75" -> "G.58";
     "G.513" -> "G.58";
     "G.514" -> "G.58";
     "G.123" -> "G.59";
     "G.125" -> "G.59";
     "G.139" -> "G.59";
     "G.62" -> "G.61";
     "G.96" -> "G.61";
     "G.139" -> "G.61";
     "G.502" -> "G.61";
     "G.575" -> "G.61";
     "G.64" -> "G.62";
     "G.66" -> "G.62";
     "G.70" -> "G.62";
     "G.75" -> "G.62";
     "G.64" -> "G.63";
     "G.75" -> "G.63";
     "G.79" -> "G.63";
     "G.594" -> "G.63";
     "G.66" -> "G.64";
     "G.70" -> "G.66";
     "G.79" -> "G.70";
     "G.79" -> "G.75";
     "G.78" -> "G.76";
     "G.78" -> "G.77";
     "G.79" -> "G.78";
     "G.594" -> "G.79";
     "G.139" -> "G.96";
     "G.575" -> "G.96";
     "G.591" -> "G.96";
     "G.123" -> "G.122";
     "G.124" -> "G.123";
     "G.125" -> "G.124";
     "G.139" -> "G.125";
     "G.139" -> "G.138";
     "G.594" -> "G.139";
     "G.253" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.502" -> "G.253";
     "G.503" -> "G.502";
     "G.510" -> "G.503";
     "G.509" -> "G.504";
     "G.506" -> "G.505";
     "G.510" -> "G.505";
     "G.513" -> "G.505";
     "G.510" -> "G.506";
     "G.513" -> "G.506";
     "G.510" -> "G.509";
     "G.513" -> "G.510";
     "G.514" -> "G.510";
     "G.514" -> "G.513";
     "G.594" -> "G.514";
     "G.593" -> "G.529";
     "G.576" -> "G.575";
     "G.594" -> "G.575";
     "G.594" -> "G.576";
     "G.594" -> "G.591";
     "G.594" -> "G.593";
   }

Required for
------------

:ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
