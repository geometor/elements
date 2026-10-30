:order: 520
:number: 520
:canonical_id: G.520
:original_id: XIII.13
:volume: III
:book: XIII
:type: prop
:subtype: problem
:categories: problem, construction, solid-geometry, regular-solids
:category: problem, construction, solid-geometry, regular-solids
:tags: book-xiii, point, segment, circle, angle, triangle, convertendo, square, pyramid, sphere, equality
:dependencies: G.11, G.76, G.110, G.118, G.171, G.180, G.446, G.455, G.519
:excerpt: *To construct a pyramid, to comprehend it in a given sphere, and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid.*

.. _G.520:
.. _XIII.13:

G.520
=====

.. rubric:: `XIII.13 <https://geometor.github.io/euclid/heath/volume_III/book_xiii/propositions/13/>`_

.. enunciation::

   *To construct a pyramid, to comprehend it in a given sphere, and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid.*

.. signature:: problem

   | :fn:`construct_pyramid_comprehend <G.520>`\ () → :g:`/ B A / <g1:/ B A />`, :g:`/ A D / <g1:/ A D />`
   | **construct** :g:`/ B A / <g1:/ B A />` is the diameter of the given sphere, and :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ E F / = g1:/ F G / = g1:/ G E / = g1:/ K E / = g1:/ K F / = g1:/ K G />` to the side of the pyramid

.. picture:: g1.svg
   :alt: Proposition 13 Diagrams

.. step:: construct

   Let the diameter :g:`/ A B / <g1:/ A B />` of the given sphere be set out, and let it be cut at :g:`C <g1:C>` so that :g:`/ A C / <g1:/ A C />` is double of :g:`/ C B / <g1:/ C B />`

.. step:: construct

   Let the semicircle :g:`( A D B ) <g1:( A D B )>` be described on :g:`/ A B / <g1:/ A B />`

.. step:: construct

   :fn:`perpendicular_at <G.19>`\ (:g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>`) → :g:`/ C D / <g1:/ C D />`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`A <g1:A>`) → :g:`/ D A / <g1:/ D A />`

.. step:: construct

   :fn:`segment <G.3>`\ () → :g:`( E F G ) <g1:( E F G )>`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`C <g1:C>`) → :g:`/ D C / <g1:/ D C />`, :fn:`segment <G.3>`\ () → :g:`< E F G > <g1:< E F G >>`, :fn:`segment <G.3>`\ () → :g:`( E F G ) <g1:( E F G )>`, :fn:`segment <G.3>`\ () → :g:`H <g1:H>`, :fn:`segment <G.3>`\ (:g:`E <g1:E>`, :g:`H <g1:H>`) → :g:`/ E H / <g1:/ E H />`, :fn:`segment <G.3>`\ (:g:`H <g1:H>`, :g:`F <g1:F>`) → :g:`/ H F / <g1:/ H F />`, :fn:`segment <G.3>`\ (:g:`H <g1:H>`, :g:`G <g1:G>`) → :g:`/ H G / <g1:/ H G />`

.. step:: construct

   :fn:`set_straight_line <G.455>`: From :g:`H <g1:H>` let :g:`/ H K / <g1:/ H K />` be set up at right angles to the plane of :g:`( E F G ) <g1:( E F G )>`, let :g:`/ H K / <g1:/ H K />` :eq:`equal <g1:/ H K / = g1:/ A C />` to :g:`/ A C / <g1:/ A C />` be cut off from :g:`/ H K / <g1:/ H K />`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`K <g1:K>`, :g:`E <g1:E>`) → :g:`/ K E / <g1:/ K E />`, :fn:`segment <G.3>`\ (:g:`K <g1:K>`, :g:`F <g1:F>`) → :g:`/ K F / <g1:/ K F />`, :fn:`segment <G.3>`\ (:g:`K <g1:K>`, :g:`G <g1:G>`) → :g:`/ K G / <g1:/ K G />`

.. step:: assert

   Since :g:`/ K H / <g1:/ K H />` is at right angles to the plane of :g:`( E F G ) <g1:( E F G )>`,

.. step:: assert ∵ straight_line_right_def <G.446>

   Therefore it will also make right angles with all the straight lines which meet it and are in the plane of :g:`( E F G ) <g1:( E F G )>`.

.. step:: assert

   Each of :g:`/ H E / <g1:/ H E />`, :g:`/ H F / <g1:/ H F />`, :g:`/ H G / <g1:/ H G />` meets it:

.. step:: assert

   Therefore :g:`/ H K / <g1:/ H K />` is at right angles to each of :g:`/ H E / <g1:/ H E />`, :g:`/ H F / <g1:/ H F />`, :g:`/ H G / <g1:/ H G />`.

.. step:: assert

   And, since :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ H K /; g1:/ C D / = g1:/ H E />` to :g:`/ H K / <g1:/ H K />`, and :g:`/ C D / <g1:/ C D />` to :g:`/ H E / <g1:/ H E />`, and they contain :eq:`right angles <g1:< A C D ) = g1:< K H E )>`,

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ D A / <g1:/ D A />` is :eq:`equal <g1:/ D A / = g1:/ K E />` to the base :g:`/ K E / <g1:/ K E />`.

.. step:: assert

   For the same reason each of :g:`/ K F / <g1:/ K F />`, :g:`/ K G / <g1:/ K G />` is also :eq:`equal <g1:/ K F / = g1:/ K G / = g1:/ D A />` to :g:`/ D A / <g1:/ D A />`; therefore :g:`/ K E / <g1:/ K E />`, :g:`/ K F / <g1:/ K F />`, :g:`/ K G / <g1:/ K G />` are :eq:`equal <g1:/ K E / = g1:/ K F / = g1:/ K G />` to one another.

.. step:: assert

   And, since :g:`/ A C / <g1:/ A C />` is double of :g:`/ C B / <g1:/ C B />`,

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is triple of :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   But, as :g:`/ A B / <g1:/ A B />` is to :g:`/ B C / <g1:/ B C />`, so is the square on :g:`/ A D / <g1:/ A D />` to the square on :g:`/ D C / <g1:/ D C />`, as will be proved afterwards.

.. step:: assert

   Therefore the square on :g:`/ A D / <g1:/ A D />` is triple of the square on :g:`/ D C / <g1:/ D C />`.

.. step:: assert ∵ equilateral_triangle_inscribed <G.519>

   The square on :g:`/ F E / <g1:/ F E />` is also triple of the square on :g:`/ E H / <g1:/ E H />`, and :g:`/ D C / <g1:/ D C />` is :eq:`equal <g1:/ D C / = g1:/ E H />` to :g:`/ E H / <g1:/ E H />`.

.. step:: assert

   Therefore :g:`/ D A / <g1:/ D A />` is also :eq:`equal <g1:/ D A / = g1:/ E F />` to :g:`/ E F / <g1:/ E F />`.

.. step:: assert

   :g:`/ D A / <g1:/ D A />` was proved :eq:`equal <g1:/ D A / = g1:/ K E / = g1:/ K F / = g1:/ K G />` to each of :g:`/ K E / <g1:/ K E />`, :g:`/ K F / <g1:/ K F />`, :g:`/ K G / <g1:/ K G />`;

.. step:: assert

   Therefore each of :g:`/ E F / <g1:/ E F />`, :g:`/ F G / <g1:/ F G />`, :g:`/ G E / <g1:/ G E />` is also :eq:`equal <g1:/ E F / = g1:/ F G / = g1:/ G E / = g1:/ K E / = g1:/ K F / = g1:/ K G />` to each of :g:`/ K E / <g1:/ K E />`, :g:`/ K F / <g1:/ K F />`, :g:`/ K G / <g1:/ K G />`; therefore the four triangles :g:`< E F G > <g1:< E F G >>`, :g:`< K E F > <g1:< K E F >>`, :g:`< K F G > <g1:< K F G >>`, :g:`< K E G > <g1:< K E G >>` are :eq:`equilateral <g1:/ E F / = g1:/ F G / = g1:/ G E / = g1:/ K E / = g1:/ K F / = g1:/ K G />`.

.. step:: assert

   Therefore a pyramid has been constructed out of four :eq:`equilateral <g1:/ E F / = g1:/ F G / = g1:/ G E / = g1:/ K E / = g1:/ K F / = g1:/ K G />` triangles, :g:`< E F G > <g1:< E F G >>` being its base and :g:`K <g1:K>` its vertex.

.. step:: assert

   It is next required to comprehend it in the given sphere and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid.

.. step:: construct

   :fn:`extend <G.7>`\ (:g:`/ K H / <g1:/ K H />`) → :g:`/ H L / <g1:/ H L />`

.. step:: construct

   :fn:`cut_equal_segment <G.9>`\ (:g:`/ C B / <g1:/ C B />`) → :g:`/ H L / <g1:/ H L />` (:eq:`equal <g1:/ H L / = g1:/ C B />`)

.. step:: assert ∵ right_angled_triangle <G.171>

   Since, as :g:`/ A C / <g1:/ A C />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`/ C D / <g1:/ C D />` to :g:`/ C B / <g1:/ C B />`, while :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ K H /; g1:/ C D / = g1:/ H E /; g1:/ C B / = g1:/ H L />` to :g:`/ K H / <g1:/ K H />`, :g:`/ C D / <g1:/ C D />` to :g:`/ H E / <g1:/ H E />`, and :g:`/ C B / <g1:/ C B />` to :g:`/ H L / <g1:/ H L />`.

.. step:: assert ∵ straight_lines_proportional_vi_17 <G.180>

   Therefore, as :g:`/ K H / <g1:/ K H />` is to :g:`/ H E / <g1:/ H E />`, so is :g:`/ E H / <g1:/ E H />` to :g:`/ H L / <g1:/ H L />`; therefore the rectangle :g:`/ K H / <g1:/ K H />`, :g:`/ H L / <g1:/ H L />` is equal to the square on :g:`/ E H / <g1:/ E H />`.

.. step:: assert

   Each of :g:`< K H E ) <g1:< K H E )>`, :g:`< E H L ) <g1:< E H L )>` is :eq:`right <g1:< K H E ) = g1:< E H L )>`;

.. step:: assert ∵ right_angled_triangle, thales_semicircle_theorem <G.171, G.110>

   Therefore the semicircle described on :g:`/ K L / <g1:/ K L />` will pass through :g:`E <g1:E>` also.

.. step:: assert

   If then, :g:`/ K L / <g1:/ K L />` remaining fixed, the semicircle be carried round and restored to the same position from which it began to be moved, it will also pass through :g:`F <g1:F>`, :g:`G <g1:G>`, since, if :g:`/ F L / <g1:/ F L />`, :g:`/ L G / <g1:/ L G />` be joined, the angles at :g:`F <g1:F>`, :g:`G <g1:G>` similarly become right angles

.. step:: assert

   And the pyramid will be comprehended in the given sphere.

.. step:: assert

   For :g:`/ K L / <g1:/ K L />`, the diameter of the sphere, is :eq:`equal <g1:/ K L / = g1:/ A B />` to the diameter :g:`/ A B / <g1:/ A B />` of the given sphere, inasmuch as :g:`/ K H / <g1:/ K H />` was made :eq:`equal <g1:/ K H / = g1:/ A C /; g1:/ H L / = g1:/ C B />` to :g:`/ A C / <g1:/ A C />`, and :g:`/ H L / <g1:/ H L />` to :g:`/ C B / <g1:/ C B />`.

.. step:: assert

   I say next that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid.

.. step:: assert

   Since :g:`/ A C / <g1:/ A C />` is double of :g:`/ C B / <g1:/ C B />`,

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is triple of :g:`/ B C / <g1:/ B C />`; and, :term:`*convertendo* <convertendo>`, :g:`/ B A / <g1:/ B A />` is one and a half times :g:`/ A C / <g1:/ A C />`.

.. step:: assert

   But, as :g:`/ B A / <g1:/ B A />` is to :g:`/ A C / <g1:/ A C />`, so is the square on :g:`/ B A / <g1:/ B A />` to the square on :g:`/ A D / <g1:/ A D />`.

.. step:: assert

   Therefore the square on :g:`/ B A / <g1:/ B A />` is also one and a half times the square on :g:`/ A D / <g1:/ A D />`.

.. step:: conclude

   :g:`/ B A / <g1:/ B A />` is the diameter of the given sphere, and :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ E F / = g1:/ F G / = g1:/ G E / = g1:/ K E / = g1:/ K F / = g1:/ K G />` to the side of the pyramid.

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
     "G.20" [label="G.20", tooltip="G.20 (I.12): Construct a perpendicular to a given infinite line from a given point not on it.", fillcolor="#222244", URL="../G.20/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.24" [label="G.24", tooltip="G.24 (I.14): If two rays at a point on a line on opposite sides make adjacent angles summing to two right angles, the two rays are collinear.", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
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
     "G.45" [label="G.45", tooltip="G.45 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.38): Triangles on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.39): Equal triangles on the same base and on the same side lie in the same parallels.", fillcolor="#222244", URL="../G.52/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.85/index.html", target="_top"];
     "G.94" [label="G.94", tooltip="G.94 (III.16): The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumfere...", fillcolor="#222244", URL="../G.94/index.html", target="_top"];
     "G.96" [label="G.96", tooltip="G.96 (III.18): If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined is perpendicular to the tangent.", fillcolor="#222244", URL="../G.96/index.html", target="_top"];
     "G.97" [label="G.97", tooltip="G.97 (III.19): If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle is on the straight line so drawn.", fillcolor="#222244", URL="../G.97/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.20): In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.99" [label="G.99", tooltip="G.99 (III.21): In a circle the angles in the same segment are equal.", fillcolor="#222244", URL="../G.99/index.html", target="_top"];
     "G.100" [label="G.100", tooltip="G.100 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.100/index.html", target="_top"];
     "G.101" [label="G.101", tooltip="G.101 (III.def.11): Similar segments of circles are those which admit equal angles, or in which the angles are equal.", fillcolor="#224422", URL="../G.101/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.24): Similar segments of circles on equal straight lines are equal.", fillcolor="#222244", URL="../G.103/index.html", target="_top"];
     "G.105" [label="G.105", tooltip="G.105 (III.26): In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.105/index.html", target="_top"];
     "G.106" [label="G.106", tooltip="G.106 (III.27): In equal circles angles standing on equal circumferences are equal, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.106/index.html", target="_top"];
     "G.108" [label="G.108", tooltip="G.108 (III.29): In equal circles equal circumferences are subtended by equal straight lines.", fillcolor="#222244", URL="../G.108/index.html", target="_top"];
     "G.110" [label="G.110", tooltip="G.110 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.110/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.32): If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangen...", fillcolor="#222244", URL="../G.111/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (IV.2): Inscribe in a given circle a triangle equiangular with a given triangle.", fillcolor="#222244", URL="../G.118/index.html", target="_top"];
     "G.133" [label="G.133", tooltip="G.133 (IV.15): Inscribe in a given circle an equilateral and equiangular hexagon.", fillcolor="#222244", URL="../G.133/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.136" [label="G.136", tooltip="G.136 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.136/index.html", target="_top"];
     "G.137" [label="G.137", tooltip="G.137 (V.3): If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then alsoex aequali the magnitudes taken is...", fillcolor="#222244", URL="../G.137/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (V.4): If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples wh...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.146/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.150/index.html", target="_top"];
     "G.151" [label="G.151", tooltip="G.151 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.151/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.152/index.html", target="_top"];
     "G.153" [label="G.153", tooltip="G.153 (V.16): If four magnitudes be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.153/index.html", target="_top"];
     "G.157" [label="G.157", tooltip="G.157 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and ifex aequali the first be greater than the third, the fourth...", fillcolor="#222244", URL="../G.157/index.html", target="_top"];
     "G.159" [label="G.159", tooltip="G.159 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.159/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.164" [label="G.164", tooltip="G.164 (VI.2): If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionall...", fillcolor="#222244", URL="../G.164/index.html", target="_top"];
     "G.166" [label="G.166", tooltip="G.166 (VI.4): In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.", fillcolor="#222244", URL="../G.166/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (VI.def.1): Similar polygons are such as have their angles severally equal and the sides about the equal angles proportional.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.171" [label="G.171", tooltip="G.171 (VI.8): If in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another.", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.177" [label="G.177", tooltip="G.177 (VI.14): In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are...", fillcolor="#222244", URL="../G.177/index.html", target="_top"];
     "G.179" [label="G.179", tooltip="G.179 (VI.16): If four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes eq...", fillcolor="#222244", URL="../G.179/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (VI.17): If three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes equals the squa...", fillcolor="#222244", URL="../G.180/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.454" [label="G.454", tooltip="G.454 (XI.11): From a given elevated point to draw a straight line perpendicular to a given plane.", fillcolor="#222244", URL="../G.454/index.html", target="_top"];
     "G.455" [label="G.455", tooltip="G.455 (XI.12): To set up a straight line at right angles to a given plane from a given point in it.", fillcolor="#222244", URL="../G.455/index.html", target="_top"];
     "G.519" [label="G.519", tooltip="G.519 (XIII.12): *If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.*", fillcolor="#222244", URL="../G.519/index.html", target="_top"];
     "G.520" [label="G.520", tooltip="G.520 (XIII.13): *To construct a pyramid, to comprehend it in a given sphere, and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyrami...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.52" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.80" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.20" -> "G.4";
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
     "G.28" -> "G.7";
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
     "G.60" -> "G.11";
     "G.105" -> "G.11";
     "G.108" -> "G.11";
     "G.447" -> "G.11";
     "G.520" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.94" -> "G.12";
     "G.98" -> "G.12";
     "G.110" -> "G.12";
     "G.133" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.20" -> "G.15";
     "G.34" -> "G.15";
     "G.76" -> "G.15";
     "G.447" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.17";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.20" -> "G.18";
     "G.22" -> "G.18";
     "G.76" -> "G.18";
     "G.110" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.454" -> "G.19";
     "G.454" -> "G.20";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.60" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.60" -> "G.24";
     "G.177" -> "G.24";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.133" -> "G.25";
     "G.447" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.94" -> "G.28";
     "G.96" -> "G.28";
     "G.110" -> "G.28";
     "G.166" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.94" -> "G.30";
     "G.96" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.106" -> "G.34";
     "G.118" -> "G.34";
     "G.47" -> "G.37";
     "G.447" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.39";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.166" -> "G.40";
     "G.42" -> "G.41";
     "G.166" -> "G.41";
     "G.45" -> "G.42";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.451" -> "G.42";
     "G.45" -> "G.44";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.52" -> "G.44";
     "G.59" -> "G.44";
     "G.454" -> "G.44";
     "G.455" -> "G.44";
     "G.98" -> "G.45";
     "G.100" -> "G.45";
     "G.110" -> "G.45";
     "G.111" -> "G.45";
     "G.118" -> "G.45";
     "G.133" -> "G.45";
     "G.171" -> "G.45";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.166" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.51" -> "G.49";
     "G.52" -> "G.50";
     "G.54" -> "G.50";
     "G.163" -> "G.51";
     "G.164" -> "G.51";
     "G.164" -> "G.52";
     "G.60" -> "G.54";
     "G.163" -> "G.54";
     "G.60" -> "G.59";
     "G.519" -> "G.60";
     "G.85" -> "G.76";
     "G.520" -> "G.76";
     "G.85" -> "G.80";
     "G.103" -> "G.85";
     "G.118" -> "G.94";
     "G.97" -> "G.96";
     "G.111" -> "G.97";
     "G.99" -> "G.98";
     "G.106" -> "G.98";
     "G.100" -> "G.99";
     "G.110" -> "G.100";
     "G.111" -> "G.100";
     "G.105" -> "G.101";
     "G.105" -> "G.103";
     "G.106" -> "G.105";
     "G.133" -> "G.105";
     "G.108" -> "G.106";
     "G.133" -> "G.106";
     "G.133" -> "G.108";
     "G.111" -> "G.110";
     "G.519" -> "G.110";
     "G.520" -> "G.110";
     "G.118" -> "G.111";
     "G.520" -> "G.118";
     "G.519" -> "G.133";
     "G.145" -> "G.135";
     "G.149" -> "G.135";
     "G.137" -> "G.136";
     "G.139" -> "G.137";
     "G.139" -> "G.138";
     "G.142" -> "G.138";
     "G.149" -> "G.138";
     "G.150" -> "G.138";
     "G.153" -> "G.138";
     "G.159" -> "G.138";
     "G.163" -> "G.138";
     "G.159" -> "G.139";
     "G.147" -> "G.142";
     "G.152" -> "G.142";
     "G.164" -> "G.142";
     "G.177" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.146" -> "G.145";
     "G.147" -> "G.145";
     "G.151" -> "G.145";
     "G.157" -> "G.145";
     "G.164" -> "G.146";
     "G.177" -> "G.146";
     "G.151" -> "G.147";
     "G.157" -> "G.147";
     "G.153" -> "G.148";
     "G.163" -> "G.148";
     "G.164" -> "G.148";
     "G.177" -> "G.148";
     "G.152" -> "G.149";
     "G.151" -> "G.150";
     "G.157" -> "G.150";
     "G.153" -> "G.151";
     "G.153" -> "G.152";
     "G.163" -> "G.152";
     "G.166" -> "G.153";
     "G.159" -> "G.157";
     "G.166" -> "G.159";
     "G.164" -> "G.163";
     "G.177" -> "G.163";
     "G.166" -> "G.164";
     "G.171" -> "G.166";
     "G.171" -> "G.170";
     "G.520" -> "G.171";
     "G.179" -> "G.177";
     "G.180" -> "G.179";
     "G.520" -> "G.180";
     "G.444" -> "G.443";
     "G.451" -> "G.444";
     "G.450" -> "G.445";
     "G.447" -> "G.446";
     "G.451" -> "G.446";
     "G.454" -> "G.446";
     "G.520" -> "G.446";
     "G.451" -> "G.447";
     "G.454" -> "G.447";
     "G.451" -> "G.450";
     "G.454" -> "G.451";
     "G.455" -> "G.451";
     "G.455" -> "G.454";
     "G.520" -> "G.455";
     "G.520" -> "G.519";
   }

Required for
------------

:ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
