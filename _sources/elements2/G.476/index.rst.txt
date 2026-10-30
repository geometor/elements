:order: 476
:number: 476
:canonical_id: G.476
:original_id: XI.29
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, segment, triangle, quadrilateral, polygon, parallelepiped, equality
:dependencies: G.11, G.15, G.47, G.49
:excerpt: Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal.

.. _G.476:
.. _XI.29:

G.476
=====

.. rubric:: `XI.29 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/29/>`_

.. enunciation::

   Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal.

.. signature:: theorem

   | :fn:`parallelepipedal_solids_base <G.476>`\ (:g:`< C M > <g1:< C M >>`, :g:`< C N > <g1:< C N >>`, :g:`< A B > <g1:< A B >>`, :g:`/ A G / <g1:/ A G />`)
   | **given** :g:`< C M > <g1:< C M >>`, :g:`< C N > <g1:< C N >>` be parallelepipedal solids on the same base :g:`< A B > <g1:< A B >>` and of the same height, let the extremities of their sides which stand up, namely :g:`/ A G / <g1:/ A G />`, :g:`/ A F / <g1:/ A F />`, :g:`/ L M / <g1:/ L M />`, :g:`/ L N / <g1:/ L N />`, :g:`/ C D / <g1:/ C D />`, :g:`/ C E / <g1:/ C E />`, :g:`/ B H / <g1:/ B H />`, :g:`/ B K / <g1:/ B K />`, be on the same straight lines :g:`/ F N / <g1:/ F N />`, :g:`/ D K / <g1:/ D K />`
   | **prove** the solid :g:`< C M > <g1:< C M >>` is :eq:`equal <g1:< C M > = g1:< C N >>` to the solid :g:`< C N > <g1:< C N >>`

.. picture:: g1.svg
   :alt: Proposition 29

.. step:: given

   :g:`< C M > <g1:< C M >>`, :g:`< C N > <g1:< C N >>` be parallelepipedal solids on the same base :g:`< A B > <g1:< A B >>` and of the same height, let the extremities of their sides which stand up, namely :g:`/ A G / <g1:/ A G />`, :g:`/ A F / <g1:/ A F />`, :g:`/ L M / <g1:/ L M />`, :g:`/ L N / <g1:/ L N />`, :g:`/ C D / <g1:/ C D />`, :g:`/ C E / <g1:/ C E />`, :g:`/ B H / <g1:/ B H />`, :g:`/ B K / <g1:/ B K />`, be on the same straight lines :g:`/ F N / <g1:/ F N />`, :g:`/ D K / <g1:/ D K />`

.. step:: assert ∵ parallelogram_properties <G.47>

   Since each of the figures :g:`< C H > <g1:< C H >>`, :g:`< C K > <g1:< C K >>` is a parallelogram, :g:`/ C B / <g1:/ C B />` is :eq:`equal <g1:/ C B / = g1:/ D H / = g1:/ E K />` to each of :g:`/ D H / <g1:/ D H />`, :g:`/ E K / <g1:/ E K />`.

.. step:: assert

   Hence :g:`/ D H / <g1:/ D H />` is also :eq:`equal <g1:/ D H / = g1:/ E K />` to :g:`/ E K / <g1:/ E K />`.

.. step:: construct

   Let :g:`/ E H / <g1:/ E H />` be subtracted from each

.. step:: assert

   Therefore the remainder :g:`/ D E / <g1:/ D E />` is :eq:`equal <g1:/ D E / = g1:/ H K />` to the remainder :g:`/ H K / <g1:/ H K />`.

.. step:: assert ∵ sss_congruence, sas_congruence, parallelograms_equal_bases <G.15, G.11, G.49>

   Hence :g:`< D C E > <g1:< D C E >>` is also :eq:`equal <g1:< D C E > = g1:< H B K >; g1:< D G > = g1:< H N >>` to :g:`< H B K > <g1:< H B K >>`, and the parallelogram :g:`< D G > <g1:< D G >>` to the parallelogram :g:`< H N > <g1:< H N >>`.

.. step:: assert

   For the same reason also :g:`< A F G > <g1:< A F G >>` is also :eq:`equal <g1:< A F G > = g1:< M L N >>` to :g:`< M L N > <g1:< M L N >>`.

.. step:: assert

   The parallelogram :g:`< C F > <g1:< C F >>` is :eq:`equal <g1:< C F > = g1:< B M >; g1:< C G > = g1:< B N >>` to the parallelogram :g:`< B M > <g1:< B M >>`, and :g:`< C G > <g1:< C G >>` to :g:`< B N > <g1:< B N >>`, for they are opposite;

.. step:: assert

   Therefore the prism contained by the two triangles :g:`< A F G > <g1:< A F G >>`, :g:`< D C E > <g1:< D C E >>` and the three parallelograms :g:`< A D > <g1:< A D >>`, :g:`< D G > <g1:< D G >>`, :g:`< C G > <g1:< C G >>` is equal to the prism contained by the two triangles :g:`< M L N > <g1:< M L N >>`, :g:`< H B K > <g1:< H B K >>` and the three parallelograms :g:`< B M > <g1:< B M >>`, :g:`< H N > <g1:< H N >>`, :g:`< B N > <g1:< B N >>`.

.. step:: construct

   Let there be added to each the solid of which the parallelogram :g:`< A B > <g1:< A B >>` is the base and :g:`< G E H M > <g1:< G E H M >>` its opposite

.. step:: conclude

   Therefore the whole parallelepipedal solid :g:`< C M > <g1:< C M >>` is :eq:`equal <g1:< C M > = g1:< C N >>` to the whole parallelepipedal solid :g:`< C N > <g1:< C N >>`.

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
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.476" [label="G.476", tooltip="G.476 (XI.29): Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
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
     "G.48" -> "G.6";
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
     "G.48" -> "G.11";
     "G.476" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.476" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.46" -> "G.39";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.476" -> "G.47";
     "G.49" -> "G.48";
     "G.476" -> "G.49";
   }

Required for
------------

:ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.486 <G.486>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`

.. toctree::
   :hidden:

   code
   heath
