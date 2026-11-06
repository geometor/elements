:canonical_id: G.530
:original_id: XI.24
:title: G.530 solid contained parallel
:volume: III
:book: XI
:type: prop

G.530 solid contained parallel — Heath
======================================

.. rubric:: `XI.24 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/24/>`_

.. enunciation::

   If a :term:`solid <G.529>` be contained by :term:`parallel planes <G.516>`, the opposite :term:`planes <G.7>` in it are equal and parallelogrammic.

.. picture:: g1.svg
   :alt: Proposition 24 figure

For let the solid :g:`< C D H G > <g1:< C D H G >>` be contained by the parallel planes :g:`< A C > <g1:< A C >>`, :g:`< G F > <g1:< G F >>`, :g:`< A H > <g1:< A H >>`, :g:`< D F > <g1:< D F >>`, :g:`< B F > <g1:< B F >>`, :g:`< A E > <g1:< A E >>`; I say that the opposite planes in it are equal and parallelogrammic.

.. subclause::

   For, since the two parallel planes :g:`< B G > <g1:< B G >>`, :g:`< C E > <g1:< C E >>` are cut by the plane :g:`< A C > <g1:< A C >>`,

.. assertion::

   their common sections are :term:`parallel <G.52>`. :just:`[G.519] <G.519>`

.. assertion::

   Therefore :g:`/ A B / <g1:/ A B />` is parallel to :g:`/ D C / <g1:/ D C />`.

.. subclause::

   Again, since the two parallel planes :g:`< B F > <g1:< B F >>`, :g:`< A E > <g1:< A E >>` are cut by the plane :g:`< A C > <g1:< A C >>`,

.. assertion:: [G.519] <G.519>

   their common sections are parallel.

.. assertion::

   Therefore :g:`/ B C / <g1:/ B C />` is parallel to :g:`/ A D / <g1:/ A D />`.

.. subclause::

   But :g:`/ A B / <g1:/ A B />` was also proved parallel to :g:`/ D C / <g1:/ D C />`;

.. assertion::

   therefore :g:`< A C > <g1:< A C >>` is a parallelogram.

.. assertion::

   Similarly we can prove that each of the planes :g:`< D F > <g1:< D F >>`, :g:`< F G > <g1:< F G >>`, :g:`< G B > <g1:< G B >>`, :g:`< B F > <g1:< B F >>`, :g:`< A E > <g1:< A E >>` is a parallelogram.

Let :g:`/ A H / <g1:/ A H />`, :g:`/ D F / <g1:/ D F />` be joined.

.. subclause::

   Then, since :g:`/ A B / <g1:/ A B />` is parallel to :g:`/ D C / <g1:/ D C />`, and :g:`/ B H / <g1:/ B H />` to :g:`/ C F / <g1:/ C F />`, the two :term:`straight lines <G.4>` :g:`/ A B / <g1:/ A B />`, :g:`/ B H / <g1:/ B H />` which meet one another are parallel to the two straight lines :g:`/ D C / <g1:/ D C />`, :g:`/ C F / <g1:/ C F />` which meet one another, not in the same plane;

.. assertion::

   therefore they will contain equal :term:`angles <G.22>`; :just:`[G.512] <G.512>` therefore the angle :g:`< A B H ) <g1:< A B H )>` is :eq:`equal <g1:< A B H ) = g1:< D C F )>` to the angle :g:`< D C F ) <g1:< D C F )>`.

.. subclause::

   And, since the two sides :g:`/ A B / <g1:/ A B />`, :g:`/ B H / <g1:/ B H />` are :eq:`equal <g1:/ A B / = g1:/ D C /; g1:/ B H / = g1:/ C F />` to the two sides :g:`/ D C / <g1:/ D C />`, :g:`/ C F / <g1:/ C F />`, :just:`[G.62] <G.62>` and the angle :g:`< A B H ) <g1:< A B H )>` is :eq:`equal <g1:< A B H ) = g1:< D C F )>` to the angle :g:`< D C F ) <g1:< D C F )>`,

.. assertion::

   therefore the base :g:`/ A H / <g1:/ A H />` is :eq:`equal <g1:/ A H / = g1:/ D F />` to the base :g:`/ D F / <g1:/ D F />`, and the :term:`triangle <G.12>` :g:`< A B H > <g1:< A B H >>` is :eq:`equal <g1:< A B H > = g1:< D C F >>` to the triangle :g:`< D C F > <g1:< D C F >>`. :just:`[G.24] <G.24>`

.. subclause::

   And the parallelogram :g:`< B G > <g1:< B G >>` is double of the triangle :g:`< A B H > <g1:< A B H >>`, and the parallelogram :g:`< C E > <g1:< C E >>` double of the triangle :g:`< D C F > <g1:< D C F >>`; :just:`[G.62] <G.62>`

.. assertion::

   therefore the parallelogram :g:`< B G > <g1:< B G >>` is :eq:`equal <g1:< B G > = g1:< C E >>` to the parallelogram :g:`< C E > <g1:< C E >>`.

.. assertion::

   Similarly we can prove that :g:`< A C > <g1:< A C >>` is also :eq:`equal <g1:< A C > = g1:< G F >; g1:< A E > = g1:< B F >>` to :g:`< G F > <g1:< G F >>`, and :g:`< A E > <g1:< A E >>` to :g:`< B F > <g1:< B F >>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

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
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.502" [label="G.502", tooltip="G.502 (XI.1): A part of a segment cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.502/index.html", target="_top"];
     "G.503" [label="G.503", tooltip="G.503 (XI.2): If two segments cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.503/index.html", target="_top"];
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", fillcolor="#222244", URL="../G.504/index.html", target="_top"];
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.506" [label="G.506", tooltip="G.506 (XI.4): If a segment be set up at right angles to two segments which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.506/index.html", target="_top"];
     "G.507" [label="G.507", tooltip="G.507 (XI.5): If a segment be set up at right angles to three segments which meet one another, at their common point of section, the three segments are in one plane.", fillcolor="#222244", URL="../G.507/index.html", target="_top"];
     "G.508" [label="G.508", tooltip="G.508 (XI.6): If two segments be at right angles to the same plane, the segments is parallel.", fillcolor="#222244", URL="../G.508/index.html", target="_top"];
     "G.509" [label="G.509", tooltip="G.509 (XI.7): If two segments be parallel and points be taken at random on each of them, the segment joining the points is in the same plane with the parallel lines.", fillcolor="#222244", URL="../G.509/index.html", target="_top"];
     "G.510" [label="G.510", tooltip="G.510 (XI.8): If two segments be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.510/index.html", target="_top"];
     "G.511" [label="G.511", tooltip="G.511 (XI.9): Straight lines which are parallel to the same segment and are not in the same plane with it are also parallel to one another.", fillcolor="#222244", URL="../G.511/index.html", target="_top"];
     "G.512" [label="G.512", tooltip="G.512 (XI.10): If two segments meeting one another be parallel to two segments meeting one another not in the same plane, they will contain equal angles.", fillcolor="#222244", URL="../G.512/index.html", target="_top"];
     "G.516" [label="G.516", tooltip="G.516 (XI.def.8): Parallel planes are those which do not meet.", fillcolor="#224422", URL="../G.516/index.html", target="_top"];
     "G.519" [label="G.519", tooltip="G.519 (XI.16): If two parallel planes be cut by any plane, their common sections are parallel.", fillcolor="#222244", URL="../G.519/index.html", target="_top"];
     "G.529" [label="G.529", tooltip="G.529 (XI.def.1): Asolid is that which has length, breadth, and depth.", fillcolor="#224422", URL="../G.529/index.html", target="_top"];
     "G.530" [label="G.530", tooltip="G.530 (XI.24): If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.506" -> "G.1";
     "G.507" -> "G.1";
     "G.509" -> "G.1";
     "G.519" -> "G.1";
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
     "G.52" -> "G.2";
     "G.53" -> "G.2";
     "G.54" -> "G.2";
     "G.55" -> "G.2";
     "G.56" -> "G.2";
     "G.504" -> "G.2";
     "G.509" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.60" -> "G.3";
     "G.504" -> "G.3";
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
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.54" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.60" -> "G.4";
     "G.61" -> "G.4";
     "G.62" -> "G.4";
     "G.502" -> "G.4";
     "G.503" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.506" -> "G.4";
     "G.507" -> "G.4";
     "G.508" -> "G.4";
     "G.509" -> "G.4";
     "G.510" -> "G.4";
     "G.511" -> "G.4";
     "G.512" -> "G.4";
     "G.519" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.502" -> "G.7";
     "G.503" -> "G.7";
     "G.504" -> "G.7";
     "G.505" -> "G.7";
     "G.506" -> "G.7";
     "G.507" -> "G.7";
     "G.508" -> "G.7";
     "G.509" -> "G.7";
     "G.510" -> "G.7";
     "G.511" -> "G.7";
     "G.512" -> "G.7";
     "G.519" -> "G.7";
     "G.530" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.502" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.61" -> "G.11";
     "G.502" -> "G.11";
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
     "G.51" -> "G.12";
     "G.53" -> "G.12";
     "G.60" -> "G.12";
     "G.62" -> "G.12";
     "G.503" -> "G.12";
     "G.508" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.34" -> "G.14";
     "G.41" -> "G.14";
     "G.51" -> "G.14";
     "G.60" -> "G.14";
     "G.503" -> "G.14";
     "G.508" -> "G.14";
     "G.510" -> "G.14";
     "G.512" -> "G.14";
     "G.530" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.40" -> "G.16";
     "G.54" -> "G.16";
     "G.56" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.53" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.40" -> "G.19";
     "G.54" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
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
     "G.37" -> "G.22";
     "G.40" -> "G.22";
     "G.41" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.54" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.60" -> "G.22";
     "G.62" -> "G.22";
     "G.512" -> "G.22";
     "G.530" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.60" -> "G.24";
     "G.62" -> "G.24";
     "G.506" -> "G.24";
     "G.508" -> "G.24";
     "G.530" -> "G.24";
     "G.28" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.51" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.506" -> "G.29";
     "G.508" -> "G.29";
     "G.512" -> "G.29";
     "G.31" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.40" -> "G.33";
     "G.54" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.505" -> "G.33";
     "G.506" -> "G.33";
     "G.507" -> "G.33";
     "G.508" -> "G.33";
     "G.510" -> "G.33";
     "G.511" -> "G.33";
     "G.37" -> "G.34";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.62" -> "G.36";
     "G.40" -> "G.37";
     "G.54" -> "G.37";
     "G.56" -> "G.37";
     "G.40" -> "G.38";
     "G.41" -> "G.40";
     "G.54" -> "G.40";
     "G.56" -> "G.40";
     "G.506" -> "G.40";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.62" -> "G.51";
     "G.506" -> "G.51";
     "G.53" -> "G.52";
     "G.54" -> "G.52";
     "G.56" -> "G.52";
     "G.60" -> "G.52";
     "G.62" -> "G.52";
     "G.508" -> "G.52";
     "G.509" -> "G.52";
     "G.510" -> "G.52";
     "G.511" -> "G.52";
     "G.512" -> "G.52";
     "G.519" -> "G.52";
     "G.530" -> "G.52";
     "G.54" -> "G.53";
     "G.60" -> "G.53";
     "G.508" -> "G.54";
     "G.56" -> "G.55";
     "G.60" -> "G.56";
     "G.62" -> "G.56";
     "G.510" -> "G.56";
     "G.512" -> "G.60";
     "G.62" -> "G.61";
     "G.502" -> "G.61";
     "G.530" -> "G.62";
     "G.253" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.502" -> "G.253";
     "G.503" -> "G.253";
     "G.503" -> "G.502";
     "G.519" -> "G.502";
     "G.508" -> "G.503";
     "G.510" -> "G.503";
     "G.507" -> "G.504";
     "G.509" -> "G.504";
     "G.506" -> "G.505";
     "G.507" -> "G.505";
     "G.508" -> "G.505";
     "G.510" -> "G.505";
     "G.511" -> "G.505";
     "G.507" -> "G.506";
     "G.510" -> "G.506";
     "G.511" -> "G.506";
     "G.508" -> "G.507";
     "G.511" -> "G.508";
     "G.510" -> "G.509";
     "G.511" -> "G.510";
     "G.512" -> "G.511";
     "G.530" -> "G.512";
     "G.519" -> "G.516";
     "G.530" -> "G.516";
     "G.530" -> "G.519";
     "G.530" -> "G.529";
   }

Required for
------------

:ref:`G.531 <G.531>`, :ref:`G.541 <G.541>`, :ref:`G.542 <G.542>`, :ref:`G.543 <G.543>`, :ref:`G.544 <G.544>`, :ref:`G.546 <G.546>`, :ref:`G.547 <G.547>`, :ref:`G.550 <G.550>`, :ref:`G.554 <G.554>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.560 <G.560>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`
