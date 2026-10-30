:order: 127
:number: 127
:canonical_id: G.127
:original_id: IV.9
:volume: II
:book: IV
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles, polygons
:category: problem, construction, plane-geometry, circles, polygons
:tags: book-iv, point, segment, circle, angle, quadrilateral, square, circumscribed, equality
:dependencies: G.13, G.15
:excerpt: About a given square to circumscribe a circle.

.. _G.127:
.. _IV.9:

G.127
=====

.. rubric:: `IV.9 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/09/>`_

.. enunciation::

   About a given square to circumscribe a circle.

.. signature:: problem

   | :fn:`square_circumscribe_circle <G.127>`\ (:g:`< A B C D > <g1:< A B C D >>`)
   | **given** :g:`< A B C D > <g1:< A B C D >>` be the given square
   | **construct** about the given square a circle has been circumscribed

.. picture:: g1.svg
   :alt: Proposition IV. 9 Diagram

.. step:: given

   :g:`< A B C D > <g1:< A B C D >>` be the given square

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`, :fn:`segment <G.3>`\ (:g:`B <g1:B>`, :g:`D <g1:D>`) → :g:`/ B D / <g1:/ B D />`

.. step:: intersect

   Let them cut one another at :g:`E <g1:E>`.

.. step:: assert

   Since :g:`/ D A / <g1:/ D A />` is :eq:`equal <g1:/ D A / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />`, and :g:`/ A C / <g1:/ A C />` is common, therefore the two sides :g:`/ D A / <g1:/ D A />`, :g:`/ A C / <g1:/ A C />` are :eq:`equal <g1:/ D A / = g1:/ B A /; g1:/ A C / = g1:/ A C />` to the two sides :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`

.. step:: assert

   And the base :g:`/ D C / <g1:/ D C />` is :eq:`equal <g1:/ D C / = g1:/ B C />` to the base :g:`/ B C / <g1:/ B C />`

.. step:: assert ∵ sss_congruence <G.15>

   Therefore :g:`< D A C ) <g1:< D A C )>` is :eq:`equal <g1:< D A C ) = g1:< B A C )>` to :g:`< B A C ) <g1:< B A C )>`.

.. step:: assert

   Therefore :g:`< D A B ) <g1:< D A B )>` is :eq:`bisected <g1:< D A C ) = g1:< B A C )>` by :g:`/ A C / <g1:/ A C />`.

.. step:: assert

   Similarly we can prove that each of :g:`< A B C ) <g1:< A B C )>`, :g:`< B C D ) <g1:< B C D )>`, :g:`< C D A ) <g1:< C D A )>` is bisected by :g:`/ A C / <g1:/ A C />`, :g:`/ D B / <g1:/ D B />`.

.. step:: assert

   Since :g:`< D A B ) <g1:< D A B )>` is :eq:`equal <g1:< D A B ) = g1:< A B C )>` to :g:`< A B C ) <g1:< A B C )>`, and :g:`< E A B ) <g1:< E A B )>` is half :g:`< D A B ) <g1:< D A B )>`, and :g:`< E B A ) <g1:< E B A )>` half :g:`< A B C ) <g1:< A B C )>`, therefore :g:`< E A B ) <g1:< E A B )>` is also :eq:`equal <g1:< E A B ) = g1:< E B A )>` to :g:`< E B A ) <g1:< E B A )>`

.. step:: assert ∵ equal_angles_isosceles <G.13>

   So that the side :g:`/ E A / <g1:/ E A />` is also :eq:`equal <g1:/ E A / = g1:/ E B />` to :g:`/ E B / <g1:/ E B />`.

.. step:: assert

   Similarly we can prove that each of :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />` is :eq:`equal <g1:/ E A / = g1:/ E B / = g1:/ E C / = g1:/ E D />` to each of :g:`/ E C / <g1:/ E C />`, :g:`/ E D / <g1:/ E D />`.

.. step:: assert

   Therefore the four straight lines :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />`, :g:`/ E C / <g1:/ E C />`, :g:`/ E D / <g1:/ E D />` are :eq:`equal <g1:/ E A / = g1:/ E B / = g1:/ E C / = g1:/ E D />` to one another.

.. step:: assert

   Therefore the circle described with center :g:`E <g1:E>` and distance one of :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />`, :g:`/ E C / <g1:/ E C />`, :g:`/ E D / <g1:/ E D />` will pass also through the remaining points

.. step:: assert

   And it will have been circumscribed about the square :g:`< A B C D > <g1:< A B C D >>`.

.. step:: construct

   Let it be circumscribed, as :g:`( A B C D ) <g1:( A B C D )>`.

.. step:: conclude

   Therefore about the given square a circle has been circumscribed.

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
     "G.127" [label="G.127", tooltip="G.127 (IV.9): About a given square to circumscribe a circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
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
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.14" -> "G.12";
     "G.127" -> "G.13";
     "G.15" -> "G.14";
     "G.127" -> "G.15";
   }

.. toctree::
   :hidden:

   code
   heath
