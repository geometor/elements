:order: 55
:number: 55
:canonical_id: G.55
:original_id: I.42
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, angle, triangle, quadrilateral, parallelogram, equality
:dependencies: G.34, G.44, G.51, G.54
:excerpt: Construct, in a given angle, a parallelogram equal in area to a given triangle.

.. _G.55:
.. _I.42:

G.55
====

.. rubric:: `I.42 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/42/>`_

.. enunciation::

   Construct, in a given angle, a parallelogram equal in area to a given triangle.

.. signature:: problem

   | :fn:`parallelogram_from_triangle <G.55>`\ (:g:`< A B C > <g1:< A B C >>`, :g:`< D ) <g1:< D )>`) → :g:`< C E F ) <g1:< C E F )>`
   | **given** :g:`< A B C > <g1:< A B C >>`, :g:`< D ) <g1:< D )>`
   | **construct** construct in :g:`< D ) <g1:< D )>` a parallelogram :eq:`equal <g1:< F E C G > = g1:< A B C >>` to :g:`< A B C > <g1:< A B C >>`

.. picture:: g1.svg
   :alt: Folio 0353 Figure 2 - Proposition 42

.. step:: given

   :g:`< A B C > <g1:< A B C >>`, :g:`< D ) <g1:< D )>`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`, :fn:`segment <G.3>`\ () → :g:`E <g1:E>`, :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`E <g1:E>`) → :g:`/ A E / <g1:/ A E />`

.. step:: construct

   :fn:`copy_angle <G.34>`\ (:g:`/ E C / <g1:/ E C />`, :g:`E <g1:E>`, :g:`< D ) <g1:< D )>`) → :g:`< C E F ) <g1:< C E F )>` (:eq:`equal <g1:< C E F ) = g1:< D )>`)

.. step:: construct

   :fn:`parallel_line <G.44>`\ (:g:`A <g1:A>`, :g:`/ E C / <g1:/ E C />`) → :g:`/ A G / <g1:/ A G />`

.. step:: construct

   :fn:`parallel_line <G.44>`\ (:g:`C <g1:C>`, :g:`/ E F / <g1:/ E F />`) → :g:`/ C G / <g1:/ C G />`

.. step:: assert

   Then :g:`< F E C G > <g1:< F E C G >>` is a parallelogram.

.. step:: assert ∵ triangles_equal_bases <G.51>

   And, since :g:`/ B E / <g1:/ B E />` is :eq:`equal <g1:/ B E / = g1:/ E C />` to :g:`/ E C / <g1:/ E C />`, :g:`< A B E > <g1:< A B E >>` is also :eq:`equal <g1:< A B E > = g1:< A E C >>` to :g:`< A E C > <g1:< A E C >>`, for they are on :eq:`equal <g1:/ B E / = g1:/ E C />` bases :g:`/ B E / <g1:/ B E />`, :g:`/ E C / <g1:/ E C />` and in the same parallels :g:`/ B C / <g1:/ B C />`, :g:`/ A G / <g1:/ A G />`

.. step:: assert

   Therefore :g:`< A B C > <g1:< A B C >>` is double of :g:`< A E C > <g1:< A E C >>`.

.. step:: assert ∵ parallelogram_double_triangle <G.54>

   The parallelogram :g:`< F E C G > <g1:< F E C G >>` is also double of :g:`< A E C > <g1:< A E C >>`, for it has the same base with it and is in the same parallels with it;

.. step:: assert

   Therefore the parallelogram :g:`< F E C G > <g1:< F E C G >>` is :eq:`equal <g1:< F E C G > = g1:< A B C >>` to :g:`< A B C > <g1:< A B C >>`.

.. step:: conclude

   It has :g:`< C E F ) <g1:< C E F )>` :eq:`equal <g1:< C E F ) = g1:< D )>` to the given angle :g:`< D ) <g1:< D )>`.

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
     "G.46" [label="G.46", tooltip="G.46 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.38): Triangles on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.42): Construct, in a given angle, a parallelogram equal in area to a given triangle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.29" -> "G.9";
     "G.33" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
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
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.55" -> "G.34";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.55" -> "G.44";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.51" -> "G.49";
     "G.54" -> "G.50";
     "G.55" -> "G.51";
     "G.55" -> "G.54";
   }

Required for
------------

:ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.75 <G.75>`, :ref:`G.190 <G.190>`, :ref:`G.193 <G.193>`, :ref:`G.194 <G.194>`, :ref:`G.195 <G.195>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.353 <G.353>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.370 <G.370>`, :ref:`G.374 <G.374>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.388 <G.388>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.484 <G.484>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
