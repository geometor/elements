:order: 168
:number: 168
:canonical_id: G.168
:original_id: VI.6
:volume: II
:book: VI
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, proportions, similar-figures
:category: theorem, proof, plane-geometry, proportions, similar-figures
:tags: book-vi, point, segment, angle, triangle, proportion, equality
:dependencies: G.11, G.34, G.45, G.146, G.148, G.166
:excerpt: If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles is equiangular and will have those angles equal which the corresponding sides subtend.

.. _G.168:
.. _VI.6:

G.168
=====

.. rubric:: `VI.6 <https://geometor.github.io/euclid/heath/volume_II/book_vi/propositions/06/>`_

.. enunciation::

   If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles is equiangular and will have those angles equal which the corresponding sides subtend.

.. signature:: theorem

   | :fn:`triangles_angle_equal <G.168>`\ (:g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>`, :g:`< B A C ) <g1:< B A C )>`, :g:`< E D F ) <g1:< E D F )>`)
   | **given** :g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` be two triangles having one angle :g:`< B A C ) <g1:< B A C )>` :eq:`equal <g1:< B A C ) = g1:< E D F )>` to one angle :g:`< E D F ) <g1:< E D F )>` and the sides about the equal angles proportional, so that
   | **prove** :g:`< A B C > <g1:< A B C >>` is :eq:`equiangular <g1:< B A C ) = g1:< E D F ); g1:< A B C ) = g1:< D E F ); g1:< A C B ) = g1:< D F E )>` with :g:`< D E F > <g1:< D E F >>`, and will have :g:`< A B C ) <g1:< A B C )>` :eq:`equal <g1:< A B C ) = g1:< D E F ); g1:< A C B ) = g1:< D F E )>` to :g:`< D E F ) <g1:< D E F )>`, and :g:`< A C B ) <g1:< A C B )>` to :g:`< D F E ) <g1:< D F E )>`

.. picture:: g1.svg
   :alt: Proposition 6 diagram

.. step:: given

   :g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` be two triangles having one angle :g:`< B A C ) <g1:< B A C )>` :eq:`equal <g1:< B A C ) = g1:< E D F )>` to one angle :g:`< E D F ) <g1:< E D F )>` and the sides about the equal angles proportional, so that

.. step:: assert

   As :g:`/ B A / <g1:/ B A />` is to :g:`/ A C / <g1:/ A C />`, so is :g:`/ E D / <g1:/ E D />` to :g:`/ D F / <g1:/ D F />`;

.. step:: construct

   :fn:`copy_angle <G.34>`: On :g:`/ D F / <g1:/ D F />`, and at :g:`D <g1:D>`, :g:`F <g1:F>` on it, let there be constructed :g:`< F D G ) <g1:< F D G )>` :eq:`equal <g1:< F D G ) = g1:< B A C ) = g1:< E D F )>` to either of :g:`< B A C ) <g1:< B A C )>`, :g:`< E D F ) <g1:< E D F )>`, and :g:`< D F G ) <g1:< D F G )>` :eq:`equal <g1:< D F G ) = g1:< A C B )>` to :g:`< A C B ) <g1:< A C B )>`

.. step:: assert ∵ triangle_angle_sum <G.45>

   Therefore the remaining angle at :g:`< B ) <g1:< B )>` is :eq:`equal <g1:< B ) = g1:< G )>` to the remaining angle at :g:`< G ) <g1:< G )>`.

.. step:: assert

   Therefore :g:`< A B C > <g1:< A B C >>` is :eq:`equiangular <g1:< B A C ) = g1:< F D G ); g1:< A C B ) = g1:< D F G ); g1:< B ) = g1:< G )>` with :g:`< D G F > <g1:< D G F >>`.

.. step:: assert ∵ equiangular_triangles_sides <G.166>

   Therefore, proportionally, as :g:`/ B A / <g1:/ B A />` is to :g:`/ A C / <g1:/ A C />`, so is :g:`/ G D / <g1:/ G D />` to :g:`/ D F / <g1:/ D F />`.

.. step:: assert

   But, by hypothesis, as :g:`/ B A / <g1:/ B A />` is to :g:`/ A C / <g1:/ A C />`, so also is :g:`/ E D / <g1:/ E D />` to :g:`/ D F / <g1:/ D F />`

.. step:: assert ∵ ratios_ratio <G.148>

   Therefore also, as :g:`/ E D / <g1:/ E D />` is to :g:`/ D F / <g1:/ D F />`, so is :g:`/ G D / <g1:/ G D />` to :g:`/ D F / <g1:/ D F />`.

.. step:: assert ∵ magnitudes_ratio_equal <G.146>

   Therefore :g:`/ E D / <g1:/ E D />` is :eq:`equal <g1:/ E D / = g1:/ D G />` to :g:`/ D G / <g1:/ D G />`;

.. step:: assert

   And :g:`/ D F / <g1:/ D F />` is common

.. step:: assert

   Therefore the two sides :g:`/ E D / <g1:/ E D />`, :g:`/ D F / <g1:/ D F />` are :eq:`equal <g1:/ E D / = g1:/ G D />; g1:/ D F / = g1:/ D F />` to the two sides :g:`/ G D / <g1:/ G D />`, :g:`/ D F / <g1:/ D F />`; and :g:`< E D F ) <g1:< E D F )>` is :eq:`equal <g1:< E D F ) = g1:< G D F )>` to :g:`< G D F ) <g1:< G D F )>`;

.. step:: assert

   Therefore the base :g:`/ E F / <g1:/ E F />` is :eq:`equal <g1:/ E F / = g1:/ G F />` to the base :g:`/ G F / <g1:/ G F />`,

.. step:: assert ∵ sas_congruence <G.11>

   And :g:`< D E F > <g1:< D E F >>` is :eq:`equal <g1:< D E F > = g1:< D G F >>` to :g:`< D G F > <g1:< D G F >>`, and the remaining angles will be :eq:`equal <g1:< D F G ) = g1:< D F E ); g1:< D G F ) = g1:< D E F )>` to the remaining angles, namely those which the equal sides subtend.

.. step:: assert

   Therefore :g:`< D F G ) <g1:< D F G )>` is :eq:`equal <g1:< D F G ) = g1:< D F E ); g1:< D G F ) = g1:< D E F )>` to :g:`< D F E ) <g1:< D F E )>`, and :g:`< D G F ) <g1:< D G F )>` to :g:`< D E F ) <g1:< D E F )>`.

.. step:: assert

   :g:`< D F G ) <g1:< D F G )>` is :eq:`equal <g1:< D F G ) = g1:< A C B )>` to :g:`< A C B ) <g1:< A C B )>`

.. step:: assert

   Therefore :g:`< A C B ) <g1:< A C B )>` is also :eq:`equal <g1:< A C B ) = g1:< D F E )>` to :g:`< D F E ) <g1:< D F E )>`.

.. step:: assert

   And, by hypothesis, :g:`< B A C ) <g1:< B A C )>` is also :eq:`equal <g1:< B A C ) = g1:< E D F )>` to :g:`< E D F ) <g1:< E D F )>`

.. step:: assert ∵ triangle_angle_sum <G.45>

   Therefore the remaining angle at :g:`< B ) <g1:< B )>` is also :eq:`equal <g1:< B ) = g1:< E )>` to the remaining angle at :g:`< E ) <g1:< E )>`.

.. step:: conclude

   Therefore :g:`< A B C > <g1:< A B C >>` is :eq:`equiangular <g1:< B A C ) = g1:< E D F ); g1:< A C B ) = g1:< D F E ); g1:< B ) = g1:< E )>` with :g:`< D E F > <g1:< D E F >>`.

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
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.38): Triangles on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.39): Equal triangles on the same base and on the same side lie in the same parallels.", fillcolor="#222244", URL="../G.52/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.136" [label="G.136", tooltip="G.136 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.136/index.html", target="_top"];
     "G.137" [label="G.137", tooltip="G.137 (V.3): If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then alsoex aequali the magnitudes taken is...", fillcolor="#222244", URL="../G.137/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (V.4): If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples wh...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.146/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.150/index.html", target="_top"];
     "G.151" [label="G.151", tooltip="G.151 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.151/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.152/index.html", target="_top"];
     "G.153" [label="G.153", tooltip="G.153 (V.16): If four magnitudes be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.153/index.html", target="_top"];
     "G.157" [label="G.157", tooltip="G.157 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and ifex aequali the first be greater than the third, the fourth...", fillcolor="#222244", URL="../G.157/index.html", target="_top"];
     "G.159" [label="G.159", tooltip="G.159 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.159/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.164" [label="G.164", tooltip="G.164 (VI.2): If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionall...", fillcolor="#222244", URL="../G.164/index.html", target="_top"];
     "G.166" [label="G.166", tooltip="G.166 (VI.4): In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.", fillcolor="#222244", URL="../G.166/index.html", target="_top"];
     "G.168" [label="G.168", tooltip="G.168 (VI.6): If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles is equiangular and will have those angles equal which the corres...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.28" -> "G.7";
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
     "G.168" -> "G.11";
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
     "G.28" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.166" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.168" -> "G.34";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.39";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.166" -> "G.40";
     "G.42" -> "G.41";
     "G.166" -> "G.41";
     "G.45" -> "G.42";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.45" -> "G.44";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.52" -> "G.44";
     "G.168" -> "G.45";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.166" -> "G.47";
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
     "G.137" -> "G.136";
     "G.139" -> "G.137";
     "G.139" -> "G.138";
     "G.142" -> "G.138";
     "G.149" -> "G.138";
     "G.150" -> "G.138";
     "G.153" -> "G.138";
     "G.159" -> "G.138";
     "G.163" -> "G.138";
     "G.159" -> "G.139";
     "G.147" -> "G.142";
     "G.152" -> "G.142";
     "G.164" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.146" -> "G.145";
     "G.147" -> "G.145";
     "G.151" -> "G.145";
     "G.157" -> "G.145";
     "G.164" -> "G.146";
     "G.168" -> "G.146";
     "G.151" -> "G.147";
     "G.157" -> "G.147";
     "G.153" -> "G.148";
     "G.163" -> "G.148";
     "G.164" -> "G.148";
     "G.168" -> "G.148";
     "G.152" -> "G.149";
     "G.151" -> "G.150";
     "G.157" -> "G.150";
     "G.153" -> "G.151";
     "G.153" -> "G.152";
     "G.163" -> "G.152";
     "G.166" -> "G.153";
     "G.159" -> "G.157";
     "G.166" -> "G.159";
     "G.164" -> "G.163";
     "G.166" -> "G.164";
     "G.168" -> "G.166";
   }

Required for
------------

:ref:`G.185 <G.185>`, :ref:`G.197 <G.197>`, :ref:`G.322 <G.322>`, :ref:`G.324 <G.324>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.513 <G.513>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
