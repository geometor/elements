:order: 164
:number: 164
:canonical_id: G.164
:original_id: VI.2
:volume: II
:book: VI
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, proportions, similar-figures
:category: theorem, proof, plane-geometry, proportions, similar-figures
:tags: book-vi, point, segment, triangle, parallel, equality
:dependencies: G.51, G.52, G.142, G.146, G.148, G.163
:excerpt: If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section is parallel to the remaining side of the triangle.

.. _G.164:
.. _VI.2:

G.164
=====

.. rubric:: `VI.2 <https://geometor.github.io/euclid/heath/volume_II/book_vi/propositions/02/>`_

.. enunciation::

   If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section is parallel to the remaining side of the triangle.

.. signature:: theorem

   | :fn:`straight_line_drawn_vi_2 <G.164>`\ ()
   | **prove** :g:`/ D E / <g1:/ D E />` is parallel to :g:`/ B C / <g1:/ B C />`

.. picture:: g1.svg
   :alt: Book VI Proposition 2

.. step:: construct

   Let :g:`/ D E / <g1:/ D E />` be drawn parallel to :g:`/ B C / <g1:/ B C />`, one of the sides of :g:`< A B C > <g1:< A B C >>`

.. step:: assert

   I say that, as :g:`/ B D / <g1:/ B D />` is to :g:`/ D A / <g1:/ D A />`, so is :g:`/ C E / <g1:/ C E />` to :g:`/ E A / <g1:/ E A />`.

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`B <g1:B>`, :g:`E <g1:E>`) → :g:`/ B E / <g1:/ B E />`, :fn:`segment <G.3>`\ (:g:`C <g1:C>`, :g:`D <g1:D>`) → :g:`/ C D / <g1:/ C D />`

.. step:: assert

   Therefore :g:`< B D E > <g1:< B D E >>` is :eq:`equal <g1:< B D E > = g1:< C D E >>` to :g:`< C D E > <g1:< C D E >>`;

.. step:: assert ∵ triangles_equal_bases <G.51>

   For they are on the same base :g:`/ D E / <g1:/ D E />` and in the same parallels :g:`/ D E / <g1:/ D E />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   :g:`< A D E > <g1:< A D E >>` is another area.

.. step:: assert ∵ equal_magnitudes_ratio <G.142>

   Equals have the same ratio to the same

.. step:: assert

   Therefore, as :g:`< B D E > <g1:< B D E >>` is to :g:`< A D E > <g1:< A D E >>`, so is :g:`< C D E > <g1:< C D E >>` to :g:`< A D E > <g1:< A D E >>`.

.. step:: assert ∵ triangles_parallelograms_height <G.163>

   But, as :g:`< B D E > <g1:< B D E >>` is to :g:`< A D E > <g1:< A D E >>`, so is :g:`/ B D / <g1:/ B D />` to :g:`/ D A / <g1:/ D A />`; for, being under the same height, the perpendicular drawn from :g:`E <g1:E>` to :g:`/ A B / <g1:/ A B />`, they are to one another as their bases.

.. step:: assert

   For the same reason also, as :g:`< C D E > <g1:< C D E >>` is to :g:`< A D E > <g1:< A D E >>`, so is :g:`/ C E / <g1:/ C E />` to :g:`/ E A / <g1:/ E A />`.

.. step:: assert ∵ ratios_ratio <G.148>

   Therefore also, as :g:`/ B D / <g1:/ B D />` is to :g:`/ D A / <g1:/ D A />`, so is :g:`/ C E / <g1:/ C E />` to :g:`/ E A / <g1:/ E A />`.

.. step:: construct

   Let the sides :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />` of :g:`< A B C > <g1:< A B C >>` be cut proportionally, so that, as :g:`/ B D / <g1:/ B D />` is to :g:`/ D A / <g1:/ D A />`, so is :g:`/ C E / <g1:/ C E />` to :g:`/ E A / <g1:/ E A />`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`/ D E / <g1:/ D E />`

.. step:: assert ∵ triangles_parallelograms_height <G.163>

   With the same construction, since, as :g:`/ B D / <g1:/ B D />` is to :g:`/ D A / <g1:/ D A />`, so is :g:`/ C E / <g1:/ C E />` to :g:`/ E A / <g1:/ E A />`, but, as :g:`/ B D / <g1:/ B D />` is to :g:`/ D A / <g1:/ D A />`, so is :g:`< B D E > <g1:< B D E >>` to :g:`< A D E > <g1:< A D E >>`, and, as :g:`/ C E / <g1:/ C E />` is to :g:`/ E A / <g1:/ E A />`, so is :g:`< C D E > <g1:< C D E >>` to :g:`< A D E > <g1:< A D E >>`.

.. step:: assert

   Therefore also,

.. step:: assert ∵ ratios_ratio <G.148>

   As :g:`< B D E > <g1:< B D E >>` is to :g:`< A D E > <g1:< A D E >>`, so is :g:`< C D E > <g1:< C D E >>` to :g:`< A D E > <g1:< A D E >>`.

.. step:: assert

   Therefore each of :g:`< B D E > <g1:< B D E >>`, :g:`< C D E > <g1:< C D E >>` has the same ratio to :g:`< A D E > <g1:< A D E >>`.

.. step:: assert ∵ magnitudes_ratio_equal <G.146>

   Therefore :g:`< B D E > <g1:< B D E >>` is :eq:`equal <g1:< B D E > = g1:< C D E >>` to :g:`< C D E > <g1:< C D E >>`;

.. step:: assert

   And they are on the same base :g:`/ D E / <g1:/ D E />`.

.. step:: assert ∵ equal_triangles_same_base_parallel <G.52>

   Equal triangles which are on the same base are also in the same parallels.

.. step:: conclude

   Therefore :g:`/ D E / <g1:/ D E />` is parallel to :g:`/ B C / <g1:/ B C />`.

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
     "G.52" [label="G.52", tooltip="G.52 (I.39): Equal triangles on the same base and on the same side lie in the same parallels.", fillcolor="#222244", URL="../G.52/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.146/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.152/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.164" [label="G.164", tooltip="G.164 (VI.2): If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionall...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.52" -> "G.1";
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
     "G.52" -> "G.44";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.51" -> "G.49";
     "G.52" -> "G.50";
     "G.54" -> "G.50";
     "G.163" -> "G.51";
     "G.164" -> "G.51";
     "G.164" -> "G.52";
     "G.163" -> "G.54";
     "G.145" -> "G.135";
     "G.149" -> "G.135";
     "G.142" -> "G.138";
     "G.149" -> "G.138";
     "G.163" -> "G.138";
     "G.152" -> "G.142";
     "G.164" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.146" -> "G.145";
     "G.164" -> "G.146";
     "G.163" -> "G.148";
     "G.164" -> "G.148";
     "G.152" -> "G.149";
     "G.163" -> "G.152";
     "G.164" -> "G.163";
   }

Required for
------------

:ref:`G.165 <G.165>`, :ref:`G.166 <G.166>`, :ref:`G.167 <G.167>`, :ref:`G.168 <G.168>`, :ref:`G.169 <G.169>`, :ref:`G.171 <G.171>`, :ref:`G.172 <G.172>`, :ref:`G.173 <G.173>`, :ref:`G.174 <G.174>`, :ref:`G.175 <G.175>`, :ref:`G.176 <G.176>`, :ref:`G.181 <G.181>`, :ref:`G.184 <G.184>`, :ref:`G.185 <G.185>`, :ref:`G.187 <G.187>`, :ref:`G.188 <G.188>`, :ref:`G.189 <G.189>`, :ref:`G.190 <G.190>`, :ref:`G.191 <G.191>`, :ref:`G.192 <G.192>`, :ref:`G.193 <G.193>`, :ref:`G.194 <G.194>`, :ref:`G.195 <G.195>`, :ref:`G.196 <G.196>`, :ref:`G.197 <G.197>`, :ref:`G.319 <G.319>`, :ref:`G.320 <G.320>`, :ref:`G.322 <G.322>`, :ref:`G.323 <G.323>`, :ref:`G.324 <G.324>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.336 <G.336>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.340 <G.340>`, :ref:`G.341 <G.341>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.351 <G.351>`, :ref:`G.352 <G.352>`, :ref:`G.353 <G.353>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.372 <G.372>`, :ref:`G.374 <G.374>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.424 <G.424>`, :ref:`G.425 <G.425>`, :ref:`G.426 <G.426>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.430 <G.430>`, :ref:`G.431 <G.431>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.461 <G.461>`, :ref:`G.468 <G.468>`, :ref:`G.473 <G.473>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.513 <G.513>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
