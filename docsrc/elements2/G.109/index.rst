:order: 109
:number: 109
:canonical_id: G.109
:original_id: III.30
:volume: II
:book: III
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles
:category: problem, construction, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, bisect, arc, equality
:dependencies: G.11, G.107
:excerpt: To bisect a given circumference.

.. _G.109:
.. _III.30:

G.109
=====

.. rubric:: `III.30 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/30/>`_

.. enunciation::

   To bisect a given circumference.

Let :g:`( A D B ) <0067.g1:( A D B )>` be the given circumference;
thus it is required to bisect the circumference :g:`( A D B ) <0067.g1:( A D B )>`.

Let :g:`/ A B / <0067.g1:/ A B />` be joined and bisected at
:g:`C <0067.g1:C>`; from the point :g:`C <0067.g1:C>` let :g:`/ C D / <0067.g1:/ C D />` be drawn
at right angles to the straight line :g:`/ A B / <0067.g1:/ A B />`,
and let :g:`/ A D / <0067.g1:/ A D />`, :g:`/ D B / <0067.g1:/ D B />` be joined.

.. picture:: 0067.g1.svg
   :alt: Diagram

Then, since :g:`/ A C / <0067.g1:/ A C />` is :eq:`equal <0067.g1:/ A C / = 0067.g1:/ C B />` to :g:`/ C B / <0067.g1:/ C B />`,
and :g:`/ C D / <0067.g1:/ C D />` is common,
the two sides :g:`/ A C / <0067.g1:/ A C />`, :g:`/ C D / <0067.g1:/ C D />` are :eq:`equal <0067.g1:/ A C / = 0067.g1:/ B C /; 0067.g1:/ C D / = 0067.g1:/ C D />` to the two sides :g:`/ B C / <0067.g1:/ B C />`, :g:`/ C D / <0067.g1:/ C D />`;
and the angle :g:`< A C D ) <0067.g1:< A C D )>` is :eq:`equal <0067.g1:< A C D ) = 0067.g1:< B C D )>` to the angle :g:`< B C D ) <0067.g1:< B C D )>`, for each is
right;

.. assertion:: [G.11] <G.11>

   therefore the base :g:`/ A D / <0067.g1:/ A D />` is :eq:`equal <0067.g1:/ A D / = 0067.g1:/ D B />` to the base :g:`/ D B / <0067.g1:/ D B />`.

But equal straight lines cut off equal circumferences, the
greater equal to the greater, and the less to the less; :just:`[G.107] <G.107>`

.. subclause::

   and each of the circumferences :g:`( A D ) <0067.g1:( A D )>`, :g:`( D B ) <0067.g1:( D B )>` is less than a semicircle;

.. assertion::

   therefore the circumference :g:`( A D ) <0067.g1:( A D )>` is :eq:`equal <0067.g1:( A D ) = 0067.g1:( D B )>` to the circumference :g:`( D B ) <0067.g1:( D B )>`.

Therefore the given circumference has been bisected at
the point :g:`D <0067.g1:D>`.

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
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is cal...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): To find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.85/index.html", target="_top"];
     "G.101" [label="G.101", tooltip="G.101 (III.def.11): Similar segments of circles are those which admit equal angles, or in which the angles are equal to one another.", fillcolor="#224422", URL="../G.101/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.24): Similar segments of circles on equal straight lines are equal to one another.", fillcolor="#222244", URL="../G.103/index.html", target="_top"];
     "G.105" [label="G.105", tooltip="G.105 (III.26): In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.105/index.html", target="_top"];
     "G.107" [label="G.107", tooltip="G.107 (III.28): In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.", fillcolor="#222244", URL="../G.107/index.html", target="_top"];
     "G.109" [label="G.109", tooltip="G.109 (III.30): To bisect a given circumference.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.80" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.105" -> "G.11";
     "G.109" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.76" -> "G.15";
     "G.107" -> "G.15";
     "G.76" -> "G.18";
     "G.85" -> "G.76";
     "G.85" -> "G.80";
     "G.103" -> "G.85";
     "G.105" -> "G.101";
     "G.105" -> "G.103";
     "G.107" -> "G.105";
     "G.109" -> "G.107";
   }

Required for
------------

:ref:`G.134 <G.134>`
