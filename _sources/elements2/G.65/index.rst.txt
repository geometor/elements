:order: 65
:number: 65
:canonical_id: G.65
:original_id: II.4
:volume: I
:book: II
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, geometric-algebra
:category: theorem, proof, plane-geometry, geometric-algebra
:tags: book-ii, point, segment, angle, quadrilateral, polygon, square, rectangle, equality
:dependencies: G.12, G.13, G.42, G.44, G.47, G.59
:excerpt: If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.

.. _G.65:
.. _II.4:

G.65
====

.. rubric:: `II.4 <https://geometor.github.io/euclid/heath/volume_I/book_ii/propositions/04/>`_

.. enunciation::

   If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.

.. picture:: g1.svg
   :alt: Diagram

.. step:: construct

   For let :g:`/ A B / <g1:/ A B />` be cut at random at :g:`C <g1:C>`

.. step:: construct [G.59] <G.59>

   For let the square :g:`< A D E B > <g1:< A D E B >>` be described on :g:`/ A B / <g1:/ A B />`.

.. step:: construct

   **segment** :g:`/ B D / <g1:/ B D />`

.. step:: construct

   Through :g:`C <g1:C>` let :g:`/ C F / <g1:/ C F />` be drawn parallel to either :g:`/ A D / <g1:/ A D />` or :g:`/ B E / <g1:/ B E />`

.. step:: construct [G.44] <G.44>

   Through :g:`G <g1:G>` let :g:`/ H K / <g1:/ H K />` be drawn parallel to either :g:`/ A B / <g1:/ A B />` or :g:`/ D E / <g1:/ D E />`.

.. step:: assert [G.42] <G.42>

   Since :g:`/ C F / <g1:/ C F />` is parallel to :g:`/ A D / <g1:/ A D />`, and :g:`/ B D / <g1:/ B D />` has fallen on them, the exterior angle :g:`< C G B ) <g1:< C G B )>` is :eq:`equal <g1:< C G B ) = g1:< A D B )>` to the interior and opposite angle :g:`< A D B ) <g1:< A D B )>`.

.. step:: assert [G.12] <G.12>

   :g:`< A D B ) <g1:< A D B )>` is :eq:`equal <g1:< A D B ) = g1:< A B D )>` to :g:`< A B D ) <g1:< A B D )>`, since the side :g:`/ A B / <g1:/ A B />` is also :eq:`equal <g1:/ A B / = g1:/ A D />` to :g:`/ A D / <g1:/ A D />`

.. step:: assert [G.13, G.47] <G.13, G.47>

   Therefore :g:`< C G B ) <g1:< C G B )>` is also :eq:`equal <g1:< C G B ) = g1:< G B C )>` to :g:`< G B C ) <g1:< G B C )>`, so that the side :g:`/ B C / <g1:/ B C />` is also :eq:`equal <g1:/ B C / = g1:/ C G />` to the side :g:`/ C G / <g1:/ C G />`. But :g:`/ B C / <g1:/ B C />` is :eq:`equal <g1:/ B C / = g1:/ G K /; g1:/ C G / = g1:/ B K />` to :g:`/ G K / <g1:/ G K />`, and :g:`/ C G / <g1:/ C G />` to :g:`/ B K / <g1:/ B K />`

.. step:: assert

   Therefore :g:`/ G K / <g1:/ G K />` is also :eq:`equal <g1:/ G K / = g1:/ B K />` to :g:`/ B K / <g1:/ B K />`

.. step:: assert

   Therefore :g:`< C G K B > <g1:< C G K B >>` is :eq:`equilateral <g1:/ B C / = g1:/ C G / = g1:/ G K / = g1:/ B K />`.

.. step:: assert

   I say next that it is also right-angled.

.. step:: assert [G.42] <G.42>

   Since :g:`/ C G / <g1:/ C G />` is parallel to :g:`/ B K / <g1:/ B K />`, :g:`< K B C ) <g1:< K B C )>`, :g:`< G C B ) <g1:< G C B )>` are equal to two right angles.

.. step:: assert

   :g:`< K B C ) <g1:< K B C )>` is right

.. step:: assert

   Therefore :g:`< G C B ) <g1:< G C B )>` is also :eq:`right <g1:< G C B ) = g1:< K B C )>`,

.. step:: assert [G.47] <G.47>

   So that the opposite angles :g:`< C G K ) <g1:< C G K )>`, :g:`< G K B ) <g1:< G K B )>` are also :eq:`right <g1:< C G K ) = g1:< G K B ) = g1:< K B C ) = g1:< G C B )>`.

.. step:: assert

   Therefore :g:`< C G K B > <g1:< C G K B >>` is right-angled

.. step:: assert

   And it was also proved :eq:`equilateral <g1:/ B C / = g1:/ C G / = g1:/ G K / = g1:/ B K />`

.. step:: assert

   Therefore it is a square;

.. step:: assert

   And it is described on :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   For the same reason :g:`< H F > <g1:< H F >>` is also a square;

.. step:: assert [G.47] <G.47>

   And it is described on :g:`/ H G / <g1:/ H G />`, that is :g:`/ A C / <g1:/ A C />`.

.. step:: assert

   Therefore the squares :g:`< H F > <g1:< H F >>`, :g:`< K C > <g1:< K C >>` are the squares on :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   Since :g:`< A G > <g1:< A G >>` is :eq:`equal <g1:< A G > = g1:< G E >>` to :g:`< G E > <g1:< G E >>`, and :g:`< A G > <g1:< A G >>` is the rectangle :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`, for :g:`/ C G / <g1:/ C G />` is :eq:`equal <g1:/ C G / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`, therefore :g:`< G E > <g1:< G E >>` is also equal to the rectangle :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   Therefore :g:`< A G > <g1:< A G >>`, :g:`< G E > <g1:< G E >>` are equal to twice the rectangle :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   The squares :g:`< H F > <g1:< H F >>`, :g:`< C K > <g1:< C K >>` are also the squares on :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`

.. step:: assert

   Therefore the four areas :g:`< H F > <g1:< H F >>`, :g:`< C K > <g1:< C K >>`, :g:`< A G > <g1:< A G >>`, :g:`< G E > <g1:< G E >>` are equal to the squares on :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` and twice the rectangle contained by :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   :g:`< H F > <g1:< H F >>`, :g:`< C K > <g1:< C K >>`, :g:`< A G > <g1:< A G >>`, :g:`< G E > <g1:< G E >>` are the whole :g:`< A D E B > <g1:< A D E B >>`, which is the square on :g:`/ A B / <g1:/ A B />`.

.. step:: conclude

   Therefore the square on :g:`/ A B / <g1:/ A B />` is equal to the squares on :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` and twice the rectangle contained by :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`.

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
     "G.13" [label="G.13", tooltip="G.13 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", fillcolor="#222244", URL="../G.13/index.html", target="_top"];
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
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.65" [label="G.65", tooltip="G.65 (II.4): If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.29" -> "G.9";
     "G.33" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.47" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.65" -> "G.12";
     "G.65" -> "G.13";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.59" -> "G.42";
     "G.65" -> "G.42";
     "G.59" -> "G.44";
     "G.65" -> "G.44";
     "G.59" -> "G.47";
     "G.65" -> "G.47";
     "G.65" -> "G.59";
   }

Required for
------------

:ref:`G.73 <G.73>`, :ref:`G.286 <G.286>`, :ref:`G.341 <G.341>`, :ref:`G.351 <G.351>`, :ref:`G.352 <G.352>`, :ref:`G.353 <G.353>`, :ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.372 <G.372>`, :ref:`G.374 <G.374>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.418 <G.418>`, :ref:`G.435 <G.435>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`

.. toctree::
   :hidden:

   code
   heath
