:order: 71
:number: 71
:canonical_id: G.71
:original_id: II.10
:volume: I
:book: II
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, geometric-algebra
:category: theorem, proof, plane-geometry, geometric-algebra
:tags: book-ii, point, segment, angle, square, bisect, equality
:dependencies: G.1, G.9, G.12, G.13, G.19, G.25, G.41, G.42, G.44, G.45, G.47, G.60
:excerpt: If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

.. _G.71:
.. _II.10:

G.71
====

.. rubric:: `II.10 <https://geometor.github.io/euclid/heath/volume_I/book_ii/propositions/10/>`_

.. enunciation::

   If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

.. picture:: g1.svg
   :alt: 0409.g1

.. step:: assert

   For let a straight line :g:`/ A B / <g1:/ A B />` be :eq:`bisected <g1:/ A C / = g1:/ C B />` at :g:`C <g1:C>`

.. step:: assert

   Let a straight line :g:`/ B D / <g1:/ B D />` be added to it in a straight line

.. step:: construct [G.19] <G.19>

   For let :g:`/ C E / <g1:/ C E />` be drawn from :g:`C <g1:C>` at right angles to :g:`/ A B / <g1:/ A B />`

.. step:: construct [G.9] <G.9>

   Let it be made :eq:`equal <g1:/ C E / = g1:/ A C / = g1:/ C B />` to either :g:`/ A C / <g1:/ A C />` or :g:`/ C B / <g1:/ C B />`

.. step:: construct

   **segment** :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />`

.. step:: construct

   Through :g:`E <g1:E>` let :g:`/ E F / <g1:/ E F />` be drawn parallel to :g:`/ A D / <g1:/ A D />`

.. step:: construct [G.44] <G.44>

   Through :g:`D <g1:D>` let :g:`/ F D / <g1:/ F D />` be drawn parallel to :g:`/ C E / <g1:/ C E />`.

.. step:: assert [G.42] <G.42>

   Since a straight line :g:`/ E F / <g1:/ E F />` falls on the parallel straight lines :g:`/ E C / <g1:/ E C />`, :g:`/ F D / <g1:/ F D />`, :g:`< C E F ) <g1:< C E F )>`, :g:`< E F D ) <g1:< E F D )>` are equal to two right angles

.. step:: assert

   Therefore :g:`< F E B ) <g1:< F E B )>`, :g:`< E F D ) <g1:< E F D )>` are less than two right angles.

.. step:: assert [G.41] <G.41>

   Straight lines produced from angles less than two right angles meet

.. step:: assert

   Therefore :g:`/ E B / <g1:/ E B />`, :g:`/ F D / <g1:/ F D />`, if produced in the direction :g:`B <g1:B>`, :g:`D <g1:D>`, will meet.

.. step:: construct

   Let them be produced and meet at :g:`G <g1:G>`

.. step:: construct

   **segment** :g:`/ A G / <g1:/ A G />`

.. step:: assert [G.12] <G.12>

   Since :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ C E />` to :g:`/ C E / <g1:/ C E />`, :g:`< E A C ) <g1:< E A C )>` is also :eq:`equal <g1:< E A C ) = g1:< A E C )>` to :g:`< A E C ) <g1:< A E C )>`

.. step:: assert

   And the angle at :g:`< A C E ) <g1:< A C E )>` is right

.. step:: assert [G.45] <G.45>

   Therefore each of :g:`< E A C ) <g1:< E A C )>`, :g:`< A E C ) <g1:< A E C )>` is half a right angle.

.. step:: assert

   For the same reason each of :g:`< C E B ) <g1:< C E B )>`, :g:`< E B C ) <g1:< E B C )>` is also half a right angle

.. step:: assert

   Therefore :g:`< A E B ) <g1:< A E B )>` is right.

.. step:: assert [G.25] <G.25>

   And, since :g:`< E B C ) <g1:< E B C )>` is half a right angle, :g:`< D B G ) <g1:< D B G )>` is also half a right angle.

.. step:: assert [G.42] <G.42>

   :g:`< B D G ) <g1:< B D G )>` is also :eq:`right <g1:< B D G ) = g1:< D C E )>`, for it is :eq:`equal <g1:< B D G ) = g1:< D C E )>` to :g:`< D C E ) <g1:< D C E )>`, they being alternate

.. step:: assert [G.45] <G.45>

   Therefore the remaining angle :g:`< D G B ) <g1:< D G B )>` is half a right angle;

.. step:: assert

   Therefore :g:`< D G B ) <g1:< D G B )>` is :eq:`equal <g1:< D G B ) = g1:< D B G )>` to :g:`< D B G ) <g1:< D B G )>`,

.. step:: assert [G.13] <G.13>

   So that the side :g:`/ B D / <g1:/ B D />` is also :eq:`equal <g1:/ B D / = g1:/ G D />` to the side :g:`/ G D / <g1:/ G D />`.

.. step:: assert [G.47] <G.47>

   Since :g:`< E G F ) <g1:< E G F )>` is half a right angle, and the angle at :g:`< E F G ) <g1:< E F G )>` is :eq:`right <g1:< E F G ) = g1:< D C E )>`, for it is :eq:`equal <g1:< E F G ) = g1:< D C E )>` to the opposite angle, the angle at :g:`< D C E ) <g1:< D C E )>`.

.. step:: assert [G.45] <G.45>

   The remaining angle :g:`< F E G ) <g1:< F E G )>` is half a right angle;

.. step:: assert

   Therefore :g:`< E G F ) <g1:< E G F )>` is :eq:`equal <g1:< E G F ) = g1:< F E G )>` to :g:`< F E G ) <g1:< F E G )>`,

.. step:: assert [G.13] <G.13>

   So that the side :g:`/ G F / <g1:/ G F />` is also :eq:`equal <g1:/ G F / = g1:/ E F />` to the side :g:`/ E F / <g1:/ E F />`.

.. step:: assert

   Since the square on :g:`/ E C / <g1:/ E C />` is :eq:`equal <g1:/ E C / = g1:/ C A />` to the square on :g:`/ C A / <g1:/ C A />`, the squares on :g:`/ E C / <g1:/ E C />`, :g:`/ C A / <g1:/ C A />` are double of the square on :g:`/ C A / <g1:/ C A />`.

.. step:: assert [G.60] <G.60>

   The square on :g:`/ E A / <g1:/ E A />` is equal to the squares on :g:`/ E C / <g1:/ E C />`, :g:`/ C A / <g1:/ C A />`

.. step:: assert [G.1] <G.1>

   Therefore the square on :g:`/ E A / <g1:/ E A />` is double of the square on :g:`/ A C / <g1:/ A C />`.

.. step:: assert

   Since :g:`/ F G / <g1:/ F G />` is :eq:`equal <g1:/ F G / = g1:/ E F />` to :g:`/ E F / <g1:/ E F />`, the square on :g:`/ F G / <g1:/ F G />` is also :eq:`equal <g1:/ F G / = g1:/ F E />` to the square on :g:`/ F E / <g1:/ F E />`

.. step:: assert

   Therefore the squares on :g:`/ G F / <g1:/ G F />`, :g:`/ F E / <g1:/ F E />` are double of the square on :g:`/ E F / <g1:/ E F />`.

.. step:: assert [G.60] <G.60>

   The square on :g:`/ E G / <g1:/ E G />` is equal to the squares on :g:`/ G F / <g1:/ G F />`, :g:`/ F E / <g1:/ F E />`

.. step:: assert

   Therefore the square on :g:`/ E G / <g1:/ E G />` is double of the square on :g:`/ E F / <g1:/ E F />`.

.. step:: assert [G.47] <G.47>

   :g:`/ E F / <g1:/ E F />` is :eq:`equal <g1:/ E F / = g1:/ C D />` to :g:`/ C D / <g1:/ C D />`

.. step:: assert

   Therefore the square on :g:`/ E G / <g1:/ E G />` is double of the square on :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   The square on :g:`/ E A / <g1:/ E A />` was also proved double of the square on :g:`/ A C / <g1:/ A C />`

.. step:: assert

   Therefore the squares on :g:`/ A E / <g1:/ A E />`, :g:`/ E G / <g1:/ E G />` are double of the squares on :g:`/ A C / <g1:/ A C />`, :g:`/ C D / <g1:/ C D />`.

.. step:: assert [G.60] <G.60>

   The square on :g:`/ A G / <g1:/ A G />` is equal to the squares on :g:`/ A E / <g1:/ A E />`, :g:`/ E G / <g1:/ E G />`

.. step:: assert

   Therefore the square on :g:`/ A G / <g1:/ A G />` is double of the squares on :g:`/ A C / <g1:/ A C />`, :g:`/ C D / <g1:/ C D />`.

.. step:: assert [G.60] <G.60>

   The squares on :g:`/ A D / <g1:/ A D />`, :g:`/ D G / <g1:/ D G />` are equal to the square on :g:`/ A G / <g1:/ A G />`

.. step:: assert

   Therefore the squares on :g:`/ A D / <g1:/ A D />`, :g:`/ D G / <g1:/ D G />` are double of the squares on :g:`/ A C / <g1:/ A C />`, :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   :g:`/ D G / <g1:/ D G />` is :eq:`equal <g1:/ D G / = g1:/ D B />` to :g:`/ D B / <g1:/ D B />`

.. step:: conclude

   Therefore the squares on :g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />` are double of the squares on :g:`/ A C / <g1:/ A C />`, :g:`/ C D / <g1:/ C D />`.

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
     "G.13" [label="G.13", tooltip="G.13 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", fillcolor="#222244", URL="../G.13/index.html", target="_top"];
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
     "G.45" [label="G.45", tooltip="G.45 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.71" [label="G.71", tooltip="G.71 (II.10): If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight lin...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.71" -> "G.1";
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
     "G.71" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.71" -> "G.12";
     "G.71" -> "G.13";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.71" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.60" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.60" -> "G.24";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.71" -> "G.25";
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
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.71" -> "G.41";
     "G.45" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.71" -> "G.42";
     "G.45" -> "G.44";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.71" -> "G.44";
     "G.71" -> "G.45";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.71" -> "G.47";
     "G.50" -> "G.48";
     "G.54" -> "G.50";
     "G.60" -> "G.54";
     "G.60" -> "G.59";
     "G.71" -> "G.60";
   }

.. toctree::
   :hidden:

   code
   heath
