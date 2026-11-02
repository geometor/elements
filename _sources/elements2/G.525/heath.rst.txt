:canonical_id: G.525
:original_id: XI.20
:title: G.525 solid angle contained
:volume: III
:book: XI
:type: prop

G.525 solid angle contained — Heath
===================================

.. rubric:: `XI.20 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/20/>`_

.. enunciation::

   If a :term:`solid angle <G.524>` be contained by three :term:`plane angles <G.22>`, any two, taken together in any manner, are greater than the remaining one.

For let the solid angle at :g:`A <g1:A>` be contained by the three plane angles :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>`; I say that any two of the angles :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>`, taken together in any manner, are greater than the remaining one.

.. picture:: g1.svg
   :alt: Book XI, Proposition 20

.. subclause::

   If now the angles :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>` are :eq:`equal <g1:< B A C ) = g1:< C A D ) = g1:< D A B )>` to one another,

.. assertion::

   it is manifest that any two are greater than the remaining one.

.. subclause::

   But, if not, let :g:`< B A C ) <g1:< B A C )>` be greater,

and on the :term:`straight line <G.4>` :g:`/ A B / <g1:/ A B />`, and at the :term:`point <G.1>` :g:`A <g1:A>` on it, let the
angle :g:`< B A E ) <g1:< B A E )>` be constructed, in the :term:`plane <G.7>` through :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`, :eq:`equal <g1:< B A E ) = g1:< D A B )>` to the angle :g:`< D A B ) <g1:< D A B )>`; let :g:`/ A E / <g1:/ A E />` be made :eq:`equal <g1:/ A E / = g1:/ A D />` to :g:`/ A D / <g1:/ A D />`, and let :g:`/ B E C / <g1:/ B E C />`, drawn across through the point :g:`E <g1:E>`, cut the straight lines :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />` at the points :g:`B <g1:B>`, :g:`C <g1:C>`; let :g:`/ D B / <g1:/ D B />`, :g:`/ D C / <g1:/ D C />` be joined.

.. subclause::

   Now, since :g:`/ D A / <g1:/ D A />` is :eq:`equal <g1:/ D A / = g1:/ A E />` to :g:`/ A E / <g1:/ A E />`, and :g:`/ A B / <g1:/ A B />` is common, two sides are :eq:`equal <g1:/ D A / = g1:/ A E />` to two sides ; and the angle :g:`< D A B ) <g1:< D A B )>` is :eq:`equal <g1:< D A B ) = g1:< B A E )>` to the angle :g:`< B A E ) <g1:< B A E )>`;

.. assertion:: [G.24] <G.24>

   therefore the base :g:`/ D B / <g1:/ D B />` is :eq:`equal <g1:/ D B / = g1:/ B E />` to the base :g:`/ B E / <g1:/ B E />`.

.. subclause::

   And, since the two sides :g:`/ B D / <g1:/ B D />`, :g:`/ D C / <g1:/ D C />` are greater than :g:`/ B C / <g1:/ B C />`, :just:`[G.45] <G.45>` and of these :g:`/ D B / <g1:/ D B />` was proved :eq:`equal <g1:/ D B / = g1:/ B E />` to :g:`/ B E / <g1:/ B E />`,

.. assertion::

   therefore the remainder :g:`/ D C / <g1:/ D C />` is greater than the remainder :g:`/ E C / <g1:/ E C />`.

.. subclause::

   Now, since :g:`/ D A / <g1:/ D A />` is :eq:`equal <g1:/ D A / = g1:/ A E />` to :g:`/ A E / <g1:/ A E />`, and :g:`/ A C / <g1:/ A C />` is common, and the base :g:`/ D C / <g1:/ D C />` is greater than the base :g:`/ E C / <g1:/ E C />`,

.. assertion::

   therefore the angle :g:`< D A C ) <g1:< D A C )>` is greater than the angle :g:`< E A C ) <g1:< E A C )>`. :just:`[G.50] <G.50>`

.. subclause::

   But the angle :g:`< D A B ) <g1:< D A B )>` was also proved :eq:`equal <g1:< D A B ) = g1:< B A E )>` to the angle :g:`< B A E ) <g1:< B A E )>` ;

.. assertion::

   therefore the angles :g:`< D A B ) <g1:< D A B )>`, :g:`< D A C ) <g1:< D A C )>` are greater than the angle :g:`< B A C ) <g1:< B A C )>`.

Similarly we can prove that the remaining angles also, taken together two and two, are greater than the remaining one.

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
     "G.524" [label="G.524", tooltip="G.524 (XI.def.11): Asolid angle is the inclination constituted by more than twolines which meet one another and are not in the samesurface, towards all the lines. Otherwise: Asolid angle is that whic...", fillcolor="#224422", URL="../G.524/index.html", target="_top"];
     "G.525" [label="G.525", tooltip="G.525 (XI.20): If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.524" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
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
     "G.524" -> "G.22";
     "G.525" -> "G.22";
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
     "G.36" -> "G.33";
     "G.36" -> "G.35";
     "G.39" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.41" -> "G.40";
     "G.45" -> "G.40";
     "G.43" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.49" -> "G.44";
     "G.47" -> "G.45";
     "G.525" -> "G.45";
     "G.48" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.49";
     "G.525" -> "G.50";
     "G.525" -> "G.524";
   }

Required for
------------

:ref:`G.526 <G.526>`
