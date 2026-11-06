:order: 546
:number: 546
:canonical_id: G.546
:original_id: XI.36
:title: G.546 segments proportional parallelepipedal
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, polygon, straight-line, proportional, solid, equilateral-triangle, solid-angle, plane-angle, reciprocally-related, plane-surface, rectilineal-angle, perpendicular, height, equilateral, proportion, parallelepiped, equality
:dependencies: G.4, G.7, G.13, G.21, G.22, G.30, G.33, G.180, G.209, G.224, G.225, G.524, G.529, G.541, G.545
:excerpt: If three segments be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with the aforesaid solid.

.. _G.546:
.. _XI.36:

G.546 segments proportional parallelepipedal
============================================

.. rubric:: `XI.36 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/36/>`_

.. enunciation::

   If three :term:`segments <G.4>` be :term:`proportional <G.180>`, the parallelepipedal :term:`solid <G.529>` formed out of the three is equal to the parallelepipedal solid on the mean which is :term:`equilateral <G.13>`, but equiangular with the aforesaid solid.

.. signature:: theorem

   | :fn:`segments_proportional_parallelepipedal <G.546>`\ (:g:`/ A / <g1:/ A />`, :g:`/ B / <g1:/ B />`, :g:`/ C / <g1:/ C />`)
   | **given** :g:`/ A / <g1:/ A />`, :g:`/ B / <g1:/ B />`, :g:`/ C / <g1:/ C />` be three segments in proportion, so that, as :g:`/ A / <g1:/ A />` is to :g:`/ B / <g1:/ B />`, so is :g:`/ B / <g1:/ B />` to :g:`/ C / <g1:/ C />`
   | **prove** the solid formed out of :g:`/ A / <g1:/ A />`, :g:`/ B / <g1:/ B />`, :g:`/ C / <g1:/ C />` is equal to the solid on :g:`/ B / <g1:/ B />` which is equilateral, but equiangular with the aforesaid solid

.. picture:: g1.svg
   :alt: Proposition 36 diagram

.. step:: given

   :g:`/ A / <g1:/ A />`, :g:`/ B / <g1:/ B />`, :g:`/ C / <g1:/ C />` be three segments in proportion, so that, as :g:`/ A / <g1:/ A />` is to :g:`/ B / <g1:/ B />`, so is :g:`/ B / <g1:/ B />` to :g:`/ C / <g1:/ C />`

.. step:: construct

   Let there be set out the :term:`solid angle <G.524>` at :g:`E <g1:E>` contained by :g:`< D E G ) <g1:< D E G )>`, :g:`< G E F ) <g1:< G E F )>`, :g:`< F E D ) <g1:< F E D )>`, let each of :g:`/ D E / <g1:/ D E />`, :g:`/ G E / <g1:/ G E />`, :g:`/ E F / <g1:/ E F />` be made :eq:`equal <g1:/ D E / = g1:/ G E / = g1:/ E F / = g1:/ B />` to :g:`/ B / <g1:/ B />`

.. step:: construct

   Let the parallelepipedal solid :g:`< E K > <g1:< E K >>` be completed, let :g:`/ L M / <g1:/ L M />` be made :eq:`equal <g1:/ L M / = g1:/ A />` to :g:`/ A / <g1:/ A />`

.. step:: construct

   On :g:`/ L M / <g1:/ L M />`, and at :g:`L <g1:L>` on it, let there be constructed a solid angle equal to the solid angle at :g:`E <g1:E>`, namely that contained by :g:`< N L O ) <g1:< N L O )>`, :g:`< O L M ) <g1:< O L M )>`, :g:`< M L N ) <g1:< M L N )>`

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ B / <g1:/ B />`, and :g:`/ L N / <g1:/ L N />` :eq:`equal <g1:/ L N / = g1:/ C />` to :g:`/ C / <g1:/ C />`) → :g:`/ L O / <g1:/ L O />` (:eq:`equal <g1:/ L O / = g1:/ B />`)

.. step:: assert

   Since, as :g:`/ A / <g1:/ A />` is to :g:`/ B / <g1:/ B />`, so is :g:`/ B / <g1:/ B />` to :g:`/ C / <g1:/ C />`, while :g:`/ A / <g1:/ A />` :eq:`= <g1:/ A / = g1:/ L M /; g1:/ B / = g1:/ L O / = g1:/ E D /; g1:/ C / = g1:/ L N />` :g:`/ L M / <g1:/ L M />`, :g:`/ B / <g1:/ B />` to each of :g:`/ L O / <g1:/ L O />`, :g:`/ E D / <g1:/ E D />`, and :g:`/ C / <g1:/ C />` to :g:`/ L N / <g1:/ L N />`,

.. step:: assert

   as :g:`/ L M / <g1:/ L M />` is to :g:`/ E F / <g1:/ E F />`, so is :g:`/ D E / <g1:/ D E />` to :g:`/ L N / <g1:/ L N />`

.. step:: assert

   the sides about the :eq:`= <g1:< N L M ) = g1:< D E F )>` :term:`angles <G.22>` :g:`< N L M ) <g1:< N L M )>`, :g:`< D E F ) <g1:< D E F )>` are :term:`reciprocally proportional <G.224>`

.. step:: assert ∵ equal_equiangular_parallelograms <G.225>

   the parallelogram :g:`< M N > <g1:< M N >>` is :eq:`equal <g1:< M N > = g1:< D F >>` to the parallelogram :g:`< D F > <g1:< D F >>`

.. step:: assert

   since :g:`< D E F ) <g1:< D E F )>`, :g:`< N L M ) <g1:< N L M )>` are two :term:`plane <G.7>` :term:`rectilineal angles <G.30>`, and on them the elevated segments :g:`/ L O / <g1:/ L O />`, :g:`/ E G / <g1:/ E G />` are set up which :eq:`= <g1:/ L O / = g1:/ E G />` and contain equal angles with the original segments,

.. step:: assert ∵ there_equal_plane <G.545>

   the :term:`perpendiculars <G.33>` drawn from :g:`G <g1:G>`, :g:`O <g1:O>` to the planes through :g:`/ N L / <g1:/ N L />`, :g:`/ L M / <g1:/ L M />` and :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` are equal to one another; hence the solids :g:`< L H > <g1:< L H >>`, :g:`< E K > <g1:< E K >>` are of the same :term:`height <G.209>`

.. step:: assert ∵ parallelepipedal_solids_equal <G.541>

   Parallelepipedal solids on equal bases and of the same height are equal to one another

.. step:: assert

   the solid :g:`< H L > <g1:< H L >>` is :eq:`equal <g1:< H L > = g1:< E K >>` to the solid :g:`< E K > <g1:< E K >>`

.. step:: assert

   :g:`< L H > <g1:< L H >>` is the solid formed out of :g:`/ A / <g1:/ A />`, :g:`/ B / <g1:/ B />`, :g:`/ C / <g1:/ C />`, and :g:`< E K > <g1:< E K >>` the solid on :g:`/ B / <g1:/ B />`

.. step:: conclude

   the parallelepipedal solid formed out of :g:`/ A / <g1:/ A />`, :g:`/ B / <g1:/ B />`, :g:`/ C / <g1:/ C />` is equal to the solid on :g:`/ B / <g1:/ B />` which is equilateral, but equiangular with the aforesaid solid

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
     "G.54" [label="G.54", tooltip="G.54 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
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
     "G.75" [label="G.75", tooltip="G.75 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.75/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (I.def.11): An obtuse angle is greater than a right angle.", fillcolor="#224422", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (I.def.21): A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.", fillcolor="#224422", URL="../G.78/index.html", target="_top"];
     "G.79" [label="G.79", tooltip="G.79 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.79/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (I.48): If the square on one side of a triangle equals the sum of the squares on the other two sides, the angle contained by those two sides is right.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.171" [label="G.171", tooltip="G.171 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.13): Inverse ratio means taking theconsequent as antecedent in relation to the antecedent as consequent.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (V.def.7): When, of theequimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then th...", fillcolor="#224422", URL="../G.185/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.187" [label="G.187", tooltip="G.187 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.187/index.html", target="_top"];
     "G.189" [label="G.189", tooltip="G.189 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.189/index.html", target="_top"];
     "G.190" [label="G.190", tooltip="G.190 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.190/index.html", target="_top"];
     "G.193" [label="G.193", tooltip="G.193 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.193/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VI.def.4): The height of anyfigure is theperpendicular drawn from the vertex to the base.", fillcolor="#224422", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.210/index.html", target="_top"];
     "G.224" [label="G.224", tooltip="G.224 (VI.def.2): Reciprocally related figures have their sides about equal angles reciprocally proportional.", fillcolor="#224422", URL="../G.224/index.html", target="_top"];
     "G.225" [label="G.225", tooltip="G.225 (VI.14): In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are...", fillcolor="#222244", URL="../G.225/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.502" [label="G.502", tooltip="G.502 (XI.1): A part of a segment cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.502/index.html", target="_top"];
     "G.503" [label="G.503", tooltip="G.503 (XI.2): If two segments cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.503/index.html", target="_top"];
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", fillcolor="#222244", URL="../G.504/index.html", target="_top"];
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.506" [label="G.506", tooltip="G.506 (XI.4): If a segment be set up at right angles to two segments which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.506/index.html", target="_top"];
     "G.507" [label="G.507", tooltip="G.507 (XI.5): If a segment be set up at right angles to three segments which meet one another, at their common point of section, the three segments are in one plane.", fillcolor="#222244", URL="../G.507/index.html", target="_top"];
     "G.508" [label="G.508", tooltip="G.508 (XI.6): If two segments be at right angles to the same plane, the segments is parallel.", fillcolor="#222244", URL="../G.508/index.html", target="_top"];
     "G.509" [label="G.509", tooltip="G.509 (XI.7): If two segments be parallel and points be taken at random on each of them, the segment joining the points is in the same plane with the parallel lines.", fillcolor="#222244", URL="../G.509/index.html", target="_top"];
     "G.510" [label="G.510", tooltip="G.510 (XI.8): If two segments be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.510/index.html", target="_top"];
     "G.511" [label="G.511", tooltip="G.511 (XI.9): Straight lines which are parallel to the same segment and are not in the same plane with it are also parallel to one another.", fillcolor="#222244", URL="../G.511/index.html", target="_top"];
     "G.512" [label="G.512", tooltip="G.512 (XI.10): If two segments meeting one another be parallel to two segments meeting one another not in the same plane, they will contain equal angles.", fillcolor="#222244", URL="../G.512/index.html", target="_top"];
     "G.516" [label="G.516", tooltip="G.516 (XI.def.8): Parallel planes are those which do not meet.", fillcolor="#224422", URL="../G.516/index.html", target="_top"];
     "G.519" [label="G.519", tooltip="G.519 (XI.16): If two parallel planes be cut by any plane, their common sections are parallel.", fillcolor="#222244", URL="../G.519/index.html", target="_top"];
     "G.524" [label="G.524", tooltip="G.524 (XI.def.11): Asolid angle is the inclination constituted by more than twolines which meet one another and are not in the samesurface, towards all the lines. Otherwise: Asolid angle is that whic...", fillcolor="#224422", URL="../G.524/index.html", target="_top"];
     "G.529" [label="G.529", tooltip="G.529 (XI.def.1): Asolid is that which has length, breadth, and depth.", fillcolor="#224422", URL="../G.529/index.html", target="_top"];
     "G.530" [label="G.530", tooltip="G.530 (XI.24): If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.", fillcolor="#222244", URL="../G.530/index.html", target="_top"];
     "G.531" [label="G.531", tooltip="G.531 (XI.25): If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.", fillcolor="#222244", URL="../G.531/index.html", target="_top"];
     "G.533" [label="G.533", tooltip="G.533 (XI.def.2): Anextremity of asolid is asurface.", fillcolor="#224422", URL="../G.533/index.html", target="_top"];
     "G.535" [label="G.535", tooltip="G.535 (XI.def.10): Equal and similar solid figures are thosecontained by similar planes equal in multitude and in magnitude.", fillcolor="#224422", URL="../G.535/index.html", target="_top"];
     "G.537" [label="G.537", tooltip="G.537 (XI.def.13): Aprism is asolid figure contained byplanes two of which, namely those which are opposite, are equal, similar andparallel, while the rest are parallelograms.", fillcolor="#224422", URL="../G.537/index.html", target="_top"];
     "G.539" [label="G.539", tooltip="G.539 (XI.29): Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same segments, are equal.", fillcolor="#222244", URL="../G.539/index.html", target="_top"];
     "G.540" [label="G.540", tooltip="G.540 (XI.30): Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same segments, are equal.", fillcolor="#222244", URL="../G.540/index.html", target="_top"];
     "G.541" [label="G.541", tooltip="G.541 (XI.31): Parallelepipedal solids which are on equal bases and of the same height are equal.", fillcolor="#222244", URL="../G.541/index.html", target="_top"];
     "G.545" [label="G.545", tooltip="G.545 (XI.35): If there be two equal plane angles, and on their vertices there be set up elevated segments containing equal angles with the original segments respectively, if on the elevated segm...", fillcolor="#222244", URL="../G.545/index.html", target="_top"];
     "G.546" [label="G.546", tooltip="G.546 (XI.36): If three segments be proportional, the parallelepipedal solid formed out of the three is equal to the parallelepipedal solid on the mean which is equilateral, but equiangular with ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.75" -> "G.1";
     "G.79" -> "G.1";
     "G.80" -> "G.1";
     "G.506" -> "G.1";
     "G.507" -> "G.1";
     "G.509" -> "G.1";
     "G.519" -> "G.1";
     "G.524" -> "G.1";
     "G.545" -> "G.1";
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
     "G.54" -> "G.2";
     "G.55" -> "G.2";
     "G.56" -> "G.2";
     "G.58" -> "G.2";
     "G.504" -> "G.2";
     "G.509" -> "G.2";
     "G.524" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.60" -> "G.3";
     "G.65" -> "G.3";
     "G.504" -> "G.3";
     "G.533" -> "G.3";
     "G.539" -> "G.3";
     "G.540" -> "G.3";
     "G.541" -> "G.3";
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
     "G.54" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.58" -> "G.4";
     "G.60" -> "G.4";
     "G.61" -> "G.4";
     "G.62" -> "G.4";
     "G.65" -> "G.4";
     "G.75" -> "G.4";
     "G.79" -> "G.4";
     "G.80" -> "G.4";
     "G.225" -> "G.4";
     "G.502" -> "G.4";
     "G.503" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.506" -> "G.4";
     "G.507" -> "G.4";
     "G.508" -> "G.4";
     "G.509" -> "G.4";
     "G.510" -> "G.4";
     "G.511" -> "G.4";
     "G.512" -> "G.4";
     "G.519" -> "G.4";
     "G.531" -> "G.4";
     "G.539" -> "G.4";
     "G.540" -> "G.4";
     "G.541" -> "G.4";
     "G.545" -> "G.4";
     "G.546" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.524" -> "G.5";
     "G.10" -> "G.6";
     "G.533" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.502" -> "G.7";
     "G.503" -> "G.7";
     "G.504" -> "G.7";
     "G.505" -> "G.7";
     "G.506" -> "G.7";
     "G.507" -> "G.7";
     "G.508" -> "G.7";
     "G.509" -> "G.7";
     "G.510" -> "G.7";
     "G.511" -> "G.7";
     "G.512" -> "G.7";
     "G.519" -> "G.7";
     "G.524" -> "G.7";
     "G.530" -> "G.7";
     "G.531" -> "G.7";
     "G.537" -> "G.7";
     "G.541" -> "G.7";
     "G.545" -> "G.7";
     "G.546" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.66" -> "G.9";
     "G.67" -> "G.9";
     "G.187" -> "G.9";
     "G.189" -> "G.9";
     "G.209" -> "G.9";
     "G.224" -> "G.9";
     "G.539" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.502" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
     "G.502" -> "G.11";
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
     "G.78" -> "G.12";
     "G.79" -> "G.12";
     "G.80" -> "G.12";
     "G.210" -> "G.12";
     "G.503" -> "G.12";
     "G.508" -> "G.12";
     "G.539" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.63" -> "G.13";
     "G.75" -> "G.13";
     "G.546" -> "G.13";
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
     "G.79" -> "G.14";
     "G.80" -> "G.14";
     "G.210" -> "G.14";
     "G.503" -> "G.14";
     "G.508" -> "G.14";
     "G.510" -> "G.14";
     "G.512" -> "G.14";
     "G.530" -> "G.14";
     "G.540" -> "G.14";
     "G.541" -> "G.14";
     "G.545" -> "G.14";
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
     "G.54" -> "G.16";
     "G.56" -> "G.16";
     "G.64" -> "G.16";
     "G.65" -> "G.16";
     "G.66" -> "G.16";
     "G.67" -> "G.16";
     "G.70" -> "G.16";
     "G.75" -> "G.16";
     "G.80" -> "G.16";
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
     "G.210" -> "G.18";
     "G.540" -> "G.18";
     "G.541" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.39" -> "G.19";
     "G.40" -> "G.19";
     "G.54" -> "G.19";
     "G.64" -> "G.19";
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
     "G.80" -> "G.21";
     "G.545" -> "G.21";
     "G.546" -> "G.21";
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
     "G.54" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.58" -> "G.22";
     "G.60" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.64" -> "G.22";
     "G.75" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.78" -> "G.22";
     "G.79" -> "G.22";
     "G.80" -> "G.22";
     "G.224" -> "G.22";
     "G.225" -> "G.22";
     "G.512" -> "G.22";
     "G.524" -> "G.22";
     "G.530" -> "G.22";
     "G.545" -> "G.22";
     "G.546" -> "G.22";
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
     "G.506" -> "G.24";
     "G.508" -> "G.24";
     "G.530" -> "G.24";
     "G.539" -> "G.24";
     "G.545" -> "G.24";
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
     "G.80" -> "G.29";
     "G.506" -> "G.29";
     "G.508" -> "G.29";
     "G.512" -> "G.29";
     "G.539" -> "G.29";
     "G.545" -> "G.29";
     "G.31" -> "G.30";
     "G.48" -> "G.30";
     "G.546" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.39" -> "G.33";
     "G.40" -> "G.33";
     "G.54" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.75" -> "G.33";
     "G.76" -> "G.33";
     "G.77" -> "G.33";
     "G.78" -> "G.33";
     "G.79" -> "G.33";
     "G.80" -> "G.33";
     "G.209" -> "G.33";
     "G.505" -> "G.33";
     "G.506" -> "G.33";
     "G.507" -> "G.33";
     "G.508" -> "G.33";
     "G.510" -> "G.33";
     "G.511" -> "G.33";
     "G.541" -> "G.33";
     "G.545" -> "G.33";
     "G.546" -> "G.33";
     "G.37" -> "G.34";
     "G.75" -> "G.34";
     "G.80" -> "G.34";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.62" -> "G.36";
     "G.64" -> "G.36";
     "G.79" -> "G.36";
     "G.80" -> "G.36";
     "G.39" -> "G.37";
     "G.40" -> "G.37";
     "G.54" -> "G.37";
     "G.56" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.38";
     "G.79" -> "G.39";
     "G.225" -> "G.39";
     "G.41" -> "G.40";
     "G.54" -> "G.40";
     "G.56" -> "G.40";
     "G.506" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.541" -> "G.48";
     "G.62" -> "G.51";
     "G.506" -> "G.51";
     "G.545" -> "G.51";
     "G.53" -> "G.52";
     "G.54" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.60" -> "G.52";
     "G.62" -> "G.52";
     "G.64" -> "G.52";
     "G.65" -> "G.52";
     "G.66" -> "G.52";
     "G.67" -> "G.52";
     "G.70" -> "G.52";
     "G.75" -> "G.52";
     "G.79" -> "G.52";
     "G.508" -> "G.52";
     "G.509" -> "G.52";
     "G.510" -> "G.52";
     "G.511" -> "G.52";
     "G.512" -> "G.52";
     "G.519" -> "G.52";
     "G.530" -> "G.52";
     "G.531" -> "G.52";
     "G.537" -> "G.52";
     "G.541" -> "G.52";
     "G.54" -> "G.53";
     "G.58" -> "G.53";
     "G.60" -> "G.53";
     "G.508" -> "G.54";
     "G.56" -> "G.55";
     "G.60" -> "G.56";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.75" -> "G.56";
     "G.510" -> "G.56";
     "G.66" -> "G.58";
     "G.67" -> "G.58";
     "G.75" -> "G.58";
     "G.79" -> "G.58";
     "G.541" -> "G.58";
     "G.545" -> "G.58";
     "G.65" -> "G.60";
     "G.512" -> "G.60";
     "G.62" -> "G.61";
     "G.66" -> "G.61";
     "G.67" -> "G.61";
     "G.70" -> "G.61";
     "G.502" -> "G.61";
     "G.64" -> "G.62";
     "G.65" -> "G.62";
     "G.66" -> "G.62";
     "G.67" -> "G.62";
     "G.70" -> "G.62";
     "G.75" -> "G.62";
     "G.530" -> "G.62";
     "G.539" -> "G.62";
     "G.64" -> "G.63";
     "G.75" -> "G.63";
     "G.79" -> "G.63";
     "G.80" -> "G.63";
     "G.545" -> "G.63";
     "G.65" -> "G.64";
     "G.66" -> "G.64";
     "G.541" -> "G.64";
     "G.67" -> "G.65";
     "G.539" -> "G.65";
     "G.70" -> "G.66";
     "G.210" -> "G.67";
     "G.79" -> "G.70";
     "G.210" -> "G.70";
     "G.79" -> "G.75";
     "G.80" -> "G.75";
     "G.78" -> "G.76";
     "G.78" -> "G.77";
     "G.79" -> "G.78";
     "G.80" -> "G.79";
     "G.545" -> "G.79";
     "G.545" -> "G.80";
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.256" -> "G.169";
     "G.171" -> "G.170";
     "G.176" -> "G.170";
     "G.183" -> "G.170";
     "G.185" -> "G.170";
     "G.186" -> "G.170";
     "G.189" -> "G.170";
     "G.190" -> "G.170";
     "G.193" -> "G.170";
     "G.210" -> "G.170";
     "G.531" -> "G.170";
     "G.186" -> "G.171";
     "G.190" -> "G.171";
     "G.189" -> "G.173";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.187" -> "G.176";
     "G.189" -> "G.176";
     "G.190" -> "G.176";
     "G.193" -> "G.176";
     "G.210" -> "G.176";
     "G.531" -> "G.176";
     "G.541" -> "G.176";
     "G.183" -> "G.180";
     "G.190" -> "G.180";
     "G.224" -> "G.180";
     "G.546" -> "G.180";
     "G.182" -> "G.181";
     "G.190" -> "G.181";
     "G.193" -> "G.181";
     "G.183" -> "G.182";
     "G.193" -> "G.183";
     "G.225" -> "G.183";
     "G.541" -> "G.183";
     "G.186" -> "G.184";
     "G.186" -> "G.185";
     "G.187" -> "G.186";
     "G.225" -> "G.187";
     "G.541" -> "G.187";
     "G.210" -> "G.189";
     "G.225" -> "G.189";
     "G.541" -> "G.189";
     "G.193" -> "G.190";
     "G.210" -> "G.193";
     "G.210" -> "G.209";
     "G.539" -> "G.209";
     "G.540" -> "G.209";
     "G.541" -> "G.209";
     "G.546" -> "G.209";
     "G.225" -> "G.210";
     "G.225" -> "G.224";
     "G.546" -> "G.224";
     "G.546" -> "G.225";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.256" -> "G.248";
     "G.531" -> "G.248";
     "G.256" -> "G.253";
     "G.502" -> "G.253";
     "G.503" -> "G.253";
     "G.531" -> "G.256";
     "G.503" -> "G.502";
     "G.519" -> "G.502";
     "G.508" -> "G.503";
     "G.510" -> "G.503";
     "G.507" -> "G.504";
     "G.509" -> "G.504";
     "G.506" -> "G.505";
     "G.507" -> "G.505";
     "G.508" -> "G.505";
     "G.510" -> "G.505";
     "G.511" -> "G.505";
     "G.507" -> "G.506";
     "G.510" -> "G.506";
     "G.511" -> "G.506";
     "G.508" -> "G.507";
     "G.511" -> "G.508";
     "G.510" -> "G.509";
     "G.511" -> "G.510";
     "G.545" -> "G.510";
     "G.512" -> "G.511";
     "G.530" -> "G.512";
     "G.519" -> "G.516";
     "G.530" -> "G.516";
     "G.530" -> "G.519";
     "G.546" -> "G.524";
     "G.530" -> "G.529";
     "G.531" -> "G.529";
     "G.533" -> "G.529";
     "G.537" -> "G.529";
     "G.539" -> "G.529";
     "G.540" -> "G.529";
     "G.541" -> "G.529";
     "G.546" -> "G.529";
     "G.531" -> "G.530";
     "G.541" -> "G.530";
     "G.541" -> "G.531";
     "G.535" -> "G.533";
     "G.541" -> "G.535";
     "G.539" -> "G.537";
     "G.540" -> "G.539";
     "G.541" -> "G.539";
     "G.541" -> "G.540";
     "G.546" -> "G.541";
     "G.546" -> "G.545";
   }

.. toctree::
   :hidden:

   code
   heath
