:order: 456
:number: 456
:canonical_id: G.456
:original_id: XI.13
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, right-angle, plane, equality, reductio-ad-absurdum
:dependencies: G.445, G.446
:excerpt: From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

.. _G.456:
.. _XI.13:

G.456
=====

.. rubric:: `XI.13 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/13/>`_

.. enunciation::

   From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

.. signature:: theorem

   | :fn:`point_straight_lines <G.456>`\ ()
   | **prove** They are in one plane: which is impossible

.. picture:: g1.svg
   :alt: Proposition 13

.. step:: construct

   If possible, from the same point :g:`A <g1:A>` let :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />` be set up at right angles to the plane of reference and on the same side, and let a plane be drawn through :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`

.. step:: assert ∵ planes_cut_common <G.445>

   It will then make, as section through :g:`A <g1:A>` in the plane of reference, a straight line.

.. step:: assert

   Let it make :g:`/ D A E / <g1:/ D A E />`

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`, :g:`/ D A E / <g1:/ D A E />` are in one plane.

.. step:: assert ∵ straight_line_right_def <G.446>

   And, since :g:`/ C A / <g1:/ C A />` is at right angles to the plane of reference, it will also make right angles with all the straight lines which meet it and are in the plane of reference.

.. step:: assert

   :g:`/ D A E / <g1:/ D A E />` meets it and is in the plane of reference;

.. step:: assert

   Therefore :g:`< C A E ) <g1:< C A E )>` is right.

.. step:: assert

   For the same reason :g:`< B A E ) <g1:< B A E )>` is also right;

.. step:: assert

   Therefore :g:`< C A E ) <g1:< C A E )>` is :eq:`equal <g1:< C A E ) = g1:< B A E )>` to :g:`< B A E ) <g1:< B A E )>`.

.. step:: conclude

   They are in one plane: which is impossible.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.456" [label="G.456", tooltip="G.456 (XI.13): From the same point two straight lines cannot be set up at right angles to the same plane on the same side.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.456" -> "G.445";
     "G.456" -> "G.446";
   }

Required for
------------

:ref:`G.464 <G.464>`

.. toctree::
   :hidden:

   code
   heath
