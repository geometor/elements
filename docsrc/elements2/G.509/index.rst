:order: 509
:number: 509
:canonical_id: G.509
:original_id: XIII.2
:volume: III
:book: XIII
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry, regular-solids
:category: theorem, proof, solid-geometry, regular-solids
:tags: book-xiii, segment, triangle, polygon, square, extreme-and-mean-ratio, ratio, equality
:dependencies: G.163
:excerpt: If the square on a straight line be five times the square on a segment of it, then, when the double of the said segment is cut in extreme and mean ratio, the greater segment is the remaining part of the original straight line.

.. _G.509:
.. _XIII.2:

G.509
=====

.. rubric:: `XIII.2 <https://geometor.github.io/euclid/heath/volume_III/book_xiii/propositions/02/>`_

.. enunciation::

   If the square on a straight line be five times the square on a segment of it, then, when the double of the said segment is cut in extreme and mean ratio, the greater segment is the remaining part of the original straight line.

.. picture:: g1.svg
   :alt: Book XIII, Proposition 2

.. step:: assert

   For let the square on :g:`/ A B / <g1:/ A B />` be five times the square on the segment :g:`/ A C / <g1:/ A C />` of it

.. step:: assert

   Let :g:`/ C D / <g1:/ C D />` be double of :g:`/ A C / <g1:/ A C />`

.. step:: construct

   Let the squares :g:`< A F > <g1:< A F >>`, :g:`< C G > <g1:< C G >>` be described on :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` respectively, let the figure in :g:`< A F > <g1:< A F >>` be drawn

.. step:: construct

   Let :g:`/ B E / <g1:/ B E />` be drawn through.

.. step:: assert

   Since the square on :g:`/ B A / <g1:/ B A />` is five times the square on :g:`/ A C / <g1:/ A C />`,

.. step:: assert

   :g:`< A F > <g1:< A F >>` is five times :g:`< A H > <g1:< A H >>`.

.. step:: assert

   Therefore the gnomon :g:`< M N O > <g1:< M N O >>` is quadruple of :g:`< A H > <g1:< A H >>`.

.. step:: assert

   And, since :g:`/ D C / <g1:/ D C />` is double of :g:`/ C A / <g1:/ C A />`,

.. step:: assert

   Therefore the square on :g:`/ D C / <g1:/ D C />` is quadruple of the square on :g:`/ C A / <g1:/ C A />`, that is, :g:`< C G > <g1:< C G >>` is quadruple of :g:`< A H > <g1:< A H >>`.

.. step:: assert

   The gnomon :g:`< M N O > <g1:< M N O >>` was also proved quadruple of :g:`< A H > <g1:< A H >>`;

.. step:: assert

   Therefore the gnomon :g:`< M N O > <g1:< M N O >>` is :eq:`equal <g1:< M N O > = g1:< C G >>` to :g:`< C G > <g1:< C G >>`.

.. step:: assert

   And, since :g:`/ D C / <g1:/ D C />` is double of :g:`/ C A / <g1:/ C A />`, while :g:`/ D C / <g1:/ D C />` is :eq:`equal <g1:/ D C / = g1:/ C K /; g1:/ A C / = g1:/ C H />` to :g:`/ C K / <g1:/ C K />`, and :g:`/ A C / <g1:/ A C />` to :g:`/ C H / <g1:/ C H />`,

.. step:: assert [G.163] <G.163>

   Therefore :g:`< K B > <g1:< K B >>` is also double of :g:`< B H > <g1:< B H >>`.

.. step:: assert

   :g:`< L H > <g1:< L H >>`, :g:`< H B > <g1:< H B >>` are also double of :g:`< H B > <g1:< H B >>`;

.. step:: assert

   Therefore :g:`< K B > <g1:< K B >>` is equal to :g:`< L H > <g1:< L H >>`, :g:`< H B > <g1:< H B >>`.

.. step:: assert

   The whole gnomon :g:`< M N O > <g1:< M N O >>` was also proved :eq:`equal <g1:< M N O > = g1:< C G >>` to the whole :g:`< C G > <g1:< C G >>`;

.. step:: assert

   Therefore the remainder :g:`< H F > <g1:< H F >>` is :eq:`equal <g1:< H F > = g1:< B G >>` to :g:`< B G > <g1:< B G >>`.

.. step:: assert

   :g:`< B G > <g1:< B G >>` is the rectangle :g:`/ C D / <g1:/ C D />`, :g:`/ D B / <g1:/ D B />`, for :g:`/ C D / <g1:/ C D />` is :eq:`equal <g1:/ C D / = g1:/ D G />` to :g:`/ D G / <g1:/ D G />`; and :g:`< H F > <g1:< H F >>` is the square on :g:`/ C B / <g1:/ C B />`;

.. step:: assert

   Therefore the rectangle :g:`/ C D / <g1:/ C D />`, :g:`/ D B / <g1:/ D B />` is equal to the square on :g:`/ C B / <g1:/ C B />`.

.. step:: assert

   Therefore, as :g:`/ D C / <g1:/ D C />` is to :g:`/ C B / <g1:/ C B />`, so is :g:`/ C B / <g1:/ C B />` to :g:`/ B D / <g1:/ B D />`.

.. step:: assert

   :g:`/ D C / <g1:/ D C />` is greater than :g:`/ C B / <g1:/ C B />`;

.. step:: assert

   Therefore :g:`/ C B / <g1:/ C B />` is also greater than :g:`/ B D / <g1:/ B D />`.

.. step:: assert

   Therefore, when :g:`/ C D / <g1:/ C D />` is cut in extreme and mean ratio, :g:`/ C B / <g1:/ C B />` is the greater segment.

.. step:: conclude

   Therefore etc.

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
     "G.51" [label="G.51", tooltip="G.51 (I.38): Triangles on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.152/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.509" [label="G.509", tooltip="G.509 (XIII.2): If the square on a straight line be five times the square on a segment of it, then, when the double of the said segment is cut in extreme and mean ratio, the greater segment is the...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
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
     "G.37" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
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
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.51" -> "G.49";
     "G.54" -> "G.50";
     "G.163" -> "G.51";
     "G.163" -> "G.54";
     "G.149" -> "G.135";
     "G.142" -> "G.138";
     "G.149" -> "G.138";
     "G.163" -> "G.138";
     "G.152" -> "G.142";
     "G.163" -> "G.148";
     "G.152" -> "G.149";
     "G.163" -> "G.152";
     "G.509" -> "G.163";
   }

.. toctree::
   :hidden:

   code
   heath
