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

For, if possible, from the same point :g:`A <0299.g1:A>` let the two straight lines :g:`/ A B / <0299.g1:/ A B />`, :g:`/ A C / <0299.g1:/ A C />` be set up at right angles to the plane of reference and on the same side, and let a plane be drawn through :g:`/ B A / <0299.g1:/ B A />`, :g:`/ A C / <0299.g1:/ A C />`; it will then make, as section through :g:`A <0299.g1:A>` in the plane of reference, a straight line. :just:`[G.445] <G.445>`

.. picture:: 0299.g1.svg
   :alt: Proposition 13

Let it make :g:`/ D A E / <0299.g1:/ D A E />`;

.. assertion::

   therefore the straight lines :g:`/ A B / <0299.g1:/ A B />`, :g:`/ A C / <0299.g1:/ A C />`, :g:`/ D A E / <0299.g1:/ D A E />` are in one plane.

And, since :g:`/ C A / <0299.g1:/ C A />` is at right angles to the plane of reference, it will also make right angles with all the straight lines which meet it and are in the plane of reference. :just:`[G.446] <G.446>`

.. subclause::

   But :g:`/ D A E / <0299.g1:/ D A E />` meets it and is in the plane of reference;

.. assertion::

   therefore the angle :g:`< C A E ) <0299.g1:< C A E )>` is right.

.. subclause::

   For the same reason the angle :g:`< B A E ) <0299.g1:< B A E )>` is also right;

.. assertion::

   therefore the angle :g:`< C A E ) <0299.g1:< C A E )>` is :eq:`equal <0299.g1:< C A E ) = 0299.g1:< B A E )>` to the angle :g:`< B A E ) <0299.g1:< B A E )>`.

.. assertion::

   And they are in one plane: which is impossible.

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
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line is at right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.456" [label="G.456", tooltip="G.456 (XI.13): From the same point two straight lines cannot be set up at right angles to the same plane on the same side.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.456" -> "G.445";
     "G.456" -> "G.446";
   }

Required for
------------

:ref:`G.464 <G.464>`
