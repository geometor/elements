:order: 165
:number: 165
:canonical_id: G.165
:original_id: IV.13
:title: G.165 pentagon equilateral equiangular
:volume: II
:book: IV
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles, polygons
:category: problem, construction, plane-geometry, circles, polygons
:tags: book-iv, point, segment, circle, angle, triangle, polygon, equilateral-triangle, circle-inscribed-in-figure, plane-angle, straight-line, trilateral, line, right-angle, centre, diameter, extremity, equilateral, inscribed, pentagon, equality
:dependencies: G.1, G.3, G.4, G.10, G.11, G.13, G.22, G.24, G.33, G.51, G.61, G.118, G.153
:excerpt: In a given pentagon, which is equilateral and equiangular, to inscribe a circle.

.. _G.165:
.. _IV.13:

G.165 pentagon equilateral equiangular
======================================

.. rubric:: `IV.13 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/13/>`_

.. enunciation::

   In a given pentagon, which is :term:`equilateral <G.13>` and equiangular, to inscribe a :term:`circle <G.10>`.

.. signature:: problem

   | :fn:`pentagon_equilateral_equiangular <G.165>`\ (:g:`< A B C D E > <g1:< A B C D E >>`)
   | **given** :g:`< A B C D E > <g1:< A B C D E >>` be the given equilateral and equiangular pentagon
   | **construct** inscribe a circle in the pentagon :g:`< A B C D E > <g1:< A B C D E >>`

.. picture:: g1.svg
   :alt: Book IV Proposition 13: Circle GHKLM inscribed in regular pentagon ABCDE

.. step:: given

   :g:`< A B C D E > <g1:< A B C D E >>` be the given equilateral and equiangular pentagon

.. step:: construct

   Let :g:`< B C D ) <g1:< B C D )>`, :g:`< C D E ) <g1:< C D E )>` be bisected by :g:`/ C F / <g1:/ C F />`, :g:`/ D F / <g1:/ D F />` respectively

.. step:: construct

   And from :g:`F <g1:F>`, at which :g:`/ C F / <g1:/ C F />`, :g:`/ D F / <g1:/ D F />` meet one another, let :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` be joined.

.. step:: assert

   :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`, and :g:`/ C F / <g1:/ C F />` common, :g:`/ B C / <g1:/ B C />`, :g:`/ C F / <g1:/ C F />` :eq:`= <g1:/ B C / = g1:/ D C /; g1:/ C F / = g1:/ C F />` :g:`/ D C / <g1:/ D C />`, :g:`/ C F / <g1:/ C F />`

.. step:: assert

   :g:`< B C F ) <g1:< B C F )>` :eq:`= <g1:< B C F ) = g1:< D C F )>` :g:`< D C F ) <g1:< D C F )>`

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ B F / <g1:/ B F />` :eq:`= <g1:/ B F / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, and :g:`< B C F > <g1:< B C F >>` is :eq:`equal <g1:< B C F > = g1:< D C F >>` to :g:`< D C F > <g1:< D C F >>`, and the remaining angles will be equal to the remaining angles, namely those which the equal sides subtend

.. step:: assert

   :g:`< C B F ) <g1:< C B F )>` :eq:`= <g1:< C B F ) = g1:< C D F )>` :g:`< C D F ) <g1:< C D F )>`

.. step:: assert

   since :g:`< C D E ) <g1:< C D E )>` is double of :g:`< C D F ) <g1:< C D F )>`, and :g:`< C D E ) <g1:< C D E )>` :eq:`= <g1:< C D E ) = g1:< A B C )>` :g:`< A B C ) <g1:< A B C )>`,

.. step:: assert

   While :g:`< C D F ) <g1:< C D F )>` :eq:`= <g1:< C D F ) = g1:< C B F )>` :g:`< C B F ) <g1:< C B F )>`

.. step:: assert

   :g:`< C B A ) <g1:< C B A )>` is also double of :g:`< C B F ) <g1:< C B F )>`

.. step:: assert

   :g:`< A B F ) <g1:< A B F )>` :eq:`= <g1:< A B F ) = g1:< F B C )>` :g:`< F B C ) <g1:< F B C )>`

.. step:: assert

   :g:`< A B C ) <g1:< A B C )>` has been :eq:`bisected <g1:< A B F ) = g1:< F B C )>` by :g:`/ B F / <g1:/ B F />`

.. step:: assert

   Similarly it can be proved that :g:`< B A E ) <g1:< B A E )>`, :g:`< A E D ) <g1:< A E D )>` have also been bisected by :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />`

.. step:: construct

   Now let :g:`/ F G / <g1:/ F G />`, :g:`/ F H / <g1:/ F H />`, :g:`/ F K / <g1:/ F K />`, :g:`/ F L / <g1:/ F L />`, :g:`/ F M / <g1:/ F M />` be drawn from :g:`F <g1:F>` :term:`perpendicular <G.33>` to :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E A / <g1:/ E A />`.

.. step:: assert

   :g:`< H C F ) <g1:< H C F )>` :eq:`= <g1:< H C F ) = g1:< K C F )>` :g:`< K C F ) <g1:< K C F )>`, and the right angle :g:`< F H C ) <g1:< F H C )>` :eq:`= <g1:< F H C ) = g1:< F K C )>` :g:`< F K C ) <g1:< F K C )>`, :g:`< F H C > <g1:< F H C >>`, :g:`< F K C > <g1:< F K C >>` are two triangles having two angles equal to two angles and one side equal to one side, namely :g:`/ F C / <g1:/ F C />` which is common to them and subtends one of the equal angles

.. step:: assert ∵ asa_aas_congruence <G.51>

   they will also have the remaining sides equal to the remaining sides

.. step:: assert

   the perpendicular :g:`/ F H / <g1:/ F H />` :eq:`= <g1:/ F H / = g1:/ F K />` the perpendicular :g:`/ F K / <g1:/ F K />`

.. step:: assert

   Similarly it can be proved that each of :g:`/ F L / <g1:/ F L />`, :g:`/ F M / <g1:/ F M />`, :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F L / = g1:/ F M / = g1:/ F G / = g1:/ F H / = g1:/ F K />` each of :g:`/ F H / <g1:/ F H />`, :g:`/ F K / <g1:/ F K />`

.. step:: assert

   the five :term:`segments <G.4>` :g:`/ F G / <g1:/ F G />`, :g:`/ F H / <g1:/ F H />`, :g:`/ F K / <g1:/ F K />`, :g:`/ F L / <g1:/ F L />`, :g:`/ F M / <g1:/ F M />` :eq:`= <g1:/ F G / = g1:/ F H / = g1:/ F K / = g1:/ F L / = g1:/ F M />`

.. step:: assert

   the circle described with :term:`center <G.11>` :g:`F <g1:F>` and distance one of :g:`/ F G / <g1:/ F G />`, :g:`/ F H / <g1:/ F H />`, :g:`/ F K / <g1:/ F K />`, :g:`/ F L / <g1:/ F L />`, :g:`/ F M / <g1:/ F M />` will pass also through the remaining :term:`points <G.1>`

.. step:: assert

   it will touch :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E A / <g1:/ E A />`, because the :term:`angles <G.22>` at :g:`< F G B ) <g1:< F G B )>`, :g:`< F H C ) <g1:< F H C )>`, :g:`< F K C ) <g1:< F K C )>`, :g:`< F L D ) <g1:< F L D )>`, :g:`< F M E ) <g1:< F M E )>` are right

.. step:: assert ∵ segment_drawn_right <G.118>

   If it does not touch them, but cuts them, it will result that the segment drawn at right angles to the :term:`diameter <G.61>` of the circle from its :term:`extremity <G.3>` falls within the circle: which was proved absurd

.. step:: assert

   the circle described with center :g:`F <g1:F>` and distance one of :g:`/ F G / <g1:/ F G />`, :g:`/ F H / <g1:/ F H />`, :g:`/ F K / <g1:/ F K />`, :g:`/ F L / <g1:/ F L />`, :g:`/ F M / <g1:/ F M />` will not cut :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E A / <g1:/ E A />`

.. step:: assert

   it will touch them

.. step:: construct

   Let it be described, as :g:`( G H K L M ) <g1:( G H K L M )>`.

.. step:: conclude

   :term:`inscribe a circle in <G.153>` the pentagon :g:`< A B C D E > <g1:< A B C D E >>`

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
     "G.11" [label="G.11", tooltip="G.11 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.13/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.14/index.html", target="_top"];
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
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.38/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.def.2): Asegment is said totouch a circle which, meeting thecircle and being produced, does not cut the circle.", fillcolor="#224422", URL="../G.111/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.117/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (III.16): The segment drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the segment and the arc another segment ca...", fillcolor="#222244", URL="../G.118/index.html", target="_top"];
     "G.153" [label="G.153", tooltip="G.153 (IV.def.5): Similarly acircle is said to beinscribed in a figure when the arc of the circle touches each side of thefigure in which it is inscribed.", fillcolor="#224422", URL="../G.153/index.html", target="_top"];
     "G.165" [label="G.165", tooltip="G.165 (IV.13): In a given pentagon, which is equilateral and equiangular, to inscribe a circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.11" -> "G.1";
     "G.14" -> "G.1";
     "G.15" -> "G.1";
     "G.17" -> "G.1";
     "G.20" -> "G.1";
     "G.21" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.28" -> "G.1";
     "G.29" -> "G.1";
     "G.31" -> "G.1";
     "G.32" -> "G.1";
     "G.34" -> "G.1";
     "G.37" -> "G.1";
     "G.40" -> "G.1";
     "G.165" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.18" -> "G.2";
     "G.22" -> "G.2";
     "G.30" -> "G.2";
     "G.33" -> "G.2";
     "G.34" -> "G.2";
     "G.37" -> "G.2";
     "G.40" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.118" -> "G.3";
     "G.165" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.12" -> "G.4";
     "G.14" -> "G.4";
     "G.17" -> "G.4";
     "G.18" -> "G.4";
     "G.20" -> "G.4";
     "G.21" -> "G.4";
     "G.22" -> "G.4";
     "G.24" -> "G.4";
     "G.25" -> "G.4";
     "G.28" -> "G.4";
     "G.29" -> "G.4";
     "G.30" -> "G.4";
     "G.31" -> "G.4";
     "G.32" -> "G.4";
     "G.33" -> "G.4";
     "G.34" -> "G.4";
     "G.37" -> "G.4";
     "G.40" -> "G.4";
     "G.41" -> "G.4";
     "G.61" -> "G.4";
     "G.111" -> "G.4";
     "G.117" -> "G.4";
     "G.118" -> "G.4";
     "G.165" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.153" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.153" -> "G.10";
     "G.165" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.61" -> "G.11";
     "G.165" -> "G.11";
     "G.13" -> "G.12";
     "G.17" -> "G.12";
     "G.20" -> "G.12";
     "G.24" -> "G.12";
     "G.25" -> "G.12";
     "G.28" -> "G.12";
     "G.29" -> "G.12";
     "G.31" -> "G.12";
     "G.32" -> "G.12";
     "G.34" -> "G.12";
     "G.41" -> "G.12";
     "G.42" -> "G.12";
     "G.43" -> "G.12";
     "G.44" -> "G.12";
     "G.51" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.165" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.34" -> "G.14";
     "G.41" -> "G.14";
     "G.43" -> "G.14";
     "G.51" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.40" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.42" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.40" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.30" -> "G.22";
     "G.31" -> "G.22";
     "G.32" -> "G.22";
     "G.33" -> "G.22";
     "G.34" -> "G.22";
     "G.37" -> "G.22";
     "G.40" -> "G.22";
     "G.41" -> "G.22";
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.51" -> "G.22";
     "G.77" -> "G.22";
     "G.118" -> "G.22";
     "G.165" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.165" -> "G.24";
     "G.28" -> "G.25";
     "G.44" -> "G.25";
     "G.118" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.31" -> "G.30";
     "G.118" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.40" -> "G.33";
     "G.42" -> "G.33";
     "G.77" -> "G.33";
     "G.118" -> "G.33";
     "G.165" -> "G.33";
     "G.37" -> "G.34";
     "G.37" -> "G.36";
     "G.40" -> "G.37";
     "G.42" -> "G.37";
     "G.40" -> "G.38";
     "G.41" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.118" -> "G.42";
     "G.44" -> "G.43";
     "G.118" -> "G.44";
     "G.165" -> "G.51";
     "G.118" -> "G.61";
     "G.165" -> "G.61";
     "G.118" -> "G.77";
     "G.118" -> "G.111";
     "G.118" -> "G.117";
     "G.165" -> "G.118";
     "G.165" -> "G.153";
   }

.. toctree::
   :hidden:

   code
   heath
