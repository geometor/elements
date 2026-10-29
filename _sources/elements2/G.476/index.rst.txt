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
:excerpt: Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

.. _G.476:
.. _XI.29:

G.476
=====

.. rubric:: `XI.29 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/29/>`_

.. enunciation::

   Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

Let :g:`< C M > <0337.g2:< C M >>`, :g:`< C N > <0337.g2:< C N >>` be parallelepipedal solids on the same base :g:`< A B > <0337.g2:< A B >>` and of the same height, and let the extremities of their sides which stand up, namely :g:`/ A G / <0337.g2:/ A G />`, :g:`/ A F / <0337.g2:/ A F />`, :g:`/ L M / <0337.g2:/ L M />`, :g:`/ L N / <0337.g2:/ L N />`, :g:`/ C D / <0337.g2:/ C D />`, :g:`/ C E / <0337.g2:/ C E />`, :g:`/ B H / <0337.g2:/ B H />`, :g:`/ B K / <0337.g2:/ B K />`, be on the same straight lines :g:`/ F N / <0337.g2:/ F N />`, :g:`/ D K / <0337.g2:/ D K />`; I say that the solid :g:`< C M > <0337.g2:< C M >>` is :eq:`equal <0337.g2:< C M > = 0337.g2:< C N >>` to the solid :g:`< C N > <0337.g2:< C N >>`.

.. picture:: 0337.g2.svg
   :alt: Proposition 29

.. subclause::

   For, since each of the figures :g:`< C H > <0337.g2:< C H >>`, :g:`< C K > <0337.g2:< C K >>` is a parallelogram, :g:`/ C B / <0337.g2:/ C B />` is :eq:`equal <0337.g2:/ C B / = 0337.g2:/ D H / = 0337.g2:/ E K />` to each of the straight lines :g:`/ D H / <0337.g2:/ D H />`, :g:`/ E K / <0337.g2:/ E K />`, :just:`[G.47] <G.47>`

.. assertion::

   hence :g:`/ D H / <0337.g2:/ D H />` is also :eq:`equal <0337.g2:/ D H / = 0337.g2:/ E K />` to :g:`/ E K / <0337.g2:/ E K />`.

Let :g:`/ E H / <0337.g2:/ E H />` be subtracted from each;

.. assertion::

   therefore the remainder :g:`/ D E / <0337.g2:/ D E />` is :eq:`equal <0337.g2:/ D E / = 0337.g2:/ H K />` to the remainder :g:`/ H K / <0337.g2:/ H K />`.

.. assertion::

   Hence the triangle :g:`< D C E > <0337.g2:< D C E >>` is also :eq:`equal <0337.g2:< D C E > = 0337.g2:< H B K >; 0337.g2:< D G > = 0337.g2:< H N >>` to the triangle :g:`< H B K > <0337.g2:< H B K >>`, :just:`[G.15, G.11] <G.15, G.11>` and the parallelogram :g:`< D G > <0337.g2:< D G >>` to the parallelogram :g:`< H N > <0337.g2:< H N >>`. :just:`[G.49] <G.49>`

.. assertion::

   For the same reason also the triangle :g:`< A F G > <0337.g2:< A F G >>` is also :eq:`equal <0337.g2:< A F G > = 0337.g2:< M L N >>` to the triangle :g:`< M L N > <0337.g2:< M L N >>`.

.. subclause::

   But the parallelogram :g:`< C F > <0337.g2:< C F >>` is :eq:`equal <0337.g2:< C F > = 0337.g2:< B M >; 0337.g2:< C G > = 0337.g2:< B N >>` to the parallelogram :g:`< B M > <0337.g2:< B M >>`, and :g:`< C G > <0337.g2:< C G >>` to :g:`< B N > <0337.g2:< B N >>`, for they are opposite;

.. assertion::

   therefore the prism contained by the two triangles :g:`< A F G > <0337.g2:< A F G >>`, :g:`< D C E > <0337.g2:< D C E >>` and the three parallelograms :g:`< A D > <0337.g2:< A D >>`, :g:`< D G > <0337.g2:< D G >>`, :g:`< C G > <0337.g2:< C G >>` is equal to the prism contained by the two triangles :g:`< M L N > <0337.g2:< M L N >>`, :g:`< H B K > <0337.g2:< H B K >>` and the three parallelograms :g:`< B M > <0337.g2:< B M >>`, :g:`< H N > <0337.g2:< H N >>`, :g:`< B N > <0337.g2:< B N >>`.

Let there be added to each the solid of which the parallelogram :g:`< A B > <0337.g2:< A B >>` is the base and :g:`< G E H M > <0337.g2:< G E H M >>` its opposite;

.. assertion::

   therefore the whole parallelepipedal solid :g:`< C M > <0337.g2:< C M >>` is :eq:`equal <0337.g2:< C M > = 0337.g2:< C N >>` to the whole parallelepipedal solid :g:`< C N > <0337.g2:< C N >>`.

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
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1): Things which are equal to the same thing are also equal to one another.", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another ;", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1): To draw a straight line from any point to any point.", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3): To describe a circle with any centre and distance.", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1): On a given finite straight line to construct an equilateral triangle.", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3): If equals be subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2): To produce a finite straight line continuously in a straight line.", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2): To place at a given point (as an extremity) a straight line equal to a given straight line.", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3): Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4): [7] 4. Things which coincide with one another are equal to one another.", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4): If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base...", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5): In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another...", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7): Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities),...", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8): If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal...", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.9): To bisect a given rectilineal angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): To bisect a given finite straight line.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is cal...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): To draw a straight line at right angles to a given straight line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals be added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): That all right angles are equal to one another.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): If two straight lines cut one another, they make the vertical angles equal to one another.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): [8] 5. The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of...", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet ...", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior an...", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms which are on the same base and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms which are on equal bases and in the same parallels are equal to one another.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.476" [label="G.476", tooltip="G.476 (XI.29): Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
