:canonical_id: G.493
:original_id: XII.7
:volume: III
:book: XII
:type: prop

G.493 — Heath
=============

.. rubric:: `XII.7 <https://geometor.github.io/euclid/heath/volume_III/book_xii/propositions/07/>`_

.. enunciation::

   Any prism which has a triangular base is divided into three pyramids equal to one another which have triangular bases.

Let there be a prism in which the triangle :g:`< A B C > <g1:< A B C >>` is the base and :g:`< D E F > <g1:< D E F >>` its opposite; I say that the prism :g:`< A B C D E F > <g1:< A B C D E F >>` is divided into three pyramids :eq:`equal <g1:< C A B D > = g1:< C D E B > = g1:< D E C F >>` to one another, which have triangular bases.

.. picture:: g1.svg
   :alt: Book XII, Proposition 7

For let :g:`/ B D / <g1:/ B D />`, :g:`/ E C / <g1:/ E C />`, :g:`/ C D / <g1:/ C D />` be joined.

.. subclause::

   Since :g:`< A B E D > <g1:< A B E D >>` is a parallelogram, and :g:`/ B D / <g1:/ B D />` is its diameter,

.. assertion::

   therefore the triangle :g:`< A B D > <g1:< A B D >>` is :eq:`equal <g1:< A B D > = g1:< E B D >>` to the triangle :g:`< E B D > <g1:< E B D >>`; :just:`[G.47] <G.47>` therefore also the pyramid of which the triangle :g:`< A B D > <g1:< A B D >>` is the base and the point :g:`C <g1:C>` the vertex is :eq:`equal <g1:< C A B D > = g1:< C D E B >>` to the pyramid of which the triangle :g:`< D E B > <g1:< D E B >>` is the base and the point :g:`C <g1:C>` the vertex. :just:`[G.491] <G.491>`

.. subclause::

   But the pyramid of which the triangle :g:`< D E B > <g1:< D E B >>` is the base and the point :g:`C <g1:C>` the vertex is the same with the pyramid of which the triangle :g:`< E B C > <g1:< E B C >>` is the base and the point :g:`D <g1:D>` the vertex; for they are contained by the same planes.

.. assertion::

   Therefore the pyramid of which the triangle :g:`< A B D > <g1:< A B D >>` is the base and the point :g:`C <g1:C>` the vertex is also :eq:`equal <g1:< C A B D > = g1:< C D E B >>` to the pyramid of which the triangle :g:`< E B C > <g1:< E B C >>` is the base and the point :g:`D <g1:D>` the vertex.

.. subclause::

   Again, since :g:`< F C B E > <g1:< F C B E >>` is a parallelogram, and :g:`/ C E / <g1:/ C E />` is its diameter,

.. assertion:: [G.47] <G.47>

   the triangle :g:`< C E F > <g1:< C E F >>` is :eq:`equal <g1:< C E F > = g1:< C B E >>` to the triangle :g:`< C B E > <g1:< C B E >>`.

.. assertion::

   Therefore also the pyramid of which the triangle :g:`< B C E > <g1:< B C E >>` is the base and the point :g:`D <g1:D>` the vertex is :eq:`equal <g1:< C D E B > = g1:< D E C F >>` to the pyramid of which the triangle :g:`< E C F > <g1:< E C F >>` is the base and the point :g:`D <g1:D>` the vertex. :just:`[G.491] <G.491>`

.. subclause::

   But the pyramid of which the triangle :g:`< B C E > <g1:< B C E >>` is the base and the point :g:`D <g1:D>` the vertex was proved :eq:`equal <g1:< C D E B > = g1:< C A B D >>` to the pyramid of which the triangle :g:`< A B D > <g1:< A B D >>` is the base and the point :g:`C <g1:C>` the vertex;

.. assertion::

   therefore also the pyramid of which the triangle :g:`< C E F > <g1:< C E F >>` is the base and the point :g:`D <g1:D>` the vertex is :eq:`equal <g1:< D E C F > = g1:< C A B D >>` to the pyramid of which the triangle :g:`< A B D > <g1:< A B D >>` is the base and the point :g:`C <g1:C>` the vertex; therefore the prism :g:`< A B C D E F > <g1:< A B C D E F >>` has been divided into three pyramids :eq:`equal <g1:< C A B D > = g1:< C D E B > = g1:< D E C F >>` to one another which have triangular bases.

.. subclause::

   And, since the pyramid of which the triangle :g:`< A B D > <g1:< A B D >>` is the base and the point :g:`C <g1:C>` the vertex is the same with the pyramid of which the triangle :g:`< C A B > <g1:< C A B >>` is the base and the point :g:`D <g1:D>` the vertex, for they are contained by the same planes, while the pyramid of which the triangle :g:`< A B D > <g1:< A B D >>` is the base and the point :g:`C <g1:C>` the vertex was proved to be a third of the prism in which the triangle :g:`< A B C > <g1:< A B C >>` is the base and :g:`< D E F > <g1:< D E F >>` its opposite,

.. assertion::

   therefore also the pyramid of which the triangle :g:`< A B C > <g1:< A B C >>` is the base and the point :g:`D <g1:D>` the vertex is a third of the prism which has the same base, the triangle :g:`< A B C > <g1:< A B C >>`, and :g:`< D E F > <g1:< D E F >>` as its opposite.

.. assertion::

   PORISM. *From this it is manifest that any pyramid is a third part of the prism which has the same base with it and equal height.* :just:`Q. E. D.`

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
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.85/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.20): In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.99" [label="G.99", tooltip="G.99 (III.21): In a circle the angles in the same segment are equal.", fillcolor="#222244", URL="../G.99/index.html", target="_top"];
     "G.100" [label="G.100", tooltip="G.100 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.100/index.html", target="_top"];
     "G.101" [label="G.101", tooltip="G.101 (III.def.11): Similar segments of circles are those which admit equal angles, or in which the angles are equal.", fillcolor="#224422", URL="../G.101/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.24): Similar segments of circles on equal straight lines are equal.", fillcolor="#222244", URL="../G.103/index.html", target="_top"];
     "G.105" [label="G.105", tooltip="G.105 (III.26): In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.105/index.html", target="_top"];
     "G.106" [label="G.106", tooltip="G.106 (III.27): In equal circles angles standing on equal circumferences are equal, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.106/index.html", target="_top"];
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
     "G.157" [label="G.157", tooltip="G.157 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and ifex aequali the first be greater than the third, the fourth...", fillcolor="#222244", URL="../G.157/index.html", target="_top"];
     "G.159" [label="G.159", tooltip="G.159 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.159/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.164" [label="G.164", tooltip="G.164 (VI.2): If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionall...", fillcolor="#222244", URL="../G.164/index.html", target="_top"];
     "G.166" [label="G.166", tooltip="G.166 (VI.4): In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.", fillcolor="#222244", URL="../G.166/index.html", target="_top"];
     "G.168" [label="G.168", tooltip="G.168 (VI.6): If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles is equiangular and will have those angles equal which the corres...", fillcolor="#222244", URL="../G.168/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (VI.def.1): Similar polygons are such as have their angles severally equal and the sides about the equal angles proportional.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.174" [label="G.174", tooltip="G.174 (VI.11): To two given straight lines to find a third proportional.", fillcolor="#222244", URL="../G.174/index.html", target="_top"];
     "G.175" [label="G.175", tooltip="G.175 (VI.12): To three given straight lines to find a fourth proportional.", fillcolor="#222244", URL="../G.175/index.html", target="_top"];
     "G.178" [label="G.178", tooltip="G.178 (VI.15): In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one ang...", fillcolor="#222244", URL="../G.178/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (VI.18): Describe on a given segment a rectilinear figure similar and similarly situated to a given rectilinear figure.", fillcolor="#222244", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.9): When three magnitudes are proportional, the first is said to have to the third theduplicate ratio of that which it has to the second.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (VI.19): Similar triangles are to one another in the duplicate ratio of the corresponding sides.", fillcolor="#222244", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (VI.20): Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio duplicate...", fillcolor="#222244", URL="../G.185/index.html", target="_top"];
     "G.187" [label="G.187", tooltip="G.187 (VI.22): If four straight lines be proportional, the polygons similar and similarly described upon them is proportional; and, if the polygons similar and similarly described upon them be pr...", fillcolor="#222244", URL="../G.187/index.html", target="_top"];
     "G.313" [label="G.313", tooltip="G.313 (X.1): Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and ...", fillcolor="#222244", URL="../G.313/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.448" [label="G.448", tooltip="G.448 (XI.5): If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.", fillcolor="#222244", URL="../G.448/index.html", target="_top"];
     "G.449" [label="G.449", tooltip="G.449 (XI.6): If two straight lines be at right angles to the same plane, the straight lines is parallel.", fillcolor="#222244", URL="../G.449/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.452" [label="G.452", tooltip="G.452 (XI.9): Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.", fillcolor="#222244", URL="../G.452/index.html", target="_top"];
     "G.453" [label="G.453", tooltip="G.453 (XI.10): If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.", fillcolor="#222244", URL="../G.453/index.html", target="_top"];
     "G.460" [label="G.460", tooltip="G.460 (XI.16): If two parallel planes be cut by any plane, their common sections are parallel.", fillcolor="#222244", URL="../G.460/index.html", target="_top"];
     "G.469" [label="G.469", tooltip="G.469 (XI.24): If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.", fillcolor="#222244", URL="../G.469/index.html", target="_top"];
     "G.470" [label="G.470", tooltip="G.470 (XI.25): If a parallelepipedal solid be cut by a plane which is parallel to the opposite planes, then, as the base is to the base, so will the solid be to the solid.", fillcolor="#222244", URL="../G.470/index.html", target="_top"];
     "G.474" [label="G.474", tooltip="G.474 (XI.def.10): Equal and similar solid figures are those contained by similar planes equal in multitude and in magnitude.", fillcolor="#224422", URL="../G.474/index.html", target="_top"];
     "G.475" [label="G.475", tooltip="G.475 (XI.28): If a parallelepipedal solid be cut by a plane through the diagonals of the opposite planes, the solid is bisected by the plane.", fillcolor="#222244", URL="../G.475/index.html", target="_top"];
     "G.476" [label="G.476", tooltip="G.476 (XI.29): Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal.", fillcolor="#222244", URL="../G.476/index.html", target="_top"];
     "G.477" [label="G.477", tooltip="G.477 (XI.30): Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are not on the same straight lines, are equal.", fillcolor="#222244", URL="../G.477/index.html", target="_top"];
     "G.478" [label="G.478", tooltip="G.478 (XI.31): Parallelepipedal solids which are on equal bases and of the same height are equal.", fillcolor="#222244", URL="../G.478/index.html", target="_top"];
     "G.486" [label="G.486", tooltip="G.486 (XI.39): If there be two prisms of equal height, and one have a parallelogram as base and the other a triangle, and if the parallelogram be double of the triangle, the prisms is equal.", fillcolor="#222244", URL="../G.486/index.html", target="_top"];
     "G.487" [label="G.487", tooltip="G.487 (XII.1): Similar polygons inscribed in circles are to one another as the squares on the diameters.", fillcolor="#222244", URL="../G.487/index.html", target="_top"];
     "G.488" [label="G.488", tooltip="G.488 (XII.2): Circles are to one another as the squares on the diameters.", fillcolor="#222244", URL="../G.488/index.html", target="_top"];
     "G.489" [label="G.489", tooltip="G.489 (XII.3): Any pyramid which has a triangular base is divided into two pyramids equal and similar to one another, similar to the whole and having triangular bases, and into two equal prisms; ...", fillcolor="#222244", URL="../G.489/index.html", target="_top"];
     "G.490" [label="G.490", tooltip="G.490 (XII.4): If there be two pyramids of the same height which have triangular bases, and each of them be divided into two pyramids equal to one another and similar to the whole, and into two e...", fillcolor="#222244", URL="../G.490/index.html", target="_top"];
     "G.491" [label="G.491", tooltip="G.491 (XII.5): Pyramids which are of the same height and have triangular bases are to one another as the bases.", fillcolor="#222244", URL="../G.491/index.html", target="_top"];
     "G.493" [label="G.493", tooltip="G.493 (XII.7): Any prism which has a triangular base is divided into three pyramids equal to one another which have triangular bases.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.52" -> "G.1";
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
     "G.24" -> "G.6";
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
     "G.174" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.105" -> "G.11";
     "G.168" -> "G.11";
     "G.447" -> "G.11";
     "G.449" -> "G.11";
     "G.469" -> "G.11";
     "G.476" -> "G.11";
     "G.489" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.98" -> "G.12";
     "G.110" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.76" -> "G.15";
     "G.447" -> "G.15";
     "G.449" -> "G.15";
     "G.453" -> "G.15";
     "G.476" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.76" -> "G.18";
     "G.110" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.178" -> "G.24";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.447" -> "G.25";
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
     "G.106" -> "G.34";
     "G.168" -> "G.34";
     "G.181" -> "G.34";
     "G.478" -> "G.34";
     "G.47" -> "G.37";
     "G.447" -> "G.37";
     "G.39" -> "G.38";
     "G.460" -> "G.38";
     "G.40" -> "G.39";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.166" -> "G.40";
     "G.449" -> "G.40";
     "G.42" -> "G.41";
     "G.166" -> "G.41";
     "G.45" -> "G.42";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.451" -> "G.42";
     "G.489" -> "G.42";
     "G.45" -> "G.44";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.52" -> "G.44";
     "G.174" -> "G.44";
     "G.175" -> "G.44";
     "G.98" -> "G.45";
     "G.100" -> "G.45";
     "G.110" -> "G.45";
     "G.168" -> "G.45";
     "G.181" -> "G.45";
     "G.185" -> "G.45";
     "G.487" -> "G.45";
     "G.49" -> "G.46";
     "G.453" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.166" -> "G.47";
     "G.469" -> "G.47";
     "G.475" -> "G.47";
     "G.476" -> "G.47";
     "G.486" -> "G.47";
     "G.489" -> "G.47";
     "G.493" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.478" -> "G.48";
     "G.51" -> "G.49";
     "G.476" -> "G.49";
     "G.52" -> "G.50";
     "G.54" -> "G.50";
     "G.163" -> "G.51";
     "G.164" -> "G.51";
     "G.164" -> "G.52";
     "G.163" -> "G.54";
     "G.85" -> "G.76";
     "G.85" -> "G.80";
     "G.103" -> "G.85";
     "G.99" -> "G.98";
     "G.106" -> "G.98";
     "G.100" -> "G.99";
     "G.110" -> "G.100";
     "G.105" -> "G.101";
     "G.105" -> "G.103";
     "G.106" -> "G.105";
     "G.487" -> "G.106";
     "G.487" -> "G.110";
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
     "G.470" -> "G.138";
     "G.159" -> "G.139";
     "G.147" -> "G.142";
     "G.152" -> "G.142";
     "G.164" -> "G.142";
     "G.178" -> "G.142";
     "G.478" -> "G.142";
     "G.145" -> "G.143";
     "G.313" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.146" -> "G.145";
     "G.147" -> "G.145";
     "G.151" -> "G.145";
     "G.157" -> "G.145";
     "G.164" -> "G.146";
     "G.168" -> "G.146";
     "G.178" -> "G.146";
     "G.187" -> "G.146";
     "G.478" -> "G.146";
     "G.151" -> "G.147";
     "G.157" -> "G.147";
     "G.153" -> "G.148";
     "G.163" -> "G.148";
     "G.164" -> "G.148";
     "G.168" -> "G.148";
     "G.178" -> "G.148";
     "G.184" -> "G.148";
     "G.187" -> "G.148";
     "G.478" -> "G.148";
     "G.488" -> "G.148";
     "G.491" -> "G.148";
     "G.152" -> "G.149";
     "G.185" -> "G.149";
     "G.490" -> "G.149";
     "G.151" -> "G.150";
     "G.157" -> "G.150";
     "G.153" -> "G.151";
     "G.153" -> "G.152";
     "G.163" -> "G.152";
     "G.166" -> "G.153";
     "G.184" -> "G.153";
     "G.488" -> "G.153";
     "G.490" -> "G.153";
     "G.491" -> "G.153";
     "G.159" -> "G.157";
     "G.166" -> "G.159";
     "G.185" -> "G.159";
     "G.187" -> "G.159";
     "G.164" -> "G.163";
     "G.178" -> "G.163";
     "G.184" -> "G.163";
     "G.185" -> "G.163";
     "G.166" -> "G.164";
     "G.174" -> "G.164";
     "G.175" -> "G.164";
     "G.489" -> "G.164";
     "G.168" -> "G.166";
     "G.181" -> "G.166";
     "G.185" -> "G.166";
     "G.487" -> "G.166";
     "G.185" -> "G.168";
     "G.487" -> "G.168";
     "G.181" -> "G.170";
     "G.185" -> "G.170";
     "G.487" -> "G.170";
     "G.489" -> "G.170";
     "G.184" -> "G.174";
     "G.187" -> "G.174";
     "G.187" -> "G.175";
     "G.184" -> "G.178";
     "G.187" -> "G.181";
     "G.184" -> "G.182";
     "G.184" -> "G.183";
     "G.185" -> "G.184";
     "G.187" -> "G.184";
     "G.487" -> "G.185";
     "G.490" -> "G.187";
     "G.491" -> "G.313";
     "G.444" -> "G.443";
     "G.460" -> "G.443";
     "G.449" -> "G.444";
     "G.451" -> "G.444";
     "G.448" -> "G.445";
     "G.450" -> "G.445";
     "G.447" -> "G.446";
     "G.448" -> "G.446";
     "G.449" -> "G.446";
     "G.451" -> "G.446";
     "G.448" -> "G.447";
     "G.451" -> "G.447";
     "G.452" -> "G.447";
     "G.449" -> "G.448";
     "G.452" -> "G.449";
     "G.451" -> "G.450";
     "G.452" -> "G.451";
     "G.453" -> "G.452";
     "G.469" -> "G.453";
     "G.489" -> "G.453";
     "G.469" -> "G.460";
     "G.470" -> "G.469";
     "G.478" -> "G.469";
     "G.478" -> "G.470";
     "G.475" -> "G.474";
     "G.478" -> "G.474";
     "G.489" -> "G.474";
     "G.486" -> "G.475";
     "G.477" -> "G.476";
     "G.478" -> "G.476";
     "G.478" -> "G.477";
     "G.486" -> "G.478";
     "G.489" -> "G.486";
     "G.490" -> "G.486";
     "G.488" -> "G.487";
     "G.491" -> "G.488";
     "G.490" -> "G.489";
     "G.491" -> "G.489";
     "G.491" -> "G.490";
     "G.493" -> "G.491";
   }

Required for
------------

:ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`
