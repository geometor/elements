:order: 459
:number: 459
:canonical_id: G.459
:original_id: XI.15
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, parallel, plane, equality
:dependencies: G.42, G.44, G.446, G.447, G.452, G.454, G.458
:excerpt: If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

.. _G.459:
.. _XI.15:

G.459
=====

.. rubric:: `XI.15 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/15/>`_

.. enunciation::

   If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.

For let the two straight lines :g:`/ A B / <0301.g1:/ A B />`, :g:`/ B C / <0301.g1:/ B C />` meeting one another be parallel to the two straight lines :g:`/ D E / <0301.g1:/ D E />`, :g:`/ E F / <0301.g1:/ E F />` meeting one another, not being in the same plane ; I say that the planes produced through :g:`/ A B / <0301.g1:/ A B />`, :g:`/ B C / <0301.g1:/ B C />` and :g:`/ D E / <0301.g1:/ D E />`, :g:`/ E F / <0301.g1:/ E F />` will not meet one another.

.. picture:: 0301.g1.svg
   :alt: Book XI, Proposition 15

For let :g:`/ B G / <0301.g1:/ B G />` be drawn from the point :g:`B <0301.g1:B>` perpendicular to the plane through :g:`/ D E / <0301.g1:/ D E />`, :g:`/ E F / <0301.g1:/ E F />` :just:`[G.454] <G.454>`, and let it meet the plane at the point :g:`G <0301.g1:G>`; through :g:`G <0301.g1:G>` let :g:`/ G H / <0301.g1:/ G H />` be drawn parallel to :g:`/ E D / <0301.g1:/ E D />`, and :g:`/ G K / <0301.g1:/ G K />` parallel to :g:`/ E F / <0301.g1:/ E F />`. :just:`[G.44] <G.44>`

.. subclause::

   Now, since :g:`/ B G / <0301.g1:/ B G />` is at right angles to the plane through :g:`/ D E / <0301.g1:/ D E />`, :g:`/ E F / <0301.g1:/ E F />`,

.. assertion::

   therefore it will also make right angles with all the straight lines which meet it and are in the plane through :g:`/ D E / <0301.g1:/ D E />`, :g:`/ E F / <0301.g1:/ E F />`. :just:`[G.446] <G.446>`

.. subclause::

   But each of the straight lines :g:`/ G H / <0301.g1:/ G H />`, :g:`/ G K / <0301.g1:/ G K />` meets it and is in the plane through :g:`/ D E / <0301.g1:/ D E />`, :g:`/ E F / <0301.g1:/ E F />`;

.. assertion::

   therefore each of the angles :g:`< B G H ) <0301.g1:< B G H )>`, :g:`< B G K ) <0301.g1:< B G K )>` is :eq:`right <0301.g1:< B G H ) = 0301.g1:< B G K )>`.

.. subclause:: [G.452] <G.452>

   And, since :g:`/ B A / <0301.g1:/ B A />` is parallel to :g:`/ G H / <0301.g1:/ G H />`,

.. assertion::

   therefore the angles :g:`< G B A ) <0301.g1:< G B A )>`, :g:`< B G H ) <0301.g1:< B G H )>` are equal to two right angles. :just:`[G.42] <G.42>`

.. subclause::

   But the angle :g:`< B G H ) <0301.g1:< B G H )>` is right;

.. assertion::

   therefore the angle :g:`< G B A ) <0301.g1:< G B A )>` is also right; therefore :g:`/ G B / <0301.g1:/ G B />` is at right angles to :g:`/ B A / <0301.g1:/ B A />`.

.. assertion::

   For the same reason :g:`/ G B / <0301.g1:/ G B />` is also at right angles to :g:`/ B C / <0301.g1:/ B C />`.

.. subclause::

   Since then the straight line :g:`/ G B / <0301.g1:/ G B />` is set up at right angles to the two straight lines :g:`/ B A / <0301.g1:/ B A />`, :g:`/ B C / <0301.g1:/ B C />` which cut one another,

.. assertion::

   therefore :g:`/ G B / <0301.g1:/ G B />` is also at right angles to the plane through :g:`/ B A / <0301.g1:/ B A />`, :g:`/ B C / <0301.g1:/ B C />`. :just:`[G.447] <G.447>`

.. subclause::

   But planes to which the same straight line is at right angles are parallel ; :just:`[G.458] <G.458>`

.. assertion::

   therefore the plane through :g:`/ A B / <0301.g1:/ A B />`, :g:`/ B C / <0301.g1:/ B C />` is parallel to the plane through :g:`/ D E / <0301.g1:/ D E />`, :g:`/ E F / <0301.g1:/ E F />`.

.. assertion::

   Therefore, if two straight lines meeting one another be parallel to two straight lines meeting one another, not in the same plane, the planes through them are parallel.

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
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1): Things which are equal to the same thing are also equal to one another.", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another ;", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1): To draw a straight line from any point to any point.", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3): To describe a circle with any centre and distance.", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1): On a given finite straight line to construct an equilateral triangle.", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3): If equals be subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2): To produce a finite straight line continuously in a straight line.", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2): To place at a given point (as an extremity) a straight line equal to a given straight line.", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3): Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4): [7] 4. Things which coincide with one another are equal to one another.", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4): If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base...", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5): In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another...", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7): Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities),...", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8): If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal...", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.9): To bisect a given rectilineal angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): To bisect a given finite straight line.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is cal...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): To draw a straight line at right angles to a given straight line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.20" [label="G.20", tooltip="G.20 (I.12): To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.", fillcolor="#222244", URL="../G.20/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals be added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): That all right angles are equal to one another.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): If two straight lines cut one another, they make the vertical angles equal to one another.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): [8] 5. The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle two angles taken together in any manner are less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle two sides taken together in any manner are greater than the remaining one.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manne...", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of...", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.28): If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to...", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet ...", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior an...", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Through a given point to draw a straight line parallel to a given straight line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line is at right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through the...", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.448" [label="G.448", tooltip="G.448 (XI.5): If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.", fillcolor="#222244", URL="../G.448/index.html", target="_top"];
     "G.449" [label="G.449", tooltip="G.449 (XI.6): If two straight lines be at right angles to the same plane, the straight lines will be parallel.", fillcolor="#222244", URL="../G.449/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.452" [label="G.452", tooltip="G.452 (XI.9): Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.", fillcolor="#222244", URL="../G.452/index.html", target="_top"];
     "G.454" [label="G.454", tooltip="G.454 (XI.11): From a given elevated point to draw a straight line perpendicular to a given plane.", fillcolor="#222244", URL="../G.454/index.html", target="_top"];
     "G.457" [label="G.457", tooltip="G.457 (XI.def.8): Parallel planes are those which do not meet.", fillcolor="#224422", URL="../G.457/index.html", target="_top"];
     "G.458" [label="G.458", tooltip="G.458 (XI.14): Planes to which the same straight line is at right angles will be parallel.", fillcolor="#222244", URL="../G.458/index.html", target="_top"];
     "G.459" [label="G.459", tooltip="G.459 (XI.15): If two straight lines meeting one another be parallel to two straight lines meeting one another, not being in the same plane, the planes through them are parallel.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.28" -> "G.7";
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
     "G.449" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.20" -> "G.15";
     "G.34" -> "G.15";
     "G.447" -> "G.15";
     "G.449" -> "G.15";
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
     "G.28" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.447" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.458" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.447" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.39";
     "G.44" -> "G.39";
     "G.449" -> "G.40";
     "G.42" -> "G.41";
     "G.451" -> "G.42";
     "G.459" -> "G.42";
     "G.454" -> "G.44";
     "G.459" -> "G.44";
     "G.444" -> "G.443";
     "G.449" -> "G.444";
     "G.451" -> "G.444";
     "G.448" -> "G.445";
     "G.450" -> "G.445";
     "G.458" -> "G.445";
     "G.447" -> "G.446";
     "G.448" -> "G.446";
     "G.449" -> "G.446";
     "G.451" -> "G.446";
     "G.454" -> "G.446";
     "G.458" -> "G.446";
     "G.459" -> "G.446";
     "G.448" -> "G.447";
     "G.451" -> "G.447";
     "G.452" -> "G.447";
     "G.454" -> "G.447";
     "G.459" -> "G.447";
     "G.449" -> "G.448";
     "G.452" -> "G.449";
     "G.451" -> "G.450";
     "G.452" -> "G.451";
     "G.454" -> "G.451";
     "G.459" -> "G.452";
     "G.459" -> "G.454";
     "G.458" -> "G.457";
     "G.459" -> "G.458";
   }
