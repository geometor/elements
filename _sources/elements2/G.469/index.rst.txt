:order: 469
:number: 469
:canonical_id: G.469
:original_id: XI.24
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, segment, angle, triangle, quadrilateral, polygon, parallel, parallelogram, plane, equality
:dependencies: G.11, G.47, G.453, G.460
:excerpt: If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

.. _G.469:
.. _XI.24:

G.469
=====

.. rubric:: `XI.24 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/24/>`_

.. enunciation::

   If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

.. signature:: theorem

   | :fn:`solid_contained_parallel <G.469>`\ ()
   | **prove** the opposite planes in it are equal and parallelogrammic

.. picture:: g1.svg
   :alt: Proposition 24 figure

.. step:: assert

   Let the solid :g:`< C D H G > <g1:< C D H G >>` be contained by the parallel planes :g:`< A C > <g1:< A C >>`, :g:`< G F > <g1:< G F >>`, :g:`< A H > <g1:< A H >>`, :g:`< D F > <g1:< D F >>`, :g:`< B F > <g1:< B F >>`, :g:`< A E > <g1:< A E >>`

.. step:: assert

   Since the two parallel planes :g:`< B G > <g1:< B G >>`, :g:`< C E > <g1:< C E >>` are cut by the plane :g:`< A C > <g1:< A C >>`,

.. step:: assert ∵ parallel_planes_cut <G.460>

   Their common sections are parallel.

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is parallel to :g:`/ D C / <g1:/ D C />`.

.. step:: assert

   Since the two parallel planes :g:`< B F > <g1:< B F >>`, :g:`< A E > <g1:< A E >>` are cut by the plane :g:`< A C > <g1:< A C >>`,

.. step:: assert ∵ parallel_planes_cut <G.460>

   Their common sections are parallel.

.. step:: assert

   Therefore :g:`/ B C / <g1:/ B C />` is parallel to :g:`/ A D / <g1:/ A D />`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` was also proved parallel to :g:`/ D C / <g1:/ D C />`;

.. step:: assert

   Therefore :g:`< A C > <g1:< A C >>` is a parallelogram.

.. step:: assert

   Similarly we can prove that each of the planes :g:`< D F > <g1:< D F >>`, :g:`< F G > <g1:< F G >>`, :g:`< G B > <g1:< G B >>`, :g:`< B F > <g1:< B F >>`, :g:`< A E > <g1:< A E >>` is a parallelogram.

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`H <g1:H>`) → :g:`/ A H / <g1:/ A H />`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`F <g1:F>`) → :g:`/ D F / <g1:/ D F />`

.. step:: assert

   Since :g:`/ A B / <g1:/ A B />` is parallel to :g:`/ D C / <g1:/ D C />`, and :g:`/ B H / <g1:/ B H />` to :g:`/ C F / <g1:/ C F />`, :g:`/ A B / <g1:/ A B />`, :g:`/ B H / <g1:/ B H />` which meet one another are parallel to :g:`/ D C / <g1:/ D C />`, :g:`/ C F / <g1:/ C F />` which meet one another, not in the same plane;

.. step:: assert ∵ straight_lines_meeting <G.453>

   Therefore they will contain equal angles; therefore :g:`< A B H ) <g1:< A B H )>` is :eq:`equal <g1:< A B H ) = g1:< D C F )>` to :g:`< D C F ) <g1:< D C F )>`.

.. step:: assert ∵ parallelogram_properties <G.47>

   And, since the two sides :g:`/ A B / <g1:/ A B />`, :g:`/ B H / <g1:/ B H />` are :eq:`equal <g1:/ A B / = g1:/ D C /; g1:/ B H / = g1:/ C F />` to the two sides :g:`/ D C / <g1:/ D C />`, :g:`/ C F / <g1:/ C F />`, and :g:`< A B H ) <g1:< A B H )>` is :eq:`equal <g1:< A B H ) = g1:< D C F )>` to :g:`< D C F ) <g1:< D C F )>`.

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ A H / <g1:/ A H />` is :eq:`equal <g1:/ A H / = g1:/ D F />` to the base :g:`/ D F / <g1:/ D F />`, and :g:`< A B H > <g1:< A B H >>` is :eq:`equal <g1:< A B H > = g1:< D C F >>` to :g:`< D C F > <g1:< D C F >>`.

.. step:: assert ∵ parallelogram_properties <G.47>

   The parallelogram :g:`< B G > <g1:< B G >>` is double of :g:`< A B H > <g1:< A B H >>`, and the parallelogram :g:`< C E > <g1:< C E >>` double of :g:`< D C F > <g1:< D C F >>`.

.. step:: assert

   Therefore the parallelogram :g:`< B G > <g1:< B G >>` is :eq:`equal <g1:< B G > = g1:< C E >>` to the parallelogram :g:`< C E > <g1:< C E >>`.

.. step:: conclude

   Similarly we can prove that :g:`< A C > <g1:< A C >>` is also :eq:`equal <g1:< A C > = g1:< G F >; g1:< A E > = g1:< B F >>` to :g:`< G F > <g1:< G F >>`, and :g:`< A E > <g1:< A E >>` to :g:`< B F > <g1:< B F >>`.

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
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.448" [label="G.448", tooltip="G.448 (XI.5): If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.", fillcolor="#222244", URL="../G.448/index.html", target="_top"];
     "G.449" [label="G.449", tooltip="G.449 (XI.6): If two straight lines be at right angles to the same plane, the straight lines is parallel.", fillcolor="#222244", URL="../G.449/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.452" [label="G.452", tooltip="G.452 (XI.9): Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.", fillcolor="#222244", URL="../G.452/index.html", target="_top"];
     "G.453" [label="G.453", tooltip="G.453 (XI.10): If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.", fillcolor="#222244", URL="../G.453/index.html", target="_top"];
     "G.460" [label="G.460", tooltip="G.460 (XI.16): If two parallel planes be cut by any plane, their common sections are parallel.", fillcolor="#222244", URL="../G.460/index.html", target="_top"];
     "G.469" [label="G.469", tooltip="G.469 (XI.24): If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
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
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.447" -> "G.11";
     "G.449" -> "G.11";
     "G.469" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.447" -> "G.15";
     "G.449" -> "G.15";
     "G.453" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.25" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.447" -> "G.25";
     "G.27" -> "G.26";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.47" -> "G.37";
     "G.447" -> "G.37";
     "G.39" -> "G.38";
     "G.460" -> "G.38";
     "G.40" -> "G.39";
     "G.46" -> "G.39";
     "G.449" -> "G.40";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.451" -> "G.42";
     "G.453" -> "G.46";
     "G.469" -> "G.47";
     "G.444" -> "G.443";
     "G.460" -> "G.443";
     "G.449" -> "G.444";
     "G.451" -> "G.444";
     "G.448" -> "G.445";
     "G.450" -> "G.445";
     "G.447" -> "G.446";
     "G.448" -> "G.446";
     "G.449" -> "G.446";
     "G.451" -> "G.446";
     "G.448" -> "G.447";
     "G.451" -> "G.447";
     "G.452" -> "G.447";
     "G.449" -> "G.448";
     "G.452" -> "G.449";
     "G.451" -> "G.450";
     "G.452" -> "G.451";
     "G.453" -> "G.452";
     "G.469" -> "G.453";
     "G.469" -> "G.460";
   }

Required for
------------

:ref:`G.470 <G.470>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.486 <G.486>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`

.. toctree::
   :hidden:

   code
   heath
