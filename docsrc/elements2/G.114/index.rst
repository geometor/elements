:order: 114
:number: 114
:canonical_id: G.114
:original_id: III.35
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, rectangle, equality
:dependencies: G.60, G.66, G.78
:excerpt: If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other.

.. _G.114:
.. _III.35:

G.114
=====

.. rubric:: `III.35 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/35/>`_

.. enunciation::

   If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other.

.. signature:: theorem

   | :fn:`circle_straight_lines_iii_35 <G.114>`\ ()
   | **prove** the rectangle contained by :g:`/ A E / <g1:/ A E />`, :g:`/ E C / <g1:/ E C />` is equal to the rectangle contained by :g:`/ D E / <g1:/ D E />`, :g:`/ E B / <g1:/ E B />`

.. picture:: g1.svg
   :alt: Proposition 35 Case 1 diagram

.. picture:: g2.svg
   :alt: Proposition 35 Case 2 diagram

.. step:: intersect

   In :g:`( A B C D ) <g1:( A B C D )>` let :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` cut one another at :g:`E <g1:E>`

.. step:: assert ∵ circle_radii <G.2>

   If now :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` are through the center, so that :g:`E <g1:E>` is the center of :g:`( A B C D ) <g1:( A B C D )>`, it is manifest that, :g:`/ A E / <g1:/ A E />`, :g:`/ E C / <g1:/ E C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E B / <g1:/ E B />` being :eq:`equal <g1:/ A E / = g1:/ E C / = g1:/ D E / = g1:/ E B />`, the rectangle contained by :g:`/ A E / <g1:/ A E />`, :g:`/ E C / <g1:/ E C />` is also equal to the rectangle contained by :g:`/ D E / <g1:/ D E />`, :g:`/ E B / <g1:/ E B />`.

.. step:: assert

   Next let :g:`/ A C / <g2:/ A C />`, :g:`/ D B / <g2:/ D B />` not be through the center

.. step:: construct

   Let the center of :g:`( A B C D ) <g2:( A B C D )>` be taken

.. step:: assert

   Let it be :g:`F <g2:F>`

.. step:: construct

   From :g:`F <g2:F>` let :g:`/ F G / <g2:/ F G />`, :g:`/ F H / <g2:/ F H />` be drawn perpendicular to :g:`/ A C / <g2:/ A C />`, :g:`/ D B / <g2:/ D B />`, and let :g:`/ F B / <g2:/ F B />`, :g:`/ F C / <g2:/ F C />`, :g:`/ F E / <g2:/ F E />` be joined.

.. step:: assert ∵ circle_straight_line <G.78>

   Since a straight line :g:`/ G F / <g2:/ G F />` through the center cuts a straight line :g:`/ A C / <g2:/ A C />` not through the center at right angles → it also bisects it;

.. step:: assert

   Therefore :g:`/ A G / <g2:/ A G />` is :eq:`equal <g2:/ A G / = g2:/ G C />` to :g:`/ G C / <g2:/ G C />`.

.. step:: assert ∵ difference_of_squares_equal_unequal <G.66>

   Since, then, :g:`/ A C / <g2:/ A C />` has been cut into equal parts at :g:`G <g2:G>` and into unequal parts at :g:`E <g2:E>`, the rectangle contained by :g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />` together with the square on :g:`/ E G / <g2:/ E G />` is equal to the square on :g:`/ G C / <g2:/ G C />`

.. step:: construct

   Let the square on :g:`/ G F / <g2:/ G F />` be added

.. step:: assert

   Therefore the rectangle :g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />` together with the squares on :g:`/ G E / <g2:/ G E />`, :g:`/ G F / <g2:/ G F />` is equal to the squares on :g:`/ C G / <g2:/ C G />`, :g:`/ G F / <g2:/ G F />`.

.. step:: assert ∵ pythagorean_theorem <G.60>

   The square on :g:`/ F E / <g2:/ F E />` is equal to the squares on :g:`/ E G / <g2:/ E G />`, :g:`/ G F / <g2:/ G F />`, and the square on :g:`/ F C / <g2:/ F C />` is equal to the squares on :g:`/ C G / <g2:/ C G />`, :g:`/ G F / <g2:/ G F />`

.. step:: assert

   Therefore the rectangle :g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />` together with the square on :g:`/ F E / <g2:/ F E />` is equal to the square on :g:`/ F C / <g2:/ F C />`.

.. step:: assert

   :g:`/ F C / <g2:/ F C />` is :eq:`equal <g2:/ F C / = g2:/ F B />` to :g:`/ F B / <g2:/ F B />`

.. step:: assert

   Therefore the rectangle :g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />` together with the square on :g:`/ E F / <g2:/ E F />` is equal to the square on :g:`/ F B / <g2:/ F B />`.

.. step:: assert

   The same reason, also, the rectangle :g:`/ D E / <g2:/ D E />`, :g:`/ E B / <g2:/ E B />` together with the square on :g:`/ F E / <g2:/ F E />` is equal to the square on :g:`/ F B / <g2:/ F B />`.

.. step:: assert

   The rectangle :g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />` together with the square on :g:`/ F E / <g2:/ F E />` was also proved equal to the square on :g:`/ F B / <g2:/ F B />`

.. step:: assert

   Therefore the rectangle :g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />` together with the square on :g:`/ F E / <g2:/ F E />` is equal to the rectangle :g:`/ D E / <g2:/ D E />`, :g:`/ E B / <g2:/ E B />` together with the square on :g:`/ F E / <g2:/ F E />`.

.. step:: construct

   Let the square on :g:`/ F E / <g2:/ F E />` be subtracted from each

.. step:: conclude

   Therefore the rectangle contained by :g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />` which remains is equal to the rectangle contained by :g:`/ D E / <g2:/ D E />`, :g:`/ E B / <g2:/ E B />`.

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
     "G.24" [label="G.24", tooltip="G.24 (I.14): If two rays at a point on a line on opposite sides make adjacent angles summing to two right angles, the two rays are collinear.", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.43): In any parallelogram, the complements of the parallelograms about the diagonal are equal in area.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.66" [label="G.66", tooltip="G.66 (II.5): If a straight line be cut into equal and unequal segments, the rectangle contained by the unequal segments of the whole together with the square on the straight line between the po...", fillcolor="#222244", URL="../G.66/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (III.3): If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects ...", fillcolor="#222244", URL="../G.78/index.html", target="_top"];
     "G.114" [label="G.114", tooltip="G.114 (III.35): If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the rectangle contained by the segments of the other.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
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
     "G.24" -> "G.6";
     "G.25" -> "G.6";
     "G.48" -> "G.6";
     "G.56" -> "G.6";
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
     "G.37" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.78" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.78" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.78" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.56" -> "G.21";
     "G.60" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.60" -> "G.24";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.47" -> "G.37";
     "G.78" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.66" -> "G.44";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.56" -> "G.47";
     "G.59" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.66" -> "G.49";
     "G.54" -> "G.50";
     "G.60" -> "G.54";
     "G.66" -> "G.56";
     "G.60" -> "G.59";
     "G.66" -> "G.59";
     "G.114" -> "G.60";
     "G.114" -> "G.66";
     "G.114" -> "G.78";
   }

.. toctree::
   :hidden:

   code
   heath
