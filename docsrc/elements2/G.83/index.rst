:order: 83
:number: 83
:canonical_id: G.83
:original_id: III.8
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, triangle, arc, equality, reductio-ad-absurdum
:dependencies: G.11, G.31, G.32, G.35, G.76
:excerpt: If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, of the straight lines which fall on the concave circumference, that through the centre is greatest, while of the rest the nearer to that through the centre is always greater than the more remote, but, of the straight lines falling on the convex circumference, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal straight lines will fall on the circle from the point, one on each side of the least.

.. _G.83:
.. _III.8:

G.83
====

.. rubric:: `III.8 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/08/>`_

.. enunciation::

   If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, of the straight lines which fall on the concave circumference, that through the centre is greatest, while of the rest the nearer to that through the centre is always greater than the more remote, but, of the straight lines falling on the convex circumference, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal straight lines will fall on the circle from the point, one on each side of the least.

.. signature:: theorem

   | :fn:`point_taken_outside <G.83>`\ ()
   | **prove** no other straight line equal to :g:`/ D K / <g1:/ D K />` will fall on the circle from :g:`D <g1:D>`

.. picture:: g1.svg
   :alt: Diagram for Proposition 8

.. step:: construct

   Let :g:`( A B C ) <g1:( A B C )>` be a circle, and let a point :g:`D <g1:D>` be taken outside :g:`( A B C ) <g1:( A B C )>`

.. step:: construct

   Let there be drawn through from it straight lines :g:`/ D A / <g1:/ D A />`, :g:`/ D E / <g1:/ D E />`, :g:`/ D F / <g1:/ D F />`, :g:`/ D C / <g1:/ D C />`, and let :g:`/ D A / <g1:/ D A />` be through the center

.. step:: assert

   I say that, of the straight lines falling on the concave circumference :g:`( A E F C ) <g1:( A E F C )>`, :g:`/ D A / <g1:/ D A />` through the center is greatest, while :g:`/ D E / <g1:/ D E />` is greater than :g:`/ D F / <g1:/ D F />` and :g:`/ D F / <g1:/ D F />` than :g:`/ D C / <g1:/ D C />`

.. step:: assert

   But, of the straight lines falling on the convex circumference :g:`( H L K G ) <g1:( H L K G )>`, :g:`/ D G / <g1:/ D G />` between the point and the diameter :g:`/ A G / <g1:/ A G />` is least

.. step:: assert

   And the nearer to the least :g:`/ D G / <g1:/ D G />` is always less than the more remote, namely :g:`/ D K / <g1:/ D K />` than :g:`/ D L / <g1:/ D L />`, and :g:`/ D L / <g1:/ D L />` than :g:`/ D H / <g1:/ D H />`.

.. step:: construct

   :fn:`find_circle_center <G.76>`: Let the center of :g:`( A B C ) <g1:( A B C )>` be taken

.. step:: assert

   Let it be :g:`M <g1:M>`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`M <g1:M>`, :g:`E <g1:E>`) → :g:`/ M E / <g1:/ M E />`, :fn:`segment <G.3>`\ (:g:`M <g1:M>`, :g:`F <g1:F>`) → :g:`/ M F / <g1:/ M F />`, :fn:`segment <G.3>`\ (:g:`M <g1:M>`, :g:`C <g1:C>`) → :g:`/ M C / <g1:/ M C />`, :fn:`segment <G.3>`\ (:g:`M <g1:M>`, :g:`K <g1:K>`) → :g:`/ M K / <g1:/ M K />`, :fn:`segment <G.3>`\ (:g:`M <g1:M>`, :g:`L <g1:L>`) → :g:`/ M L / <g1:/ M L />`, :fn:`segment <G.3>`\ (:g:`M <g1:M>`, :g:`H <g1:H>`) → :g:`/ M H / <g1:/ M H />`

.. step:: construct

   Since :g:`/ A M / <g1:/ A M />` is :eq:`equal <g1:/ A M / = g1:/ E M />` to :g:`/ E M / <g1:/ E M />`, let :g:`/ M D / <g1:/ M D />` be added to each

.. step:: assert

   Therefore :g:`/ A D / <g1:/ A D />` is equal to :g:`/ E M / <g1:/ E M />`, :g:`/ M D / <g1:/ M D />`.

.. step:: assert ∵ triangle_inequality <G.31>

   :g:`/ E M / <g1:/ E M />`, :g:`/ M D / <g1:/ M D />` are greater than :g:`/ E D / <g1:/ E D />`

.. step:: assert

   Therefore :g:`/ A D / <g1:/ A D />` is also greater than :g:`/ E D / <g1:/ E D />`.

.. step:: assert

   Since :g:`/ M E / <g1:/ M E />` is :eq:`equal <g1:/ M E / = g1:/ M F />` to :g:`/ M F / <g1:/ M F />`, and :g:`/ M D / <g1:/ M D />` is common, therefore :g:`/ E M / <g1:/ E M />`, :g:`/ M D / <g1:/ M D />` are :eq:`equal <g1:/ E M / = g1:/ F M />` to :g:`/ F M / <g1:/ F M />`, :g:`/ M D / <g1:/ M D />`

.. step:: assert

   And :g:`< E M D ) <g1:< E M D )>` is greater than :g:`< F M D ) <g1:< F M D )>`

.. step:: assert ∵ hinge_theorem <G.35>

   Therefore the base :g:`/ E D / <g1:/ E D />` is greater than the base :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   Similarly we can prove that :g:`/ F D / <g1:/ F D />` is greater than :g:`/ C D / <g1:/ C D />`

.. step:: assert

   Therefore :g:`/ D A / <g1:/ D A />` is greatest, while :g:`/ D E / <g1:/ D E />` is greater than :g:`/ D F / <g1:/ D F />`, and :g:`/ D F / <g1:/ D F />` than :g:`/ D C / <g1:/ D C />`.

.. step:: assert ∵ triangle_inequality <G.31>

   Next, since :g:`/ M K / <g1:/ M K />`, :g:`/ K D / <g1:/ K D />` are greater than :g:`/ M D / <g1:/ M D />`.

.. step:: assert

   And :g:`/ M G / <g1:/ M G />` is :eq:`equal <g1:/ M G / = g1:/ M K />` to :g:`/ M K / <g1:/ M K />`, therefore the remainder :g:`/ K D / <g1:/ K D />` is greater than the remainder :g:`/ G D / <g1:/ G D />`,

.. step:: assert

   So that :g:`/ G D / <g1:/ G D />` is less than :g:`/ K D / <g1:/ K D />`.

.. step:: assert ∵ interior_triangle_bounds <G.32>

   And, since on :g:`/ M D / <g1:/ M D />`, one of the sides of :g:`< M L D > <g1:< M L D >>`, two straight lines :g:`/ M K / <g1:/ M K />`, :g:`/ K D / <g1:/ K D />` were constructed meeting within the triangle, therefore :g:`/ M K / <g1:/ M K />`, :g:`/ K D / <g1:/ K D />` are less than :g:`/ M L / <g1:/ M L />`, :g:`/ L D / <g1:/ L D />`

.. step:: assert

   And :g:`/ M K / <g1:/ M K />` is :eq:`equal <g1:/ M K / = g1:/ M L />` to :g:`/ M L / <g1:/ M L />`

.. step:: assert

   Therefore the remainder :g:`/ D K / <g1:/ D K />` is less than the remainder :g:`/ D L / <g1:/ D L />`.

.. step:: assert

   Similarly we can prove that :g:`/ D L / <g1:/ D L />` is also less than :g:`/ D H / <g1:/ D H />`

.. step:: assert

   Therefore :g:`/ D G / <g1:/ D G />` is least, while :g:`/ D K / <g1:/ D K />` is less than :g:`/ D L / <g1:/ D L />`, and :g:`/ D L / <g1:/ D L />` than :g:`/ D H / <g1:/ D H />`.

.. step:: assert

   I say also that only two equal straight lines will fall from :g:`D <g1:D>` on the circle, one on each side of the least :g:`/ D G / <g1:/ D G />`.

.. step:: construct

   :fn:`copy_angle <G.34>`\ (:g:`/ M D / <g1:/ M D />`, :g:`M <g1:M>`, :g:`< K M D ) <g1:< K M D )>`) → :g:`< D M B ) <g1:< D M B )>` (:eq:`equal <g1:< D M B ) = g1:< K M D )>`)

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`

.. step:: assert

   Since :g:`/ M K / <g1:/ M K />` is :eq:`equal <g1:/ M K / = g1:/ M B />` to :g:`/ M B / <g1:/ M B />`, and :g:`/ M D / <g1:/ M D />` is common → the two sides :g:`/ K M / <g1:/ K M />`, :g:`/ M D / <g1:/ M D />` are :eq:`equal <g1:/ K M / = g1:/ B M />` to the two sides :g:`/ B M / <g1:/ B M />`, :g:`/ M D / <g1:/ M D />` respectively;

.. step:: assert

   And :g:`< K M D ) <g1:< K M D )>` is :eq:`equal <g1:< K M D ) = g1:< B M D )>` to :g:`< B M D ) <g1:< B M D )>`

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ D K / <g1:/ D K />` is :eq:`equal <g1:/ D K / = g1:/ D B />` to the base :g:`/ D B / <g1:/ D B />`.

.. step:: assert

   If possible, let a straight line so fall, and let it be :g:`/ D N / <g1:/ D N />`

.. step:: assert

   Since :g:`/ D K / <g1:/ D K />` is :eq:`equal <g1:/ D K / = g1:/ D N />` to :g:`/ D N / <g1:/ D N />`, while :g:`/ D K / <g1:/ D K />` is :eq:`equal <g1:/ D K / = g1:/ D B />` to :g:`/ D B / <g1:/ D B />` → :g:`/ D B / <g1:/ D B />` is also :eq:`equal <g1:/ D B / = g1:/ D N />` to :g:`/ D N / <g1:/ D N />`,

.. step:: assert

   That is, the nearer to the least :g:`/ D G / <g1:/ D G />` equal to the more remote: which was proved impossible.

.. step:: conclude

   Therefore no more than two equal straight lines will fall on :g:`( A B C ) <g1:( A B C )>` from :g:`D <g1:D>`, one on each side of :g:`/ D G / <g1:/ D G />` the least.

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
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.21): Segments constructed from the endpoints of one side of a triangle to an interior point have a lesser sum but contain a greater angle than the other two sides.", fillcolor="#222244", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.24): If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.83" [label="G.83", tooltip="G.83 (III.8): If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.27" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.8" -> "G.6";
     "G.25" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.27" -> "G.7";
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
     "G.35" -> "G.11";
     "G.83" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.35" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.76" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.76" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.32" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.35" -> "G.30";
     "G.32" -> "G.31";
     "G.33" -> "G.31";
     "G.83" -> "G.31";
     "G.83" -> "G.32";
     "G.34" -> "G.33";
     "G.35" -> "G.34";
     "G.83" -> "G.35";
     "G.83" -> "G.76";
   }

.. toctree::
   :hidden:

   code
   heath
