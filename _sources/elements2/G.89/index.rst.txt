:order: 89
:number: 89
:canonical_id: G.89
:original_id: III.13
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, tangent, equality, reductio-ad-absurdum
:dependencies: G.77, G.86, G.88
:excerpt: A circle does not touch a circle at more points than one, whether it touch it internally or externally.

.. _G.89:
.. _III.13:

G.89
====

.. rubric:: `III.13 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/13/>`_

.. enunciation::

   A circle does not touch a circle at more points than one, whether it touch it internally or externally.

For, if possible, let the circle :g:`( A B D C ) <0038.g3:( A B D C )>` touch the circle
:g:`( E B F D ) <0038.g3:( E B F D )>`, first internally, at more
points than one, namely :g:`D <0038.g3:D>`, :g:`B <0038.g3:B>`.

.. picture:: 0038.g3.svg
   :alt: Proposition 13 diagram

Let the centre :g:`G <0038.g3:G>` of the circle
:g:`( A B D C ) <0038.g3:( A B D C )>`, and the centre :g:`H <0038.g3:H>` of
:g:`( E B F D ) <0038.g3:( E B F D )>`, be taken.

Therefore the straight line
joined from :g:`G <0038.g3:G>` to :g:`H <0038.g3:H>` will fall on
:g:`B <0038.g3:B>`, :g:`D <0038.g3:D>`. :just:`[G.86] <G.86>`

Let it so fall, as :g:`/ B G H D / <0038.g3:/ B G H D />`.

Then, since the point :g:`G <0038.g3:G>` is
the centre of the circle :g:`( A B C D ) <0038.g3:( A B C D )>`,

.. assertion::

   :g:`/ B G / <0038.g3:/ B G />` is :eq:`equal <0038.g3:/ B G / = 0038.g3:/ G D />` to :g:`/ G D / <0038.g3:/ G D />`;

.. assertion::

   therefore :g:`/ B G / <0038.g3:/ B G />` is greater than :g:`/ H D / <0038.g3:/ H D />`;

.. assertion::

   therefore :g:`/ B H / <0038.g3:/ B H />` is much greater than :g:`/ H D / <0038.g3:/ H D />`.

Again, since the point :g:`H <0038.g3:H>` is the centre of the circle
:g:`( E B F D ) <0038.g3:( E B F D )>`,

.. assertion::

   :g:`/ B H / <0038.g3:/ B H />` is :eq:`equal <0038.g3:/ B H / = 0038.g3:/ H D />` to :g:`/ H D / <0038.g3:/ H D />`;

but it was also proved much greater than it: which is
impossible.

Therefore a circle does not touch a circle internally at
more points than one.

I say further that neither does it so touch it externally.

For, if possible, let the circle :g:`( A C K ) <0038.g3:( A C K )>` touch the circle
:g:`( A B D C ) <0038.g3:( A B D C )>` at more points than one, namely :g:`A <0038.g3:A>`, :g:`C <0038.g3:C>`,
and let :g:`/ A C / <0038.g3:/ A C />` be joined.

Then, since on the circumference of each of the circles
:g:`( A B D C ) <0038.g3:( A B D C )>`, :g:`( A C K ) <0038.g3:( A C K )>` two points :g:`A <0038.g3:A>`, :g:`C <0038.g3:C>` have been taken at random,
the straight line joining the points will fall within each
circle; :just:`[G.77] <G.77>`
but it fell within the circle :g:`( A B C D ) <0038.g3:( A B C D )>` and outside :g:`( A C K ) <0038.g3:( A C K )>`
:just:`[G.88] <G.88>`: which is absurd.

Therefore a circle does not touch a circle externally at
more points than one.

And it was proved that neither does it so touch it
internally.

.. qed::

   Therefore etc. :just:`Q. E. D.`

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
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): To find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (III.2): If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.", fillcolor="#222244", URL="../G.77/index.html", target="_top"];
     "G.86" [label="G.86", tooltip="G.86 (III.11): If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the c...", fillcolor="#222244", URL="../G.86/index.html", target="_top"];
     "G.88" [label="G.88", tooltip="G.88 (III.def.3): **Circles** are said to touch one another which, meeting one another, do not cut one another.", fillcolor="#224422", URL="../G.88/index.html", target="_top"];
     "G.89" [label="G.89", tooltip="G.89 (III.13): A circle does not touch a circle at more points than one, whether it touch it internally or externally.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.77" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.76" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.76" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.29" -> "G.27";
     "G.77" -> "G.27";
     "G.30" -> "G.29";
     "G.77" -> "G.30";
     "G.77" -> "G.76";
     "G.89" -> "G.77";
     "G.89" -> "G.86";
     "G.89" -> "G.88";
   }
