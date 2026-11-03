:canonical_id: G.159
:original_id: IV.7
:title: G.159 circumscribe about a given circle a square
:volume: II
:book: IV
:type: prop

G.159 circumscribe about a given circle a square — Heath
========================================================

.. rubric:: `IV.7 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/07/>`_

.. enunciation::

   About a given :term:`circle <G.10>` to circumscribe a :term:`square <G.63>`.

Let :g:`( A B C D ) <g1:( A B C D )>` be the given circle;
thus it is required to circumscribe a square about the circle
:g:`( A B C D ) <g1:( A B C D )>`.

Let two :term:`diameters <G.61>` :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` of the
circle :g:`( A B C D ) <g1:( A B C D )>` be drawn :term:`at right angles <G.33>`
to one another, and through the :term:`points <G.1>`
:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` let :g:`/ F G / <g1:/ F G />`, :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />`, :g:`/ K F / <g1:/ K F />` be
drawn :term:`touching the circle <G.111>` :g:`( A B C D ) <g1:( A B C D )>`.
:just:`[G.118] <G.118>`

.. picture:: g1.svg
   :alt: Proposition IV. 7 Diagram

Then, since :g:`/ F G / <g1:/ F G />` touches the circle
:g:`( A B C D ) <g1:( A B C D )>`,
and :g:`/ E A / <g1:/ E A />` has been joined from the :term:`centre <G.11>`
:g:`E <g1:E>` to the point of contact at :g:`A <g1:A>`,

.. assertion:: [G.120] <G.120>

   therefore the :term:`angles <G.22>` at :g:`A <g1:A>` are right.

For the same reason

.. assertion::

   the angles at the points :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` are also right.

Now, since the angle :g:`< A E B ) <g1:< A E B )>` is right,
and the angle :g:`< E B G ) <g1:< E B G )>` is also :eq:`right <g1:< A E B ) = g1:< E B G )>`,

.. assertion:: [G.54] <G.54>

   therefore :g:`/ G H / <g1:/ G H />` is :term:`parallel <G.52>` to :g:`/ A C / <g1:/ A C />`.

For the same reason

.. assertion::

   :g:`/ A C / <g1:/ A C />` is also parallel to :g:`/ F K / <g1:/ F K />`,

so that :g:`/ G H / <g1:/ G H />` is also parallel to :g:`/ F K / <g1:/ F K />`. :just:`[G.57] <G.57>`

Similarly we can prove that

.. assertion::

   each of the :term:`straight lines <G.4>` :g:`/ G F / <g1:/ G F />`, :g:`/ H K / <g1:/ H K />` is parallel to :g:`/ B E D / <g1:/ B E D />`.

Therefore :g:`< F G H K > <g1:< F G H K >>`, :g:`< G H C A > <g1:< G H C A >>`, :g:`< A C K F > <g1:< A C K F >>`, :g:`< F G B D > <g1:< F G B D >>`, :g:`< B H K D > <g1:< B H K D >>` are parallelograms;
therefore :g:`/ G F / <g1:/ G F />` is :eq:`equal <g1:/ G F / = g1:/ H K />` to :g:`/ H K / <g1:/ H K />`, and :g:`/ G H / <g1:/ G H />` :eq:`to <g1:/ G H / = g1:/ F K />` :g:`/ F K / <g1:/ F K />`. :just:`[G.62] <G.62>`

And, since :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ B D />` to :g:`/ B D / <g1:/ B D />`,
and :g:`/ A C / <g1:/ A C />` is also :eq:`equal <g1:/ A C / = g1:/ G H / = g1:/ F K />` to each of the straight lines :g:`/ G H / <g1:/ G H />`, :g:`/ F K / <g1:/ F K />`,

.. subclause:: [G.62] <G.62>

   while :g:`/ B D / <g1:/ B D />` is :eq:`equal <g1:/ B D / = g1:/ G F / = g1:/ H K />` to each of the straight lines :g:`/ G F / <g1:/ G F />`, :g:`/ H K / <g1:/ H K />`,

therefore the :term:`quadrilateral <G.12>` :g:`< F G H K > <g1:< F G H K >>` is :eq:`equilateral <g1:/ G F / = g1:/ G H / = g1:/ H K / = g1:/ F K />`.

I say next that it is also right-angled.

For, since :g:`< G B E A > <g1:< G B E A >>` is a parallelogram,
and the angle :g:`< A E B ) <g1:< A E B )>` is right,
therefore the angle :g:`< A G B ) <g1:< A G B )>` is also :eq:`right <g1:< A E B ) = g1:< A G B )>`. :just:`[G.62] <G.62>`

Similarly we can prove that

.. assertion::

   the angles at :g:`< G H K ) <g1:< G H K )>`, :g:`< H K F ) <g1:< H K F )>`, :g:`< K F G ) <g1:< K F G )>` are also :eq:`right <g1:< A G B ) = g1:< G H K ) = g1:< H K F ) = g1:< K F G )>`.

Therefore :g:`< F G H K > <g1:< F G H K >>` is right-angled.

But it was also proved :eq:`equilateral <g1:/ G F / = g1:/ G H / = g1:/ H K / = g1:/ F K />`;

.. assertion::

   therefore it is a square;

and it has been :term:`circumscribed about the circle <G.150>` :g:`( A B C D ) <g1:( A B C D )>`.

Therefore about the given circle a square has been
circumscribed.

.. qed::

   :just:`Q. E. F.`

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
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.57" [label="G.57", tooltip="G.57 (I.30): Lines parallel to the same line are parallel to one another.", fillcolor="#222244", URL="../G.57/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.def.2): Asegment is said totouch a circle which, meeting thecircle and being produced, does not cut the circle.", fillcolor="#224422", URL="../G.111/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.117/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (III.16): The segment drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the segment and the arc another segment ca...", fillcolor="#222244", URL="../G.118/index.html", target="_top"];
     "G.120" [label="G.120", tooltip="G.120 (III.18): If a segment touch a circle, and a segment be joined from the center to the point of contact, the segment so joined is perpendicular to the tangent.", fillcolor="#222244", URL="../G.120/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (IV.def.4): Apolygon is said to becircumscribed about a circle, when each side of the circumscribedfigure touches the arc of thecircle.", fillcolor="#224422", URL="../G.150/index.html", target="_top"];
     "G.159" [label="G.159", tooltip="G.159 (IV.7): Circumscribe about a given circle a square.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.120" -> "G.1";
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
     "G.52" -> "G.2";
     "G.53" -> "G.2";
     "G.54" -> "G.2";
     "G.55" -> "G.2";
     "G.56" -> "G.2";
     "G.57" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.118" -> "G.3";
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
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.54" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.57" -> "G.4";
     "G.61" -> "G.4";
     "G.62" -> "G.4";
     "G.111" -> "G.4";
     "G.117" -> "G.4";
     "G.118" -> "G.4";
     "G.120" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.150" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.150" -> "G.10";
     "G.159" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.61" -> "G.11";
     "G.120" -> "G.11";
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
     "G.51" -> "G.12";
     "G.53" -> "G.12";
     "G.62" -> "G.12";
     "G.63" -> "G.12";
     "G.150" -> "G.12";
     "G.159" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.63" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.34" -> "G.14";
     "G.41" -> "G.14";
     "G.43" -> "G.14";
     "G.51" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.40" -> "G.16";
     "G.56" -> "G.16";
     "G.57" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.42" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.40" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
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
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.54" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.57" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.77" -> "G.22";
     "G.118" -> "G.22";
     "G.120" -> "G.22";
     "G.159" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.62" -> "G.24";
     "G.28" -> "G.25";
     "G.44" -> "G.25";
     "G.118" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.31" -> "G.30";
     "G.118" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.40" -> "G.33";
     "G.42" -> "G.33";
     "G.54" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.77" -> "G.33";
     "G.118" -> "G.33";
     "G.120" -> "G.33";
     "G.159" -> "G.33";
     "G.37" -> "G.34";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.62" -> "G.36";
     "G.40" -> "G.37";
     "G.42" -> "G.37";
     "G.54" -> "G.37";
     "G.56" -> "G.37";
     "G.40" -> "G.38";
     "G.41" -> "G.40";
     "G.54" -> "G.40";
     "G.56" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.118" -> "G.42";
     "G.120" -> "G.42";
     "G.44" -> "G.43";
     "G.118" -> "G.44";
     "G.120" -> "G.44";
     "G.62" -> "G.51";
     "G.53" -> "G.52";
     "G.54" -> "G.52";
     "G.56" -> "G.52";
     "G.57" -> "G.52";
     "G.62" -> "G.52";
     "G.159" -> "G.52";
     "G.54" -> "G.53";
     "G.159" -> "G.54";
     "G.56" -> "G.55";
     "G.57" -> "G.56";
     "G.62" -> "G.56";
     "G.159" -> "G.57";
     "G.62" -> "G.61";
     "G.118" -> "G.61";
     "G.159" -> "G.61";
     "G.159" -> "G.62";
     "G.159" -> "G.63";
     "G.118" -> "G.77";
     "G.120" -> "G.77";
     "G.118" -> "G.111";
     "G.120" -> "G.111";
     "G.118" -> "G.117";
     "G.159" -> "G.118";
     "G.159" -> "G.120";
     "G.159" -> "G.150";
   }

Required for
------------

:ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`
