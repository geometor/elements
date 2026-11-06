:order: 104
:number: 104
:canonical_id: G.104
:original_id: III.6
:title: G.104 touching circles have distinct centers
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, circles-touching, centre, tangent, equality, reductio-ad-absurdum
:dependencies: G.10, G.11, G.14, G.16, G.26, G.103
:excerpt: Two circles that touch one another do not have the same center.

.. _G.104:
.. _III.6:

G.104 touching circles have distinct centers
============================================

.. rubric:: `III.6 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/06/>`_

.. enunciation::

   Two :term:`circles <G.10>` that :term:`touch one another <G.103>` do not have the same :term:`center <G.11>`.

.. signature:: theorem

   | :fn:`touching_circles_distinct_centers <G.104>`\ (:g:`( A B C ) <g1:( A B C )>`, :g:`( C D E ) <g1:( C D E )>`, :g:`C <g1:C>`)
   | **given** :g:`( A B C ) <g1:( A B C )>`, :g:`( C D E ) <g1:( C D E )>` touching at :g:`C <g1:C>`
   | **prove** center(:g:`( A B C ) <g1:( A B C )>`) ≠ center(:g:`( C D E ) <g1:( C D E )>`)

.. picture:: g1.svg
   :alt: Proposition 6 Diagram

.. step:: given ∵ circles_said_touch_def <G.103>

   :g:`( A B C ) <g1:( A B C )>`, :g:`( C D E ) <g1:( C D E )>` touching at :g:`C <g1:C>`

.. step:: construct ∵ segment <G.14>

   assume common center :g:`F <g1:F>`; :fn:`segment <G.14>`\ (:g:`F <g1:F>`, :g:`C <g1:C>`) → :g:`/ F C / <g1:/ F C />`, draw :g:`/ F E B / <g1:/ F E B />`

.. step:: assert ∵ circle_radii, circle_center <G.10, G.11>

   :g:`F <g1:F>` = center(:g:`( A B C ) <g1:( A B C )>`) → :g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`

.. step:: assert ∵ circle_radii, equal_transitive, whole_greater_than_part <G.10, G.16, G.26>

   :g:`F <g1:F>` = center(:g:`( C D E ) <g1:( C D E )>`) → :g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ F E />` :g:`/ F E / <g1:/ F E />` → :g:`/ F E / <g1:/ F E />` :eq:`= <g1:/ F E / = g1:/ F B />` :g:`/ F B / <g1:/ F B />` (< > ⇒⇐)

.. step:: conclude

   center(:g:`( A B C ) <g1:( A B C )>`) ≠ center(:g:`( C D E ) <g1:( C D E )>`)

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
     "G.14" [label="G.14", tooltip="G.14 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.14/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.16/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.def.3): Circles are said totouch one another which, meeting one another, do not cut one another.", fillcolor="#224422", URL="../G.103/index.html", target="_top"];
     "G.104" [label="G.104", tooltip="G.104 (III.6): Two circles that touch one another do not have the same center.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.11" -> "G.1";
     "G.14" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.14" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.11" -> "G.10";
     "G.104" -> "G.10";
     "G.104" -> "G.11";
     "G.104" -> "G.14";
     "G.104" -> "G.16";
     "G.104" -> "G.26";
     "G.104" -> "G.103";
   }

.. toctree::
   :hidden:

   code
   heath
