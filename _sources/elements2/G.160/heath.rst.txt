:canonical_id: G.160
:original_id: IV.8
:title: G.160 square inscribe circle
:volume: II
:book: IV
:type: prop

G.160 square inscribe circle — Heath
====================================

.. rubric:: `IV.8 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/08/>`_

.. enunciation::

   In a given :term:`square <G.63>` to inscribe a :term:`circle <G.10>`.

Let :g:`< A B C D > <g1:< A B C D >>` be the given square;
thus it is required to :term:`inscribe a circle in <G.153>` the given square
:g:`< A B C D > <g1:< A B C D >>`.

Let the :term:`straight lines <G.4>` :g:`/ A D / <g1:/ A D />`, :g:`/ A B / <g1:/ A B />` be
bisected at the :term:`points <G.1>` :g:`E <g1:E>`, :g:`F <g1:F>` respectively
:just:`[G.31] <G.31>`,
through :g:`E <g1:E>` let :g:`/ E H / <g1:/ E H />` be drawn :term:`parallel <G.52>`
to either :g:`/ A B / <g1:/ A B />` or :g:`/ C D / <g1:/ C D />`, and through
:g:`F <g1:F>` let :g:`/ F K / <g1:/ F K />` be drawn parallel to either
:g:`/ A D / <g1:/ A D />` or :g:`/ B C / <g1:/ B C />`; :just:`[G.58] <G.58>`
therefore each of the :term:`figures <G.9>` :g:`< A F K D > <g1:< A F K D >>`, :g:`< F B C K > <g1:< F B C K >>`,
:g:`< A B H E > <g1:< A B H E >>`, :g:`< E H C D > <g1:< E H C D >>`, :g:`< A F G E > <g1:< A F G E >>`, :g:`< G H C K > <g1:< G H C K >>`, :g:`< F B H G > <g1:< F B H G >>`, :g:`< E G K D > <g1:< E G K D >>` is a parallelogram,
and their opposite sides are evidently equal. :just:`[G.62] <G.62>`

.. picture:: g1.svg
   :alt: Proposition IV. 8 Diagram

Now, since :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />`,
and :g:`/ A E / <g1:/ A E />` is half of :g:`/ A D / <g1:/ A D />`, and :g:`/ A F / <g1:/ A F />` half of :g:`/ A B / <g1:/ A B />`,

.. assertion::

   therefore :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ A F />` to :g:`/ A F / <g1:/ A F />`,

so that the opposite sides are also equal;

.. assertion::

   therefore :g:`/ F G / <g1:/ F G />` is :eq:`equal <g1:/ F G / = g1:/ G E />` to :g:`/ G E / <g1:/ G E />`.

Similarly we can prove that each of the straight lines :g:`/ G H / <g1:/ G H />`,
:g:`/ G K / <g1:/ G K />` is :eq:`equal <g1:/ G H / = g1:/ G K / = g1:/ F G / = g1:/ G E />` to each of the straight lines :g:`/ F G / <g1:/ F G />`, :g:`/ G E / <g1:/ G E />`;

.. assertion::

   therefore the four straight lines :g:`/ G E / <g1:/ G E />`, :g:`/ G F / <g1:/ G F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ G K / <g1:/ G K />` are :eq:`equal <g1:/ G E / = g1:/ G F / = g1:/ G H / = g1:/ G K />` to one another.

Therefore the circle described with :term:`centre <G.14>` :g:`G <g1:G>` and distance
one of the straight lines :g:`/ G E / <g1:/ G E />`, :g:`/ G F / <g1:/ G F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ G K / <g1:/ G K />` will pass also
through the remaining points.

And it will touch the straight lines :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D A / <g1:/ D A />`,
because the :term:`angles <G.22>` at :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`H <g1:H>`, :g:`K <g1:K>` are right.

For, if the circle cuts :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D A / <g1:/ D A />`, the straight
:term:`line <G.2>` drawn :term:`at right angles <G.32>` to the :term:`diameter <G.61>` of the circle from
its :term:`extremity <G.6>` will fall within the circle: which was proved
absurd; :just:`[G.118] <G.118>`
therefore the circle described with centre :g:`G <g1:G>` and distance
one of the straight lines :g:`/ G E / <g1:/ G E />`, :g:`/ G F / <g1:/ G F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ G K / <g1:/ G K />` will not cut
the straight lines :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D A / <g1:/ D A />`.

Therefore it will touch them, and will have been inscribed
in the square :g:`< A B C D > <g1:< A B C D >>`.

Therefore in the given square a circle has been inscribed.

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
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.def.2): Asegment is said totouch a circle which, meeting thecircle and being produced, does not cut the circle.", fillcolor="#224422", URL="../G.111/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.117/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (III.16): The segment drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the segment and the arc another segment ca...", fillcolor="#222244", URL="../G.118/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (IV.def.1): Apolygon is said to beinscribed in a polygon when the respectiveangles of the inscribedfigure lie on the respective sides of that in which it is inscribed.", fillcolor="#224422", URL="../G.152/index.html", target="_top"];
     "G.153" [label="G.153", tooltip="G.153 (IV.def.5): Similarly acircle is said to beinscribed in a figure when the arc of the circle touches each side of thefigure in which it is inscribed.", fillcolor="#224422", URL="../G.153/index.html", target="_top"];
     "G.160" [label="G.160", tooltip="G.160 (IV.8): In a given square to inscribe a circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.152" -> "G.9";
     "G.153" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.153" -> "G.10";
     "G.160" -> "G.10";
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
     "G.63" -> "G.11";
     "G.152" -> "G.11";
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
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.77" -> "G.22";
     "G.118" -> "G.22";
     "G.152" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.62" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.118" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.48" -> "G.28";
     "G.30" -> "G.29";
     "G.48" -> "G.29";
     "G.118" -> "G.29";
     "G.31" -> "G.30";
     "G.41" -> "G.31";
     "G.160" -> "G.31";
     "G.33" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.42" -> "G.32";
     "G.55" -> "G.32";
     "G.56" -> "G.32";
     "G.77" -> "G.32";
     "G.118" -> "G.32";
     "G.36" -> "G.33";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.62" -> "G.35";
     "G.39" -> "G.36";
     "G.42" -> "G.36";
     "G.56" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.56" -> "G.39";
     "G.41" -> "G.40";
     "G.45" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.118" -> "G.42";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.118" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.62" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.62" -> "G.56";
     "G.160" -> "G.58";
     "G.62" -> "G.61";
     "G.118" -> "G.61";
     "G.160" -> "G.62";
     "G.160" -> "G.63";
     "G.118" -> "G.77";
     "G.118" -> "G.111";
     "G.118" -> "G.117";
     "G.160" -> "G.118";
     "G.160" -> "G.152";
     "G.160" -> "G.153";
   }
