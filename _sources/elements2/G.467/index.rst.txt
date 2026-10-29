:order: 467
:number: 467
:canonical_id: G.467
:original_id: XI.22
:volume: III
:book: XI
:type: prop
:subtype: problem
:categories: problem, construction, solid-geometry
:category: problem, construction, solid-geometry
:tags: book-xi, point, segment, angle, plane, equality
:dependencies: G.11, G.35
:excerpt: If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

.. _G.467:
.. _XI.22:

G.467
=====

.. rubric:: `XI.22 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/22/>`_

.. enunciation::

   If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

.. picture:: g1.svg
   :alt: Proposition 22, Figure 1

.. picture:: g2.svg
   :alt: Proposition 22, Figure 2

.. step:: given

   there be three plane angles :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>`, of which two, taken together in any manner, are greater than the remaining one, namely :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>` greater than :g:`< G H K ) <g1:< G H K )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` greater than :g:`< A B C ) <g1:< A B C )>`, and, further, :g:`< G H K ) <g1:< G H K )>`, :g:`< A B C ) <g1:< A B C )>` greater than :g:`< D E F ) <g1:< D E F )>`

.. step:: assert

   Let :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />` be :eq:`equal <g1:/ A B / = g1:/ B C / = g1:/ D E / = g1:/ E F / = g1:/ G H / = g1:/ H K />`

.. step:: construct

   **segment** :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />`, :g:`/ G K / <g1:/ G K />`

.. step:: assert

   If :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` are :eq:`equal <g1:< A B C ) = g1:< D E F ) = g1:< G H K )>` to one another, it is manifest that, :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />`, :g:`/ G K / <g1:/ G K />` being :eq:`equal <g1:/ A C / = g1:/ D F / = g1:/ G K />` also, it is possible to construct a triangle out of straight lines equal to :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />`, :g:`/ G K / <g1:/ G K />`.

.. step:: assert

   But, if not, let them be unequal

.. step:: construct

   On :g:`/ H K / <g2:/ H K />`, and at :g:`H <g2:H>` on it, let :g:`< K H L ) <g2:< K H L )>` be constructed :eq:`equal <g2:< K H L ) = g1:< A B C )>` to :g:`< A B C ) <g1:< A B C )>`

.. step:: construct

   Let :g:`/ H L / <g2:/ H L />` be made :eq:`equal <g2:/ H L / = g1:/ A B / = g1:/ B C / = g1:/ D E / = g1:/ E F / = g2:/ G H / = g2:/ H K />` to one of :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, :g:`/ G H / <g2:/ G H />`, :g:`/ H K / <g2:/ H K />`

.. step:: construct

   **segment** :g:`/ K L / <g2:/ K L />`, :g:`/ G L / <g2:/ G L />`

.. step:: assert

   Since the two sides :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are :eq:`equal <g1:/ A B / = g2:/ K H /; g1:/ B C / = g2:/ H L />` to the two sides :g:`/ K H / <g2:/ K H />`, :g:`/ H L / <g2:/ H L />`, and the angle at :g:`B <g1:B>` is :eq:`equal <g1:< A B C ) = g2:< K H L )>` to :g:`< K H L ) <g2:< K H L )>`,

.. step:: assert [G.11] <G.11>

   Therefore the base :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g2:/ K L />` to the base :g:`/ K L / <g2:/ K L />`.

.. step:: assert

   *And*, since :g:`< A B C ) <g1:< A B C )>`, :g:`< G H K ) <g2:< G H K )>` are greater than :g:`< D E F ) <g1:< D E F )>`,

.. step:: assert

   While :g:`< A B C ) <g1:< A B C )>` is :eq:`equal <g1:< A B C ) = g2:< K H L )>` to :g:`< K H L ) <g2:< K H L )>`,

.. step:: assert

   Therefore :g:`< G H L ) <g2:< G H L )>` is greater than :g:`< D E F ) <g1:< D E F )>`.

.. step:: assert

   And, since the two sides :g:`/ G H / <g2:/ G H />`, :g:`/ H L / <g2:/ H L />` are :eq:`equal <g2:/ G H / = g1:/ D E /; g2:/ H L / = g1:/ E F />` to the two sides :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, and :g:`< G H L ) <g2:< G H L )>` is greater than :g:`< D E F ) <g1:< D E F )>`,

.. step:: assert [G.35] <G.35>

   Therefore the base :g:`/ G L / <g2:/ G L />` is greater than the base :g:`/ D F / <g1:/ D F />`.

.. step:: assert

   :g:`/ G K / <g2:/ G K />`, :g:`/ K L / <g2:/ K L />` are greater than :g:`/ G L / <g2:/ G L />`.

.. step:: assert

   Therefore :g:`/ G K / <g2:/ G K />`, :g:`/ K L / <g2:/ K L />` are much greater than :g:`/ D F / <g1:/ D F />`.

.. step:: assert

   :g:`/ K L / <g2:/ K L />` is :eq:`equal <g2:/ K L / = g1:/ A C />` to :g:`/ A C / <g1:/ A C />`;

.. step:: assert

   Therefore :g:`/ A C / <g1:/ A C />`, :g:`/ G K / <g1:/ G K />` are greater than the remaining straight line :g:`/ D F / <g1:/ D F />`.

.. step:: assert

   Similarly we can prove that :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />` are greater than :g:`/ G K / <g1:/ G K />`, and further :g:`/ D F / <g1:/ D F />`, :g:`/ G K / <g1:/ G K />` are greater than :g:`/ A C / <g1:/ A C />`.

.. step:: conclude

   Therefore it is possible to construct a triangle out of straight lines equal to :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />`, :g:`/ G K / <g1:/ G K />`.

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
     "G.35" [label="G.35", tooltip="G.35 (I.24): If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
     "G.467" [label="G.467", tooltip="G.467 (XI.22): If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to con...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.33" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.35" -> "G.11";
     "G.467" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.35" -> "G.12";
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
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.35" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.35" -> "G.34";
     "G.467" -> "G.35";
   }

Required for
------------

:ref:`G.468 <G.468>`

.. toctree::
   :hidden:

   code
   heath
