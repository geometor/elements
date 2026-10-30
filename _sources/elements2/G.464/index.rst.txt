:order: 464
:number: 464
:canonical_id: G.464
:original_id: XI.19
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, polygon, right-angle, plane, reductio-ad-absurdum
:dependencies: G.456, G.462
:excerpt: If two planes which cut one another be at right angles to any plane, their common section is at right angles to the same plane.

.. _G.464:
.. _XI.19:

G.464
=====

.. rubric:: `XI.19 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/19/>`_

.. enunciation::

   If two planes which cut one another be at right angles to any plane, their common section is at right angles to the same plane.

.. signature:: theorem

   | :fn:`planes_cut_right <G.464>`\ ()
   | **prove** :g:`/ B D / <g1:/ B D />` is at right angles to the plane of reference

.. picture:: g1.svg
   :alt: Book XI, Proposition 19

.. step:: assert

   Let the two planes :g:`< A B > <g1:< A B >>`, :g:`< B C > <g1:< B C >>` be at right angles to the plane of reference, and let :g:`/ B D / <g1:/ B D />` be their common section

.. step:: construct

   Suppose it is not, and from :g:`D <g1:D>` let :g:`/ D E / <g1:/ D E />` be drawn in the plane :g:`< A B > <g1:< A B >>` at right angles to :g:`/ A D / <g1:/ A D />`, and :g:`/ D F / <g1:/ D F />` in the plane :g:`< B C > <g1:< B C >>` at right angles to :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   Since the plane :g:`< A B > <g1:< A B >>` is at right angles to the plane of reference, and :g:`/ D E / <g1:/ D E />` has been drawn in the plane :g:`< A B > <g1:< A B >>` at right angles to :g:`/ A D / <g1:/ A D />`, their common section,

.. step:: assert ∵ plane_right_angles_def <G.462>

   Therefore :g:`/ D E / <g1:/ D E />` is at right angles to the plane of reference.

.. step:: assert

   Similarly we can prove that :g:`/ D F / <g1:/ D F />` is also at right angles to the plane of reference.

.. step:: assert ∵ point_straight_lines <G.456>

   Therefore from the same point :g:`D <g1:D>` two straight lines have been set up at right angles to the plane of reference on the same side: which is impossible.

.. step:: conclude

   Therefore no straight line except the common section :g:`/ D B / <g1:/ D B />` of the planes :g:`< A B > <g1:< A B >>`, :g:`< B C > <g1:< B C >>` can be set up from :g:`D <g1:D>` at right angles to the plane of reference.

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
     "G.456" [label="G.456", tooltip="G.456 (XI.13): From the same point two straight lines cannot be set up at right angles to the same plane on the same side.", fillcolor="#222244", URL="../G.456/index.html", target="_top"];
     "G.462" [label="G.462", tooltip="G.462 (XI.def.4): Aplane is at right angles to a plane when the straight lines drawn, in one of the planes, at right angles to the common section of the planes are at right angles to the remaining p...", fillcolor="#224422", URL="../G.462/index.html", target="_top"];
     "G.464" [label="G.464", tooltip="G.464 (XI.19): If two planes which cut one another be at right angles to any plane, their common section is at right angles to the same plane.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.456" -> "G.445";
     "G.456" -> "G.446";
     "G.464" -> "G.456";
     "G.464" -> "G.462";
   }

.. toctree::
   :hidden:

   code
   heath
