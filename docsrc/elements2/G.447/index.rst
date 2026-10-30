:order: 447
:number: 447
:canonical_id: G.447
:original_id: XI.4
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, triangle, right-angle, plane, equality
:dependencies: G.11, G.15, G.25, G.37, G.446
:excerpt: If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.

.. _G.447:
.. _XI.4:

G.447
=====

.. rubric:: `XI.4 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/04/>`_

.. enunciation::

   If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.

.. signature:: theorem

   | :fn:`straight_line_set <G.447>`\ ()
   | **prove** :g:`/ E F / <g1:/ E F />` is also at right angles to the plane through :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Book XI, Proposition 4

.. step:: construct

   Let a straight line :g:`/ E F / <g1:/ E F />` be set up at right angles to :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, which cut one another at :g:`E <g1:E>`, from :g:`E <g1:E>`

.. step:: construct

   Let :g:`/ A E / <g1:/ A E />`, :g:`/ E B / <g1:/ E B />`, :g:`/ C E / <g1:/ C E />`, :g:`/ E D / <g1:/ E D />` be cut off :eq:`equal <g1:/ A E / = g1:/ E B / = g1:/ C E / = g1:/ E D />` to one another

.. step:: construct

   Let any straight line :g:`/ G E H / <g1:/ G E H />` be drawn across through :g:`E <g1:E>`, at random

.. step:: construct

   Let :g:`/ A D / <g1:/ A D />`, :g:`/ C B / <g1:/ C B />` be joined, and further let :g:`/ F A / <g1:/ F A />`, :g:`/ F G / <g1:/ F G />`, :g:`/ F D / <g1:/ F D />`, :g:`/ F C / <g1:/ F C />`, :g:`/ F H / <g1:/ F H />`, :g:`/ F B / <g1:/ F B />` be joined from :g:`F <g1:F>` taken at random &lt

.. step:: assert

   On :g:`/ E F / <g1:/ E F />` &gt

.. step:: assert

   .

.. step:: assert ∵ vertical_angles_equal <G.25>

   Since :g:`/ A E / <g1:/ A E />`, :g:`/ E D / <g1:/ E D />` are :eq:`equal <g1:/ A E / = g1:/ C E /; g1:/ E D / = g1:/ E B />` to :g:`/ C E / <g1:/ C E />`, :g:`/ E B / <g1:/ E B />`, and contain :eq:`equal <g1:< A E D ) = g1:< C E B )>` angles.

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ C B />` to the base :g:`/ C B / <g1:/ C B />`, and :g:`< A E D > <g1:< A E D >>` will be :eq:`equal <g1:< A E D > = g1:< C E B >>` to :g:`< C E B > <g1:< C E B >>`; so that :g:`< D A E ) <g1:< D A E )>` is also :eq:`equal <g1:< D A E ) = g1:< E B C )>` to :g:`< E B C ) <g1:< E B C )>`.

.. step:: assert ∵ vertical_angles_equal <G.25>

   :g:`< A E G ) <g1:< A E G )>` is also :eq:`equal <g1:< A E G ) = g1:< B E H )>` to :g:`< B E H ) <g1:< B E H )>`;

.. step:: assert ∵ asa_aas_congruence <G.37>

   Therefore :g:`< A G E > <g1:< A G E >>`, :g:`< B E H > <g1:< B E H >>` are two triangles which have two angles :eq:`equal <g1:< D A E ) = g1:< E B C ); g1:< A E G ) = g1:< B E H )>` to two angles respectively, and one side :eq:`equal <g1:/ A E / = g1:/ E B />` to one side, namely that adjacent to the :eq:`equal <g1:< D A E ) = g1:< E B C ); g1:< A E G ) = g1:< B E H )>` angles, that is to say, :g:`/ A E / <g1:/ A E />` to :g:`/ E B / <g1:/ E B />`; therefore they will also have the remaining sides :eq:`equal <g1:/ G E / = g1:/ E H /; g1:/ A G / = g1:/ B H />` to the remaining sides.

.. step:: assert

   Therefore :g:`/ G E / <g1:/ G E />` is :eq:`equal <g1:/ G E / = g1:/ E H /; g1:/ A G / = g1:/ B H />` to :g:`/ E H / <g1:/ E H />`, and :g:`/ A G / <g1:/ A G />` to :g:`/ B H / <g1:/ B H />`.

.. step:: assert

   And, since :g:`/ A E / <g1:/ A E />` is :eq:`equal <g1:/ A E / = g1:/ E B />` to :g:`/ E B / <g1:/ E B />`, while :g:`/ F E / <g1:/ F E />` is common and at right angles,

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ F A / <g1:/ F A />` is :eq:`equal <g1:/ F A / = g1:/ F B />` to the base :g:`/ F B / <g1:/ F B />`.

.. step:: assert

   For the same reason :g:`/ F C / <g1:/ F C />` is also :eq:`equal <g1:/ F C / = g1:/ F D />` to :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   And, since :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ C B />` to :g:`/ C B / <g1:/ C B />`, and :g:`/ F A / <g1:/ F A />` is also :eq:`equal <g1:/ F A / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`, the two sides :g:`/ F A / <g1:/ F A />`, :g:`/ A D / <g1:/ A D />` are :eq:`equal <g1:/ F A / = g1:/ F B /; g1:/ A D / = g1:/ B C />` to the two sides :g:`/ F B / <g1:/ F B />`, :g:`/ B C / <g1:/ B C />` respectively; and the base :g:`/ F D / <g1:/ F D />` was proved :eq:`equal <g1:/ F D / = g1:/ F C />` to the base :g:`/ F C / <g1:/ F C />`;

.. step:: assert ∵ sss_congruence <G.15>

   Therefore :g:`< F A D ) <g1:< F A D )>` is also :eq:`equal <g1:< F A D ) = g1:< F B C )>` to :g:`< F B C ) <g1:< F B C )>`.

.. step:: assert

   Since, again, :g:`/ A G / <g1:/ A G />` was proved :eq:`equal <g1:/ A G / = g1:/ B H />` to :g:`/ B H / <g1:/ B H />`, and further :g:`/ F A / <g1:/ F A />` also :eq:`equal <g1:/ F A / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`, the two sides :g:`/ F A / <g1:/ F A />`, :g:`/ A G / <g1:/ A G />` are :eq:`equal <g1:/ F A / = g1:/ F B /; g1:/ A G / = g1:/ B H />` to the two sides :g:`/ F B / <g1:/ F B />`, :g:`/ B H / <g1:/ B H />`. And :g:`< F A G ) <g1:< F A G )>` was proved :eq:`equal <g1:< F A G ) = g1:< F B H )>` to :g:`< F B H ) <g1:< F B H )>`;

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ F G / <g1:/ F G />` is :eq:`equal <g1:/ F G / = g1:/ F H />` to the base :g:`/ F H / <g1:/ F H />`.

.. step:: assert

   Now since, again, :g:`/ G E / <g1:/ G E />` was proved :eq:`equal <g1:/ G E / = g1:/ E H />` to :g:`/ E H / <g1:/ E H />`, and :g:`/ E F / <g1:/ E F />` is common, the two sides :g:`/ G E / <g1:/ G E />`, :g:`/ E F / <g1:/ E F />` are :eq:`equal <g1:/ G E / = g1:/ H E />` to the two sides :g:`/ H E / <g1:/ H E />`, :g:`/ E F / <g1:/ E F />`; and the base :g:`/ F G / <g1:/ F G />` is :eq:`equal <g1:/ F G / = g1:/ F H />` to the base :g:`/ F H / <g1:/ F H />`;

.. step:: assert ∵ sss_congruence <G.15>

   Therefore :g:`< G E F ) <g1:< G E F )>` is :eq:`equal <g1:< G E F ) = g1:< H E F )>` to :g:`< H E F ) <g1:< H E F )>`.

.. step:: assert

   Therefore each of :g:`< G E F ) <g1:< G E F )>`, :g:`< H E F ) <g1:< H E F )>` is :eq:`right <g1:< G E F ) = g1:< H E F )>`.

.. step:: assert

   Therefore :g:`/ F E / <g1:/ F E />` is at :eq:`right angles <g1:< G E F ) = g1:< H E F )>` to :g:`/ G H / <g1:/ G H />` drawn at random through :g:`E <g1:E>`.

.. step:: assert

   Similarly we can prove that :g:`/ F E / <g1:/ F E />` will also make right angles with all the straight lines which meet it and are in the plane of reference.

.. step:: assert ∵ straight_line_right_def <G.446>

   A straight line is at right angles to a plane when it makes right angles with all the straight lines which meet it and are in that same plane.

.. step:: assert

   Therefore :g:`/ F E / <g1:/ F E />` is at right angles to the plane of reference.

.. step:: assert

   The plane of reference is the plane through :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

.. step:: conclude

   Therefore :g:`/ F E / <g1:/ F E />` is at right angles to the plane through :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all segments falling upon it from its center are equal.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1): Construct a segment between any two points.", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3): Construct a circle with any center and radius.", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1): Construct an equilateral triangle on a given finite segment.", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3): If equals are subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2): Extend a finite segment continuously in a straight line.", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2): Construct at a given point a segment equal to a given segment.", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3): Cut off from the greater of two unequal segments a segment equal to the less.", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4): Things that coincide with one another are equal.", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4): Triangles with two sides and the included angle equal are congruent (SAS).", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5): In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): Bisect a given finite segment.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line standing on a straight line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing line is perpendicular to that on which...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): Construct a line at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.27" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.8" -> "G.6";
     "G.25" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.27" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.27" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.447" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.447" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.447" -> "G.25";
     "G.27" -> "G.26";
     "G.37" -> "G.27";
     "G.447" -> "G.37";
     "G.447" -> "G.446";
   }

Required for
------------

:ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.454 <G.454>`, :ref:`G.455 <G.455>`, :ref:`G.459 <G.459>`, :ref:`G.463 <G.463>`, :ref:`G.468 <G.468>`, :ref:`G.469 <G.469>`, :ref:`G.470 <G.470>`, :ref:`G.471 <G.471>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.520 <G.520>`, :ref:`G.521 <G.521>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
