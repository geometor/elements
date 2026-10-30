:order: 194
:number: 194
:canonical_id: G.194
:original_id: VI.29
:volume: II
:book: VI
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, proportions, similar-figures
:category: problem, construction, plane-geometry, proportions, similar-figures
:tags: book-vi, point, segment, line, triangle, polygon, parallelogram, similar, equality
:dependencies: G.49, G.56, G.186, G.189, G.190, G.191
:excerpt: To a given straight line to apply a parallelogram equal to a given polygon and exceeding by a parallelogrammic figure similar to a given one.

.. _G.194:
.. _VI.29:

G.194
=====

.. rubric:: `VI.29 <https://geometor.github.io/euclid/heath/volume_II/book_vi/propositions/29/>`_

.. enunciation::

   To a given straight line to apply a parallelogram equal to a given polygon and exceeding by a parallelogrammic figure similar to a given one.

.. signature:: problem

   | :fn:`straight_line_apply_vi_29 <G.194>`\ (:g:`/ A B / <g1:/ A B />`, :g:`< C > <g1:< C >>`, :g:`< D > <g1:< D >>`) → :g:`< A O > <g1:< A O >>`, :g:`< Q P > <g1:< Q P >>`
   | **given** :g:`/ A B / <g1:/ A B />` , :g:`< C > <g1:< C >>` the given rectilineal figure to which the figure to be applied to :g:`/ A B / <g1:/ A B />` is required to be equal, :g:`< D > <g1:< D >>` that to which the excess is required to be similar
   | **construct** to :g:`/ A B / <g1:/ A B />` there has been applied the parallelogram :g:`< A O > <g1:< A O >>` :eq:`equal <g1:< A O > = g1:< C >>` to the given rectilineal figure :g:`< C > <g1:< C >>` and exceeding by a parallelogrammic figure :g:`< Q P > <g1:< Q P >>` which is similar to :g:`< D > <g1:< D >>`, since :g:`< P Q > <g1:< P Q >>` is also similar to :g:`< E L > <g1:< E L >>`

.. picture:: g1.svg
   :alt: Book VI Proposition 29

.. step:: given

   :g:`/ A B / <g1:/ A B />` , :g:`< C > <g1:< C >>` the given rectilineal figure to which the figure to be applied to :g:`/ A B / <g1:/ A B />` is required to be equal, :g:`< D > <g1:< D >>` that to which the excess is required to be similar

.. step:: construct

   :fn:`construct_figure_similar <G.190>`: Let :g:`/ A B / <g1:/ A B />` be :eq:`bisected <g1:/ A E / = g1:/ E B />` at :g:`E <g1:E>` ; let there be described on :g:`/ E B / <g1:/ E B />` the parallelogram :g:`< B F > <g1:< B F >>` similar and similarly situated to :g:`< D > <g1:< D >>` ; and let :g:`< G H > <g1:< G H >>` be constructed at once equal to the sum of :g:`< B F > <g1:< B F >>`, :g:`< C > <g1:< C >>` and similar and similarly situated to :g:`< D > <g1:< D >>`.

.. step:: assert

   Let :g:`/ K H / <g1:/ K H />` correspond to :g:`/ F L / <g1:/ F L />` and :g:`/ K G / <g1:/ K G />` to :g:`/ F E / <g1:/ F E />`.

.. step:: assert

   Since :g:`< G H > <g1:< G H >>` is greater than :g:`< F B > <g1:< F B >>`,

.. step:: assert

   Therefore :g:`/ K H / <g1:/ K H />` is also greater than :g:`/ F L / <g1:/ F L />`, and :g:`/ K G / <g1:/ K G />` than :g:`/ F E / <g1:/ F E />`.

.. step:: construct

   Let :g:`[ F L ] <g1:[ F L ]>`, :g:`[ F E ] <g1:[ F E ]>` be produced, let :g:`/ F L M / <g1:/ F L M />` be :eq:`equal <g1:/ F L M / = g1:/ K H />; g1:/ F E N / = g1:/ K G />` to :g:`/ K H / <g1:/ K H />`, and :g:`/ F E N / <g1:/ F E N />` to :g:`/ K G / <g1:/ K G />`, and let :g:`< M N > <g1:< M N >>` be completed ;

.. step:: assert

   Therefore :g:`< M N > <g1:< M N >>` is both :eq:`equal <g1:< M N > = g1:< G H >>` and similar to :g:`< G H > <g1:< G H >>`.

.. step:: assert

   :g:`< G H > <g1:< G H >>` is similar to :g:`< E L > <g1:< E L >>` ;

.. step:: assert ∵ figures_similar_polygon <G.186>

   Therefore :g:`< M N > <g1:< M N >>` is also similar to :g:`< E L > <g1:< E L >>` ;

.. step:: assert ∵ parallelogram_there_taken <G.191>

   Therefore :g:`< E L > <g1:< E L >>` is about the same diameter with :g:`< M N > <g1:< M N >>`.

.. step:: construct

   Let their diameter :g:`/ F O / <g1:/ F O />` be drawn, and let the figure be described.

.. step:: assert

   Since :g:`< G H > <g1:< G H >>` is equal to :g:`< E L > <g1:< E L >>`, :g:`< C > <g1:< C >>`, while :g:`< G H > <g1:< G H >>` is :eq:`equal <g1:< G H > = g1:< M N >>` to :g:`< M N > <g1:< M N >>`,

.. step:: assert

   Therefore :g:`< M N > <g1:< M N >>` is also equal to :g:`< E L > <g1:< E L >>`, :g:`< C > <g1:< C >>`.

.. step:: construct

   Let :g:`< E L > <g1:< E L >>` be subtracted from each ;

.. step:: assert

   Therefore the remainder, the gnomon :g:`< X W V > <g1:< X W V >>`, is :eq:`equal <g1:< X W V > = g1:< C >>` to :g:`< C > <g1:< C >>`.

.. step:: assert

   Since :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ E B />` to :g:`/ E B / <g1:/ E B />`,

.. step:: assert ∵ parallelograms_equal_bases, parallelogram_complements <G.49, G.56>

   :g:`< A N > <g1:< A N >>` is also :eq:`equal <g1:< A N > = g1:< N B > = g1:< L P >>` to :g:`< N B > <g1:< N B >>`, that is, to :g:`< L P > <g1:< L P >>`.

.. step:: construct

   Let :g:`< E O > <g1:< E O >>` be added to each ;

.. step:: assert

   Therefore the whole :g:`< A O > <g1:< A O >>` is :eq:`equal <g1:< A O > = g1:< V W X >>` to the gnomon :g:`< V W X > <g1:< V W X >>`.

.. step:: assert

   The gnomon :g:`< V W X > <g1:< V W X >>` is :eq:`equal <g1:< V W X > = g1:< C >>` to :g:`< C > <g1:< C >>` ;

.. step:: assert

   Therefore :g:`< A O > <g1:< A O >>` is also :eq:`equal <g1:< A O > = g1:< C >>` to :g:`< C > <g1:< C >>`.

.. step:: conclude ∵ parallelogram_parallelograms_diameter <G.189>

   Therefore to :g:`/ A B / <g1:/ A B />` there has been applied the parallelogram :g:`< A O > <g1:< A O >>` :eq:`equal <g1:< A O > = g1:< C >>` to the given rectilineal figure :g:`< C > <g1:< C >>` and exceeding by a parallelogrammic figure :g:`< Q P > <g1:< Q P >>` which is similar to :g:`< D > <g1:< D >>`, since :g:`< P Q > <g1:< P Q >>` is also similar to :g:`< E L > <g1:< E L >>`.

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
     "G.43" [label="G.43", tooltip="G.43 (I.30): Lines parallel to the same line are parallel to one another.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
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
     "G.55" [label="G.55", tooltip="G.55 (I.42): Construct, in a given angle, a parallelogram equal in area to a given triangle.", fillcolor="#222244", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.43): In any parallelogram, the complements of the parallelograms about the diagonal are equal in area.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.57" [label="G.57", tooltip="G.57 (I.44): Apply to a given segment, in a given angle, a parallelogram equal in area to a given triangle.", fillcolor="#222244", URL="../G.57/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.45): Construct, in a given angle, a parallelogram equal in area to a given polygon.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.20): In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.99" [label="G.99", tooltip="G.99 (III.21): In a circle the angles in the same segment are equal.", fillcolor="#222244", URL="../G.99/index.html", target="_top"];
     "G.100" [label="G.100", tooltip="G.100 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.100/index.html", target="_top"];
     "G.110" [label="G.110", tooltip="G.110 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.110/index.html", target="_top"];
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
     "G.154" [label="G.154", tooltip="G.154 (V.17): If magnitudes be proportional componendo, they is proportional separando.", fillcolor="#222244", URL="../G.154/index.html", target="_top"];
     "G.155" [label="G.155", tooltip="G.155 (V.18): If magnitudes be proportional separando, they is proportional componendo.", fillcolor="#222244", URL="../G.155/index.html", target="_top"];
     "G.157" [label="G.157", tooltip="G.157 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and ifex aequali the first be greater than the third, the fourth...", fillcolor="#222244", URL="../G.157/index.html", target="_top"];
     "G.159" [label="G.159", tooltip="G.159 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.159/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.164" [label="G.164", tooltip="G.164 (VI.2): If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionall...", fillcolor="#222244", URL="../G.164/index.html", target="_top"];
     "G.166" [label="G.166", tooltip="G.166 (VI.4): In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.", fillcolor="#222244", URL="../G.166/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (VI.def.1): Similar polygons are such as have their angles severally equal and the sides about the equal angles proportional.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.171" [label="G.171", tooltip="G.171 (VI.8): If in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another.", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.174" [label="G.174", tooltip="G.174 (VI.11): To two given straight lines to find a third proportional.", fillcolor="#222244", URL="../G.174/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (VI.13): To two given straight lines to find a mean proportional.", fillcolor="#222244", URL="../G.176/index.html", target="_top"];
     "G.178" [label="G.178", tooltip="G.178 (VI.15): In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one ang...", fillcolor="#222244", URL="../G.178/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (VI.18): Describe on a given segment a rectilinear figure similar and similarly situated to a given rectilinear figure.", fillcolor="#222244", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.9): When three magnitudes are proportional, the first is said to have to the third theduplicate ratio of that which it has to the second.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (VI.19): Similar triangles are to one another in the duplicate ratio of the corresponding sides.", fillcolor="#222244", URL="../G.184/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (VI.21): Figures which are similar to the same polygon are also similar to one another.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.189" [label="G.189", tooltip="G.189 (VI.24): In any parallelogram the parallelograms about the diameter are similar both to the whole and to one another.", fillcolor="#222244", URL="../G.189/index.html", target="_top"];
     "G.190" [label="G.190", tooltip="G.190 (VI.25): Construct one and the same figure similar to a given polygon and equal to another given polygon.", fillcolor="#222244", URL="../G.190/index.html", target="_top"];
     "G.191" [label="G.191", tooltip="G.191 (VI.26): If from a parallelogram there be taken away a parallelogram similar and similarly situated to the whole and having a common angle with it, it is about the same diameter with the wh...", fillcolor="#222244", URL="../G.191/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (VI.29): To a given straight line to apply a parallelogram equal to a given polygon and exceeding by a parallelogrammic figure similar to a given one.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.43" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.52" -> "G.1";
     "G.57" -> "G.1";
     "G.58" -> "G.1";
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
     "G.28" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.27" -> "G.9";
     "G.29" -> "G.9";
     "G.33" -> "G.9";
     "G.174" -> "G.9";
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
     "G.98" -> "G.12";
     "G.110" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.110" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.56" -> "G.21";
     "G.58" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.58" -> "G.24";
     "G.178" -> "G.24";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.57" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.110" -> "G.28";
     "G.166" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.55" -> "G.34";
     "G.181" -> "G.34";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.39";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.166" -> "G.40";
     "G.42" -> "G.41";
     "G.57" -> "G.41";
     "G.166" -> "G.41";
     "G.43" -> "G.42";
     "G.45" -> "G.42";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.57" -> "G.42";
     "G.58" -> "G.42";
     "G.58" -> "G.43";
     "G.45" -> "G.44";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.52" -> "G.44";
     "G.55" -> "G.44";
     "G.57" -> "G.44";
     "G.174" -> "G.44";
     "G.191" -> "G.44";
     "G.98" -> "G.45";
     "G.100" -> "G.45";
     "G.110" -> "G.45";
     "G.171" -> "G.45";
     "G.181" -> "G.45";
     "G.49" -> "G.46";
     "G.58" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.56" -> "G.47";
     "G.58" -> "G.47";
     "G.166" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.51" -> "G.49";
     "G.194" -> "G.49";
     "G.52" -> "G.50";
     "G.54" -> "G.50";
     "G.55" -> "G.51";
     "G.163" -> "G.51";
     "G.164" -> "G.51";
     "G.164" -> "G.52";
     "G.55" -> "G.54";
     "G.163" -> "G.54";
     "G.57" -> "G.55";
     "G.58" -> "G.55";
     "G.57" -> "G.56";
     "G.194" -> "G.56";
     "G.58" -> "G.57";
     "G.190" -> "G.57";
     "G.190" -> "G.58";
     "G.99" -> "G.98";
     "G.100" -> "G.99";
     "G.110" -> "G.100";
     "G.176" -> "G.110";
     "G.145" -> "G.135";
     "G.149" -> "G.135";
     "G.154" -> "G.135";
     "G.137" -> "G.136";
     "G.154" -> "G.136";
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
     "G.178" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.146" -> "G.145";
     "G.147" -> "G.145";
     "G.151" -> "G.145";
     "G.157" -> "G.145";
     "G.164" -> "G.146";
     "G.178" -> "G.146";
     "G.191" -> "G.146";
     "G.151" -> "G.147";
     "G.157" -> "G.147";
     "G.153" -> "G.148";
     "G.155" -> "G.148";
     "G.163" -> "G.148";
     "G.164" -> "G.148";
     "G.178" -> "G.148";
     "G.184" -> "G.148";
     "G.191" -> "G.148";
     "G.152" -> "G.149";
     "G.151" -> "G.150";
     "G.157" -> "G.150";
     "G.153" -> "G.151";
     "G.155" -> "G.151";
     "G.153" -> "G.152";
     "G.163" -> "G.152";
     "G.166" -> "G.153";
     "G.184" -> "G.153";
     "G.189" -> "G.153";
     "G.190" -> "G.153";
     "G.155" -> "G.154";
     "G.189" -> "G.155";
     "G.159" -> "G.157";
     "G.166" -> "G.159";
     "G.189" -> "G.159";
     "G.164" -> "G.163";
     "G.178" -> "G.163";
     "G.184" -> "G.163";
     "G.190" -> "G.163";
     "G.166" -> "G.164";
     "G.174" -> "G.164";
     "G.189" -> "G.164";
     "G.171" -> "G.166";
     "G.181" -> "G.166";
     "G.171" -> "G.170";
     "G.181" -> "G.170";
     "G.186" -> "G.170";
     "G.189" -> "G.170";
     "G.176" -> "G.171";
     "G.184" -> "G.174";
     "G.190" -> "G.176";
     "G.184" -> "G.178";
     "G.190" -> "G.181";
     "G.184" -> "G.182";
     "G.184" -> "G.183";
     "G.190" -> "G.184";
     "G.189" -> "G.186";
     "G.194" -> "G.186";
     "G.191" -> "G.189";
     "G.194" -> "G.189";
     "G.194" -> "G.190";
     "G.194" -> "G.191";
   }

Required for
------------

:ref:`G.195 <G.195>`

.. toctree::
   :hidden:

   code
   heath
