:order: 106
:number: 106
:canonical_id: G.106
:original_id: III.8
:title: G.106 point taken outside
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, triangle, straight-line, centre, diameter, plane-angle, trilateral, arc, equality, reductio-ad-absurdum
:dependencies: G.1, G.4, G.10, G.11, G.12, G.14, G.24, G.45, G.46, G.48, G.49, G.61, G.98
:excerpt: If a point be taken outside a circle and from the point segments be drawn through to the circle, one of which is through the center and the others are drawn at random, then, of the segments which fall on the concave arc, that through the center is greatest, while of the rest the nearer to that through the center is always greater than the more remote, but, of the segments falling on the convex arc, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal segments will fall on the circle from the point, one on each side of the least.

.. _G.106:
.. _III.8:

G.106 point taken outside
=========================

.. rubric:: `III.8 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/08/>`_

.. enunciation::

   If a :term:`point <G.1>` be taken outside a :term:`circle <G.10>` and from the point :term:`segments <G.4>` be drawn through to the circle, one of which is through the :term:`center <G.11>` and the others are drawn at random, then, of the segments which fall on the concave arc, that through the center is greatest, while of the rest the nearer to that through the center is always greater than the more remote, but, of the segments falling on the convex arc, that between the point and the :term:`diameter <G.61>` is least, while of the rest the nearer to the least is always less than the more remote, and only two equal segments will fall on the circle from the point, one on each side of the least.

.. signature:: theorem

   | :fn:`point_taken_outside <G.106>`\ ()
   | **prove** no other segment equal to :g:`/ D K / <g1:/ D K />` will fall on the circle from :g:`D <g1:D>`

.. picture:: g1.svg
   :alt: Diagram for Proposition 8

.. step:: construct

   Let :g:`( A B C ) <g1:( A B C )>` be a circle, and let a point :g:`D <g1:D>` be taken outside :g:`( A B C ) <g1:( A B C )>`

.. step:: construct

   Let there be drawn through from it segments :g:`/ D A / <g1:/ D A />`, :g:`/ D E / <g1:/ D E />`, :g:`/ D F / <g1:/ D F />`, :g:`/ D C / <g1:/ D C />`, and let :g:`/ D A / <g1:/ D A />` be through the center

.. step:: assert

   I say that, of the segments falling on the concave arc :g:`( A E F C ) <g1:( A E F C )>`, :g:`/ D A / <g1:/ D A />` through the center is greatest, while :g:`/ D E / <g1:/ D E />` > :g:`/ D F / <g1:/ D F />` and :g:`/ D F / <g1:/ D F />` than :g:`/ D C / <g1:/ D C />`

.. step:: assert

   But, of the segments falling on the convex arc :g:`( H L K G ) <g1:( H L K G )>`, :g:`/ D G / <g1:/ D G />` between the point and the diameter :g:`/ A G / <g1:/ A G />` is least

.. step:: assert

   the nearer to the least :g:`/ D G / <g1:/ D G />` is always less than the more remote, namely :g:`/ D K / <g1:/ D K />` than :g:`/ D L / <g1:/ D L />`, and :g:`/ D L / <g1:/ D L />` than :g:`/ D H / <g1:/ D H />`

.. step:: construct

   :fn:`find_circle_center <G.98>`: Let the center of :g:`( A B C ) <g1:( A B C )>` be taken

.. step:: assert

   Let it be :g:`M <g1:M>`

.. step:: construct

   :fn:`segment <G.14>`\ (:g:`M <g1:M>`, :g:`E <g1:E>`) → :g:`/ M E / <g1:/ M E />`, :fn:`segment <G.14>`\ (:g:`M <g1:M>`, :g:`F <g1:F>`) → :g:`/ M F / <g1:/ M F />`, :fn:`segment <G.14>`\ (:g:`M <g1:M>`, :g:`C <g1:C>`) → :g:`/ M C / <g1:/ M C />`, :fn:`segment <G.14>`\ (:g:`M <g1:M>`, :g:`K <g1:K>`) → :g:`/ M K / <g1:/ M K />`, :fn:`segment <G.14>`\ (:g:`M <g1:M>`, :g:`L <g1:L>`) → :g:`/ M L / <g1:/ M L />`, :fn:`segment <G.14>`\ (:g:`M <g1:M>`, :g:`H <g1:H>`) → :g:`/ M H / <g1:/ M H />`

.. step:: construct

   Since :g:`/ A M / <g1:/ A M />` is :eq:`equal <g1:/ A M / = g1:/ E M />` to :g:`/ E M / <g1:/ E M />`, let :g:`/ M D / <g1:/ M D />` be added to each

.. step:: assert

   :g:`/ A D / <g1:/ A D />` is equal to :g:`/ E M / <g1:/ E M />`, :g:`/ M D / <g1:/ M D />`

.. step:: assert ∵ triangle_inequality <G.45>

   :g:`/ E M / <g1:/ E M />`, :g:`/ M D / <g1:/ M D />` are greater than :g:`/ E D / <g1:/ E D />`

.. step:: assert

   :g:`/ A D / <g1:/ A D />` is also greater than :g:`/ E D / <g1:/ E D />`

.. step:: assert

   :g:`/ M E / <g1:/ M E />` :eq:`= <g1:/ M E / = g1:/ M F />` :g:`/ M F / <g1:/ M F />`, and :g:`/ M D / <g1:/ M D />` is common, therefore :g:`/ E M / <g1:/ E M />`, :g:`/ M D / <g1:/ M D />` :eq:`= <g1:/ E M / = g1:/ F M />` :g:`/ F M / <g1:/ F M />`, :g:`/ M D / <g1:/ M D />`

.. step:: assert

   :g:`< E M D ) <g1:< E M D )>` > :g:`< F M D ) <g1:< F M D )>`

.. step:: assert ∵ hinge_theorem <G.49>

   :g:`/ E D / <g1:/ E D />` > :g:`/ F D / <g1:/ F D />`

.. step:: assert

   Similarly we can prove that :g:`/ F D / <g1:/ F D />` > :g:`/ C D / <g1:/ C D />`

.. step:: assert

   :g:`/ D A / <g1:/ D A />` is greatest, while :g:`/ D E / <g1:/ D E />` > :g:`/ D F / <g1:/ D F />`, and :g:`/ D F / <g1:/ D F />` than :g:`/ D C / <g1:/ D C />`

.. step:: assert ∵ triangle_inequality <G.45>

   Next, since :g:`/ M K / <g1:/ M K />`, :g:`/ K D / <g1:/ K D />` are greater than :g:`/ M D / <g1:/ M D />`

.. step:: assert

   :g:`/ M G / <g1:/ M G />` :eq:`= <g1:/ M G / = g1:/ M K />` :g:`/ M K / <g1:/ M K />`, therefore :g:`/ K D / <g1:/ K D />` > :g:`/ G D / <g1:/ G D />`,

.. step:: assert

   So that :g:`/ G D / <g1:/ G D />` < :g:`/ K D / <g1:/ K D />`

.. step:: assert ∵ interior_triangle_bounds <G.46>

   since on :g:`/ M D / <g1:/ M D />`, one of the sides of :g:`< M L D > <g1:< M L D >>`, two segments :g:`/ M K / <g1:/ M K />`, :g:`/ K D / <g1:/ K D />` were constructed meeting within the :term:`triangle <G.12>`, therefore :g:`/ M K / <g1:/ M K />`, :g:`/ K D / <g1:/ K D />` are less than :g:`/ M L / <g1:/ M L />`, :g:`/ L D / <g1:/ L D />`

.. step:: assert

   :g:`/ M K / <g1:/ M K />` :eq:`= <g1:/ M K / = g1:/ M L />` :g:`/ M L / <g1:/ M L />`

.. step:: assert

   :g:`/ D K / <g1:/ D K />` < :g:`/ D L / <g1:/ D L />`

.. step:: assert

   Similarly we can prove that :g:`/ D L / <g1:/ D L />` is also less than :g:`/ D H / <g1:/ D H />`

.. step:: assert

   :g:`/ D G / <g1:/ D G />` is least, while :g:`/ D K / <g1:/ D K />` < :g:`/ D L / <g1:/ D L />`, and :g:`/ D L / <g1:/ D L />` than :g:`/ D H / <g1:/ D H />`

.. step:: assert

   I say also that only two equal segments will fall from :g:`D <g1:D>` on the circle, one on each side of the least :g:`/ D G / <g1:/ D G />`

.. step:: construct

   :fn:`copy_angle <G.48>`\ (:g:`/ M D / <g1:/ M D />`, :g:`M <g1:M>`, :g:`< K M D ) <g1:< K M D )>`) → :g:`< D M B ) <g1:< D M B )>` (:eq:`equal <g1:< D M B ) = g1:< K M D )>`)

.. step:: construct

   :fn:`segment <G.14>`\ (:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`

.. step:: assert

   :g:`/ M K / <g1:/ M K />` :eq:`= <g1:/ M K / = g1:/ M B />` :g:`/ M B / <g1:/ M B />`, and :g:`/ M D / <g1:/ M D />` is common → :g:`/ K M / <g1:/ K M />`, :g:`/ M D / <g1:/ M D />` :eq:`= <g1:/ K M / = g1:/ B M />` :g:`/ B M / <g1:/ B M />`, :g:`/ M D / <g1:/ M D />`

.. step:: assert

   :g:`< K M D ) <g1:< K M D )>` :eq:`= <g1:< K M D ) = g1:< B M D )>` :g:`< B M D ) <g1:< B M D )>`

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ D K / <g1:/ D K />` :eq:`= <g1:/ D K / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`

.. step:: assert

   If possible, let a segment so fall, and let it be :g:`/ D N / <g1:/ D N />`

.. step:: assert

   :g:`/ D K / <g1:/ D K />` :eq:`= <g1:/ D K / = g1:/ D N />` :g:`/ D N / <g1:/ D N />`, while :g:`/ D K / <g1:/ D K />` :eq:`= <g1:/ D K / = g1:/ D B />` :g:`/ D B / <g1:/ D B />` → :g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D B / = g1:/ D N />` :g:`/ D N / <g1:/ D N />`,

.. step:: assert

   That is, the nearer to the least :g:`/ D G / <g1:/ D G />` equal to the more remote: which was proved impossible

.. step:: conclude

   no more than two equal segments will fall on :g:`( A B C ) <g1:( A B C )>` from :g:`D <g1:D>`, one on each side of :g:`/ D G / <g1:/ D G />` the least

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
     "G.46" [label="G.46", tooltip="G.46 (I.21): Segments constructed from the endpoints of one side of a triangle to an interior point have a lesser sum but contain a greater angle than the other two sides.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.24): If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.106" [label="G.106", tooltip="G.106 (III.8): If a point be taken outside a circle and from the point segments be drawn through to the circle, one of which is through the center and the others are drawn at random, then, of the...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.46" -> "G.1";
     "G.47" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.98" -> "G.1";
     "G.106" -> "G.1";
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
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.46" -> "G.3";
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
     "G.46" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.49" -> "G.4";
     "G.61" -> "G.4";
     "G.98" -> "G.4";
     "G.106" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.98" -> "G.10";
     "G.106" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
     "G.98" -> "G.11";
     "G.106" -> "G.11";
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
     "G.46" -> "G.12";
     "G.47" -> "G.12";
     "G.48" -> "G.12";
     "G.49" -> "G.12";
     "G.106" -> "G.12";
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
     "G.49" -> "G.14";
     "G.106" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.47" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.40" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.45" -> "G.18";
     "G.46" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.40" -> "G.19";
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
     "G.46" -> "G.22";
     "G.48" -> "G.22";
     "G.49" -> "G.22";
     "G.98" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.49" -> "G.24";
     "G.106" -> "G.24";
     "G.28" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.49" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.45" -> "G.26";
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
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.40" -> "G.33";
     "G.98" -> "G.33";
     "G.37" -> "G.34";
     "G.37" -> "G.36";
     "G.40" -> "G.37";
     "G.40" -> "G.38";
     "G.41" -> "G.40";
     "G.43" -> "G.41";
     "G.46" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.49" -> "G.44";
     "G.46" -> "G.45";
     "G.47" -> "G.45";
     "G.106" -> "G.45";
     "G.106" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.48";
     "G.106" -> "G.48";
     "G.106" -> "G.49";
     "G.106" -> "G.61";
     "G.106" -> "G.98";
   }

.. toctree::
   :hidden:

   code
   heath
