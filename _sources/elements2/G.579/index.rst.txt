:order: 579
:number: 579
:canonical_id: G.579
:original_id: XIII.1
:title: G.579 segment cut extreme
:volume: III
:book: XIII
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry, regular-solids
:category: theorem, proof, solid-geometry, regular-solids
:tags: book-xiii, point, segment, triangle, polygon, straight-line, extreme-and-mean-ratio, square, figure, contained-rectangle, gnomon, ratio, equality
:dependencies: G.4, G.9, G.18, G.63, G.81, G.86, G.210, G.228, G.242
:excerpt: If a segment be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half.

.. _G.579:
.. _XIII.1:

G.579 segment cut extreme
=========================

.. rubric:: `XIII.1 <https://geometor.github.io/euclid/heath/volume_III/book_xiii/propositions/01/>`_

.. enunciation::

   If a :term:`segment <G.4>` be cut in :term:`extreme and mean ratio <G.242>`, the :term:`square <G.63>` on the greater segment added to the half of the whole is five times the square on the half.

.. signature:: theorem

   | :fn:`segment_cut_extreme <G.579>`\ ()
   | **prove** the square on :g:`/ C D / <g1:/ C D />` is five times the square on :g:`/ A D / <g1:/ A D />`

.. picture:: g1.svg
   :alt: Book XIII, Proposition 1

.. step:: construct

   Let :g:`/ A B / <g1:/ A B />` be cut in extreme and mean ratio at :g:`C <g1:C>`

.. step:: assert

   Let :g:`/ A C / <g1:/ A C />` be the greater segment

.. step:: construct

   :fn:`extend <G.18>`\ (:g:`/ C A / <g1:/ C A />`) → :g:`/ A D / <g1:/ A D />`

.. step:: construct

   Let :g:`/ A D / <g1:/ A D />` be made half of :g:`/ A B / <g1:/ A B />`

.. step:: construct

   Let the squares :g:`< A E > <g1:< A E >>`, :g:`< D F > <g1:< D F >>` be described on :g:`/ A B / <g1:/ A B />`, :g:`/ D C / <g1:/ D C />`, and let the :term:`figure <G.9>` in :g:`< D F > <g1:< D F >>` be drawn

.. step:: assert

   Let :g:`/ F C / <g1:/ F C />` be carried through to :g:`G <g1:G>`

.. step:: assert

   :g:`/ A B / <g1:/ A B />` has been cut in extreme and mean ratio at :g:`C <g1:C>`,

.. step:: assert ∵ segment_said_cut_def, segments_proportional_rectangle_vi_17 <G.242, G.228>

   the :term:`rectangle <G.81>` :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` is equal to the square on :g:`/ A C / <g1:/ A C />`

.. step:: assert

   :g:`< C E > <g1:< C E >>` is the rectangle :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, and :g:`< F H > <g1:< F H >>` the square on :g:`/ A C / <g1:/ A C />`

.. step:: assert

   :g:`< C E > <g1:< C E >>` is :eq:`equal <g1:< C E > = g1:< F H >>` to :g:`< F H > <g1:< F H >>`

.. step:: assert

   since :g:`/ B A / <g1:/ B A />` is double of :g:`/ A D / <g1:/ A D />`, while :g:`/ B A / <g1:/ B A />` :eq:`= <g1:/ B A / = g1:/ K A /; g1:/ A D / = g1:/ A H />` :g:`/ K A / <g1:/ K A />`, and :g:`/ A D / <g1:/ A D />` to :g:`/ A H / <g1:/ A H />`,

.. step:: assert

   :g:`/ K A / <g1:/ K A />` is also double of :g:`/ A H / <g1:/ A H />`

.. step:: assert ∵ triangles_parallelograms_height <G.210>

   But, as :g:`/ K A / <g1:/ K A />` is to :g:`/ A H / <g1:/ A H />`, so is :g:`< C K > <g1:< C K >>` to :g:`< C H > <g1:< C H >>`

.. step:: assert

   :g:`< C K > <g1:< C K >>` is double of :g:`< C H > <g1:< C H >>`

.. step:: assert

   :g:`< L H > <g1:< L H >>`, :g:`< H C > <g1:< H C >>` are also double of :g:`< C H > <g1:< C H >>`

.. step:: assert

   :g:`< K C > <g1:< K C >>` is equal to :g:`< L H > <g1:< L H >>`, :g:`< H C > <g1:< H C >>`

.. step:: assert

   :g:`< C E > <g1:< C E >>` was also proved :eq:`equal <g1:< C E > = g1:< H F >>` to :g:`< H F > <g1:< H F >>`

.. step:: assert

   the whole square :g:`< A E > <g1:< A E >>` is :eq:`equal <g1:< A E > = g1:< M N O >>` to the :term:`gnomon <G.86>` :g:`< M N O > <g1:< M N O >>`

.. step:: assert

   since :g:`/ B A / <g1:/ B A />` is double of :g:`/ A D / <g1:/ A D />`,

.. step:: assert

   The square on :g:`/ B A / <g1:/ B A />` is quadruple of the square on :g:`/ A D / <g1:/ A D />`, that is, :g:`< A E > <g1:< A E >>` is quadruple of :g:`< D H > <g1:< D H >>`

.. step:: assert

   :g:`< A E > <g1:< A E >>` is :eq:`equal <g1:< A E > = g1:< M N O >>` to the gnomon :g:`< M N O > <g1:< M N O >>`

.. step:: assert

   the gnomon :g:`< M N O > <g1:< M N O >>` is also quadruple of :g:`< A P > <g1:< A P >>`; therefore :g:`< D F > <g1:< D F >>` is five times :g:`< A P > <g1:< A P >>`

.. step:: assert

   :g:`< D F > <g1:< D F >>` is the square on :g:`/ D C / <g1:/ D C />`, and :g:`< A P > <g1:< A P >>` the square on :g:`/ D A / <g1:/ D A />`

.. step:: conclude

   the square on :g:`/ C D / <g1:/ C D />` is five times the square on :g:`/ D A / <g1:/ D A />`

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
     "G.81" [label="G.81", tooltip="G.81 (II.def.1): Any rectangular parallelogram is said to becontained by the twosegments containing theright angle.", fillcolor="#224422", URL="../G.81/index.html", target="_top"];
     "G.86" [label="G.86", tooltip="G.86 (II.def.2): And in any parallelogrammic area let any one whatever of the parallelograms about itsdiameter with the two complements be called agnomon.", fillcolor="#224422", URL="../G.86/index.html", target="_top"];
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
     "G.227" [label="G.227", tooltip="G.227 (VI.16): If four segments be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes equals t...", fillcolor="#222244", URL="../G.227/index.html", target="_top"];
     "G.228" [label="G.228", tooltip="G.228 (VI.17): If three segments be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes equals the square on ...", fillcolor="#222244", URL="../G.228/index.html", target="_top"];
     "G.242" [label="G.242", tooltip="G.242 (VI.def.3): A segment is said to have been cut in extreme and mean ratio when, as the wholeline is to the greater segment, so is the greater to the less.", fillcolor="#224422", URL="../G.242/index.html", target="_top"];
     "G.579" [label="G.579", tooltip="G.579 (XIII.1): If a segment be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.242" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.60" -> "G.3";
     "G.65" -> "G.3";
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
     "G.60" -> "G.4";
     "G.61" -> "G.4";
     "G.62" -> "G.4";
     "G.65" -> "G.4";
     "G.81" -> "G.4";
     "G.225" -> "G.4";
     "G.227" -> "G.4";
     "G.228" -> "G.4";
     "G.579" -> "G.4";
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
     "G.187" -> "G.9";
     "G.189" -> "G.9";
     "G.209" -> "G.9";
     "G.224" -> "G.9";
     "G.579" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
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
     "G.210" -> "G.12";
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
     "G.45" -> "G.14";
     "G.47" -> "G.14";
     "G.51" -> "G.14";
     "G.58" -> "G.14";
     "G.60" -> "G.14";
     "G.65" -> "G.14";
     "G.70" -> "G.14";
     "G.210" -> "G.14";
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
     "G.45" -> "G.18";
     "G.58" -> "G.18";
     "G.66" -> "G.18";
     "G.67" -> "G.18";
     "G.210" -> "G.18";
     "G.579" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.39" -> "G.19";
     "G.40" -> "G.19";
     "G.64" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.45" -> "G.21";
     "G.47" -> "G.21";
     "G.228" -> "G.21";
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
     "G.58" -> "G.22";
     "G.60" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.64" -> "G.22";
     "G.224" -> "G.22";
     "G.225" -> "G.22";
     "G.227" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.60" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.28" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.45" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.48" -> "G.29";
     "G.31" -> "G.30";
     "G.48" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.39" -> "G.33";
     "G.40" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.81" -> "G.33";
     "G.209" -> "G.33";
     "G.227" -> "G.33";
     "G.37" -> "G.34";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.62" -> "G.36";
     "G.64" -> "G.36";
     "G.39" -> "G.37";
     "G.40" -> "G.37";
     "G.56" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.38";
     "G.225" -> "G.39";
     "G.41" -> "G.40";
     "G.56" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.62" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.60" -> "G.52";
     "G.62" -> "G.52";
     "G.64" -> "G.52";
     "G.65" -> "G.52";
     "G.66" -> "G.52";
     "G.67" -> "G.52";
     "G.70" -> "G.52";
     "G.58" -> "G.53";
     "G.60" -> "G.53";
     "G.56" -> "G.55";
     "G.60" -> "G.56";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.66" -> "G.58";
     "G.67" -> "G.58";
     "G.65" -> "G.60";
     "G.62" -> "G.61";
     "G.66" -> "G.61";
     "G.67" -> "G.61";
     "G.70" -> "G.61";
     "G.86" -> "G.61";
     "G.64" -> "G.62";
     "G.65" -> "G.62";
     "G.66" -> "G.62";
     "G.67" -> "G.62";
     "G.70" -> "G.62";
     "G.64" -> "G.63";
     "G.228" -> "G.63";
     "G.579" -> "G.63";
     "G.65" -> "G.64";
     "G.66" -> "G.64";
     "G.67" -> "G.65";
     "G.70" -> "G.66";
     "G.210" -> "G.67";
     "G.210" -> "G.70";
     "G.227" -> "G.81";
     "G.228" -> "G.81";
     "G.579" -> "G.81";
     "G.579" -> "G.86";
     "G.170" -> "G.169";
     "G.171" -> "G.170";
     "G.176" -> "G.170";
     "G.183" -> "G.170";
     "G.185" -> "G.170";
     "G.186" -> "G.170";
     "G.189" -> "G.170";
     "G.190" -> "G.170";
     "G.193" -> "G.170";
     "G.210" -> "G.170";
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
     "G.183" -> "G.180";
     "G.190" -> "G.180";
     "G.224" -> "G.180";
     "G.227" -> "G.180";
     "G.228" -> "G.180";
     "G.182" -> "G.181";
     "G.190" -> "G.181";
     "G.193" -> "G.181";
     "G.183" -> "G.182";
     "G.193" -> "G.183";
     "G.225" -> "G.183";
     "G.186" -> "G.184";
     "G.186" -> "G.185";
     "G.187" -> "G.186";
     "G.225" -> "G.187";
     "G.210" -> "G.189";
     "G.225" -> "G.189";
     "G.193" -> "G.190";
     "G.210" -> "G.193";
     "G.210" -> "G.209";
     "G.225" -> "G.210";
     "G.579" -> "G.210";
     "G.225" -> "G.224";
     "G.227" -> "G.224";
     "G.227" -> "G.225";
     "G.228" -> "G.227";
     "G.579" -> "G.228";
     "G.579" -> "G.242";
   }

Required for
------------

:ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
