:canonical_id: G.118
:original_id: III.16
:title: G.118 segment drawn right
:volume: II
:book: III
:type: prop

G.118 segment drawn right — Heath
=================================

.. rubric:: `III.16 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/16/>`_

.. enunciation::

   The :term:`straight line <G.4>` drawn :term:`at right angles <G.32>` to the :term:`diameter <G.61>` of a :term:`circle <G.10>` from its :term:`extremity <G.6>` will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the :term:`angle of the semicircle <G.117>` is greater, and the remaining :term:`angle <G.22>` less, than any :term:`acute <G.77>` :term:`rectilineal angle <G.29>`.

Let :g:`( A B C ) <g1:( A B C )>` be a circle about :g:`D <g1:D>` as :term:`centre <G.14>` and :g:`/ A B / <g1:/ A B />` as
diameter;

I say that the straight line drawn from :g:`A <g1:A>` at right angles
to :g:`/ A B / <g1:/ A B />` from its extremity will fall
outside the circle.

.. picture:: g1.svg
   :alt: Diagram for Proposition 16

For suppose it does not, but,
if possible, let it fall within as :g:`/ C A / <g1:/ C A />`,
and let :g:`/ D C / <g1:/ D C />` be joined.

Since :g:`/ D A / <g1:/ D A />` is :eq:`equal <g1:/ D A / = g1:/ D C />` to :g:`/ D C / <g1:/ D C />`,
the angle :g:`< D A C ) <g1:< D A C )>` is also :eq:`equal <g1:< D A C ) = g1:< A C D )>` to
the angle :g:`< A C D ) <g1:< A C D )>`. :just:`[G.25] <G.25>`

But the angle :g:`< D A C ) <g1:< D A C )>` is right;

.. assertion::

   therefore the angle :g:`< A C D ) <g1:< A C D )>` is also right:

thus, in the :term:`triangle <G.11>` :g:`< A C D > <g1:< A C D >>`, the two angles :g:`< D A C ) <g1:< D A C )>`, :g:`< A C D ) <g1:< A C D )>` are
equal to two right angles: which is impossible. :just:`[G.42] <G.42>`

Therefore the straight line drawn from the :term:`point <G.1>` :g:`A <g1:A>` at
right angles to :g:`/ B A / <g1:/ B A />` will not fall within the circle.

Similarly we can prove that neither will it fall on the
circumference;

.. assertion::

   therefore it will fall outside.

Let it fall as :g:`/ A E / <g1:/ A E />`;
I say next that into the space between the straight line :g:`/ A E / <g1:/ A E />`
and the circumference :g:`( C H A ) <g1:( C H A )>` another straight line cannot be
interposed.

For, if possible, let another straight line be so interposed,
as :g:`/ F A / <g1:/ F A />`, and let :g:`/ D G / <g1:/ D G />` be drawn from the point :g:`D <g1:D>` perpendicular
to :g:`/ F A / <g1:/ F A />`.

Then, since the angle :g:`< A G D ) <g1:< A G D )>` is right,

.. subclause::

   and the angle :g:`< D A G ) <g1:< D A G )>` is less than a right angle,

.. assertion:: [G.44] <G.44>

   :g:`/ A D / <g1:/ A D />` is greater than :g:`/ D G / <g1:/ D G />`.

But :g:`/ D A / <g1:/ D A />` is :eq:`equal <g1:/ D A / = g1:/ D H />` to :g:`/ D H / <g1:/ D H />`;
therefore :g:`/ D H / <g1:/ D H />` is greater than :g:`/ D G / <g1:/ D G />`, the less than the
greater: which is impossible.

Therefore another straight line cannot be interposed into
the space between the straight line and the circumference.

I say further that the angle of the semicircle contained by
the straight line :g:`/ B A / <g1:/ B A />` and the circumference :g:`( C H A ) <g1:( C H A )>` is greater
than any acute rectilineal angle,
and the remaining angle contained by the circumference :g:`( C H A ) <g1:( C H A )>`
and the straight line :g:`/ A E / <g1:/ A E />` is less than any acute rectilineal angle.

For, if there is any rectilineal angle greater than the
angle contained by the straight line :g:`/ B A / <g1:/ B A />` and the circumference
:g:`( C H A ) <g1:( C H A )>`, and any rectilineal angle less than the angle contained
by the circumference :g:`( C H A ) <g1:( C H A )>` and the straight line :g:`/ A E / <g1:/ A E />`, then
into the space between the circumference and the straight line
:g:`/ A E / <g1:/ A E />` a straight line will be interposed such as will make an
angle contained by straight lines which is greater than the
angle contained by the straight line :g:`/ B A / <g1:/ B A />` and the circumference
:g:`( C H A ) <g1:( C H A )>`, and another angle contained by straight lines which
is less than the angle contained by the circumference :g:`( C H A ) <g1:( C H A )>`
and the straight line :g:`/ A E / <g1:/ A E />`.

But such a straight line cannot be interposed;
therefore there will not be any acute angle contained by
straight lines which is greater than the angle contained by
the straight line :g:`/ B A / <g1:/ B A />` and the circumference :g:`( C H A ) <g1:( C H A )>`, nor yet
any acute angle contained by straight lines which is less than
the angle contained by the circumference :g:`( C H A ) <g1:( C H A )>` and the
straight line :g:`/ A E / <g1:/ A E />`.—

.. porism::

   From this it is manifest that the straight line
   drawn at right angles to the diameter of a circle from its
   extremity :term:`touches the circle <G.111>`.

.. qed::

   :just:`Q. E. D.`

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
     "G.29" [label="G.29", tooltip="G.29 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.37/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.def.2): Asegment is said totouch a circle which, meeting thecircle and being produced, does not cut the circle.", fillcolor="#224422", URL="../G.111/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.117/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (III.16): The segment drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the segment and the arc another segment ca...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.118" -> "G.3";
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
     "G.31" -> "G.4";
     "G.32" -> "G.4";
     "G.33" -> "G.4";
     "G.36" -> "G.4";
     "G.39" -> "G.4";
     "G.61" -> "G.4";
     "G.111" -> "G.4";
     "G.117" -> "G.4";
     "G.118" -> "G.4";
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
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.42" -> "G.11";
     "G.43" -> "G.11";
     "G.44" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.61" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.36" -> "G.16";
     "G.39" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.33" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.42" -> "G.18";
     "G.20" -> "G.19";
     "G.39" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.30" -> "G.21";
     "G.33" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.32" -> "G.22";
     "G.36" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.77" -> "G.22";
     "G.118" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.118" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.30" -> "G.29";
     "G.118" -> "G.29";
     "G.31" -> "G.30";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.42" -> "G.32";
     "G.77" -> "G.32";
     "G.118" -> "G.32";
     "G.36" -> "G.33";
     "G.36" -> "G.35";
     "G.39" -> "G.36";
     "G.42" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.41" -> "G.40";
     "G.43" -> "G.41";
     "G.118" -> "G.42";
     "G.44" -> "G.43";
     "G.118" -> "G.44";
     "G.118" -> "G.61";
     "G.118" -> "G.77";
     "G.118" -> "G.111";
     "G.118" -> "G.117";
   }

Required for
------------

:ref:`G.119 <G.119>`, :ref:`G.141 <G.141>`, :ref:`G.145 <G.145>`, :ref:`G.149 <G.149>`, :ref:`G.151 <G.151>`, :ref:`G.154 <G.154>`, :ref:`G.159 <G.159>`, :ref:`G.160 <G.160>`, :ref:`G.162 <G.162>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.165 <G.165>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.574 <G.574>`, :ref:`G.592 <G.592>`, :ref:`G.601 <G.601>`
