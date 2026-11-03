:order: 133
:number: 133
:canonical_id: G.133
:original_id: III.26
:title: G.133 equal circles equal
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, equal-circles, plane-angle, stand-upon-circumference, centre, straight-line, similar-segments-of-circles, arc, plane, equality
:dependencies: G.4, G.10, G.11, G.14, G.22, G.24, G.127, G.129, G.131, G.132
:excerpt: In equal circles equal angles stand on equal arcs, whether they stand at the centres or at the arcs.

.. _G.133:
.. _III.26:

G.133 equal circles equal
=========================

.. rubric:: `III.26 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/26/>`_

.. enunciation::

   In :term:`equal circles <G.131>` equal :term:`angles <G.22>` stand on equal arcs, whether they stand at the :term:`centres <G.11>` or at the arcs.

.. signature:: theorem

   | :fn:`equal_circles_equal <G.133>`\ (:g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>`, :g:`< B G C ) <g1:< B G C )>`, :g:`< E H F ) <g1:< E H F )>`)
   | **given** :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` be :eq:`= <g1:( A B C ) = g1:( D E F )>` circles, in them let there be :eq:`= <g1:< B G C ) = g1:< E H F ); g1:< B A C ) = g1:< E D F )>` angles, namely at the centres :g:`< B G C ) <g1:< B G C )>`, :g:`< E H F ) <g1:< E H F )>`, at the arcs :g:`< B A C ) <g1:< B A C )>`, :g:`< E D F ) <g1:< E D F )>`
   | **prove** the arc :g:`( B K C ) <g1:( B K C )>` :eq:`= <g1:( B K C ) = g1:( E L F )>` the arc :g:`( E L F ) <g1:( E L F )>`

.. picture:: g1.svg
   :alt: Diagram

.. step:: given

   :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` be :eq:`= <g1:( A B C ) = g1:( D E F )>` circles, in them let there be :eq:`= <g1:< B G C ) = g1:< E H F ); g1:< B A C ) = g1:< E D F )>` angles, namely at the centres :g:`< B G C ) <g1:< B G C )>`, :g:`< E H F ) <g1:< E H F )>`, at the arcs :g:`< B A C ) <g1:< B A C )>`, :g:`< E D F ) <g1:< E D F )>`

.. step:: construct

   :fn:`segment <G.14>`\ (:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`, :fn:`segment <G.14>`\ (:g:`E <g1:E>`, :g:`F <g1:F>`) → :g:`/ E F / <g1:/ E F />`

.. step:: assert

   :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` are :eq:`= <g1:( A B C ) = g1:( D E F )>` → the radii are :eq:`= <g1:/ B G / = g1:/ G C / = g1:/ E H / = g1:/ H F />`

.. step:: assert

   :g:`/ B G / <g1:/ B G />`, :g:`/ G C / <g1:/ G C />` :eq:`= <g1:/ B G / = g1:/ E H /; g1:/ G C / = g1:/ H F />` :g:`/ E H / <g1:/ E H />`, :g:`/ H F / <g1:/ H F />`

.. step:: assert

   the angle at :g:`G <g1:G>` :eq:`= <g1:< B G C ) = g1:< E H F )>` the angle at :g:`H <g1:H>`

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`

.. step:: assert

   since the angle at :g:`A <g1:A>` :eq:`= <g1:< B A C ) = g1:< E D F )>` the angle at :g:`D <g1:D>`,

.. step:: assert ∵ similar_segments_circles_def <G.127>

   The :term:`segment <G.4>` :g:`( B A C ) <g1:( B A C )>` is similar to the segment :g:`( E D F ) <g1:( E D F )>`

.. step:: assert

   they are upon :eq:`= <g1:/ B C / = g1:/ E F />` segments

.. step:: assert ∵ similar_segments_circles <G.129>

   :term:`Similar segments of circles <G.127>` on equal segments are equal to one another

.. step:: assert

   the segment :g:`( B A C ) <g1:( B A C )>` :eq:`= <g1:( B A C ) = g1:( E D F )>` :g:`( E D F ) <g1:( E D F )>`

.. step:: assert

   The whole :term:`circle <G.10>` :g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` the whole circle :g:`( D E F ) <g1:( D E F )>`

.. step:: conclude

   the arc :g:`( B K C ) <g1:( B K C )>` which remains :eq:`= <g1:( B K C ) = g1:( E L F )>` the arc :g:`( E L F ) <g1:( E L F )>`

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
     "G.12" [label="G.12", tooltip="G.12 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.13/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.post.3): Construct a circle ( A B ) with center A and defining radius point B.", fillcolor="#444422", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.1): Construct an equilateral triangle on a given segment.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.post.2): Extend a segment / A B / continuously along a line [ A B ] to / B C /.", fillcolor="#444422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.cn.3): If equals are subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.19/index.html", target="_top"];
     "G.20" [label="G.20", tooltip="G.20 (I.2): Construct at a given point a segment equal to a given segment.", fillcolor="#222244", URL="../G.20/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.3): Cut off from the greater of two unequal segments a segment equal to the less.", fillcolor="#222244", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.cn.4): Things / A B /, / D E / that coincide with one another are equal to one another.", fillcolor="#442222", URL="../G.23/index.html", target="_top"];
     "G.24" [label="G.24", tooltip="G.24 (I.4): Triangles with two sides and the included angle equal are congruent (SAS).", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.5): In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.33/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.102" [label="G.102", tooltip="G.102 (III.5): If two circles cut one another, they will not have the same center.", fillcolor="#222244", URL="../G.102/index.html", target="_top"];
     "G.108" [label="G.108", tooltip="G.108 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.108/index.html", target="_top"];
     "G.127" [label="G.127", tooltip="G.127 (III.def.11): Similar segments of circles are those which admit equalangles, or in which the angles are equal.", fillcolor="#224422", URL="../G.127/index.html", target="_top"];
     "G.129" [label="G.129", tooltip="G.129 (III.24): Similar segments of circles on equal segments are equal.", fillcolor="#222244", URL="../G.129/index.html", target="_top"];
     "G.131" [label="G.131", tooltip="G.131 (III.def.1): Equal circles are those thediameters of which are equal, or the radii of which are equal.", fillcolor="#224422", URL="../G.131/index.html", target="_top"];
     "G.132" [label="G.132", tooltip="G.132 (III.def.9): And, when thesegments containing theangle cut off a arc, the angle is said tostand upon that arc.", fillcolor="#224422", URL="../G.132/index.html", target="_top"];
     "G.133" [label="G.133", tooltip="G.133 (III.26): In equal circles equal angles stand on equal arcs, whether they stand at the centres or at the arcs.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.11" -> "G.1";
     "G.14" -> "G.1";
     "G.15" -> "G.1";
     "G.17" -> "G.1";
     "G.20" -> "G.1";
     "G.21" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.28" -> "G.1";
     "G.29" -> "G.1";
     "G.31" -> "G.1";
     "G.32" -> "G.1";
     "G.98" -> "G.1";
     "G.108" -> "G.1";
     "G.129" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.18" -> "G.2";
     "G.22" -> "G.2";
     "G.30" -> "G.2";
     "G.33" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.12" -> "G.4";
     "G.14" -> "G.4";
     "G.17" -> "G.4";
     "G.18" -> "G.4";
     "G.20" -> "G.4";
     "G.21" -> "G.4";
     "G.22" -> "G.4";
     "G.24" -> "G.4";
     "G.25" -> "G.4";
     "G.28" -> "G.4";
     "G.29" -> "G.4";
     "G.30" -> "G.4";
     "G.31" -> "G.4";
     "G.32" -> "G.4";
     "G.33" -> "G.4";
     "G.61" -> "G.4";
     "G.98" -> "G.4";
     "G.108" -> "G.4";
     "G.129" -> "G.4";
     "G.132" -> "G.4";
     "G.133" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.98" -> "G.10";
     "G.102" -> "G.10";
     "G.108" -> "G.10";
     "G.129" -> "G.10";
     "G.133" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.61" -> "G.11";
     "G.98" -> "G.11";
     "G.102" -> "G.11";
     "G.108" -> "G.11";
     "G.133" -> "G.11";
     "G.13" -> "G.12";
     "G.17" -> "G.12";
     "G.20" -> "G.12";
     "G.24" -> "G.12";
     "G.25" -> "G.12";
     "G.28" -> "G.12";
     "G.29" -> "G.12";
     "G.31" -> "G.12";
     "G.32" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.102" -> "G.14";
     "G.133" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.30" -> "G.22";
     "G.31" -> "G.22";
     "G.32" -> "G.22";
     "G.33" -> "G.22";
     "G.98" -> "G.22";
     "G.127" -> "G.22";
     "G.132" -> "G.22";
     "G.133" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.133" -> "G.24";
     "G.28" -> "G.25";
     "G.28" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.98" -> "G.29";
     "G.31" -> "G.30";
     "G.32" -> "G.31";
     "G.98" -> "G.32";
     "G.98" -> "G.33";
     "G.108" -> "G.33";
     "G.131" -> "G.61";
     "G.108" -> "G.98";
     "G.108" -> "G.102";
     "G.129" -> "G.108";
     "G.129" -> "G.127";
     "G.133" -> "G.127";
     "G.133" -> "G.129";
     "G.133" -> "G.131";
     "G.133" -> "G.132";
   }

Required for
------------

:ref:`G.134 <G.134>`, :ref:`G.135 <G.135>`, :ref:`G.136 <G.136>`, :ref:`G.137 <G.137>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.167 <G.167>`, :ref:`G.168 <G.168>`, :ref:`G.246 <G.246>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.590 <G.590>`, :ref:`G.592 <G.592>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
