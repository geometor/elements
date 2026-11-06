:order: 154
:number: 154
:canonical_id: G.154
:original_id: IV.4
:title: G.154 inscribe a circle in a triangle
:volume: II
:book: IV
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles, polygons
:category: problem, construction, plane-geometry, circles, polygons
:tags: book-iv, point, segment, circle, angle, triangle, trilateral, circle-inscribed-in-figure, plane-angle, straight-line, perpendicular, line, centre, diameter, extremity, inscribed, equality
:dependencies: G.10, G.11, G.12, G.15, G.16, G.22, G.31, G.33, G.35, G.51, G.118, G.152, G.153
:excerpt: Inscribe a circle in a given triangle.

.. _G.154:
.. _IV.4:

G.154 inscribe a circle in a triangle
=====================================

.. rubric:: `IV.4 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/04/>`_

.. enunciation::

   :term:`Inscribe a circle in <G.153>` a given :term:`triangle <G.12>`.

.. signature:: problem

   | :fn:`inscribe_circle_in_triangle <G.154>`\ (:g:`< A B C > <g1:< A B C >>`) → :g:`( E F G ) <g1:( E F G )>`
   | **given** :g:`< A B C > <g1:< A B C >>`
   | **construct** :g:`( E F G ) <g1:( E F G )>` is :term:`inscribed in <G.153>` :g:`< A B C > <g1:< A B C >>`

.. picture:: g1.svg
   :alt: Proposition 4 diagram

.. step:: given ∵ circle_radii, polygon_def, similarly_circle_said_def <G.10, G.12, G.153>

   :g:`< A B C > <g1:< A B C >>`

.. step:: construct ∵ bisect_angle <G.31>

   :fn:`bisect_angle <G.31>`\ (:g:`< A B C ) <g1:< A B C )>`, :g:`< A C B ) <g1:< A C B )>`) → bisectors :g:`/ B D / <g1:/ B D />`, :g:`/ C D / <g1:/ C D />` meeting at :g:`D <g1:D>`

.. step:: construct ∵ perpendicular_from, right_angle_perpendicular <G.35, G.33>

   :fn:`perpendicular_from <G.35>`\ (:g:`D <g1:D>`, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C A / <g1:/ C A />`) → :g:`/ D E / <g1:/ D E />` ⊥ :g:`/ A B / <g1:/ A B />`, :g:`/ D F / <g1:/ D F />` ⊥ :g:`/ B C / <g1:/ B C />`, :g:`/ D G / <g1:/ D G />` ⊥ :g:`/ C A / <g1:/ C A />`

.. step:: assert ∵ asa_aas_congruence, equal_transitive <G.51, G.16>

   In :g:`< E B D > <g1:< E B D >>`, :g:`< F B D > <g1:< F B D >>`: :g:`< A B D ) <g1:< A B D )>` :eq:`= <g1:< A B D ) = g1:< C B D )>` :g:`< C B D ) <g1:< C B D )>`, right :g:`< B E D ) <g1:< B E D )>` :eq:`= <g1:< B E D ) = g1:< B F D )>` :g:`< B F D ) <g1:< B F D )>`, :g:`/ B D / <g1:/ B D />` common → :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ D E / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`; similarly :g:`/ D G / <g1:/ D G />` :eq:`= <g1:/ D G / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, so :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ D E / = g1:/ D F / = g1:/ D G />` :g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D E / = g1:/ D F / = g1:/ D G />` :g:`/ D G / <g1:/ D G />`

.. step:: assert ∵ perpendicular_at_diameter_extremity_tangent <G.118>

   :term:`Angles <G.22>` at :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`G <g1:G>` are right → :term:`circle <G.10>` with :term:`center <G.11>` :g:`D <g1:D>` and radius :g:`/ D E / <g1:/ D E />` passes through :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`G <g1:G>` and touches :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C A / <g1:/ C A />` without cutting them

.. step:: conclude ∵ circle, similarly_circle_said_def <G.15, G.153>

   :fn:`circle <G.15>`\ (:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`( E F G ) <g1:( E F G )>` is inscribed in :g:`< A B C > <g1:< A B C >>`

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
     "G.35" [label="G.35", tooltip="G.35 (I.12): Construct a perpendicular to a given line from a given point not on it.", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
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
     "G.96" [label="G.96", tooltip="G.96 (I.def.18): A semicircle is the figure contained by a diameter and the arc cut off by it.", fillcolor="#224422", URL="../G.96/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.def.2): Asegment is said totouch a circle which, meeting thecircle and being produced, does not cut the circle.", fillcolor="#224422", URL="../G.111/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.117/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (III.16): The line drawn at right angles to the diameter of a circle from its extremity falls outside the circle, no other line can be interposed between it and the arc, and the angle of the...", fillcolor="#222244", URL="../G.118/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (IV.def.1): Apolygon is said to beinscribed in a polygon when the respectiveangles of the inscribedfigure lie on the respective sides of that in which it is inscribed.", fillcolor="#224422", URL="../G.152/index.html", target="_top"];
     "G.153" [label="G.153", tooltip="G.153 (IV.def.5): Similarly acircle is said to beinscribed in a figure when the arc of the circle touches each side of thefigure in which it is inscribed.", fillcolor="#224422", URL="../G.153/index.html", target="_top"];
     "G.154" [label="G.154", tooltip="G.154 (IV.4): Inscribe a circle in a given triangle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.35" -> "G.1";
     "G.37" -> "G.1";
     "G.40" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.18" -> "G.2";
     "G.22" -> "G.2";
     "G.30" -> "G.2";
     "G.33" -> "G.2";
     "G.34" -> "G.2";
     "G.35" -> "G.2";
     "G.37" -> "G.2";
     "G.40" -> "G.2";
     "G.118" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.118" -> "G.3";
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
     "G.35" -> "G.4";
     "G.37" -> "G.4";
     "G.40" -> "G.4";
     "G.41" -> "G.4";
     "G.61" -> "G.4";
     "G.111" -> "G.4";
     "G.117" -> "G.4";
     "G.118" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.96" -> "G.9";
     "G.152" -> "G.9";
     "G.153" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.35" -> "G.10";
     "G.61" -> "G.10";
     "G.96" -> "G.10";
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.153" -> "G.10";
     "G.154" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.35" -> "G.11";
     "G.61" -> "G.11";
     "G.96" -> "G.11";
     "G.154" -> "G.11";
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
     "G.152" -> "G.12";
     "G.154" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.34" -> "G.14";
     "G.35" -> "G.14";
     "G.41" -> "G.14";
     "G.43" -> "G.14";
     "G.51" -> "G.14";
     "G.118" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.35" -> "G.15";
     "G.154" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.40" -> "G.16";
     "G.154" -> "G.16";
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
     "G.51" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.30" -> "G.22";
     "G.31" -> "G.22";
     "G.32" -> "G.22";
     "G.33" -> "G.22";
     "G.34" -> "G.22";
     "G.35" -> "G.22";
     "G.37" -> "G.22";
     "G.40" -> "G.22";
     "G.41" -> "G.22";
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.51" -> "G.22";
     "G.77" -> "G.22";
     "G.118" -> "G.22";
     "G.152" -> "G.22";
     "G.154" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.28" -> "G.25";
     "G.43" -> "G.25";
     "G.44" -> "G.25";
     "G.118" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.43" -> "G.26";
     "G.51" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.35" -> "G.29";
     "G.31" -> "G.30";
     "G.118" -> "G.30";
     "G.32" -> "G.31";
     "G.154" -> "G.31";
     "G.35" -> "G.32";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.35" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.40" -> "G.33";
     "G.42" -> "G.33";
     "G.77" -> "G.33";
     "G.118" -> "G.33";
     "G.154" -> "G.33";
     "G.37" -> "G.34";
     "G.154" -> "G.35";
     "G.37" -> "G.36";
     "G.42" -> "G.36";
     "G.40" -> "G.37";
     "G.42" -> "G.37";
     "G.40" -> "G.38";
     "G.41" -> "G.40";
     "G.42" -> "G.41";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.118" -> "G.42";
     "G.44" -> "G.43";
     "G.118" -> "G.44";
     "G.154" -> "G.51";
     "G.96" -> "G.61";
     "G.118" -> "G.61";
     "G.118" -> "G.77";
     "G.118" -> "G.96";
     "G.118" -> "G.111";
     "G.118" -> "G.117";
     "G.154" -> "G.118";
     "G.154" -> "G.152";
     "G.154" -> "G.153";
   }

.. toctree::
   :hidden:

   code
   heath
