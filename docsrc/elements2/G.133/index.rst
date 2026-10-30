:order: 133
:number: 133
:canonical_id: G.133
:original_id: IV.15
:volume: II
:book: IV
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles, polygons
:category: problem, construction, plane-geometry, circles, polygons
:tags: book-iv, point, segment, circle, angle, triangle, polygon, equilateral, inscribed, hexagon, equality, porism
:dependencies: G.12, G.25, G.45, G.105, G.106, G.108
:excerpt: Inscribe in a given circle an equilateral and equiangular hexagon.

.. _G.133:
.. _IV.15:

G.133
=====

.. rubric:: `IV.15 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/15/>`_

.. enunciation::

   Inscribe in a given circle an equilateral and equiangular hexagon.

.. signature:: problem

   | :fn:`inscribe_hexagon_in_circle <G.133>`\ (:g:`( A B C D E F ) <g1:( A B C D E F )>`) → :g:`/ G E / <g1:/ G E />`
   | **given** :g:`( A B C D E F ) <g1:( A B C D E F )>`
   | **construct** the hexagon $ABCDEF$ is :eq:`equilateral <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E F / = g1:/ F A />` and equiangular

.. picture:: g1.svg
   :alt: Book IV Proposition 15: Regular hexagon :g:`< A B C D E F > <g1:< A B C D E F >>` inscribed in circle with auxiliary circle EGCH

.. step:: given

   :g:`( A B C D E F ) <g1:( A B C D E F )>`

.. step:: construct

   Let the diameter :g:`/ A D / <g1:/ A D />` of :g:`( A B C D E F ) <g1:( A B C D E F )>` be drawn

.. step:: construct

   Let the center :g:`G <g1:G>` of the circle be taken

.. step:: construct

   :fn:`circle <G.4>`\ (:g:`D <g1:D>`, :g:`/ G D / <g1:/ G D />`) → :g:`( E G C H ) <g1:( E G C H )>`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`G <g1:G>`, :g:`E <g1:E>`) → :g:`/ G E / <g1:/ G E />`, :fn:`segment <G.3>`\ (:g:`G <g1:G>`, :g:`C <g1:C>`) → :g:`/ G C / <g1:/ G C />`, :fn:`segment <G.3>`\ () → :g:`B <g1:B>`, :fn:`segment <G.3>`\ () → :g:`F <g1:F>`, :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`, :fn:`segment <G.3>`\ (:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`, :fn:`segment <G.3>`\ (:g:`C <g1:C>`, :g:`D <g1:D>`) → :g:`/ C D / <g1:/ C D />`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`/ D E / <g1:/ D E />`, :fn:`segment <G.3>`\ (:g:`E <g1:E>`, :g:`F <g1:F>`) → :g:`/ E F / <g1:/ E F />`, :fn:`segment <G.3>`\ (:g:`F <g1:F>`, :g:`A <g1:A>`) → :g:`/ F A / <g1:/ F A />`

.. step:: assert ∵ circle_radii <G.2>

   Since :g:`G <g1:G>` is the center of :g:`( A B C D E F ) <g1:( A B C D E F )>` → :g:`/ G E / <g1:/ G E />` is :eq:`equal <g1:/ G E / = g1:/ G D />` to :g:`/ G D / <g1:/ G D />`.

.. step:: assert ∵ circle_radii <G.2>

   Since :g:`D <g1:D>` is the center of :g:`( G C H ) <g1:( G C H )>` → :g:`/ D E / <g1:/ D E />` is :eq:`equal <g1:/ D E / = g1:/ G D />` to :g:`/ G D / <g1:/ G D />`.

.. step:: assert

   :g:`/ G E / <g1:/ G E />` was proved :eq:`equal <g1:/ G E / = g1:/ G D />` to :g:`/ G D / <g1:/ G D />`

.. step:: assert

   Therefore :g:`/ G E / <g1:/ G E />` is also :eq:`equal <g1:/ G E / = g1:/ D E />` to :g:`/ D E / <g1:/ D E />`;

.. step:: assert

   Therefore :g:`< E G D > <g1:< E G D >>` is :eq:`equilateral <g1:/ G E / = g1:/ G D / = g1:/ D E />`;

.. step:: assert ∵ isosceles_base_angles <G.12>

   And therefore its three angles :g:`< E G D ) <g1:< E G D )>`, :g:`< G D E ) <g1:< G D E )>`, :g:`< D E G ) <g1:< D E G )>` are :eq:`equal <g1:< E G D ) = g1:< G D E ) = g1:< D E G )>` to one another, inasmuch as, in isosceles triangles, the angles at the base are equal to one another.

.. step:: assert ∵ triangle_angle_sum <G.45>

   The three angles of the triangle are equal to two right angles

.. step:: assert

   Therefore :g:`< E G D ) <g1:< E G D )>` is one-third of two right angles.

.. step:: assert

   Similarly, :g:`< D G C ) <g1:< D G C )>` can also be proved to be one-third of two right angles.

.. step:: assert

   And, since :g:`/ G C / <g1:/ G C />` standing on :g:`/ B E / <g1:/ B E />` makes the adjacent angles :g:`< E G C ) <g1:< E G C )>`, :g:`< C G B ) <g1:< C G B )>` equal to two right angles,

.. step:: assert

   Therefore the remaining angle :g:`< C G B ) <g1:< C G B )>` is also one-third of two right angles.

.. step:: assert

   Therefore :g:`< E G D ) <g1:< E G D )>`, :g:`< D G C ) <g1:< D G C )>`, :g:`< C G B ) <g1:< C G B )>` are :eq:`equal <g1:< E G D ) = g1:< D G C ) = g1:< C G B )>` to one another

.. step:: assert ∵ vertical_angles_equal <G.25>

   So that the angles vertical to them, :g:`< B G A ) <g1:< B G A )>`, :g:`< A G F ) <g1:< A G F )>`, :g:`< F G E ) <g1:< F G E )>` are :eq:`equal <g1:< B G A ) = g1:< A G F ) = g1:< F G E )>`.

.. step:: assert

   Therefore the six angles :g:`< E G D ) <g1:< E G D )>`, :g:`< D G C ) <g1:< D G C )>`, :g:`< C G B ) <g1:< C G B )>`, :g:`< B G A ) <g1:< B G A )>`, :g:`< A G F ) <g1:< A G F )>`, :g:`< F G E ) <g1:< F G E )>` are :eq:`equal <g1:< E G D ) = g1:< D G C ) = g1:< C G B ) = g1:< B G A ) = g1:< A G F ) = g1:< F G E )>` to one another.

.. step:: assert ∵ equal_circles_equal <G.105>

   Equal angles stand on equal circumferences

.. step:: assert

   Therefore the six circumferences :g:`( A B ) <g1:( A B )>`, :g:`( B C ) <g1:( B C )>`, :g:`( C D ) <g1:( C D )>`, :g:`( D E ) <g1:( D E )>`, :g:`( E F ) <g1:( E F )>`, :g:`( F A ) <g1:( F A )>` are :eq:`equal <g1:( A B ) = g1:( B C ) = g1:( C D ) = g1:( D E ) = g1:( E F ) = g1:( F A )>` to one another.

.. step:: assert ∵ equal_circles_equal_iii_29 <G.108>

   Equal circumferences are subtended by equal straight lines

.. step:: assert

   Therefore the six straight lines are :eq:`equal <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E F / = g1:/ F A />` to one another;

.. step:: assert

   Therefore the hexagon :g:`< A B C D E F > <g1:< A B C D E F >>` is :eq:`equilateral <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E F / = g1:/ F A />`.

.. step:: assert

   I say next that it is also equiangular.

.. step:: assert

   Since the circumference :g:`( F A ) <g1:( F A )>` is :eq:`equal <g1:( F A ) = g1:( D E )>` to the circumference :g:`( D E ) <g1:( D E )>` → let the circumference :g:`( A B C D ) <g1:( A B C D )>` be added to each;

.. step:: assert

   Therefore the whole :g:`( F A B C D ) <g1:( F A B C D )>` is :eq:`equal <g1:( F A B C D ) = g1:( E D C B A )>` to the whole :g:`( E D C B A ) <g1:( E D C B A )>`;

.. step:: assert

   And :g:`< F E D ) <g1:< F E D )>` stands on the circumference :g:`( F A B C D ) <g1:( F A B C D )>`, and :g:`< A F E ) <g1:< A F E )>` on the circumference :g:`( E D C B A ) <g1:( E D C B A )>`

.. step:: assert ∵ equal_circles_angles <G.106>

   Therefore :g:`< A F E ) <g1:< A F E )>` is :eq:`equal <g1:< A F E ) = g1:< D E F )>` to :g:`< D E F ) <g1:< D E F )>`.

.. step:: assert

   Similarly it can be proved that the remaining angles of the hexagon :g:`< A B C D E F > <g1:< A B C D E F >>` are also severally equal to each of :g:`< A F E ) <g1:< A F E )>`, :g:`< F E D ) <g1:< F E D )>`

.. step:: assert

   Therefore the hexagon :g:`< A B C D E F > <g1:< A B C D E F >>` is equiangular.

.. step:: assert

   It was also proved :eq:`equilateral <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E F / = g1:/ F A />`, and it has been inscribed in :g:`( A B C D E F ) <g1:( A B C D E F )>`.

.. step:: assert

   And, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents to the circle, there will be circumscribed about the circle an equilateral and equiangular hexagon in conformity with what was explained in the case of the pentagon.

.. step:: conclude

   Further by means similar to those explained in the case of the pentagon we can both inscribe a circle in a given hexagon and circumscribe one about it.

.. porism::

   From this it is manifest that the side of the
   hexagon is equal to the radius of the circle.

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
     "G.33" [label="G.33", tooltip="G.33 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.85/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.20): In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.101" [label="G.101", tooltip="G.101 (III.def.11): Similar segments of circles are those which admit equal angles, or in which the angles are equal.", fillcolor="#224422", URL="../G.101/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.24): Similar segments of circles on equal straight lines are equal.", fillcolor="#222244", URL="../G.103/index.html", target="_top"];
     "G.105" [label="G.105", tooltip="G.105 (III.26): In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.105/index.html", target="_top"];
     "G.106" [label="G.106", tooltip="G.106 (III.27): In equal circles angles standing on equal circumferences are equal, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.106/index.html", target="_top"];
     "G.108" [label="G.108", tooltip="G.108 (III.29): In equal circles equal circumferences are subtended by equal straight lines.", fillcolor="#222244", URL="../G.108/index.html", target="_top"];
     "G.133" [label="G.133", tooltip="G.133 (IV.15): Inscribe in a given circle an equilateral and equiangular hexagon.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.80" -> "G.2";
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
     "G.105" -> "G.11";
     "G.108" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.98" -> "G.12";
     "G.133" -> "G.12";
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
     "G.42" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.133" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.106" -> "G.34";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.45" -> "G.42";
     "G.45" -> "G.44";
     "G.98" -> "G.45";
     "G.133" -> "G.45";
     "G.85" -> "G.76";
     "G.85" -> "G.80";
     "G.103" -> "G.85";
     "G.106" -> "G.98";
     "G.105" -> "G.101";
     "G.105" -> "G.103";
     "G.106" -> "G.105";
     "G.133" -> "G.105";
     "G.108" -> "G.106";
     "G.133" -> "G.106";
     "G.133" -> "G.108";
   }

Required for
------------

:ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.519 <G.519>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
