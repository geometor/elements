:canonical_id: G.98
:original_id: III.1
:title: G.98 find the center of a circle
:volume: II
:book: III
:type: prop

G.98 find the center of a circle — Heath
========================================

.. rubric:: `III.1 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/01/>`_

.. enunciation::

   To find the :term:`centre <G.11>` of a given :term:`circle <G.10>`.

Let :g:`( A B C ) <g1:( A B C )>` be the given circle;

thus it is required to find the centre of the circle :g:`( A B C ) <g1:( A B C )>`.

Let a :term:`straight line <G.4>` :g:`/ A B / <g1:/ A B />` be drawn through it at random, and let it be :eq:`bisected <g1:/ A D / = g1:/ D B />` at the :term:`point <G.1>` :g:`D <g1:D>`; from :g:`D <g1:D>` let :g:`/ D C / <g1:/ D C />` be drawn :term:`at right angles <G.33>` to :g:`/ A B / <g1:/ A B />` and let it be drawn through to :g:`E <g1:E>`; let :g:`/ C E / <g1:/ C E />` be :eq:`bisected <g1:/ C F / = g1:/ F E />` at :g:`F <g1:F>`;

I say that :g:`F <g1:F>` is the centre of the circle :g:`( A B C ) <g1:( A B C )>`.

.. picture:: g1.svg
   :alt: Proposition 1

For suppose it is not, but, if possible, let :g:`G <g1:G>` be the centre, and let :g:`/ G A / <g1:/ G A />`, :g:`/ G D / <g1:/ G D />`, :g:`/ G B / <g1:/ G B />` be joined.

Then, since :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ D B />` to :g:`/ D B / <g1:/ D B />`, and :g:`/ D G / <g1:/ D G />` is common,

.. subclause::

   the two sides :g:`/ A D / <g1:/ A D />`, :g:`/ D G / <g1:/ D G />` are :eq:`equal <g1:/ A D / = g1:/ B D />` to the two sides :g:`/ B D / <g1:/ B D />`, :g:`/ D G / <g1:/ D G />` respectively;

and the base :g:`/ G A / <g1:/ G A />` is :eq:`equal <g1:/ G A / = g1:/ G B />` to the base :g:`/ G B / <g1:/ G B />`, for they are radii;

.. assertion:: [G.29] <G.29>

   therefore the :term:`angle <G.22>` :g:`< A D G ) <g1:< A D G )>` is :eq:`equal <g1:< A D G ) = g1:< G D B )>` to the angle :g:`< G D B ) <g1:< G D B )>`.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; :just:`[G.33] <G.33>`

.. assertion::

   therefore the angle :g:`< G D B ) <g1:< G D B )>` is right.

But the angle :g:`< F D B ) <g1:< F D B )>` is also right; therefore the angle :g:`< F D B ) <g1:< F D B )>` is :eq:`equal <g1:< F D B ) = g1:< G D B )>` to the angle :g:`< G D B ) <g1:< G D B )>`, the greater to the less: which is impossible.

.. assertion::

   Therefore :g:`G <g1:G>` is not the centre of the circle :g:`( A B C ) <g1:( A B C )>`.

Similarly we can prove that neither is any other point except :g:`F <g1:F>`.

.. assertion::

   Therefore the point :g:`F <g1:F>` is the centre of the circle :g:`( A B C ) <g1:( A B C )>`.

.. enunciation::

   PORISM. From this it is manifest that, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line.

.. qed::

   Q. E. F.

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
     "G.34" [label="G.34", tooltip="G.34 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.34" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.18" -> "G.2";
     "G.22" -> "G.2";
     "G.30" -> "G.2";
     "G.33" -> "G.2";
     "G.34" -> "G.2";
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
     "G.34" -> "G.4";
     "G.98" -> "G.4";
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
     "G.98" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.98" -> "G.11";
     "G.13" -> "G.12";
     "G.17" -> "G.12";
     "G.20" -> "G.12";
     "G.24" -> "G.12";
     "G.25" -> "G.12";
     "G.28" -> "G.12";
     "G.29" -> "G.12";
     "G.31" -> "G.12";
     "G.32" -> "G.12";
     "G.34" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.34" -> "G.14";
     "G.98" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.30" -> "G.22";
     "G.31" -> "G.22";
     "G.32" -> "G.22";
     "G.33" -> "G.22";
     "G.34" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.28" -> "G.25";
     "G.28" -> "G.26";
     "G.98" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.98" -> "G.29";
     "G.31" -> "G.30";
     "G.32" -> "G.31";
     "G.98" -> "G.32";
     "G.34" -> "G.33";
     "G.98" -> "G.33";
     "G.98" -> "G.34";
   }

Required for
------------

:ref:`G.99 <G.99>`, :ref:`G.101 <G.101>`, :ref:`G.106 <G.106>`, :ref:`G.107 <G.107>`, :ref:`G.108 <G.108>`, :ref:`G.112 <G.112>`, :ref:`G.114 <G.114>`, :ref:`G.116 <G.116>`, :ref:`G.119 <G.119>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.135 <G.135>`, :ref:`G.136 <G.136>`, :ref:`G.137 <G.137>`, :ref:`G.151 <G.151>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.167 <G.167>`, :ref:`G.168 <G.168>`, :ref:`G.246 <G.246>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.590 <G.590>`, :ref:`G.592 <G.592>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`
