:canonical_id: G.161
:original_id: IV.9
:title: G.161 square circumscribe circle
:volume: II
:book: IV
:type: prop

G.161 square circumscribe circle — Heath
========================================

.. rubric:: `IV.9 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/09/>`_

.. enunciation::

   About a given :term:`square <G.63>` to circumscribe a :term:`circle <G.10>`.

Let :g:`< A B C D > <g1:< A B C D >>` be the given square;
thus it is required to :term:`circumscribe a circle about <G.155>` the square
:g:`< A B C D > <g1:< A B C D >>`.

For let :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` be joined, and let them
cut one another at :g:`E <g1:E>`.

.. picture:: g1.svg
   :alt: Proposition IV. 9 Diagram

Then, since :g:`/ D A / <g1:/ D A />` is :eq:`equal <g1:/ D A / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />`,
and :g:`/ A C / <g1:/ A C />` is common,
therefore the two sides :g:`/ D A / <g1:/ D A />`, :g:`/ A C / <g1:/ A C />` are :eq:`equal <g1:/ D A / = g1:/ B A /; g1:/ A C / = g1:/ A C />`
to the two sides :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`;
and the base :g:`/ D C / <g1:/ D C />` is :eq:`equal <g1:/ D C / = g1:/ B C />` to the base :g:`/ B C / <g1:/ B C />`;

.. assertion::

   therefore the :term:`angle <G.22>` :g:`< D A C ) <g1:< D A C )>` is :eq:`equal <g1:< D A C ) = g1:< B A C )>` to the angle :g:`< B A C ) <g1:< B A C )>`. :just:`[G.28] <G.28>`

Therefore the angle :g:`< D A B ) <g1:< D A B )>` is :eq:`bisected <g1:< D A C ) = g1:< B A C )>` by :g:`/ A C / <g1:/ A C />`.

Similarly we can prove that each of the angles :g:`< A B C ) <g1:< A B C )>`,
:g:`< B C D ) <g1:< B C D )>`, :g:`< C D A ) <g1:< C D A )>` is bisected by the straight lines :g:`/ A C / <g1:/ A C />`, :g:`/ D B / <g1:/ D B />`.

Now, since the angle :g:`< D A B ) <g1:< D A B )>` is :eq:`equal <g1:< D A B ) = g1:< A B C )>` to the angle :g:`< A B C ) <g1:< A B C )>`,
and the angle :g:`< E A B ) <g1:< E A B )>` is half the angle :g:`< D A B ) <g1:< D A B )>`,
and the angle :g:`< E B A ) <g1:< E B A )>` half the angle :g:`< A B C ) <g1:< A B C )>`,
therefore the angle :g:`< E A B ) <g1:< E A B )>` is also :eq:`equal <g1:< E A B ) = g1:< E B A )>` to the angle :g:`< E B A ) <g1:< E B A )>`;
so that the side :g:`/ E A / <g1:/ E A />` is also :eq:`equal <g1:/ E A / = g1:/ E B />` to :g:`/ E B / <g1:/ E B />`. :just:`[G.26] <G.26>`

Similarly we can prove that each of the :term:`straight lines <G.4>`
:g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />` is :eq:`equal <g1:/ E A / = g1:/ E B / = g1:/ E C / = g1:/ E D />` to each of the straight lines :g:`/ E C / <g1:/ E C />`, :g:`/ E D / <g1:/ E D />`.

Therefore the four straight lines :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />`, :g:`/ E C / <g1:/ E C />`, :g:`/ E D / <g1:/ E D />` are
:eq:`equal <g1:/ E A / = g1:/ E B / = g1:/ E C / = g1:/ E D />` to one another.

Therefore the circle described with :term:`centre <G.14>` :g:`E <g1:E>` and distance
one of the straight lines :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />`, :g:`/ E C / <g1:/ E C />`, :g:`/ E D / <g1:/ E D />` will pass also
through the remaining :term:`points <G.1>`;
and it will have been :term:`circumscribed about the square <G.155>` :g:`< A B C D > <g1:< A B C D >>`.

Let it be circumscribed, as :g:`( A B C D ) <g1:( A B C D )>`.

Therefore about the given square a circle has been
circumscribed.

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
     "G.26" [label="G.26", tooltip="G.26 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", fillcolor="#222244", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.155" [label="G.155", tooltip="G.155 (IV.def.2): Similarly afigure is said to becircumscribed about a figure when the respective sides of the circumscribed figure pass through the respectiveangles of that about which it is circum...", fillcolor="#224422", URL="../G.155/index.html", target="_top"];
     "G.156" [label="G.156", tooltip="G.156 (IV.def.6): Acircle is said to becircumscribed about a figure when the arc of the circle passes through eachangle of thefigure about which it is circumscribed.", fillcolor="#224422", URL="../G.156/index.html", target="_top"];
     "G.161" [label="G.161", tooltip="G.161 (IV.9): About a given square to circumscribe a circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
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
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.26" -> "G.9";
     "G.155" -> "G.9";
     "G.156" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.156" -> "G.10";
     "G.161" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.26" -> "G.11";
     "G.28" -> "G.11";
     "G.63" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.63" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.15" -> "G.14";
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
     "G.26" -> "G.22";
     "G.28" -> "G.22";
     "G.63" -> "G.22";
     "G.155" -> "G.22";
     "G.156" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.27" -> "G.25";
     "G.161" -> "G.26";
     "G.28" -> "G.27";
     "G.161" -> "G.28";
     "G.161" -> "G.63";
     "G.161" -> "G.155";
     "G.161" -> "G.156";
   }
