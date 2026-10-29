:order: 32
:number: 32
:canonical_id: G.32
:original_id: I.21
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, line, angle, triangle
:dependencies: G.27, G.31
:excerpt: Segments constructed from the endpoints of one side of a triangle to an interior point have a lesser sum but contain a greater angle than the other two sides.

.. _G.32:
.. _I.21:

G.32
====

.. rubric:: `I.21 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/21/>`_

.. enunciation::

   Segments constructed from the endpoints of one side of a triangle to an interior point have a lesser sum but contain a greater angle than the other two sides.

.. picture:: g1.svg
   :alt: Folio 0303 Figure 1 - Proposition 21

.. step:: construct

   On :g:`/ B C / <g1:/ B C />`, one of the sides of :g:`< A B C > <g1:< A B C >>`, from its extremities :g:`B <g1:B>`, :g:`C <g1:C>`, let :g:`/ B D / <g1:/ B D />`, :g:`/ D C / <g1:/ D C />` be constructed meeting within the triangle

.. step:: construct [G.31] <G.31>

   For let :g:`[ B D ] <g1:[ B D ]>` be drawn through to :g:`E <g1:E>`. Then, since in any triangle two sides are greater than the remaining one.

.. step:: assert

   Therefore, in :g:`< A B E > <g1:< A B E >>`, the two sides :g:`/ A B / <g1:/ A B />`, :g:`/ A E / <g1:/ A E />` are greater than :g:`/ B E / <g1:/ B E />`.

.. step:: assert

   Let :g:`/ E C / <g1:/ E C />` be added to each;

.. step:: assert

   Therefore :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />` are greater than :g:`/ B E / <g1:/ B E />`, :g:`/ E C / <g1:/ E C />`.

.. step:: assert

   Since, in :g:`< C E D > <g1:< C E D >>` → the two sides :g:`/ C E / <g1:/ C E />`, :g:`/ E D / <g1:/ E D />` are greater than :g:`/ C D / <g1:/ C D />`,

.. step:: assert

   Let :g:`/ D B / <g1:/ D B />` be added to each;

.. step:: assert

   Therefore :g:`/ C E / <g1:/ C E />`, :g:`/ E B / <g1:/ E B />` are greater than :g:`/ C D / <g1:/ C D />`, :g:`/ D B / <g1:/ D B />`.

.. step:: assert

   :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />` were proved greater than :g:`/ B E / <g1:/ B E />`, :g:`/ E C / <g1:/ E C />`

.. step:: assert

   Therefore :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />` are much greater than :g:`/ B D / <g1:/ B D />`, :g:`/ D C / <g1:/ D C />`.

.. step:: assert [G.27] <G.27>

   Since in any triangle the exterior angle is greater than the interior and opposite angle.

.. step:: assert

   Therefore, in :g:`< C D E > <g1:< C D E >>`,

.. step:: assert

   The exterior angle :g:`< B D C ) <g1:< B D C )>` is greater than :g:`< C E D ) <g1:< C E D )>`.

.. step:: assert

   For the same reason, moreover, in :g:`< A B E > <g1:< A B E >>` also,

.. step:: assert

   The exterior angle :g:`< C E B ) <g1:< C E B )>` is greater than :g:`< B A C ) <g1:< B A C )>`.

.. step:: assert

   :g:`< B D C ) <g1:< B D C )>` was proved greater than :g:`< C E B ) <g1:< C E B )>`

.. step:: conclude

   Therefore :g:`< B D C ) <g1:< B D C )>` is much greater than :g:`< B A C ) <g1:< B A C )>`.

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
     "G.32" [label="G.32", tooltip="G.32 (I.21): Segments constructed from the endpoints of one side of a triangle to an interior point have a lesser sum but contain a greater angle than the other two sides.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.29" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.32" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.32" -> "G.31";
   }

Required for
------------

:ref:`G.83 <G.83>`

.. toctree::
   :hidden:

   code
   heath
