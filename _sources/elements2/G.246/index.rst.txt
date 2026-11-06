:order: 246
:number: 246
:canonical_id: G.246
:original_id: VI.33
:title: G.246 equal circles angles
:volume: II
:book: VI
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, proportions, similar-figures
:category: theorem, proof, plane-geometry, proportions, similar-figures
:tags: book-vi, point, segment, circle, angle, equal-circles, plane-angle, in-the-same-ratio, stand-upon-circumference, centre, multiple, arc, ratio, plane, equality
:dependencies: G.11, G.14, G.22, G.131, G.132, G.134, G.170, G.176
:excerpt: In equal circles angles have the same ratio as the arcs on which they stand, whether they stand at the centres or at the arcs.

.. _G.246:
.. _VI.33:

G.246 equal circles angles
==========================

.. rubric:: `VI.33 <https://geometor.github.io/euclid/heath/volume_II/book_vi/propositions/33/>`_

.. enunciation::

   In :term:`equal circles <G.131>` :term:`angles <G.22>` have the :term:`same ratio <G.176>` as the arcs on which they stand, whether they stand at the :term:`centres <G.11>` or at the arcs.

.. signature:: theorem

   | :fn:`equal_circles_angles <G.246>`\ (:g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>`, :g:`< B G C ) <g1:< B G C )>`, :g:`< E H F ) <g1:< E H F )>`)
   | **given** :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` be :eq:`= <g1:( A B C ) = g1:( D E F )>` circles, let :g:`< B G C ) <g1:< B G C )>`, :g:`< E H F ) <g1:< E H F )>` be angles at their centres :g:`G <g1:G>`, :g:`H <g1:H>`, :g:`< B A C ) <g1:< B A C )>`, :g:`< E D F ) <g1:< E D F )>` angles at the arcs
   | **prove** also, as the arc :g:`( B C ) <g1:( B C )>` is to the arc :g:`( E F ) <g1:( E F )>`, so is :g:`< B G C ) <g1:< B G C )>` to :g:`< E H F ) <g1:< E H F )>`, and :g:`< B A C ) <g1:< B A C )>` to :g:`< E D F ) <g1:< E D F )>`

.. picture:: g1.svg
   :alt: Proposition 33

.. step:: given

   :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` be :eq:`= <g1:( A B C ) = g1:( D E F )>` circles, let :g:`< B G C ) <g1:< B G C )>`, :g:`< E H F ) <g1:< E H F )>` be angles at their centres :g:`G <g1:G>`, :g:`H <g1:H>`, :g:`< B A C ) <g1:< B A C )>`, :g:`< E D F ) <g1:< E D F )>` angles at the arcs

.. step:: assert

   I say that, as the arc :g:`( B C ) <g1:( B C )>` is to the arc :g:`( E F ) <g1:( E F )>`, so is :g:`< B G C ) <g1:< B G C )>` to :g:`< E H F ) <g1:< E H F )>`, and :g:`< B A C ) <g1:< B A C )>` to :g:`< E D F ) <g1:< E D F )>`

.. step:: construct

   Let any number of consecutive arcs :g:`( C K ) <g1:( C K )>`, :g:`( K L ) <g1:( K L )>` be made :eq:`equal <g1:( C K ) = g1:( K L ) = g1:( B C )>` to the arc :g:`( B C ) <g1:( B C )>`, and any number of consecutive arcs :g:`( F M ) <g1:( F M )>`, :g:`( M N ) <g1:( M N )>` :eq:`equal <g1:( F M ) = g1:( M N ) = g1:( E F )>` to the arc :g:`( E F ) <g1:( E F )>`

.. step:: construct

   :fn:`segment <G.14>`\ (:g:`G <g1:G>`, :g:`K <g1:K>`) → :g:`/ G K / <g1:/ G K />`, :fn:`segment <G.14>`\ (:g:`G <g1:G>`, :g:`L <g1:L>`) → :g:`/ G L / <g1:/ G L />`, :fn:`segment <G.14>`\ (:g:`H <g1:H>`, :g:`M <g1:M>`) → :g:`/ H M / <g1:/ H M />`, :fn:`segment <G.14>`\ (:g:`H <g1:H>`, :g:`N <g1:N>`) → :g:`/ H N / <g1:/ H N />`

.. step:: assert

   the arcs :g:`( B C ) <g1:( B C )>`, :g:`( C K ) <g1:( C K )>`, :g:`( K L ) <g1:( K L )>` :eq:`= <g1:( B C ) = g1:( C K ) = g1:( K L )>`,

.. step:: assert ∵ equal_arcs_equal_angles <G.134>

   :g:`< B G C ) <g1:< B G C )>`, :g:`< C G K ) <g1:< C G K )>`, :g:`< K G L ) <g1:< K G L )>` :eq:`= <g1:< B G C ) = g1:< C G K ) = g1:< K G L )>`

.. step:: assert

   whatever :term:`multiple <G.170>` the arc :g:`( B L ) <g1:( B L )>` is of :g:`( B C ) <g1:( B C )>`, that multiple also is :g:`< B G L ) <g1:< B G L )>` of :g:`< B G C ) <g1:< B G C )>`

.. step:: assert

   For the same reason also,

.. step:: assert

   Whatever multiple the arc :g:`( N E ) <g1:( N E )>` is of :g:`( E F ) <g1:( E F )>`, that multiple also is :g:`< N H E ) <g1:< N H E )>` of :g:`< E H F ) <g1:< E H F )>`

.. step:: assert ∵ equal_arcs_equal_angles <G.134>

   If then the arc :g:`( B L ) <g1:( B L )>` :eq:`= <g1:( B L ) = g1:( E N )>` the arc :g:`( E N ) <g1:( E N )>`, :g:`< B G L ) <g1:< B G L )>` :eq:`= <g1:< B G L ) = g1:< E H N )>` :g:`< E H N ) <g1:< E H N )>`; if the arc :g:`( B L ) <g1:( B L )>` > the arc :g:`( E N ) <g1:( E N )>`, :g:`< B G L ) <g1:< B G L )>` is also greater than :g:`< E H N ) <g1:< E H N )>`; and, if less, less

.. step:: assert

   There being then four magnitudes, two arcs :g:`( B C ) <g1:( B C )>`, :g:`( E F ) <g1:( E F )>`, and two angles :g:`< B G C ) <g1:< B G C )>`, :g:`< E H F ) <g1:< E H F )>`, there have been taken, of the arc :g:`( B C ) <g1:( B C )>` and :g:`< B G C ) <g1:< B G C )>` equimultiples, namely the arc :g:`( B L ) <g1:( B L )>` and :g:`< B G L ) <g1:< B G L )>`, and of the arc :g:`( E F ) <g1:( E F )>` and :g:`< E H F ) <g1:< E H F )>` equimultiples, namely the arc :g:`( E N ) <g1:( E N )>` and :g:`< E H N ) <g1:< E H N )>`

.. step:: assert

   It has been proved that, if the arc :g:`( B L ) <g1:( B L )>` is in excess of the arc :g:`( E N ) <g1:( E N )>`, :g:`< B G L ) <g1:< B G L )>` is also in excess of :g:`< E H N ) <g1:< E H N )>`; if :eq:`= <g1:( B L ) = g1:( E N )>`, :eq:`= <g1:< B G L ) = g1:< E H N )>`; and if less, less

.. step:: assert ∵ magnitudes_said_ratio_def <G.176>

   as the arc :g:`( B C ) <g1:( B C )>` is to :g:`( E F ) <g1:( E F )>`, so is :g:`< B G C ) <g1:< B G C )>` to :g:`< E H F ) <g1:< E H F )>`

.. step:: assert

   But, as :g:`< B G C ) <g1:< B G C )>` is to :g:`< E H F ) <g1:< E H F )>`, so is :g:`< B A C ) <g1:< B A C )>` to :g:`< E D F ) <g1:< E D F )>`; for they are doubles

.. step:: conclude

   also, as the arc :g:`( B C ) <g1:( B C )>` is to the arc :g:`( E F ) <g1:( E F )>`, so is :g:`< B G C ) <g1:< B G C )>` to :g:`< E H F ) <g1:< E H F )>`, and :g:`< B A C ) <g1:< B A C )>` to :g:`< E D F ) <g1:< E D F )>`

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
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.102" [label="G.102", tooltip="G.102 (III.5): Two intersecting circles do not have the same center.", fillcolor="#222244", URL="../G.102/index.html", target="_top"];
     "G.108" [label="G.108", tooltip="G.108 (III.10): A circle does not intersect another circle at more than two points.", fillcolor="#222244", URL="../G.108/index.html", target="_top"];
     "G.122" [label="G.122", tooltip="G.122 (III.def.10): Asector of a circle is thefigure which, when anangle is constructed at thecenter of thecircle, is contained by thesegments containing the angle and the arc cut off by them.", fillcolor="#224422", URL="../G.122/index.html", target="_top"];
     "G.123" [label="G.123", tooltip="G.123 (III.20): In a circle, the angle at the center is double the angle at the circumference when the angles have the same arc as base.", fillcolor="#222244", URL="../G.123/index.html", target="_top"];
     "G.126" [label="G.126", tooltip="G.126 (III.def.6): Asegment of a circle is thefigure contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.126/index.html", target="_top"];
     "G.127" [label="G.127", tooltip="G.127 (III.def.11): Similar segments of circles are those which admit equalangles, or in which the angles are equal.", fillcolor="#224422", URL="../G.127/index.html", target="_top"];
     "G.128" [label="G.128", tooltip="G.128 (III.23): On the same segment and on the same side of it, there cannot be constructed two similar and unequal segments of circles.", fillcolor="#222244", URL="../G.128/index.html", target="_top"];
     "G.129" [label="G.129", tooltip="G.129 (III.24): Similar segments of circles on equal segments are equal to one another.", fillcolor="#222244", URL="../G.129/index.html", target="_top"];
     "G.131" [label="G.131", tooltip="G.131 (III.def.1): Equal circles are those thediameters of which are equal, or the radii of which are equal.", fillcolor="#224422", URL="../G.131/index.html", target="_top"];
     "G.132" [label="G.132", tooltip="G.132 (III.def.9): And, when thesegments containing theangle cut off a arc, the angle is said tostand upon that arc.", fillcolor="#224422", URL="../G.132/index.html", target="_top"];
     "G.133" [label="G.133", tooltip="G.133 (III.26): In equal circles, equal angles stand on equal arcs, whether they stand at the centers or at the circumferences.", fillcolor="#222244", URL="../G.133/index.html", target="_top"];
     "G.134" [label="G.134", tooltip="G.134 (III.27): In equal circles, angles standing on equal arcs are equal to one another, whether they stand at the centers or at the circumferences.", fillcolor="#222244", URL="../G.134/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.246" [label="G.246", tooltip="G.246 (VI.33): In equal circles angles have the same ratio as the arcs on which they stand, whether they stand at the centres or at the arcs.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.108" -> "G.1";
     "G.129" -> "G.1";
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
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
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
     "G.122" -> "G.4";
     "G.126" -> "G.4";
     "G.128" -> "G.4";
     "G.129" -> "G.4";
     "G.132" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.122" -> "G.9";
     "G.126" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.98" -> "G.10";
     "G.102" -> "G.10";
     "G.108" -> "G.10";
     "G.122" -> "G.10";
     "G.123" -> "G.10";
     "G.126" -> "G.10";
     "G.129" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
     "G.98" -> "G.11";
     "G.102" -> "G.11";
     "G.108" -> "G.11";
     "G.122" -> "G.11";
     "G.123" -> "G.11";
     "G.133" -> "G.11";
     "G.134" -> "G.11";
     "G.246" -> "G.11";
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
     "G.53" -> "G.12";
     "G.59" -> "G.12";
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
     "G.102" -> "G.14";
     "G.108" -> "G.14";
     "G.123" -> "G.14";
     "G.128" -> "G.14";
     "G.133" -> "G.14";
     "G.246" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.47" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.40" -> "G.16";
     "G.47" -> "G.16";
     "G.56" -> "G.16";
     "G.59" -> "G.16";
     "G.102" -> "G.16";
     "G.134" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.45" -> "G.18";
     "G.53" -> "G.18";
     "G.58" -> "G.18";
     "G.59" -> "G.18";
     "G.108" -> "G.18";
     "G.123" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.40" -> "G.19";
     "G.123" -> "G.19";
     "G.133" -> "G.19";
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
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.45" -> "G.22";
     "G.48" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.58" -> "G.22";
     "G.59" -> "G.22";
     "G.122" -> "G.22";
     "G.123" -> "G.22";
     "G.127" -> "G.22";
     "G.132" -> "G.22";
     "G.133" -> "G.22";
     "G.134" -> "G.22";
     "G.246" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.129" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.133" -> "G.24";
     "G.28" -> "G.25";
     "G.43" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.123" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.43" -> "G.26";
     "G.45" -> "G.26";
     "G.98" -> "G.26";
     "G.102" -> "G.26";
     "G.134" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.48" -> "G.29";
     "G.98" -> "G.29";
     "G.31" -> "G.30";
     "G.48" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.98" -> "G.32";
     "G.108" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.40" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.59" -> "G.33";
     "G.98" -> "G.33";
     "G.37" -> "G.34";
     "G.98" -> "G.34";
     "G.108" -> "G.34";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.59" -> "G.36";
     "G.123" -> "G.36";
     "G.40" -> "G.37";
     "G.56" -> "G.37";
     "G.59" -> "G.37";
     "G.40" -> "G.38";
     "G.41" -> "G.40";
     "G.56" -> "G.40";
     "G.43" -> "G.41";
     "G.53" -> "G.41";
     "G.128" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.134" -> "G.48";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.59" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.59" -> "G.56";
     "G.59" -> "G.58";
     "G.123" -> "G.59";
     "G.131" -> "G.61";
     "G.108" -> "G.98";
     "G.108" -> "G.102";
     "G.129" -> "G.108";
     "G.123" -> "G.122";
     "G.134" -> "G.123";
     "G.128" -> "G.126";
     "G.128" -> "G.127";
     "G.129" -> "G.127";
     "G.133" -> "G.127";
     "G.129" -> "G.128";
     "G.133" -> "G.129";
     "G.133" -> "G.131";
     "G.134" -> "G.131";
     "G.246" -> "G.131";
     "G.133" -> "G.132";
     "G.134" -> "G.132";
     "G.246" -> "G.132";
     "G.134" -> "G.133";
     "G.246" -> "G.134";
     "G.170" -> "G.169";
     "G.176" -> "G.170";
     "G.246" -> "G.170";
     "G.246" -> "G.176";
   }

Required for
------------

:ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
