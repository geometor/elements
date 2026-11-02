:order: 345
:number: 345
:canonical_id: G.345
:original_id: IX.15
:title: G.345 numbers continued proportion
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, segment, number, proportional, in-the-same-ratio, prime-to-one-another, multiply, square, separando, ratio, proportion, prime, continued-proportion
:dependencies: G.84, G.85, G.176, G.180, G.197, G.248, G.249, G.276, G.278, G.279, G.282, G.297
:excerpt: If three numbers in continued proportion be the least of those which have the same ratio with them, any two whatever added together is prime to the remaining number.

.. _G.345:
.. _IX.15:

G.345 numbers continued proportion
==================================

.. rubric:: `IX.15 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/15/>`_

.. enunciation::

   If three :term:`numbers <G.248>` in :term:`continued proportion <G.180>` be the least of those which have the :term:`same ratio <G.176>` with them, any two whatever added together is :term:`prime to <G.249>` the remaining number.

.. signature:: theorem

   | :fn:`numbers_continued_proportion_ix_15 <G.345>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`)
   | **given** :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, three numbers in continued proportion, be the least of those which have the same ratio with them
   | **prove** any two of the numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` whatever added together are prime to the remaining number, namely :g:`A <g1:A>`, :g:`B <g1:B>` to :g:`C <g1:C>`

.. picture:: g1.svg
   :alt: Proposition 15 diagram

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, three numbers in continued proportion, be the least of those which have the same ratio with them

.. step:: assert

   :g:`B <g1:B>`, :g:`C <g1:C>` to :g:`A <g1:A>`

.. step:: assert

   And further :g:`A <g1:A>`, :g:`C <g1:C>` to :g:`B <g1:B>`.

.. step:: construct

   :fn:`find_numbers_continued <G.297>`: Let two numbers :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, the least of those which have the same ratio with :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, be taken.

.. step:: assert ∵ find_numbers_continued <G.297>

   It is then manifest that :g:`/ D E / <g1:/ D E />` by :term:`multiplying <G.269>` itself has made :g:`A <g1:A>`, and by multiplying :g:`/ E F / <g1:/ E F />` has made :g:`B <g1:B>`, and, further, :g:`/ E F / <g1:/ E F />` by multiplying itself has made :g:`C <g1:C>`.

.. step:: assert

   Since :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` are least,

.. step:: assert ∵ least_numbers_ratio_vii_22 <G.276>

   They are prime to one another.

.. step:: assert ∵ numbers_prime_sum <G.282>

   But, if two numbers be prime to one another, their sum is also prime to each .

.. step:: assert

   Therefore :g:`/ D F / <g1:/ D F />` is also prime to each of the numbers :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`.

.. step:: assert

   Further :g:`/ D E / <g1:/ D E />` is also prime to :g:`/ E F / <g1:/ E F />` ;

.. step:: assert

   Therefore :g:`/ D F / <g1:/ D F />`, :g:`/ D E / <g1:/ D E />` are prime to :g:`/ E F / <g1:/ E F />`.

.. step:: assert ∵ numbers_prime_number_vii_24 <G.278>

   But, if two numbers be prime to any number, their product is also prime to the other .

.. step:: assert ∵ numbers_prime_product <G.279>

   So that the product of :g:`/ D F / <g1:/ D F />`, :g:`/ D E / <g1:/ D E />` is prime to :g:`/ E F / <g1:/ E F />` ; hence the product of :g:`/ D F / <g1:/ D F />`, :g:`/ D E / <g1:/ D E />` is also prime to the :term:`square <G.63>` on :g:`/ E F / <g1:/ E F />`.

.. step:: assert ∵ rectangle_whole_and_part <G.84>

   The product of :g:`/ D F / <g1:/ D F />`, :g:`/ D E / <g1:/ D E />` is the square on :g:`/ D E / <g1:/ D E />` together with the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` .

.. step:: assert

   Therefore the square on :g:`/ D E / <g1:/ D E />` together with the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` is prime to the square on :g:`/ E F / <g1:/ E F />`.

.. step:: assert

   The square on :g:`/ D E / <g1:/ D E />` is :g:`A <g1:A>`, the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` is :g:`B <g1:B>`, and the square on :g:`/ E F / <g1:/ E F />` is :g:`C <g1:C>` ;

.. step:: assert

   Therefore :g:`A <g1:A>`, :g:`B <g1:B>` added together are prime to :g:`C <g1:C>`.

.. step:: assert

   Similarly we can prove that :g:`B <g1:B>`, :g:`C <g1:C>` added together are prime to :g:`A <g1:A>`.

.. step:: assert

   I say next that :g:`A <g1:A>`, :g:`C <g1:C>` added together are also prime to :g:`B <g1:B>`.

.. step:: assert

   Since :g:`/ D F / <g1:/ D F />` is prime to each of the numbers :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`,

.. step:: assert ∵ numbers_prime_number_vii_24, numbers_prime_product <G.278, G.279>

   The square on :g:`/ D F / <g1:/ D F />` is also prime to the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`.

.. step:: assert ∵ square_of_sum <G.85>

   The squares on :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` together with twice the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` are equal to the square on :g:`/ D F / <g1:/ D F />` .

.. step:: assert

   Therefore the squares on :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` together with twice the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` are prime to the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`.

.. step:: assert

   *:term:`Separando <G.197>`*, the squares on :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` together with once the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` are prime to the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`.

.. step:: assert

   Therefore, *separando* again, the squares on :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` are prime to the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`.

.. step:: assert

   The square on :g:`/ D E / <g1:/ D E />` is :g:`A <g1:A>`, the product of :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />` is :g:`B <g1:B>`, and the square on :g:`/ E F / <g1:/ E F />` is :g:`C <g1:C>`.

.. step:: conclude

   Therefore :g:`A <g1:A>`, :g:`C <g1:C>` added together are prime to :g:`B <g1:B>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.def.6): The extremities of a surface are lines or arcs.", fillcolor="#224422", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.def.15): A circle ( A B ) is a plane figure contained by one arc defined by a center A and a point B establishing its defining radius / A B /, such that all segments / A B /, / A C /, / A D...", fillcolor="#224422", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.13/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.post.3): Construct a circle ( A B ) with center A and defining radius point B.", fillcolor="#444422", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.1): Construct an equilateral triangle on a given segment.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.post.2): Extend a segment / A B / continuously along a line [ A B ] to / B C /.", fillcolor="#444422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.cn.3): If equals are subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.19/index.html", target="_top"];
     "G.20" [label="G.20", tooltip="G.20 (I.2): Construct at a given point a segment equal to a given segment.", fillcolor="#222244", URL="../G.20/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.3): Cut off from the greater of two unequal segments a segment equal to the less.", fillcolor="#222244", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.cn.4): Things / A B /, / D E / that coincide with one another are equal to one another.", fillcolor="#442222", URL="../G.23/index.html", target="_top"];
     "G.24" [label="G.24", tooltip="G.24 (I.4): Triangles with two sides and the included angle equal are congruent (SAS).", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.5): In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", fillcolor="#222244", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.37/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.75" [label="G.75", tooltip="G.75 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.75/index.html", target="_top"];
     "G.81" [label="G.81", tooltip="G.81 (II.def.1): Any rectangular parallelogram is said to becontained by the twosegments containing theright angle.", fillcolor="#224422", URL="../G.81/index.html", target="_top"];
     "G.84" [label="G.84", tooltip="G.84 (II.3): If a segment be cut at random, the rectangle contained by the whole and one of the segments is equal to the rectangle contained by the segments and the square on the aforesaid segm...", fillcolor="#222244", URL="../G.84/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (II.4): If a segment be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.", fillcolor="#222244", URL="../G.85/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.171" [label="G.171", tooltip="G.171 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.174" [label="G.174", tooltip="G.174 (V.def.17): Aratioex aequali arises when, there being several magnitudes and another set equal to them in multitude which taken two and two are in the same proportion, as the first is to the l...", fillcolor="#224422", URL="../G.174/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.13): Inverse ratio means taking theconsequent as antecedent in relation to the antecedent as consequent.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (V.def.7): When, of theequimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then th...", fillcolor="#224422", URL="../G.185/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.187" [label="G.187", tooltip="G.187 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.187/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.197" [label="G.197", tooltip="G.197 (V.def.15): Separation of a ratio means taking the excess by which theantecedent exceeds the consequent in relation to the consequent by itself.", fillcolor="#224422", URL="../G.197/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.249" [label="G.249", tooltip="G.249 (VII.def.12): Numbers prime to one another are those which aremeasured by anunit alone as a common measure.", fillcolor="#224422", URL="../G.249/index.html", target="_top"];
     "G.250" [label="G.250", tooltip="G.250 (VII.1): Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is...", fillcolor="#222244", URL="../G.250/index.html", target="_top"];
     "G.251" [label="G.251", tooltip="G.251 (VII.2): Given two numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.251/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.255" [label="G.255", tooltip="G.255 (VII.4): Any number is either a part or parts of any number, the less of the greater.", fillcolor="#222244", URL="../G.255/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.258" [label="G.258", tooltip="G.258 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.258/index.html", target="_top"];
     "G.261" [label="G.261", tooltip="G.261 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.261/index.html", target="_top"];
     "G.262" [label="G.262", tooltip="G.262 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.262/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VII.def.20): Numbers areproportional when the first is thesame multiple, or thesame part, or thesame parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.263/index.html", target="_top"];
     "G.265" [label="G.265", tooltip="G.265 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.265/index.html", target="_top"];
     "G.266" [label="G.266", tooltip="G.266 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.266/index.html", target="_top"];
     "G.267" [label="G.267", tooltip="G.267 (VII.14): If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.267/index.html", target="_top"];
     "G.268" [label="G.268", tooltip="G.268 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.268/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.270" [label="G.270", tooltip="G.270 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced are equal.", fillcolor="#222244", URL="../G.270/index.html", target="_top"];
     "G.271" [label="G.271", tooltip="G.271 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.271/index.html", target="_top"];
     "G.272" [label="G.272", tooltip="G.272 (VII.18): If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", fillcolor="#222244", URL="../G.272/index.html", target="_top"];
     "G.273" [label="G.273", tooltip="G.273 (VII.19): If four numbers be proportional, the number produced from the first and fourth will equals the number produced from the second and third; and, if the number produced from the first...", fillcolor="#222244", URL="../G.273/index.html", target="_top"];
     "G.274" [label="G.274", tooltip="G.274 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.274/index.html", target="_top"];
     "G.275" [label="G.275", tooltip="G.275 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.275/index.html", target="_top"];
     "G.276" [label="G.276", tooltip="G.276 (VII.22): The least numbers of those which have the same ratio with them are prime to one another.", fillcolor="#222244", URL="../G.276/index.html", target="_top"];
     "G.277" [label="G.277", tooltip="G.277 (VII.23): If two numbers be prime to one another, the number which measures the one of them is prime to the remaining number.", fillcolor="#222244", URL="../G.277/index.html", target="_top"];
     "G.278" [label="G.278", tooltip="G.278 (VII.24): If two numbers be prime to any number, their product also is prime to the same.", fillcolor="#222244", URL="../G.278/index.html", target="_top"];
     "G.279" [label="G.279", tooltip="G.279 (VII.25): If two numbers be prime to one another, the product of one of them into itself is prime to the remaining one.", fillcolor="#222244", URL="../G.279/index.html", target="_top"];
     "G.280" [label="G.280", tooltip="G.280 (VII.26): If two numbers be prime to two numbers, both to each, their products also is prime to one another.", fillcolor="#222244", URL="../G.280/index.html", target="_top"];
     "G.281" [label="G.281", tooltip="G.281 (VII.27): If two numbers be prime to one another, and each by multiplying itself make a certain number, the products is prime to one another; and, if the original numbers by multiplying the ...", fillcolor="#222244", URL="../G.281/index.html", target="_top"];
     "G.282" [label="G.282", tooltip="G.282 (VII.28): If two numbers be prime to one another, the sum is prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers is prime to one another.", fillcolor="#222244", URL="../G.282/index.html", target="_top"];
     "G.283" [label="G.283", tooltip="G.283 (VII.def.11): Aprime number is that which ismeasured by anunit alone.", fillcolor="#224422", URL="../G.283/index.html", target="_top"];
     "G.296" [label="G.296", tooltip="G.296 (VIII.1): If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio wit...", fillcolor="#222244", URL="../G.296/index.html", target="_top"];
     "G.297" [label="G.297", tooltip="G.297 (VIII.2): Find numbers in continued proportion, as many as may be prescribed, and the least that are in a given ratio.", fillcolor="#222244", URL="../G.297/index.html", target="_top"];
     "G.345" [label="G.345", tooltip="G.345 (IX.15): If three numbers in continued proportion be the least of those which have the same ratio with them, any two whatever added together is prime to the remaining number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.13" -> "G.4";
     "G.17" -> "G.4";
     "G.18" -> "G.4";
     "G.20" -> "G.4";
     "G.21" -> "G.4";
     "G.22" -> "G.4";
     "G.24" -> "G.4";
     "G.25" -> "G.4";
     "G.27" -> "G.4";
     "G.28" -> "G.4";
     "G.31" -> "G.4";
     "G.32" -> "G.4";
     "G.33" -> "G.4";
     "G.36" -> "G.4";
     "G.39" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.58" -> "G.4";
     "G.61" -> "G.4";
     "G.75" -> "G.4";
     "G.81" -> "G.4";
     "G.84" -> "G.4";
     "G.85" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.26" -> "G.9";
     "G.187" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.26" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.43" -> "G.11";
     "G.44" -> "G.11";
     "G.45" -> "G.11";
     "G.47" -> "G.11";
     "G.51" -> "G.11";
     "G.63" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.63" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.61" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.36" -> "G.16";
     "G.39" -> "G.16";
     "G.56" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.33" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.20" -> "G.19";
     "G.39" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.30" -> "G.21";
     "G.33" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.47" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.26" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.32" -> "G.22";
     "G.36" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.62" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.85" -> "G.25";
     "G.85" -> "G.26";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.48" -> "G.28";
     "G.30" -> "G.29";
     "G.48" -> "G.29";
     "G.31" -> "G.30";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.55" -> "G.32";
     "G.56" -> "G.32";
     "G.81" -> "G.32";
     "G.36" -> "G.33";
     "G.75" -> "G.33";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.62" -> "G.35";
     "G.39" -> "G.36";
     "G.56" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.56" -> "G.39";
     "G.41" -> "G.40";
     "G.45" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.62" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.62" -> "G.56";
     "G.75" -> "G.56";
     "G.85" -> "G.56";
     "G.75" -> "G.58";
     "G.84" -> "G.58";
     "G.85" -> "G.58";
     "G.62" -> "G.61";
     "G.75" -> "G.62";
     "G.85" -> "G.62";
     "G.75" -> "G.63";
     "G.84" -> "G.63";
     "G.85" -> "G.63";
     "G.297" -> "G.63";
     "G.84" -> "G.75";
     "G.85" -> "G.75";
     "G.84" -> "G.81";
     "G.85" -> "G.81";
     "G.345" -> "G.84";
     "G.345" -> "G.85";
     "G.170" -> "G.169";
     "G.249" -> "G.169";
     "G.250" -> "G.169";
     "G.251" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.268" -> "G.169";
     "G.274" -> "G.169";
     "G.277" -> "G.169";
     "G.283" -> "G.169";
     "G.171" -> "G.170";
     "G.176" -> "G.170";
     "G.185" -> "G.170";
     "G.257" -> "G.170";
     "G.186" -> "G.171";
     "G.174" -> "G.173";
     "G.297" -> "G.173";
     "G.267" -> "G.174";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.187" -> "G.176";
     "G.267" -> "G.176";
     "G.271" -> "G.176";
     "G.272" -> "G.176";
     "G.274" -> "G.176";
     "G.275" -> "G.176";
     "G.276" -> "G.176";
     "G.296" -> "G.176";
     "G.345" -> "G.176";
     "G.183" -> "G.180";
     "G.266" -> "G.180";
     "G.273" -> "G.180";
     "G.296" -> "G.180";
     "G.297" -> "G.180";
     "G.345" -> "G.180";
     "G.182" -> "G.181";
     "G.194" -> "G.181";
     "G.197" -> "G.181";
     "G.265" -> "G.181";
     "G.183" -> "G.182";
     "G.273" -> "G.183";
     "G.186" -> "G.184";
     "G.186" -> "G.185";
     "G.187" -> "G.186";
     "G.273" -> "G.187";
     "G.261" -> "G.194";
     "G.262" -> "G.194";
     "G.266" -> "G.194";
     "G.268" -> "G.194";
     "G.345" -> "G.197";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.250" -> "G.247";
     "G.268" -> "G.247";
     "G.269" -> "G.247";
     "G.283" -> "G.247";
     "G.250" -> "G.248";
     "G.251" -> "G.248";
     "G.253" -> "G.248";
     "G.255" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.258" -> "G.248";
     "G.261" -> "G.248";
     "G.262" -> "G.248";
     "G.265" -> "G.248";
     "G.266" -> "G.248";
     "G.267" -> "G.248";
     "G.268" -> "G.248";
     "G.269" -> "G.248";
     "G.270" -> "G.248";
     "G.271" -> "G.248";
     "G.272" -> "G.248";
     "G.273" -> "G.248";
     "G.274" -> "G.248";
     "G.275" -> "G.248";
     "G.276" -> "G.248";
     "G.277" -> "G.248";
     "G.278" -> "G.248";
     "G.279" -> "G.248";
     "G.280" -> "G.248";
     "G.281" -> "G.248";
     "G.282" -> "G.248";
     "G.296" -> "G.248";
     "G.297" -> "G.248";
     "G.345" -> "G.248";
     "G.250" -> "G.249";
     "G.251" -> "G.249";
     "G.275" -> "G.249";
     "G.276" -> "G.249";
     "G.277" -> "G.249";
     "G.278" -> "G.249";
     "G.279" -> "G.249";
     "G.280" -> "G.249";
     "G.281" -> "G.249";
     "G.282" -> "G.249";
     "G.296" -> "G.249";
     "G.345" -> "G.249";
     "G.251" -> "G.250";
     "G.255" -> "G.251";
     "G.255" -> "G.253";
     "G.257" -> "G.253";
     "G.261" -> "G.253";
     "G.262" -> "G.253";
     "G.263" -> "G.253";
     "G.255" -> "G.254";
     "G.258" -> "G.254";
     "G.261" -> "G.254";
     "G.262" -> "G.254";
     "G.263" -> "G.254";
     "G.274" -> "G.255";
     "G.257" -> "G.256";
     "G.263" -> "G.256";
     "G.258" -> "G.257";
     "G.261" -> "G.257";
     "G.262" -> "G.257";
     "G.265" -> "G.257";
     "G.261" -> "G.258";
     "G.262" -> "G.258";
     "G.265" -> "G.258";
     "G.262" -> "G.261";
     "G.266" -> "G.262";
     "G.265" -> "G.263";
     "G.266" -> "G.263";
     "G.271" -> "G.263";
     "G.274" -> "G.263";
     "G.268" -> "G.265";
     "G.274" -> "G.265";
     "G.267" -> "G.266";
     "G.271" -> "G.266";
     "G.274" -> "G.266";
     "G.296" -> "G.267";
     "G.270" -> "G.268";
     "G.270" -> "G.269";
     "G.271" -> "G.269";
     "G.272" -> "G.269";
     "G.276" -> "G.269";
     "G.278" -> "G.269";
     "G.281" -> "G.269";
     "G.272" -> "G.270";
     "G.275" -> "G.270";
     "G.278" -> "G.270";
     "G.272" -> "G.271";
     "G.273" -> "G.271";
     "G.276" -> "G.271";
     "G.297" -> "G.271";
     "G.273" -> "G.272";
     "G.297" -> "G.272";
     "G.278" -> "G.273";
     "G.275" -> "G.274";
     "G.278" -> "G.274";
     "G.296" -> "G.274";
     "G.278" -> "G.275";
     "G.296" -> "G.275";
     "G.297" -> "G.276";
     "G.345" -> "G.276";
     "G.278" -> "G.277";
     "G.279" -> "G.278";
     "G.280" -> "G.278";
     "G.345" -> "G.278";
     "G.281" -> "G.279";
     "G.345" -> "G.279";
     "G.281" -> "G.280";
     "G.297" -> "G.281";
     "G.345" -> "G.282";
     "G.296" -> "G.283";
     "G.297" -> "G.296";
     "G.345" -> "G.297";
   }

.. toctree::
   :hidden:

   code
   heath
