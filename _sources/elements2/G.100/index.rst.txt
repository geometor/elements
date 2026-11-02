:order: 100
:number: 100
:canonical_id: G.100
:original_id: III.3
:title: G.100 circle segment center
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, triangle, straight-line, centre, right-angle, plane-angle, trilateral, bisect, equality
:dependencies: G.4, G.10, G.14, G.25, G.28, G.32, G.51
:excerpt: If in a circle a segment through the center bisect a segment not through the center, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

.. _G.100:
.. _III.3:

G.100 circle segment center
===========================

.. rubric:: `III.3 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/03/>`_

.. enunciation::

   If in a :term:`circle <G.10>` a :term:`segment <G.4>` through the :term:`center <G.14>` bisect a segment not through the center, it also cuts it :term:`at right angles <G.32>`; and if it cut it at right angles, it also bisects it.

.. signature:: theorem

   | :fn:`circle_segment_center <G.100>`\ (:g:`( A B C ) <g1:( A B C )>`, :g:`/ C D / <g1:/ C D />`, :g:`/ A B / <g1:/ A B />`, :g:`F <g1:F>`)
   | **given** :g:`( A B C ) <g1:( A B C )>` be a circle, in it let a segment :g:`/ C D / <g1:/ C D />` through the center :eq:`bisect <g1:/ A F / = g1:/ F B />` a segment :g:`/ A B / <g1:/ A B />` not through the center at :g:`F <g1:F>`
   | **prove** it also cuts it at :eq:`right angles <g1:< A F E ) = g1:< B F E )>`; it also :eq:`bisects <g1:/ A F / = g1:/ F B />` it, that is, that :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`

.. picture:: g1.svg
   :alt: Proposition 3

.. step:: given

   :g:`( A B C ) <g1:( A B C )>` be a circle, in it let a segment :g:`/ C D / <g1:/ C D />` through the center :eq:`bisect <g1:/ A F / = g1:/ F B />` a segment :g:`/ A B / <g1:/ A B />` not through the center at :g:`F <g1:F>`

.. step:: construct

   Let the center of :g:`( A B C ) <g1:( A B C )>` be taken

.. step:: assert

   Let it be :g:`E <g1:E>`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`E <g1:E>`, :g:`A <g1:A>`) → :g:`/ E A / <g1:/ E A />`, :fn:`segment <G.13>`\ (:g:`E <g1:E>`, :g:`B <g1:B>`) → :g:`/ E B / <g1:/ E B />`

.. step:: assert

   Since :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`, and :g:`/ F E / <g1:/ F E />` is common → two sides are :eq:`equal <g1:/ A F / = g1:/ F B />` to two sides;

.. step:: assert

   And the base :g:`/ E A / <g1:/ E A />` is :eq:`equal <g1:/ E A / = g1:/ E B />` to the base :g:`/ E B / <g1:/ E B />`

.. step:: assert ∵ sss_congruence <G.28>

   Therefore :g:`< A F E ) <g1:< A F E )>` is :eq:`equal <g1:< A F E ) = g1:< B F E )>` to :g:`< B F E ) <g1:< B F E )>`.

.. step:: assert ∵ right_angle_perpendicular <G.32>

   But, when a segment set up on a segment makes the adjacent :term:`angles <G.22>` equal to one another, each of the equal angles is right

.. step:: assert

   Therefore each of :g:`< A F E ) <g1:< A F E )>`, :g:`< B F E ) <g1:< B F E )>` is :eq:`right <g1:< A F E ) = g1:< B F E )>`.

.. step:: assert

   Therefore :g:`/ C D / <g1:/ C D />`, which is through the center, and :eq:`bisects <g1:/ A F / = g1:/ F B />` :g:`/ A B / <g1:/ A B />` which is not through the center, also cuts it at :eq:`right angles <g1:< A F E ) = g1:< B F E )>`.

.. step:: assert

   Let :g:`/ C D / <g1:/ C D />` cut :g:`/ A B / <g1:/ A B />` at :eq:`right angles <g1:< A F E ) = g1:< B F E )>`

.. step:: assert

   With the same construction → since :g:`/ E A / <g1:/ E A />` is :eq:`equal <g1:/ E A / = g1:/ E B />` to :g:`/ E B / <g1:/ E B />`,

.. step:: assert ∵ isosceles_base_angles <G.25>

   :g:`< E A F ) <g1:< E A F )>` is also :eq:`equal <g1:< E A F ) = g1:< E B F )>` to :g:`< E B F ) <g1:< E B F )>`.

.. step:: assert

   The right angle :g:`< A F E ) <g1:< A F E )>` is :eq:`equal <g1:< A F E ) = g1:< B F E )>` to the right angle :g:`< B F E ) <g1:< B F E )>`, therefore :g:`< E A F > <g1:< E A F >>`, :g:`< E B F > <g1:< E B F >>` are two :term:`triangles <G.11>` having two angles :eq:`equal <g1:< E A F ) = g1:< E B F ); g1:< A F E ) = g1:< B F E )>` to two angles and one side equal to one side, namely :g:`/ E F / <g1:/ E F />`, which is common to them, and subtends one of the :eq:`equal <g1:< E A F ) = g1:< E B F )>` angles

.. step:: assert ∵ asa_aas_congruence <G.51>

   Therefore they will also have the remaining sides :eq:`equal <g1:/ A F / = g1:/ F B /; g1:/ E A / = g1:/ E B />` to the remaining sides

.. step:: conclude

   Therefore :g:`/ A F / <g1:/ A F />` is :eq:`equal <g1:/ A F / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`.

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
     "G.100" [label="G.100", tooltip="G.100 (III.3): If in a circle a segment through the center bisect a segment not through the center, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.100" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.100" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.51" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.100" -> "G.14";
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
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.32" -> "G.22";
     "G.36" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
     "G.51" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.27" -> "G.25";
     "G.100" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.100" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.100" -> "G.32";
     "G.36" -> "G.33";
     "G.36" -> "G.35";
     "G.39" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.41" -> "G.40";
     "G.51" -> "G.41";
     "G.100" -> "G.51";
   }

Required for
------------

:ref:`G.101 <G.101>`, :ref:`G.114 <G.114>`, :ref:`G.116 <G.116>`, :ref:`G.143 <G.143>`, :ref:`G.144 <G.144>`, :ref:`G.145 <G.145>`, :ref:`G.162 <G.162>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.574 <G.574>`

.. toctree::
   :hidden:

   code
   heath
