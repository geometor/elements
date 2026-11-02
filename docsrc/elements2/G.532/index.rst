:order: 532
:number: 532
:canonical_id: G.532
:original_id: XI.26
:title: G.532 segment point construct
:volume: III
:book: XI
:type: prop
:subtype: problem
:categories: problem, construction, solid-geometry
:category: problem, construction, solid-geometry
:tags: book-xi, point, segment, angle, straight-line, solid-angle, plane-angle, perpendicular, plane-surface, right-angles-to-plane, equality
:dependencies: G.1, G.4, G.24, G.28, G.48, G.505, G.513, G.514, G.524
:excerpt: On a given segment, and at a given point on it, to construct a solid angle equal to a given solid angle.

.. _G.532:
.. _XI.26:

G.532 segment point construct
=============================

.. rubric:: `XI.26 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/26/>`_

.. enunciation::

   On a given :term:`segment <G.4>`, and at a given :term:`point <G.1>` on it, to construct a :term:`solid angle <G.524>` equal to a given solid angle.

.. signature:: problem

   | :fn:`segment_point_construct <G.532>`\ (:g:`/ A B / <g1:/ A B />`, :g:`A <g1:A>`, :g:`D <g1:D>`, :g:`< E D C ) <g1:< E D C )>`) → :g:`< B A L ) <g1:< B A L )>`
   | **given** :g:`/ A B / <g1:/ A B />` , :g:`A <g1:A>` on it, the angle at :g:`D <g1:D>`, contained by :g:`< E D C ) <g1:< E D C )>`, :g:`< E D F ) <g1:< E D F )>`, :g:`< F D C ) <g1:< F D C )>`, the given solid angle
   | **construct** the solid angle at :g:`A <g1:A>`, contained by :g:`< B A L ) <g1:< B A L )>`, :g:`< B A H ) <g1:< B A H )>`, :g:`< H A L ) <g1:< H A L )>` is :eq:`equal <g1:< B A L ) = g1:< E D C ); g1:< B A H ) = g1:< E D F ); g1:< H A L ) = g1:< F D C )>` to the solid angle at :g:`D <g1:D>` contained by :g:`< E D C ) <g1:< E D C )>`, :g:`< E D F ) <g1:< E D F )>`, :g:`< F D C ) <g1:< F D C )>`

.. picture:: g1.svg
   :alt: Proposition 26

.. step:: given

   :g:`/ A B / <g1:/ A B />` , :g:`A <g1:A>` on it, the angle at :g:`D <g1:D>`, contained by :g:`< E D C ) <g1:< E D C )>`, :g:`< E D F ) <g1:< E D F )>`, :g:`< F D C ) <g1:< F D C )>`, the given solid angle

.. step:: construct

   **point**\ (:g:`/ D F / <g1:/ D F />`) → :g:`F <g1:F>`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`F <g1:F>`, :g:`G <g1:G>`) → :g:`/ F G / <g1:/ F G />`, :fn:`segment <G.13>`\ () → :g:`F <g1:F>`, :fn:`segment <G.13>`\ (:g:`E <g1:E>`, :g:`D <g1:D>`) → :g:`/ E D / <g1:/ E D />`, :fn:`segment <G.13>`\ (:g:`D <g1:D>`, :g:`C <g1:C>`) → :g:`/ D C / <g1:/ D C />`, :fn:`segment <G.13>`\ () → :g:`G <g1:G>`, :fn:`segment <G.13>`\ (:g:`D <g1:D>`, :g:`G <g1:G>`) → :g:`/ D G / <g1:/ D G />`

.. step:: construct

   :fn:`copy_angle <G.48>`: Let there be constructed on :g:`/ A B / <g1:/ A B />` and at :g:`A <g1:A>` on it :g:`< B A L ) <g1:< B A L )>` :eq:`equal <g1:< B A L ) = g1:< E D C )>` to :g:`< E D C ) <g1:< E D C )>`, and :g:`< B A K ) <g1:< B A K )>` :eq:`equal <g1:< B A K ) = g1:< E D G )>` to :g:`< E D G ) <g1:< E D G )>`, let :g:`/ A K / <g1:/ A K />` be made :eq:`equal <g1:/ A K / = g1:/ D G />` to :g:`/ D G / <g1:/ D G />`

.. step:: construct

   :fn:`set_segment_right <G.514>`: Let :g:`/ K H / <g1:/ K H />` be set up from :g:`K <g1:K>` at right angles to the plane through :g:`/ B A / <g1:/ B A />`, :g:`/ A L / <g1:/ A L />`, let :g:`/ K H / <g1:/ K H />` be made :eq:`equal <g1:/ K H / = g1:/ G F />` to :g:`/ G F / <g1:/ G F />`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`H <g1:H>`, :g:`A <g1:A>`) → :g:`/ H A / <g1:/ H A />`

.. step:: construct

   Let :g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />` be cut off :eq:`equal <g1:/ A B / = g1:/ D E />` to one another

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`H <g1:H>`, :g:`B <g1:B>`) → :g:`/ H B / <g1:/ H B />`, :fn:`segment <G.13>`\ (:g:`K <g1:K>`, :g:`B <g1:B>`) → :g:`/ K B / <g1:/ K B />`, :fn:`segment <G.13>`\ (:g:`F <g1:F>`, :g:`E <g1:E>`) → :g:`/ F E / <g1:/ F E />`, :fn:`segment <G.13>`\ (:g:`G <g1:G>`, :g:`E <g1:E>`) → :g:`/ G E / <g1:/ G E />`

.. step:: assert ∵ segment_right_angles_def <G.505>

   Since :g:`/ F G / <g1:/ F G />` is :term:`at right angles to the plane <G.505>` of reference, it will also make :term:`right angles <G.32>` with all the segments which meet it and are in the :term:`plane <G.7>` of reference .

.. step:: assert

   Therefore each of :g:`< F G D ) <g1:< F G D )>`, :g:`< F G E ) <g1:< F G E )>` is :eq:`right <g1:< F G D ) = g1:< F G E )>`.

.. step:: assert

   For the same reason each of :g:`< H K A ) <g1:< H K A )>`, :g:`< H K B ) <g1:< H K B )>` is also :eq:`right <g1:< H K A ) = g1:< H K B )>`.

.. step:: assert

   And, since the two sides :g:`/ K A / <g1:/ K A />`, :g:`/ A B / <g1:/ A B />` are :eq:`equal <g1:/ K A / = g1:/ G D /; g1:/ A B / = g1:/ D E />` to the two sides :g:`/ G D / <g1:/ G D />`, :g:`/ D E / <g1:/ D E />` respectively, and they contain equal :term:`angles <G.22>`,

.. step:: assert ∵ sas_congruence <G.24>

   Therefore the base :g:`/ K B / <g1:/ K B />` is :eq:`equal <g1:/ K B / = g1:/ G E />` to the base :g:`/ G E / <g1:/ G E />`.

.. step:: assert

   :g:`/ K H / <g1:/ K H />` is also :eq:`equal <g1:/ K H / = g1:/ G F />` to :g:`/ G F / <g1:/ G F />`, and they contain right angles ;

.. step:: assert ∵ sas_congruence <G.24>

   Therefore :g:`/ H B / <g1:/ H B />` is also :eq:`equal <g1:/ H B / = g1:/ F E />` to :g:`/ F E / <g1:/ F E />`.

.. step:: assert

   Since the two sides :g:`/ A K / <g1:/ A K />`, :g:`/ K H / <g1:/ K H />` are :eq:`equal <g1:/ A K / = g1:/ D G /; g1:/ K H / = g1:/ G F />` to the two sides :g:`/ D G / <g1:/ D G />`, :g:`/ G F / <g1:/ G F />`, and they contain right angles,

.. step:: assert ∵ sas_congruence <G.24>

   Therefore the base :g:`/ A H / <g1:/ A H />` is :eq:`equal <g1:/ A H / = g1:/ F D />` to the base :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is also :eq:`equal <g1:/ A B / = g1:/ D E />` to :g:`/ D E / <g1:/ D E />` ;

.. step:: assert

   Therefore the two sides :g:`/ H A / <g1:/ H A />`, :g:`/ A B / <g1:/ A B />` are :eq:`equal <g1:/ H A / = g1:/ D F /; g1:/ A B / = g1:/ D E />` to the two sides :g:`/ D F / <g1:/ D F />`, :g:`/ D E / <g1:/ D E />`.

.. step:: assert

   The base :g:`/ H B / <g1:/ H B />` is :eq:`equal <g1:/ H B / = g1:/ F E />` to the base :g:`/ F E / <g1:/ F E />` ;

.. step:: assert ∵ sss_congruence <G.28>

   Therefore :g:`< B A H ) <g1:< B A H )>` is :eq:`equal <g1:< B A H ) = g1:< E D F )>` to :g:`< E D F ) <g1:< E D F )>`.

.. step:: assert

   For the same reason :g:`< H A L ) <g1:< H A L )>` is also :eq:`equal <g1:< H A L ) = g1:< F D C )>` to :g:`< F D C ) <g1:< F D C )>`.

.. step:: conclude

   :g:`< B A L ) <g1:< B A L )>` is also :eq:`equal <g1:< B A L ) = g1:< E D C )>` to :g:`< E D C ) <g1:< E D C )>`.

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
     "G.34" [label="G.34", tooltip="G.34 (I.12): Construct a perpendicular to a given line from a given point not on it.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
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
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.502" [label="G.502", tooltip="G.502 (XI.1): A part of a segment cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.502/index.html", target="_top"];
     "G.503" [label="G.503", tooltip="G.503 (XI.2): If two segments cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.503/index.html", target="_top"];
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", fillcolor="#222244", URL="../G.504/index.html", target="_top"];
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.506" [label="G.506", tooltip="G.506 (XI.4): If a segment be set up at right angles to two segments which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.506/index.html", target="_top"];
     "G.509" [label="G.509", tooltip="G.509 (XI.7): If two segments be parallel and points be taken at random on each of them, the segment joining the points is in the same plane with the parallel lines.", fillcolor="#222244", URL="../G.509/index.html", target="_top"];
     "G.510" [label="G.510", tooltip="G.510 (XI.8): If two segments be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.510/index.html", target="_top"];
     "G.513" [label="G.513", tooltip="G.513 (XI.11): From a given elevated point to draw a segment perpendicular to a given plane.", fillcolor="#222244", URL="../G.513/index.html", target="_top"];
     "G.514" [label="G.514", tooltip="G.514 (XI.12): To set up a segment at right angles to a given plane from a given point in it.", fillcolor="#222244", URL="../G.514/index.html", target="_top"];
     "G.524" [label="G.524", tooltip="G.524 (XI.def.11): Asolid angle is the inclination constituted by more than twolines which meet one another and are not in the samesurface, towards all the lines. Otherwise: Asolid angle is that whic...", fillcolor="#224422", URL="../G.524/index.html", target="_top"];
     "G.532" [label="G.532", tooltip="G.532 (XI.26): On a given segment, and at a given point on it, to construct a solid angle equal to a given solid angle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.34" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.506" -> "G.1";
     "G.509" -> "G.1";
     "G.513" -> "G.1";
     "G.514" -> "G.1";
     "G.524" -> "G.1";
     "G.532" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.524" -> "G.2";
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
     "G.34" -> "G.4";
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
     "G.502" -> "G.4";
     "G.503" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.506" -> "G.4";
     "G.509" -> "G.4";
     "G.510" -> "G.4";
     "G.513" -> "G.4";
     "G.514" -> "G.4";
     "G.532" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.524" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.502" -> "G.7";
     "G.503" -> "G.7";
     "G.504" -> "G.7";
     "G.505" -> "G.7";
     "G.509" -> "G.7";
     "G.510" -> "G.7";
     "G.513" -> "G.7";
     "G.514" -> "G.7";
     "G.524" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.502" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.43" -> "G.11";
     "G.44" -> "G.11";
     "G.45" -> "G.11";
     "G.47" -> "G.11";
     "G.51" -> "G.11";
     "G.503" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.34" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.61" -> "G.14";
     "G.502" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.34" -> "G.15";
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
     "G.524" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.506" -> "G.24";
     "G.532" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.34" -> "G.28";
     "G.48" -> "G.28";
     "G.506" -> "G.28";
     "G.532" -> "G.28";
     "G.30" -> "G.29";
     "G.48" -> "G.29";
     "G.31" -> "G.30";
     "G.34" -> "G.31";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.34" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.55" -> "G.32";
     "G.56" -> "G.32";
     "G.505" -> "G.32";
     "G.506" -> "G.32";
     "G.510" -> "G.32";
     "G.513" -> "G.32";
     "G.514" -> "G.32";
     "G.36" -> "G.33";
     "G.513" -> "G.33";
     "G.513" -> "G.34";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.39" -> "G.36";
     "G.56" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.56" -> "G.39";
     "G.506" -> "G.39";
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
     "G.532" -> "G.48";
     "G.506" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.509" -> "G.52";
     "G.510" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.510" -> "G.56";
     "G.513" -> "G.58";
     "G.514" -> "G.58";
     "G.502" -> "G.61";
     "G.253" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.502" -> "G.253";
     "G.503" -> "G.502";
     "G.510" -> "G.503";
     "G.509" -> "G.504";
     "G.506" -> "G.505";
     "G.510" -> "G.505";
     "G.513" -> "G.505";
     "G.532" -> "G.505";
     "G.510" -> "G.506";
     "G.513" -> "G.506";
     "G.510" -> "G.509";
     "G.513" -> "G.510";
     "G.514" -> "G.510";
     "G.514" -> "G.513";
     "G.532" -> "G.513";
     "G.532" -> "G.514";
     "G.532" -> "G.524";
   }

.. toctree::
   :hidden:

   code
   heath
