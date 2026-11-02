:order: 135
:number: 135
:canonical_id: G.135
:original_id: III.28
:title: G.135 equal circles equal
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, equal-circles, straight-line, centre, plane-angle, stand-upon-circumference, arc, equality
:dependencies: G.4, G.28, G.131, G.133
:excerpt: In equal circles equal segments cut off equal arcs, the greater equal to the greater and the less to the less.

.. _G.135:
.. _III.28:

G.135 equal circles equal
=========================

.. rubric:: `III.28 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/28/>`_

.. enunciation::

   In :term:`equal circles <G.131>` equal :term:`segments <G.4>` cut off equal arcs, the greater equal to the greater and the less to the less.

.. signature:: theorem

   | :fn:`equal_circles_equal_iii_28 <G.135>`\ (:g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>`, :g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />`)
   | **given** :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` be :eq:`equal <g1:( A B C ) = g1:( D E F )>` circles, in the circles let :g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />` be :eq:`equal <g1:/ A B / = g1:/ D E />` segments cutting off :g:`( A C B ) <g1:( A C B )>`, :g:`( D F E ) <g1:( D F E )>` as greater arcs and :g:`( A G B ) <g1:( A G B )>`, :g:`( D H E ) <g1:( D H E )>` as lesser
   | **prove** the greater arc :g:`( A C B ) <g1:( A C B )>` is :eq:`equal <g1:( A C B ) = g1:( D F E ); g1:( A G B ) = g1:( D H E )>` to the greater arc :g:`( D F E ) <g1:( D F E )>`, and the less arc :g:`( A G B ) <g1:( A G B )>` to :g:`( D H E ) <g1:( D H E )>`

.. picture:: g1.svg
   :alt: Diagram

.. step:: given

   :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` be :eq:`equal <g1:( A B C ) = g1:( D E F )>` circles, in the circles let :g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />` be :eq:`equal <g1:/ A B / = g1:/ D E />` segments cutting off :g:`( A C B ) <g1:( A C B )>`, :g:`( D F E ) <g1:( D F E )>` as greater arcs and :g:`( A G B ) <g1:( A G B )>`, :g:`( D H E ) <g1:( D H E )>` as lesser

.. step:: construct

   Let the :term:`centres <G.14>` :g:`K <g1:K>`, :g:`L <g1:L>` of the :term:`circles <G.10>` be taken

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`A <g1:A>`, :g:`K <g1:K>`) → :g:`/ A K / <g1:/ A K />`, :fn:`segment <G.13>`\ (:g:`K <g1:K>`, :g:`B <g1:B>`) → :g:`/ K B / <g1:/ K B />`, :fn:`segment <G.13>`\ (:g:`D <g1:D>`, :g:`L <g1:L>`) → :g:`/ D L / <g1:/ D L />`, :fn:`segment <G.13>`\ (:g:`L <g1:L>`, :g:`E <g1:E>`) → :g:`/ L E / <g1:/ L E />`

.. step:: assert

   Since the circles are :eq:`equal <g1:( A B C ) = g1:( D E F )>` → the radii are also :eq:`equal <g1:/ A K / = g1:/ K B / = g1:/ D L / = g1:/ L E />`; therefore the two sides :g:`/ A K / <g1:/ A K />`, :g:`/ K B / <g1:/ K B />` are :eq:`equal <g1:/ A K / = g1:/ D L /; g1:/ K B / = g1:/ L E />` to the two

.. step:: assert

   Sides :g:`/ D L / <g1:/ D L />`, :g:`/ L E / <g1:/ L E />`

.. step:: assert

   And the base :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g1:/ D E />` to the base :g:`/ D E / <g1:/ D E />`

.. step:: assert ∵ sss_congruence <G.28>

   Therefore :g:`< A K B ) <g1:< A K B )>` is :eq:`equal <g1:< A K B ) = g1:< D L E )>` to :g:`< D L E ) <g1:< D L E )>`.

.. step:: assert ∵ equal_circles_equal <G.133>

   Equal :term:`angles <G.22>` stand on equal arcs, when they are at the centres

.. step:: assert

   Therefore the arc :g:`( A G B ) <g1:( A G B )>` is :eq:`equal <g1:( A G B ) = g1:( D H E )>` to :g:`( D H E ) <g1:( D H E )>`.

.. step:: assert

   The whole circle :g:`( A B C ) <g1:( A B C )>` is also :eq:`equal <g1:( A B C ) = g1:( D E F )>` to the whole circle :g:`( D E F ) <g1:( D E F )>`

.. step:: conclude

   Therefore the arc :g:`( A C B ) <g1:( A C B )>` which remains is also :eq:`equal <g1:( A C B ) = g1:( D F E )>` to the arc :g:`( D F E ) <g1:( D F E )>` which remains.

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
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.13/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.14/index.html", target="_top"];
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
     "G.27" [label="G.27", tooltip="G.27 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.102" [label="G.102", tooltip="G.102 (III.5): If two circles cut one another, they will not have the same center.", fillcolor="#222244", URL="../G.102/index.html", target="_top"];
     "G.108" [label="G.108", tooltip="G.108 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.108/index.html", target="_top"];
     "G.127" [label="G.127", tooltip="G.127 (III.def.11): Similar segments of circles are those which admit equalangles, or in which the angles are equal.", fillcolor="#224422", URL="../G.127/index.html", target="_top"];
     "G.129" [label="G.129", tooltip="G.129 (III.24): Similar segments of circles on equal segments are equal.", fillcolor="#222244", URL="../G.129/index.html", target="_top"];
     "G.131" [label="G.131", tooltip="G.131 (III.def.1): Equal circles are those thediameters of which are equal, or the radii of which are equal.", fillcolor="#224422", URL="../G.131/index.html", target="_top"];
     "G.132" [label="G.132", tooltip="G.132 (III.def.9): And, when thesegments containing theangle cut off a arc, the angle is said tostand upon that arc.", fillcolor="#224422", URL="../G.132/index.html", target="_top"];
     "G.133" [label="G.133", tooltip="G.133 (III.26): In equal circles equal angles stand on equal arcs, whether they stand at the centres or at the arcs.", fillcolor="#222244", URL="../G.133/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (III.28): In equal circles equal segments cut off equal arcs, the greater equal to the greater and the less to the less.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.108" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.13" -> "G.4";
     "G.17" -> "G.4";
     "G.18" -> "G.4";
     "G.20" -> "G.4";
     "G.21" -> "G.4";
     "G.22" -> "G.4";
     "G.24" -> "G.4";
     "G.25" -> "G.4";
     "G.27" -> "G.4";
     "G.28" -> "G.4";
     "G.32" -> "G.4";
     "G.61" -> "G.4";
     "G.129" -> "G.4";
     "G.132" -> "G.4";
     "G.135" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.98" -> "G.10";
     "G.102" -> "G.10";
     "G.108" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.15" -> "G.14";
     "G.61" -> "G.14";
     "G.98" -> "G.14";
     "G.102" -> "G.14";
     "G.133" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.20" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.20" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.32" -> "G.22";
     "G.127" -> "G.22";
     "G.132" -> "G.22";
     "G.133" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.133" -> "G.24";
     "G.27" -> "G.25";
     "G.28" -> "G.27";
     "G.98" -> "G.28";
     "G.135" -> "G.28";
     "G.98" -> "G.32";
     "G.131" -> "G.61";
     "G.108" -> "G.98";
     "G.108" -> "G.102";
     "G.129" -> "G.108";
     "G.129" -> "G.127";
     "G.133" -> "G.127";
     "G.133" -> "G.129";
     "G.133" -> "G.131";
     "G.135" -> "G.131";
     "G.133" -> "G.132";
     "G.135" -> "G.133";
   }

Required for
------------

:ref:`G.137 <G.137>`, :ref:`G.168 <G.168>`, :ref:`G.586 <G.586>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
