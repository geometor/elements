:order: 526
:number: 526
:canonical_id: G.526
:original_id: XI.21
:title: G.526 solid angle contained
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, triangle, solid-angle, plane-angle, right-angle, straight-line, trilateral, plane
:dependencies: G.22, G.32, G.59, G.524, G.525
:excerpt: Any solid angle is contained by plane angles less than four right angles.

.. _G.526:
.. _XI.21:

G.526 solid angle contained
===========================

.. rubric:: `XI.21 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/21/>`_

.. enunciation::

   Any :term:`solid angle <G.524>` is contained by :term:`plane angles <G.22>` less than four :term:`right angles <G.32>`.

.. signature:: theorem

   | :fn:`solid_angle_contained_xi_21 <G.526>`\ (:g:`A <g1:A>`, :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>`)
   | **given** the angle at :g:`A <g1:A>` be a solid angle contained by the plane angles :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>`
   | **prove** :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>` are less than four right angles

.. picture:: g1.svg
   :alt: Book XI, Proposition 21

.. step:: given

   the angle at :g:`A <g1:A>` be a solid angle contained by the plane angles :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>`

.. step:: construct

   :fn:`segment <G.13>`\ () → :g:`B <g1:B>`, :fn:`segment <G.13>`\ () → :g:`C <g1:C>`, :fn:`segment <G.13>`\ () → :g:`D <g1:D>`, :fn:`segment <G.13>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`, :fn:`segment <G.13>`\ (:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`, :fn:`segment <G.13>`\ (:g:`A <g1:A>`, :g:`D <g1:D>`) → :g:`/ A D / <g1:/ A D />`, :fn:`segment <G.13>`\ (:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`, :fn:`segment <G.13>`\ (:g:`C <g1:C>`, :g:`D <g1:D>`) → :g:`/ C D / <g1:/ C D />`, :fn:`segment <G.13>`\ (:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`

.. step:: assert

   Since the solid angle at :g:`B <g1:B>` is contained by the three plane angles :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>`, :g:`< C B D ) <g1:< C B D )>`,

.. step:: assert ∵ solid_angle_contained <G.525>

   Any two are greater than the remaining one; therefore :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>` are greater than :g:`< C B D ) <g1:< C B D )>`.

.. step:: assert

   For the same reason :g:`< B C A ) <g1:< B C A )>`, :g:`< A C D ) <g1:< A C D )>` are also greater than :g:`< B C D ) <g1:< B C D )>`, and :g:`< C D A ) <g1:< C D A )>`, :g:`< A D B ) <g1:< A D B )>` are greater than :g:`< C D B ) <g1:< C D B )>`; therefore the six angles :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>`, :g:`< B C A ) <g1:< B C A )>`, :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`, :g:`< A D B ) <g1:< A D B )>` are greater than the three angles :g:`< C B D ) <g1:< C B D )>`, :g:`< B C D ) <g1:< B C D )>`, :g:`< C D B ) <g1:< C D B )>`.

.. step:: assert ∵ triangle_angle_sum <G.59>

   The three angles :g:`< C B D ) <g1:< C B D )>`, :g:`< B D C ) <g1:< B D C )>`, :g:`< B C D ) <g1:< B C D )>` are equal to two right angles.

.. step:: assert

   Therefore the six angles :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>`, :g:`< B C A ) <g1:< B C A )>`, :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`, :g:`< A D B ) <g1:< A D B )>` are greater than two right angles.

.. step:: assert

   And, since the three angles of each of :g:`< A B C > <g1:< A B C >>`, :g:`< A C D > <g1:< A C D >>`, :g:`< A D B > <g1:< A D B >>` are equal to two right angles,

.. step:: assert

   Therefore the nine angles of the three :term:`triangles <G.11>`, :g:`< C B A ) <g1:< C B A )>`, :g:`< A C B ) <g1:< A C B )>`, :g:`< B A C ) <g1:< B A C )>`, :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< A D B ) <g1:< A D B )>`, :g:`< D B A ) <g1:< D B A )>`, :g:`< B A D ) <g1:< B A D )>` are equal to six right angles ;

.. step:: assert

   And of them the six angles :g:`< A B C ) <g1:< A B C )>`, :g:`< B C A ) <g1:< B C A )>`, :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`, :g:`< A D B ) <g1:< A D B )>`, :g:`< D B A ) <g1:< D B A )>` are greater than two right angles ;

.. step:: conclude

   Therefore the remaining three angles :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>` containing the solid angle are less than four right angles.

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
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.24): If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.25): If two triangles have two sides equal to two sides respectively, the one with the greater base has the greater included angle.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.524" [label="G.524", tooltip="G.524 (XI.def.11): Asolid angle is the inclination constituted by more than twolines which meet one another and are not in the samesurface, towards all the lines. Otherwise: Asolid angle is that whic...", fillcolor="#224422", URL="../G.524/index.html", target="_top"];
     "G.525" [label="G.525", tooltip="G.525 (XI.20): If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.", fillcolor="#222244", URL="../G.525/index.html", target="_top"];
     "G.526" [label="G.526", tooltip="G.526 (XI.21): Any solid angle is contained by plane angles less than four right angles.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.524" -> "G.1";
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
     "G.36" -> "G.4";
     "G.39" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.49" -> "G.4";
     "G.50" -> "G.4";
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.58" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.524" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.524" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.43" -> "G.11";
     "G.44" -> "G.11";
     "G.45" -> "G.11";
     "G.47" -> "G.11";
     "G.49" -> "G.11";
     "G.50" -> "G.11";
     "G.59" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
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
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.32" -> "G.22";
     "G.36" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.49" -> "G.22";
     "G.50" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.59" -> "G.22";
     "G.524" -> "G.22";
     "G.525" -> "G.22";
     "G.526" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.49" -> "G.24";
     "G.50" -> "G.24";
     "G.525" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.49" -> "G.25";
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
     "G.59" -> "G.32";
     "G.526" -> "G.32";
     "G.36" -> "G.33";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.39" -> "G.36";
     "G.56" -> "G.36";
     "G.59" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.56" -> "G.39";
     "G.41" -> "G.40";
     "G.45" -> "G.40";
     "G.43" -> "G.41";
     "G.53" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.49" -> "G.44";
     "G.47" -> "G.45";
     "G.525" -> "G.45";
     "G.48" -> "G.47";
     "G.49" -> "G.48";
     "G.58" -> "G.48";
     "G.50" -> "G.49";
     "G.525" -> "G.50";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.59" -> "G.56";
     "G.59" -> "G.58";
     "G.526" -> "G.59";
     "G.525" -> "G.524";
     "G.526" -> "G.524";
     "G.526" -> "G.525";
   }

.. toctree::
   :hidden:

   code
   heath
