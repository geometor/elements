:order: 93
:number: 93
:canonical_id: G.93
:original_id: III.15
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, equality
:dependencies: G.31, G.35, G.91, G.92
:excerpt: Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

.. _G.93:
.. _III.15:

G.93
====

.. rubric:: `III.15 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/15/>`_

.. enunciation::

   Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.

.. picture:: g1.svg
   :alt: Diagram for Proposition 15

.. step:: given

   :g:`( A B C D ) <g1:( A B C D )>` be a circle, let :g:`/ A D / <g1:/ A D />` be its diameter and :g:`E <g1:E>` the center

.. step:: assert

   And let :g:`/ B C / <g1:/ B C />` be nearer to the diameter :g:`/ A D / <g1:/ A D />`, and :g:`/ F G / <g1:/ F G />` more remote

.. step:: construct

   For from the center :g:`E <g1:E>` let :g:`/ E H / <g1:/ E H />`, :g:`/ E K / <g1:/ E K />` be drawn perpendicular to :g:`/ B C / <g1:/ B C />`, :g:`/ F G / <g1:/ F G />`.

.. step:: assert [G.92] <G.92>

   Since :g:`/ B C / <g1:/ B C />` is nearer to the center and :g:`/ F G / <g1:/ F G />` more remote, :g:`/ E K / <g1:/ E K />` is greater than :g:`/ E H / <g1:/ E H />`.

.. step:: construct

   Let :g:`/ E L / <g1:/ E L />` be made :eq:`equal <g1:/ E L / = g1:/ E H />` to :g:`/ E H / <g1:/ E H />`, through :g:`L <g1:L>` let :g:`/ L M / <g1:/ L M />` be drawn at right angles to :g:`/ E K / <g1:/ E K />` and carried through to :g:`N <g1:N>`

.. step:: construct

   **segment** :g:`/ M E / <g1:/ M E />`, :g:`/ E N / <g1:/ E N />`, :g:`/ F E / <g1:/ F E />`, :g:`/ E G / <g1:/ E G />`

.. step:: assert [G.91] <G.91>

   Since :g:`/ E H / <g1:/ E H />` is :eq:`equal <g1:/ E H / = g1:/ E L />` to :g:`/ E L / <g1:/ E L />` → :g:`/ B C / <g1:/ B C />` is also :eq:`equal <g1:/ B C / = g1:/ M N />` to :g:`/ M N / <g1:/ M N />`.

.. step:: assert

   Since :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ E M /; g1:/ E D / = g1:/ E N />` to :g:`/ E M / <g1:/ E M />`, and :g:`/ E D / <g1:/ E D />` to :g:`/ E N / <g1:/ E N />` → :g:`/ A D / <g1:/ A D />` is equal to :g:`/ M E / <g1:/ M E />`, :g:`/ E N / <g1:/ E N />`.

.. step:: assert [G.31] <G.31>

   :g:`/ M E / <g1:/ M E />`, :g:`/ E N / <g1:/ E N />` are greater than :g:`/ M N / <g1:/ M N />`, and :g:`/ M N / <g1:/ M N />` is :eq:`equal <g1:/ M N / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`

.. step:: assert

   Therefore :g:`/ A D / <g1:/ A D />` is greater than :g:`/ B C / <g1:/ B C />`.

.. step:: assert [G.35] <G.35>

   And, since the two sides :g:`/ M E / <g1:/ M E />`, :g:`/ E N / <g1:/ E N />` are :eq:`equal <g1:/ M E / = g1:/ F E /; g1:/ E N / = g1:/ E G />` to the two sides :g:`/ F E / <g1:/ F E />`, :g:`/ E G / <g1:/ E G />`, and :g:`< M E N ) <g1:< M E N )>` greater than :g:`< F E G ) <g1:< F E G )>`, therefore the base :g:`/ M N / <g1:/ M N />` is greater than the base :g:`/ F G / <g1:/ F G />`.

.. step:: conclude

   :g:`/ M N / <g1:/ M N />` was proved :eq:`equal <g1:/ M N / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`. Therefore the diameter :g:`/ A D / <g1:/ A D />` is greatest and :g:`/ B C / <g1:/ B C />` greater than :g:`/ F G / <g1:/ F G />`.

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
     "G.35" [label="G.35", tooltip="G.35 (I.24): If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (III.3): If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects ...", fillcolor="#222244", URL="../G.78/index.html", target="_top"];
     "G.90" [label="G.90", tooltip="G.90 (III.def.4): In a circle straight lines are said to beequally distant from the centre when the perpendiculars drawn to them from the centre are equal.", fillcolor="#224422", URL="../G.90/index.html", target="_top"];
     "G.91" [label="G.91", tooltip="G.91 (III.14): In a circle equal straight lines are equally distant from the centre, and those which are equally distant from the centre are equal.", fillcolor="#222244", URL="../G.91/index.html", target="_top"];
     "G.92" [label="G.92", tooltip="G.92 (III.def.5): And that straight line is said to beat a greater distance on which the greater perpendicular falls.", fillcolor="#224422", URL="../G.92/index.html", target="_top"];
     "G.93" [label="G.93", tooltip="G.93 (III.15): Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
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
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.35" -> "G.11";
     "G.37" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.35" -> "G.12";
     "G.78" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.76" -> "G.15";
     "G.78" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.76" -> "G.18";
     "G.78" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
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
     "G.35" -> "G.30";
     "G.33" -> "G.31";
     "G.93" -> "G.31";
     "G.34" -> "G.33";
     "G.35" -> "G.34";
     "G.44" -> "G.34";
     "G.93" -> "G.35";
     "G.47" -> "G.37";
     "G.78" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.50" -> "G.48";
     "G.54" -> "G.50";
     "G.60" -> "G.54";
     "G.60" -> "G.59";
     "G.91" -> "G.60";
     "G.91" -> "G.76";
     "G.91" -> "G.78";
     "G.91" -> "G.90";
     "G.93" -> "G.91";
     "G.93" -> "G.92";
   }

.. toctree::
   :hidden:

   code
   heath
