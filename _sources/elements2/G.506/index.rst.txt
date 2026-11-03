:order: 506
:number: 506
:canonical_id: G.506
:original_id: XI.4
:title: G.506 segment set right
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, triangle, straight-line, right-angle, right-angles-to-plane, plane-angle, trilateral, plane-surface, plane, equality
:dependencies: G.1, G.4, G.7, G.24, G.29, G.33, G.40, G.51, G.505
:excerpt: If a segment be set up at right angles to two segments which cut one another, at their common point of section, it is at right angles to the plane through them.

.. _G.506:
.. _XI.4:

G.506 segment set right
=======================

.. rubric:: `XI.4 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/04/>`_

.. enunciation::

   If a :term:`segment <G.4>` be set up :term:`at right angles <G.33>` to two segments which cut one another, at their common :term:`point <G.1>` of section, it is :term:`at right angles to the plane <G.505>` through them.

.. signature:: theorem

   | :fn:`segment_set_right <G.506>`\ ()
   | **prove** :g:`/ E F / <g1:/ E F />` is also at right angles to the plane through :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Book XI, Proposition 4

.. step:: construct

   Let a segment :g:`/ E F / <g1:/ E F />` be set up at right angles to :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, which cut one another at :g:`E <g1:E>`, from :g:`E <g1:E>`

.. step:: construct

   Let :g:`/ A E / <g1:/ A E />`, :g:`/ E B / <g1:/ E B />`, :g:`/ C E / <g1:/ C E />`, :g:`/ E D / <g1:/ E D />` be cut off :eq:`equal <g1:/ A E / = g1:/ E B / = g1:/ C E / = g1:/ E D />` to one another

.. step:: construct

   Let any segment :g:`/ G E H / <g1:/ G E H />` be drawn across through :g:`E <g1:E>`, at random

.. step:: construct

   Let :g:`/ A D / <g1:/ A D />`, :g:`/ C B / <g1:/ C B />` be joined, and further let :g:`/ F A / <g1:/ F A />`, :g:`/ F G / <g1:/ F G />`, :g:`/ F D / <g1:/ F D />`, :g:`/ F C / <g1:/ F C />`, :g:`/ F H / <g1:/ F H />`, :g:`/ F B / <g1:/ F B />` be joined from :g:`F <g1:F>` taken at random &lt

.. step:: assert

   On :g:`/ E F / <g1:/ E F />` &gt

.. step:: assert

   

.. step:: assert ∵ vertical_angles_equal <G.40>

   :g:`/ A E / <g1:/ A E />`, :g:`/ E D / <g1:/ E D />` :eq:`= <g1:/ A E / = g1:/ C E /; g1:/ E D / = g1:/ E B />` :g:`/ C E / <g1:/ C E />`, :g:`/ E B / <g1:/ E B />`, and contain :eq:`= <g1:< A E D ) = g1:< C E B )>` angles

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, and :g:`< A E D > <g1:< A E D >>` will be :eq:`equal <g1:< A E D > = g1:< C E B >>` to :g:`< C E B > <g1:< C E B >>`; so that :g:`< D A E ) <g1:< D A E )>` :eq:`= <g1:< D A E ) = g1:< E B C )>` :g:`< E B C ) <g1:< E B C )>`

.. step:: assert ∵ vertical_angles_equal <G.40>

   :g:`< A E G ) <g1:< A E G )>` :eq:`= <g1:< A E G ) = g1:< B E H )>` :g:`< B E H ) <g1:< B E H )>`

.. step:: assert ∵ asa_aas_congruence <G.51>

   :g:`< A G E > <g1:< A G E >>`, :g:`< B E H > <g1:< B E H >>` are two triangles which have two angles :eq:`= <g1:< D A E ) = g1:< E B C ); g1:< A E G ) = g1:< B E H )>` to two angles, and one side :eq:`= <g1:/ A E / = g1:/ E B />` to one side, namely that adjacent to the :eq:`= <g1:< D A E ) = g1:< E B C ); g1:< A E G ) = g1:< B E H )>` angles, that is to say, :g:`/ A E / <g1:/ A E />` to :g:`/ E B / <g1:/ E B />`; therefore they will also have the remaining sides :eq:`= <g1:/ G E / = g1:/ E H /; g1:/ A G / = g1:/ B H />` to the remaining sides

.. step:: assert

   :g:`/ G E / <g1:/ G E />` :eq:`= <g1:/ G E / = g1:/ E H /; g1:/ A G / = g1:/ B H />` :g:`/ E H / <g1:/ E H />`, and :g:`/ A G / <g1:/ A G />` to :g:`/ B H / <g1:/ B H />`

.. step:: assert

   since :g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E B />` :g:`/ E B / <g1:/ E B />`, while :g:`/ F E / <g1:/ F E />` is common and at right angles,

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ F A / <g1:/ F A />` :eq:`= <g1:/ F A / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`

.. step:: assert

   For the same reason :g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ F D />` :g:`/ F D / <g1:/ F D />`

.. step:: assert

   since :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, and :g:`/ F A / <g1:/ F A />` :eq:`= <g1:/ F A / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ F A / = g1:/ F B /; g1:/ A D / = g1:/ B C />` :g:`/ F B / <g1:/ F B />`, :g:`/ B C / <g1:/ B C />`; and :g:`/ F D / <g1:/ F D />` :eq:`= <g1:/ F D / = g1:/ F C />` :g:`/ F C / <g1:/ F C />`

.. step:: assert ∵ sss_congruence <G.29>

   :g:`< F A D ) <g1:< F A D )>` :eq:`= <g1:< F A D ) = g1:< F B C )>` :g:`< F B C ) <g1:< F B C )>`

.. step:: assert

   Since, again, :g:`/ A G / <g1:/ A G />` :eq:`= <g1:/ A G / = g1:/ B H />` :g:`/ B H / <g1:/ B H />`, and further :g:`/ F A / <g1:/ F A />` :eq:`= <g1:/ F A / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ A G / <g1:/ A G />` :eq:`= <g1:/ F A / = g1:/ F B /; g1:/ A G / = g1:/ B H />` :g:`/ F B / <g1:/ F B />`, :g:`/ B H / <g1:/ B H />`. And :g:`< F A G ) <g1:< F A G )>` :eq:`= <g1:< F A G ) = g1:< F B H )>` :g:`< F B H ) <g1:< F B H )>`

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:/ F H />` :g:`/ F H / <g1:/ F H />`

.. step:: assert

   Now since, again, :g:`/ G E / <g1:/ G E />` :eq:`= <g1:/ G E / = g1:/ E H />` :g:`/ E H / <g1:/ E H />`, and :g:`/ E F / <g1:/ E F />` is common, :g:`/ G E / <g1:/ G E />`, :g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ G E / = g1:/ H E />` :g:`/ H E / <g1:/ H E />`, :g:`/ E F / <g1:/ E F />`; and :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:/ F H />` :g:`/ F H / <g1:/ F H />`

.. step:: assert ∵ sss_congruence <G.29>

   :g:`< G E F ) <g1:< G E F )>` :eq:`= <g1:< G E F ) = g1:< H E F )>` :g:`< H E F ) <g1:< H E F )>`

.. step:: assert

   each of :g:`< G E F ) <g1:< G E F )>`, :g:`< H E F ) <g1:< H E F )>` is :eq:`right <g1:< G E F ) = g1:< H E F )>`

.. step:: assert

   :g:`/ F E / <g1:/ F E />` is at :eq:`right angles <g1:< G E F ) = g1:< H E F )>` to :g:`/ G H / <g1:/ G H />` drawn at random through :g:`E <g1:E>`

.. step:: assert

   Similarly we can prove that :g:`/ F E / <g1:/ F E />` will also make right angles with all the segments which meet it and are in the :term:`plane <G.7>` of reference

.. step:: assert ∵ segment_right_angles_def <G.505>

   A segment is at right angles to a plane when it makes right angles with all the segments which meet it and are in that same plane

.. step:: assert

   :g:`/ F E / <g1:/ F E />` is at right angles to the plane of reference

.. step:: assert

   The plane of reference is the plane through :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`

.. step:: conclude

   :g:`/ F E / <g1:/ F E />` is at right angles to the plane through :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`

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
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.506" [label="G.506", tooltip="G.506 (XI.4): If a segment be set up at right angles to two segments which cut one another, at their common point of section, it is at right angles to the plane through them.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.505" -> "G.4";
     "G.506" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.505" -> "G.7";
     "G.506" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
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
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.40" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
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
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.506" -> "G.24";
     "G.28" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.506" -> "G.29";
     "G.31" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.40" -> "G.33";
     "G.505" -> "G.33";
     "G.506" -> "G.33";
     "G.37" -> "G.34";
     "G.37" -> "G.36";
     "G.40" -> "G.37";
     "G.40" -> "G.38";
     "G.41" -> "G.40";
     "G.506" -> "G.40";
     "G.51" -> "G.41";
     "G.506" -> "G.51";
     "G.506" -> "G.505";
   }

Required for
------------

:ref:`G.507 <G.507>`, :ref:`G.508 <G.508>`, :ref:`G.510 <G.510>`, :ref:`G.511 <G.511>`, :ref:`G.512 <G.512>`, :ref:`G.513 <G.513>`, :ref:`G.514 <G.514>`, :ref:`G.518 <G.518>`, :ref:`G.522 <G.522>`, :ref:`G.528 <G.528>`, :ref:`G.530 <G.530>`, :ref:`G.531 <G.531>`, :ref:`G.532 <G.532>`, :ref:`G.541 <G.541>`, :ref:`G.542 <G.542>`, :ref:`G.543 <G.543>`, :ref:`G.544 <G.544>`, :ref:`G.545 <G.545>`, :ref:`G.546 <G.546>`, :ref:`G.547 <G.547>`, :ref:`G.549 <G.549>`, :ref:`G.550 <G.550>`, :ref:`G.554 <G.554>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.560 <G.560>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.592 <G.592>`, :ref:`G.594 <G.594>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
