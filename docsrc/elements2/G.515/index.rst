:order: 515
:number: 515
:canonical_id: G.515
:original_id: XI.13
:title: G.515 point segments set
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, straight-line, right-angles-to-plane, plane-surface, right-angle, plane-angle, plane, equality, reductio-ad-absurdum
:dependencies: G.1, G.4, G.7, G.33, G.504, G.505
:excerpt: From the same point two segments cannot be set up at right angles to the same plane on the same side.

.. _G.515:
.. _XI.13:

G.515 point segments set
========================

.. rubric:: `XI.13 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/13/>`_

.. enunciation::

   From the same :term:`point <G.1>` two :term:`segments <G.4>` cannot be set up :term:`at right angles to the same plane <G.505>` on the same side.

.. signature:: theorem

   | :fn:`point_segments_set <G.515>`\ ()
   | **prove** They are in one plane ⇒⇐

.. picture:: g1.svg
   :alt: Proposition 13

.. step:: construct

   If possible, from the same point :g:`A <g1:A>` let :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />` be set up at right angles to the plane of reference and on the same side, and let a :term:`plane <G.7>` be drawn through :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`

.. step:: assert ∵ planes_cut_common <G.504>

   It will then make, as section through :g:`A <g1:A>` in the plane of reference, a segment

.. step:: assert

   Let it make :g:`/ D A E / <g1:/ D A E />`

.. step:: assert

   :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`, :g:`/ D A E / <g1:/ D A E />` are in one plane

.. step:: assert ∵ segment_right_angles_def <G.505>

   since :g:`/ C A / <g1:/ C A />` is at right angles to the plane of reference, it will also make :term:`right angles <G.33>` with all the segments which meet it and are in the plane of reference

.. step:: assert

   :g:`/ D A E / <g1:/ D A E />` meets it and is in the plane of reference

.. step:: assert

   :g:`< C A E ) <g1:< C A E )>` is right

.. step:: assert

   For the same reason :g:`< B A E ) <g1:< B A E )>` is also right

.. step:: assert

   :g:`< C A E ) <g1:< C A E )>` :eq:`= <g1:< C A E ) = g1:< B A E )>` :g:`< B A E ) <g1:< B A E )>`

.. step:: conclude

   They are in one plane ⇒⇐

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
     "G.33" [label="G.33", tooltip="G.33 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.33/index.html", target="_top"];
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", fillcolor="#222244", URL="../G.504/index.html", target="_top"];
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.515" [label="G.515", tooltip="G.515 (XI.13): From the same point two segments cannot be set up at right angles to the same plane on the same side.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.515" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.7" -> "G.2";
     "G.22" -> "G.2";
     "G.33" -> "G.2";
     "G.504" -> "G.2";
     "G.4" -> "G.3";
     "G.504" -> "G.3";
     "G.7" -> "G.4";
     "G.22" -> "G.4";
     "G.33" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.515" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.504" -> "G.7";
     "G.505" -> "G.7";
     "G.515" -> "G.7";
     "G.33" -> "G.22";
     "G.505" -> "G.33";
     "G.515" -> "G.33";
     "G.515" -> "G.504";
     "G.515" -> "G.505";
   }

Required for
------------

:ref:`G.523 <G.523>`

.. toctree::
   :hidden:

   code
   heath
