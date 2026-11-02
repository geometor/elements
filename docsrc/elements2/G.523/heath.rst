:canonical_id: G.523
:original_id: XI.19
:title: G.523 planes cut right
:volume: III
:book: XI
:type: prop

G.523 planes cut right — Heath
==============================

.. rubric:: `XI.19 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/19/>`_

.. enunciation::

   If two :term:`planes <G.7>` which cut one another be :term:`at right angles <G.32>` to any plane, their common section will also be :term:`at right angles to the same plane <G.505>`.

For let the two planes :g:`< A B > <g1:< A B >>`, :g:`< B C > <g1:< B C >>` be at right angles to the plane of reference, and let :g:`/ B D / <g1:/ B D />` be their common section; I say that :g:`/ B D / <g1:/ B D />` is at right angles to the plane of reference.

.. picture:: g1.svg
   :alt: Book XI, Proposition 19

For suppose it is not, and from the :term:`point <G.1>` :g:`D <g1:D>` let :g:`/ D E / <g1:/ D E />` be drawn in the plane :g:`< A B > <g1:< A B >>` at right angles to the :term:`straight line <G.4>` :g:`/ A D / <g1:/ A D />`, and :g:`/ D F / <g1:/ D F />` in the plane :g:`< B C > <g1:< B C >>` at right angles to :g:`/ C D / <g1:/ C D />`.

.. subclause::

   Now, since the plane :g:`< A B > <g1:< A B >>` is at right angles to the plane of reference, and :g:`/ D E / <g1:/ D E />` has been drawn in the plane :g:`< A B > <g1:< A B >>` at right angles to :g:`/ A D / <g1:/ A D />`, their common section,

.. assertion:: [G.521] <G.521>

   therefore :g:`/ D E / <g1:/ D E />` is at right angles to the plane of reference.

.. assertion::

   Similarly we can prove that :g:`/ D F / <g1:/ D F />` is also at right angles to the plane of reference.

.. assertion::

   Therefore from the same point :g:`D <g1:D>` two straight lines have been set up at right angles to the plane of reference on the same side: which is impossible. :just:`[G.515] <G.515>`

.. assertion::

   Therefore no straight line except the common section :g:`/ D B / <g1:/ D B />` of the planes :g:`< A B > <g1:< A B >>`, :g:`< B C > <g1:< B C >>` can be set up from the point :g:`D <g1:D>` at right angles to the plane of reference.

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
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", fillcolor="#222244", URL="../G.504/index.html", target="_top"];
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.515" [label="G.515", tooltip="G.515 (XI.13): From the same point two segments cannot be set up at right angles to the same plane on the same side.", fillcolor="#222244", URL="../G.515/index.html", target="_top"];
     "G.521" [label="G.521", tooltip="G.521 (XI.def.4): Aplane is at right angles to a plane when thesegments drawn, in one of theplanes,at right angles to the common section of the planes are at right angles to the remaining plane.", fillcolor="#224422", URL="../G.521/index.html", target="_top"];
     "G.523" [label="G.523", tooltip="G.523 (XI.19): If two planes which cut one another be at right angles to any plane, their common section is at right angles to the same plane.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.515" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.22" -> "G.4";
     "G.32" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.515" -> "G.4";
     "G.521" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.504" -> "G.7";
     "G.505" -> "G.7";
     "G.521" -> "G.7";
     "G.523" -> "G.7";
     "G.32" -> "G.22";
     "G.505" -> "G.32";
     "G.521" -> "G.32";
     "G.523" -> "G.32";
     "G.515" -> "G.504";
     "G.515" -> "G.505";
     "G.523" -> "G.505";
     "G.523" -> "G.515";
     "G.523" -> "G.521";
   }
