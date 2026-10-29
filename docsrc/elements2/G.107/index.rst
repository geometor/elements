:order: 107
:number: 107
:canonical_id: G.107
:original_id: III.28
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, angle, arc, equality
:dependencies: G.15, G.105
:excerpt: In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

.. _G.107:
.. _III.28:

G.107
=====

.. rubric:: `III.28 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/28/>`_

.. enunciation::

   In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

.. picture:: g1.svg
   :alt: Diagram

.. step:: given

   :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>` be :eq:`equal <g1:( A B C ) = g1:( D E F )>` circles

.. step:: assert

   In the circles let :g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />` be :eq:`equal <g1:/ A B / = g1:/ D E />` straight lines cutting off :g:`( A C B ) <g1:( A C B )>`, :g:`( D F E ) <g1:( D F E )>` as greater circumferences and :g:`( A G B ) <g1:( A G B )>`, :g:`( D H E ) <g1:( D H E )>` as lesser

.. step:: assert

   The greater circumference :g:`( A C B ) <g1:( A C B )>` is :eq:`equal <g1:( A C B ) = g1:( D F E ); g1:( A G B ) = g1:( D H E )>` to the greater circumference :g:`( D F E ) <g1:( D F E )>`, and the less circumference :g:`( A G B ) <g1:( A G B )>` to :g:`( D H E ) <g1:( D H E )>`.

.. step:: construct

   For let the centres :g:`K <g1:K>`, :g:`L <g1:L>` of the circles be taken

.. step:: construct

   **segment** :g:`/ A K / <g1:/ A K />`, :g:`/ K B / <g1:/ K B />`, :g:`/ D L / <g1:/ D L />`, :g:`/ L E / <g1:/ L E />`

.. step:: assert

   Since the circles are :eq:`equal <g1:( A B C ) = g1:( D E F )>` → the radii are also :eq:`equal <g1:/ A K / = g1:/ K B / = g1:/ D L / = g1:/ L E />`; therefore the two sides :g:`/ A K / <g1:/ A K />`, :g:`/ K B / <g1:/ K B />` are :eq:`equal <g1:/ A K / = g1:/ D L /; g1:/ K B / = g1:/ L E />` to the two

.. step:: assert

   Sides :g:`/ D L / <g1:/ D L />`, :g:`/ L E / <g1:/ L E />`

.. step:: assert

   And the base :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g1:/ D E />` to the base :g:`/ D E / <g1:/ D E />`

.. step:: assert [G.15] <G.15>

   Therefore :g:`< A K B ) <g1:< A K B )>` is :eq:`equal <g1:< A K B ) = g1:< D L E )>` to :g:`< D L E ) <g1:< D L E )>`.

.. step:: assert [G.105] <G.105>

   Equal angles stand on equal circumferences, when they are at the centres

.. step:: assert

   Therefore the circumference :g:`( A G B ) <g1:( A G B )>` is :eq:`equal <g1:( A G B ) = g1:( D H E )>` to :g:`( D H E ) <g1:( D H E )>`.

.. step:: assert

   The whole circle :g:`( A B C ) <g1:( A B C )>` is also :eq:`equal <g1:( A B C ) = g1:( D E F )>` to the whole circle :g:`( D E F ) <g1:( D E F )>`

.. step:: conclude

   Therefore the circumference :g:`( A C B ) <g1:( A C B )>` which remains is also :eq:`equal <g1:( A C B ) = g1:( D F E )>` to the circumference :g:`( D F E ) <g1:( D F E )>` which remains.

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
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line standing on a straight line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing line is perpendicular to that on which...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (III.1): Find the centre of a given circle.", fillcolor="#222244", URL="../G.76/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.85" [label="G.85", tooltip="G.85 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.85/index.html", target="_top"];
     "G.101" [label="G.101", tooltip="G.101 (III.def.11): Similar segments of circles are those which admit equal angles, or in which the angles are equal.", fillcolor="#224422", URL="../G.101/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.24): Similar segments of circles on equal straight lines are equal.", fillcolor="#222244", URL="../G.103/index.html", target="_top"];
     "G.105" [label="G.105", tooltip="G.105 (III.26): In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.", fillcolor="#222244", URL="../G.105/index.html", target="_top"];
     "G.107" [label="G.107", tooltip="G.107 (III.28): In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
   }

Required for
------------

:ref:`G.109 <G.109>`, :ref:`G.134 <G.134>`, :ref:`G.515 <G.515>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
