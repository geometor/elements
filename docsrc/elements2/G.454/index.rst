:order: 454
:number: 454
:canonical_id: G.454
:original_id: XI.11
:volume: III
:book: XI
:type: prop
:subtype: problem
:categories: problem, construction, solid-geometry
:category: problem, construction, solid-geometry
:tags: book-xi, point, segment, perpendicular, plane
:dependencies: G.19, G.20, G.44, G.446, G.447, G.451
:excerpt: From a given elevated point to draw a straight line perpendicular to a given plane.

.. _G.454:
.. _XI.11:

G.454
=====

.. rubric:: `XI.11 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/11/>`_

.. enunciation::

   From a given elevated point to draw a straight line perpendicular to a given plane.

.. signature:: problem

   | :fn:`elevated_point_draw <G.454>`\ (:g:`A <g1:A>`) → :g:`/ A F / <g1:/ A F />`
   | **given** :g:`A <g1:A>` be the given elevated point, the plane of reference the given plane
   | **construct** from the given elevated point :g:`A <g1:A>` :g:`/ A F / <g1:/ A F />` has been drawn perpendicular to the plane of reference

.. picture:: g1.svg
   :alt: Proposition 11

.. step:: given

   :g:`A <g1:A>` be the given elevated point, the plane of reference the given plane

.. step:: construct

   Let any straight line :g:`/ B C / <g1:/ B C />` be drawn

.. step:: construct

   :fn:`perpendicular_from <G.20>`: At random, in the plane of reference, and let :g:`/ A D / <g1:/ A D />` be drawn from :g:`A <g1:A>` perpendicular to :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   If then :g:`/ A D / <g1:/ A D />` is also perpendicular to the plane of reference, that which was enjoined will have been done.

.. step:: construct

   :fn:`perpendicular_at <G.19>`: But, if not, let :g:`/ D E / <g1:/ D E />` be drawn from :g:`D <g1:D>` at right angles to :g:`/ B C / <g1:/ B C />` and in the plane of reference, let :g:`/ A F / <g1:/ A F />` be drawn from :g:`A <g1:A>` perpendicular to :g:`/ D E / <g1:/ D E />`, and let :g:`/ G H / <g1:/ G H />` be drawn through :g:`F <g1:F>` parallel to :g:`/ B C / <g1:/ B C />`.

.. step:: assert ∵ straight_line_set <G.447>

   Since :g:`/ B C / <g1:/ B C />` is at right angles to each of :g:`/ D A / <g1:/ D A />`, :g:`/ D E / <g1:/ D E />` → therefore :g:`/ B C / <g1:/ B C />` is also at right angles to the plane through :g:`/ E D / <g1:/ E D />`, :g:`/ D A / <g1:/ D A />`.

.. step:: assert

   :g:`/ G H / <g1:/ G H />` is parallel to it;

.. step:: assert ∵ straight_lines_parallel_xi_8 <G.451>

   But, if two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane

.. step:: assert

   Therefore :g:`/ G H / <g1:/ G H />` is also at right angles to the plane through :g:`/ E D / <g1:/ E D />`, :g:`/ D A / <g1:/ D A />`.

.. step:: assert ∵ straight_line_right_def <G.446>

   Therefore :g:`/ G H / <g1:/ G H />` is also at right angles to all the straight lines which meet it and are in the plane through :g:`/ E D / <g1:/ E D />`, :g:`/ D A / <g1:/ D A />`.

.. step:: assert

   :g:`/ A F / <g1:/ A F />` meets it and is in the plane through :g:`/ E D / <g1:/ E D />`, :g:`/ D A / <g1:/ D A />`;

.. step:: assert

   Therefore :g:`/ G H / <g1:/ G H />` is at right angles to :g:`/ F A / <g1:/ F A />`, so that :g:`/ F A / <g1:/ F A />` is also at right angles to :g:`/ G H / <g1:/ G H />`.

.. step:: assert

   :g:`/ A F / <g1:/ A F />` is also at right angles to :g:`/ D E / <g1:/ D E />`;

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` is at right angles to each of :g:`/ G H / <g1:/ G H />`, :g:`/ D E / <g1:/ D E />`.

.. step:: assert ∵ straight_line_set <G.447>

   But, if a straight line be set up at right angles to two straight lines which cut one another, at the point of section, it will also be at right angles to the plane through them

.. step:: assert

   Therefore :g:`/ F A / <g1:/ F A />` is at right angles to the plane through :g:`/ E D / <g1:/ E D />`, :g:`/ G H / <g1:/ G H />`.

.. step:: assert

   The plane through :g:`/ E D / <g1:/ E D />`, :g:`/ G H / <g1:/ G H />` is the plane of reference;

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` is at right angles to the plane of reference.

.. step:: conclude

   Therefore from the given elevated point :g:`A <g1:A>` :g:`/ A F / <g1:/ A F />` has been drawn perpendicular to the plane of reference.

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
     "G.20" [label="G.20", tooltip="G.20 (I.12): Construct a perpendicular to a given infinite line from a given point not on it.", fillcolor="#222244", URL="../G.20/index.html", target="_top"];
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
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.454" [label="G.454", tooltip="G.454 (XI.11): From a given elevated point to draw a straight line perpendicular to a given plane.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.20" -> "G.4";
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
     "G.447" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.20" -> "G.15";
     "G.34" -> "G.15";
     "G.447" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.17";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.20" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.454" -> "G.19";
     "G.454" -> "G.20";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.447" -> "G.25";
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
     "G.447" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.451" -> "G.42";
     "G.454" -> "G.44";
     "G.444" -> "G.443";
     "G.451" -> "G.444";
     "G.450" -> "G.445";
     "G.447" -> "G.446";
     "G.451" -> "G.446";
     "G.454" -> "G.446";
     "G.451" -> "G.447";
     "G.454" -> "G.447";
     "G.451" -> "G.450";
     "G.454" -> "G.451";
   }

Required for
------------

:ref:`G.455 <G.455>`, :ref:`G.459 <G.459>`, :ref:`G.468 <G.468>`, :ref:`G.471 <G.471>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.520 <G.520>`, :ref:`G.521 <G.521>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
