:order: 90
:number: 90
:canonical_id: G.90
:original_id: II.8
:title: G.90 four rectangles plus square
:volume: I
:book: II
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, geometric-algebra
:category: theorem, proof, plane-geometry, geometric-algebra
:tags: book-ii, point, segment, triangle, quadrilateral, polygon, straight-line, contained-rectangle, square, figure, gnomon, rectangle, equality
:dependencies: G.4, G.63, G.65, G.72, G.81, G.86
:excerpt: If a segment be cut at random, four times the rectangle contained by the whole and one of the segments together with the square on the remaining segment is equal to the square described on the whole and the aforesaid segment as on one segment.

.. _G.90:
.. _II.8:

G.90 four rectangles plus square
================================

.. rubric:: `II.8 <https://geometor.github.io/euclid/heath/volume_I/book_ii/propositions/08/>`_

.. enunciation::

   If a :term:`segment <G.4>` be cut at random, four times the :term:`rectangle contained <G.81>` by the whole and one of the segments together with the :term:`square <G.63>` on the remaining segment is equal to the square described on the whole and the aforesaid segment as on one segment.

.. signature:: theorem

   | :fn:`four_rectangles_plus_square <G.90>`\ ()
   | **prove** four times the rectangle contained by :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` together with the square on :g:`/ A C / <g1:/ A C />` is equal to the square described on :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` as on one segment

.. picture:: g1.svg
   :alt: Diagram

.. step:: construct

   Let a segment :g:`/ A B / <g1:/ A B />` be cut at random at :g:`C <g1:C>`

.. step:: construct

   Let [the segment] :g:`/ B D / <g1:/ B D />` be produced in a segment [with :g:`/ A B / <g1:/ A B />`]

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ C B / <g1:/ C B />`) → :g:`/ B D / <g1:/ B D />` (:eq:`equal <g1:/ B D / = g1:/ C B />`)

.. step:: construct

   Let the square :g:`< A E F D > <g1:< A E F D >>` be described on :g:`/ A D / <g1:/ A D />`

.. step:: construct

   Let the :term:`figure <G.9>` be drawn double.

.. step:: assert

   Since :g:`/ C B / <g1:/ C B />` is :eq:`equal <g1:/ C B / = g1:/ B D />` to :g:`/ B D / <g1:/ B D />`, while :g:`/ C B / <g1:/ C B />` is :eq:`equal <g1:/ C B / = g1:/ G K /; g1:/ B D / = g1:/ K N />` to :g:`/ G K / <g1:/ G K />`, and :g:`/ B D / <g1:/ B D />` to :g:`/ K N / <g1:/ K N />`, therefore :g:`/ G K / <g1:/ G K />` is also :eq:`equal <g1:/ G K / = g1:/ K N />` to :g:`/ K N / <g1:/ K N />`.

.. step:: assert

   For the same reason :g:`/ Q R / <g1:/ Q R />` is also :eq:`equal <g1:/ Q R / = g1:/ R P />` to :g:`/ R P / <g1:/ R P />`.

.. step:: assert ∵ parallelograms_equal_bases <G.65>

   And, since :g:`/ B C / <g1:/ B C />` is :eq:`equal <g1:/ B C / = g1:/ B D /; g1:/ G K / = g1:/ K N />` to :g:`/ B D / <g1:/ B D />`, and :g:`/ G K / <g1:/ G K />` to :g:`/ K N / <g1:/ K N />`, therefore :g:`< C K > <g1:< C K >>` is also :eq:`equal <g1:< C K > = g1:< K D >; g1:< G R > = g1:< R N >>` to :g:`< K D > <g1:< K D >>`, and :g:`< G R > <g1:< G R >>` to :g:`< R N > <g1:< R N >>`.

.. step:: assert ∵ parallelogram_complements <G.72>

   :g:`< C K > <g1:< C K >>` is :eq:`equal <g1:< C K > = g1:< R N >>` to :g:`< R N > <g1:< R N >>`, for they are complements of the parallelogram :g:`< C P > <g1:< C P >>`

.. step:: assert

   Therefore :g:`< K D > <g1:< K D >>` is also :eq:`equal <g1:< K D > = g1:< G R >>` to :g:`< G R > <g1:< G R >>`

.. step:: assert

   Therefore the four areas :g:`< D K > <g1:< D K >>`, :g:`< C K > <g1:< C K >>`, :g:`< G R > <g1:< G R >>`, :g:`< R N > <g1:< R N >>` are :eq:`equal <g1:< D K > = g1:< C K > = g1:< G R > = g1:< R N >>` to one another.

.. step:: assert

   Therefore the four are quadruple of :g:`< C K > <g1:< C K >>`.

.. step:: assert

   Since :g:`/ C B / <g1:/ C B />` is :eq:`equal <g1:/ C B / = g1:/ B D />` to :g:`/ B D / <g1:/ B D />`, while :g:`/ B D / <g1:/ B D />` is :eq:`equal <g1:/ B D / = g1:/ B K / = g1:/ C G />` to :g:`/ B K / <g1:/ B K />`, that is :g:`/ C G / <g1:/ C G />`, and :g:`/ C B / <g1:/ C B />` is :eq:`equal <g1:/ C B / = g1:/ G K / = g1:/ G Q />` to :g:`/ G K / <g1:/ G K />`, that is :g:`/ G Q / <g1:/ G Q />` → therefore :g:`/ C G / <g1:/ C G />` is also :eq:`equal <g1:/ C G / = g1:/ G Q />` to :g:`/ G Q / <g1:/ G Q />`.

.. step:: assert ∵ parallelograms_equal_bases <G.65>

   And, since :g:`/ C G / <g1:/ C G />` is :eq:`equal <g1:/ C G / = g1:/ G Q /; g1:/ Q R / = g1:/ R P />` to :g:`/ G Q / <g1:/ G Q />`, and :g:`/ Q R / <g1:/ Q R />` to :g:`/ R P / <g1:/ R P />`, :g:`< A G > <g1:< A G >>` is also :eq:`equal <g1:< A G > = g1:< M Q >; g1:< Q L > = g1:< R F >>` to :g:`< M Q > <g1:< M Q >>`, and :g:`< Q L > <g1:< Q L >>` to :g:`< R F > <g1:< R F >>`.

.. step:: assert ∵ parallelogram_complements <G.72>

   :g:`< M Q > <g1:< M Q >>` is :eq:`equal <g1:< M Q > = g1:< Q L >>` to :g:`< Q L > <g1:< Q L >>`, for they are complements of the parallelogram :g:`< M L > <g1:< M L >>`

.. step:: assert

   Therefore :g:`< A G > <g1:< A G >>` is also :eq:`equal <g1:< A G > = g1:< R F >>` to :g:`< R F > <g1:< R F >>`

.. step:: assert

   Therefore the four areas :g:`< A G > <g1:< A G >>`, :g:`< M Q > <g1:< M Q >>`, :g:`< Q L > <g1:< Q L >>`, :g:`< R F > <g1:< R F >>` are :eq:`equal <g1:< A G > = g1:< M Q > = g1:< Q L > = g1:< R F >>` to one another.

.. step:: assert

   Therefore the four are quadruple of :g:`< A G > <g1:< A G >>`.

.. step:: assert

   The four areas :g:`< C K > <g1:< C K >>`, :g:`< K D > <g1:< K D >>`, :g:`< G R > <g1:< G R >>`, :g:`< R N > <g1:< R N >>` were proved to be quadruple of :g:`< C K > <g1:< C K >>`

.. step:: assert

   Therefore the eight areas, which contain the :term:`gnomon <G.86>` :g:`< S T U > <g1:< S T U >>`, are quadruple of :g:`< A K > <g1:< A K >>`.

.. step:: assert

   Since :g:`< A K > <g1:< A K >>` is the rectangle :g:`/ A B / <g1:/ A B />`, :g:`/ B D / <g1:/ B D />`, for :g:`/ B K / <g1:/ B K />` is :eq:`equal <g1:/ B K / = g1:/ B D />` to :g:`/ B D / <g1:/ B D />`, therefore four times the rectangle :g:`/ A B / <g1:/ A B />`, :g:`/ B D / <g1:/ B D />` is quadruple of :g:`< A K > <g1:< A K >>`.

.. step:: assert

   The gnomon :g:`< S T U > <g1:< S T U >>` was also proved to be quadruple of :g:`< A K > <g1:< A K >>`

.. step:: assert

   Therefore four times the rectangle :g:`/ A B / <g1:/ A B />`, :g:`/ B D / <g1:/ B D />` is equal to the gnomon :g:`< S T U > <g1:< S T U >>`.

.. step:: construct

   Let :g:`< O H > <g1:< O H >>`, which is equal to the square on :g:`/ A C / <g1:/ A C />`, be added to each

.. step:: assert

   Therefore four times the rectangle :g:`/ A B / <g1:/ A B />`, :g:`/ B D / <g1:/ B D />` together with the square on :g:`/ A C / <g1:/ A C />` is equal to the gnomon :g:`< S T U > <g1:< S T U >>` and :g:`< O H > <g1:< O H >>`.

.. step:: assert

   The gnomon :g:`< S T U > <g1:< S T U >>` and :g:`< O H > <g1:< O H >>` are the whole square :g:`< A E F D > <g1:< A E F D >>`, which is described on :g:`/ A D / <g1:/ A D />`

.. step:: assert

   Therefore four times the rectangle :g:`/ A B / <g1:/ A B />`, :g:`/ B D / <g1:/ B D />` together with the square on :g:`/ A C / <g1:/ A C />` is equal to the square on :g:`/ A D / <g1:/ A D />`.

.. step:: assert

   :g:`/ B D / <g1:/ B D />` is :eq:`equal <g1:/ B D / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`

.. step:: conclude

   Therefore four times the rectangle contained by :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` together with the square on :g:`/ A C / <g1:/ A C />` is equal to the square on :g:`/ A D / <g1:/ A D />`, that is to the square described on :g:`/ A B / <g1:/ A B />` and :g:`/ B C / <g1:/ B C />` as on one segment.

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
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.64" [label="G.64", tooltip="G.64 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.64/index.html", target="_top"];
     "G.65" [label="G.65", tooltip="G.65 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.65/index.html", target="_top"];
     "G.72" [label="G.72", tooltip="G.72 (I.43): In any parallelogram, the complements of the parallelograms about the diagonal are equal in area.", fillcolor="#222244", URL="../G.72/index.html", target="_top"];
     "G.81" [label="G.81", tooltip="G.81 (II.def.1): Any rectangular parallelogram is said to becontained by the twosegments containing theright angle.", fillcolor="#224422", URL="../G.81/index.html", target="_top"];
     "G.86" [label="G.86", tooltip="G.86 (II.def.2): And in any parallelogrammic area let any one whatever of the parallelograms about itsdiameter with the two complements be called agnomon.", fillcolor="#224422", URL="../G.86/index.html", target="_top"];
     "G.90" [label="G.90", tooltip="G.90 (II.8): If a segment be cut at random, four times the rectangle contained by the whole and one of the segments together with the square on the remaining segment is equal to the square desc...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.60" -> "G.3";
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
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.60" -> "G.4";
     "G.61" -> "G.4";
     "G.81" -> "G.4";
     "G.90" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
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
     "G.64" -> "G.16";
     "G.65" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.33" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.20" -> "G.19";
     "G.39" -> "G.19";
     "G.64" -> "G.19";
     "G.72" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.30" -> "G.21";
     "G.33" -> "G.21";
     "G.41" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.32" -> "G.22";
     "G.36" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
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
     "G.60" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.27" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.55" -> "G.32";
     "G.56" -> "G.32";
     "G.81" -> "G.32";
     "G.36" -> "G.33";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.62" -> "G.35";
     "G.64" -> "G.35";
     "G.72" -> "G.35";
     "G.39" -> "G.36";
     "G.56" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.56" -> "G.39";
     "G.41" -> "G.40";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.62" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.60" -> "G.52";
     "G.64" -> "G.52";
     "G.65" -> "G.52";
     "G.60" -> "G.53";
     "G.56" -> "G.55";
     "G.60" -> "G.56";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.65" -> "G.60";
     "G.62" -> "G.61";
     "G.72" -> "G.61";
     "G.86" -> "G.61";
     "G.64" -> "G.62";
     "G.65" -> "G.62";
     "G.72" -> "G.62";
     "G.64" -> "G.63";
     "G.90" -> "G.63";
     "G.65" -> "G.64";
     "G.90" -> "G.65";
     "G.90" -> "G.72";
     "G.90" -> "G.81";
     "G.90" -> "G.86";
   }

.. toctree::
   :hidden:

   code
   heath
