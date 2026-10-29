:order: 466
:number: 466
:canonical_id: G.466
:original_id: XI.21
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, triangle, right-angle, plane, solid-angle
:dependencies: G.45, G.465
:excerpt: Any solid angle is contained by plane angles less than four right angles.

.. _G.466:
.. _XI.21:

G.466
=====

.. rubric:: `XI.21 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/21/>`_

.. enunciation::

   Any solid angle is contained by plane angles less than four right angles.

.. picture:: g1.svg
   :alt: Book XI, Proposition 21

.. step:: given

   the angle at :g:`A <g1:A>` be a solid angle contained by the plane angles :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>`

.. step:: construct

   For let points :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` be taken at random on :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`, :g:`/ A D / <g1:/ A D />` respectively

.. step:: construct

   **segment** :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D B / <g1:/ D B />`

.. step:: assert

   Since the solid angle at :g:`B <g1:B>` is contained by the three plane angles :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>`, :g:`< C B D ) <g1:< C B D )>`,

.. step:: assert [G.465] <G.465>

   Any two are greater than the remaining one; therefore :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>` are greater than :g:`< C B D ) <g1:< C B D )>`.

.. step:: assert

   For the same reason :g:`< B C A ) <g1:< B C A )>`, :g:`< A C D ) <g1:< A C D )>` are also greater than :g:`< B C D ) <g1:< B C D )>`, and :g:`< C D A ) <g1:< C D A )>`, :g:`< A D B ) <g1:< A D B )>` are greater than :g:`< C D B ) <g1:< C D B )>`; therefore the six angles :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>`, :g:`< B C A ) <g1:< B C A )>`, :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`, :g:`< A D B ) <g1:< A D B )>` are greater than the three angles :g:`< C B D ) <g1:< C B D )>`, :g:`< B C D ) <g1:< B C D )>`, :g:`< C D B ) <g1:< C D B )>`.

.. step:: assert [G.45] <G.45>

   The three angles :g:`< C B D ) <g1:< C B D )>`, :g:`< B D C ) <g1:< B D C )>`, :g:`< B C D ) <g1:< B C D )>` are equal to two right angles.

.. step:: assert

   Therefore the six angles :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>`, :g:`< B C A ) <g1:< B C A )>`, :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`, :g:`< A D B ) <g1:< A D B )>` are greater than two right angles.

.. step:: assert

   And, since the three angles of each of :g:`< A B C > <g1:< A B C >>`, :g:`< A C D > <g1:< A C D >>`, :g:`< A D B > <g1:< A D B >>` are equal to two right angles,

.. step:: assert

   Therefore the nine angles of the three triangles, :g:`< C B A ) <g1:< C B A )>`, :g:`< A C B ) <g1:< A C B )>`, :g:`< B A C ) <g1:< B A C )>`, :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< A D B ) <g1:< A D B )>`, :g:`< D B A ) <g1:< D B A )>`, :g:`< B A D ) <g1:< B A D )>` are equal to six right angles ;

.. step:: assert

   And of them the six angles :g:`< A B C ) <g1:< A B C )>`, :g:`< B C A ) <g1:< B C A )>`, :g:`< A C D ) <g1:< A C D )>`, :g:`< C D A ) <g1:< C D A )>`, :g:`< A D B ) <g1:< A D B )>`, :g:`< D B A ) <g1:< D B A )>` are greater than two right angles ;

.. step:: conclude

   Therefore the remaining three angles :g:`< B A C ) <g1:< B A C )>`, :g:`< C A D ) <g1:< C A D )>`, :g:`< D A B ) <g1:< D A B )>` containing the solid angle are less than four right angles.

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
     "G.36" [label="G.36", tooltip="G.36 (I.25): If two triangles have two sides equal to two sides respectively, the one with the greater base has the greater included angle.", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.465" [label="G.465", tooltip="G.465 (XI.20): If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.", fillcolor="#222244", URL="../G.465/index.html", target="_top"];
     "G.466" [label="G.466", tooltip="G.466 (XI.21): Any solid angle is contained by plane angles less than four right angles.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.35" -> "G.11";
     "G.36" -> "G.11";
     "G.465" -> "G.11";
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
     "G.42" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.35" -> "G.30";
     "G.33" -> "G.31";
     "G.465" -> "G.31";
     "G.34" -> "G.33";
     "G.35" -> "G.34";
     "G.44" -> "G.34";
     "G.36" -> "G.35";
     "G.465" -> "G.36";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.45" -> "G.42";
     "G.45" -> "G.44";
     "G.466" -> "G.45";
     "G.466" -> "G.465";
   }

.. toctree::
   :hidden:

   code
   heath
