:order: 121
:number: 121
:canonical_id: G.121
:original_id: IV.4
:volume: II
:book: IV
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles, polygons
:category: problem, construction, plane-geometry, circles, polygons
:tags: book-iv, point, segment, circle, angle, triangle, inscribed, equality
:dependencies: G.16, G.37, G.94, G.120
:excerpt: In a given triangle to inscribe a circle.

.. _G.121:
.. _IV.4:

G.121
=====

.. rubric:: `IV.4 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/04/>`_

.. enunciation::

   In a given triangle to inscribe a circle.

Let :g:`< A B C > <0091.g1:< A B C >>` be the given triangle;
thus it is required to inscribe a circle in the triangle :g:`< A B C > <0091.g1:< A B C >>`.

Let the angles :g:`< A B C ) <0091.g1:< A B C )>`, :g:`< A C B ) <0091.g1:< A C B )>`
be bisected by the straight lines
:g:`/ B D / <0091.g1:/ B D />`, :g:`/ C D / <0091.g1:/ C D />` :just:`[G.16] <G.16>`, and let these meet
one another at the point :g:`D <0091.g1:D>`;
from :g:`D <0091.g1:D>` let :g:`/ D E / <0091.g1:/ D E />`, :g:`/ D F / <0091.g1:/ D F />`, :g:`/ D G / <0091.g1:/ D G />` be
drawn perpendicular to the straight
lines :g:`/ A B / <0091.g1:/ A B />`, :g:`/ B C / <0091.g1:/ B C />`, :g:`/ C A / <0091.g1:/ C A />`.

.. picture:: 0091.g1.svg
   :alt: Proposition 4 diagram

Now, since the angle :g:`< A B D ) <0091.g1:< A B D )>`
is :eq:`equal <0091.g1:< A B D ) = 0091.g1:< C B D )>` to the angle :g:`< C B D ) <0091.g1:< C B D )>`,
and the right angle :g:`< B E D ) <0091.g1:< B E D )>` is also :eq:`equal <0091.g1:< B E D ) = 0091.g1:< B F D )>` to the right angle
:g:`< B F D ) <0091.g1:< B F D )>`,
:g:`< E B D > <0091.g1:< E B D >>`, :g:`< F B D > <0091.g1:< F B D >>` are two triangles having two angles equal to two
angles and one side equal to one side, namely that subtending
one of the equal angles, which is :g:`/ B D / <0091.g1:/ B D />` common to the
triangles;
therefore they will also have the remaining sides equal to
the remaining sides; :just:`[G.37] <G.37>`

.. assertion::

   therefore :g:`/ D E / <0091.g1:/ D E />` is :eq:`equal <0091.g1:/ D E / = 0091.g1:/ D F />` to :g:`/ D F / <0091.g1:/ D F />`.

For the same reason

.. assertion::

   :g:`/ D G / <0091.g1:/ D G />` is also :eq:`equal <0091.g1:/ D G / = 0091.g1:/ D F />` to :g:`/ D F / <0091.g1:/ D F />`.

Therefore the three straight lines :g:`/ D E / <0091.g1:/ D E />`, :g:`/ D F / <0091.g1:/ D F />`, :g:`/ D G / <0091.g1:/ D G />` are :eq:`equal <0091.g1:/ D E / = 0091.g1:/ D F / = 0091.g1:/ D G />`
to one another;
therefore the circle described with centre :g:`D <0091.g1:D>` and distance
one of the straight lines :g:`/ D E / <0091.g1:/ D E />`, :g:`/ D F / <0091.g1:/ D F />`, :g:`/ D G / <0091.g1:/ D G />` will pass also
through the remaining points, and will touch the straight
lines :g:`/ A B / <0091.g1:/ A B />`, :g:`/ B C / <0091.g1:/ B C />`, :g:`/ C A / <0091.g1:/ C A />`, because the angles at the points :g:`E <0091.g1:E>`, :g:`F <0091.g1:F>`, :g:`G <0091.g1:G>`
are right.

For, if it cuts them, the straight line drawn at right angles
to the diameter of the circle from its extremity will be found
to fall within the circle: which was proved absurd; :just:`[G.94] <G.94>`
therefore the circle described with centre :g:`D <0091.g1:D>` and distance
one of the straight lines :g:`/ D E / <0091.g1:/ D E />`, :g:`/ D F / <0091.g1:/ D F />`, :g:`/ D G / <0091.g1:/ D G />` will not cut the
straight lines :g:`/ A B / <0091.g1:/ A B />`, :g:`/ B C / <0091.g1:/ B C />`, :g:`/ C A / <0091.g1:/ C A />`;
therefore it will touch them, and will be the circle inscribed
in the triangle :g:`< A B C > <0091.g1:< A B C >>`. :just:`[G.120] <G.120>`

Let it be inscribed, as :g:`( F G E ) <0091.g1:( F G E )>`.

Therefore in the given triangle :g:`< A B C > <0091.g1:< A B C >>` the circle :g:`( E F G ) <0091.g1:( E F G )>` has
been inscribed.

.. qed::

   :just:`Q. E. F.`

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
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals be added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): That all right angles are equal to one another.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): If two straight lines cut one another, they make the vertical angles equal to one another.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): [8] 5. The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle two angles taken together in any manner are less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of...", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.94" [label="G.94", tooltip="G.94 (III.16): The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumfere...", fillcolor="#222244", URL="../G.94/index.html", target="_top"];
     "G.120" [label="G.120", tooltip="G.120 (IV.def.5): Similarly a circle is said to be inscribed in a figure when the circumference of the circle touches each side of the figure in which it is inscribed.", fillcolor="#224422", URL="../G.120/index.html", target="_top"];
     "G.121" [label="G.121", tooltip="G.121 (IV.4): In a given triangle to inscribe a circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.28" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.27" -> "G.9";
     "G.29" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.94" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.17" -> "G.16";
     "G.121" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.94" -> "G.28";
     "G.30" -> "G.29";
     "G.94" -> "G.30";
     "G.121" -> "G.37";
     "G.121" -> "G.94";
     "G.121" -> "G.120";
   }
