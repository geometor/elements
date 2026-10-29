:order: 43
:number: 43
:canonical_id: G.43
:original_id: I.30
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, angle, parallel, equality
:dependencies: G.1, G.42
:excerpt: Lines parallel to the same line are parallel to one another.

.. _G.43:
.. _I.30:

G.43
====

.. rubric:: `I.30 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/30/>`_

.. enunciation::

   Lines parallel to the same line are parallel to one another.

.. picture:: g1.svg
   :alt: Folio 0328 Figure 1 - Proposition 30

.. step:: given

   each of :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` be parallel to :g:`/ E F / <g1:/ E F />`

.. step:: assert

   For let :g:`/ G K / <g1:/ G K />` fall upon them

.. step:: assert [G.42] <G.42>

   Since :g:`/ G K / <g1:/ G K />` has fallen on the parallel straight lines :g:`/ A B / <g1:/ A B />`, :g:`/ E F / <g1:/ E F />` → :g:`< A G K ) <g1:< A G K )>` is :eq:`equal <g1:< A G K ) = g1:< G H F )>` to :g:`< G H F ) <g1:< G H F )>`.

.. step:: assert [G.42] <G.42>

   Since :g:`/ G K / <g1:/ G K />` has fallen on the parallel straight lines :g:`/ E F / <g1:/ E F />`, :g:`/ C D / <g1:/ C D />` → :g:`< G H F ) <g1:< G H F )>` is :eq:`equal <g1:< G H F ) = g1:< G K D )>` to :g:`< G K D ) <g1:< G K D )>`.

.. step:: assert

   :g:`< A G K ) <g1:< A G K )>` was also proved :eq:`equal <g1:< A G K ) = g1:< G H F )>` to :g:`< G H F ) <g1:< G H F )>`

.. step:: assert [G.1] <G.1>

   Therefore :g:`< A G K ) <g1:< A G K )>` is also :eq:`equal <g1:< A G K ) = g1:< G K D )>` to :g:`< G K D ) <g1:< G K D )>`;

.. step:: assert

   And they are alternate.

.. step:: conclude

   Therefore :g:`/ A B / <g1:/ A B />` is parallel to :g:`/ C D / <g1:/ C D />`.

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
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line standing on a straight line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing line is perpendicular to that on which...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): Construct a line at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.30): Lines parallel to the same line are parallel to one another.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.43" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.19" -> "G.5";
     "G.8" -> "G.6";
     "G.25" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.19" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.19" -> "G.15";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.42" -> "G.25";
     "G.42" -> "G.41";
     "G.43" -> "G.42";
   }

Required for
------------

:ref:`G.58 <G.58>`, :ref:`G.75 <G.75>`, :ref:`G.125 <G.125>`, :ref:`G.190 <G.190>`, :ref:`G.193 <G.193>`, :ref:`G.194 <G.194>`, :ref:`G.195 <G.195>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.370 <G.370>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.392 <G.392>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.484 <G.484>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
