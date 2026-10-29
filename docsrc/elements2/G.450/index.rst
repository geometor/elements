:order: 450
:number: 450
:canonical_id: G.450
:original_id: XI.7
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, circle, parallel, plane, reductio-ad-absurdum
:dependencies: G.445
:excerpt: If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.

.. _G.450:
.. _XI.7:

G.450
=====

.. rubric:: `XI.7 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/07/>`_

.. enunciation::

   If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.

.. picture:: g1.svg
   :alt: Book XI - Proposition 7

.. step:: given

   :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` be two parallel straight lines

.. step:: construct

   Let points :g:`E <g1:E>`, :g:`F <g1:F>` be taken at random on them respectively

.. step:: assert

   For suppose it is not, but, if possible, let it be in a more elevated plane as :g:`( E G F ) <g1:( E G F )>`

.. step:: construct

   Let a plane be drawn through :g:`( E G F ) <g1:( E G F )>`

.. step:: assert [G.445] <G.445>

   It will then make, as section in the plane of reference, a straight line.

.. step:: assert

   Let it make it, as :g:`/ E F / <g1:/ E F />`

.. step:: assert

   Therefore :g:`( E G F ) <g1:( E G F )>`, :g:`/ E F / <g1:/ E F />` will enclose an area: which is impossible.

.. step:: conclude

   Therefore the straight line joined from :g:`E <g1:E>` to :g:`F <g1:F>` is not in a plane more elevated; therefore the straight line joined from :g:`E <g1:E>` to :g:`F <g1:F>` is in the plane through the parallel straight lines :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.450" -> "G.445";
   }

Required for
------------

:ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.454 <G.454>`, :ref:`G.455 <G.455>`, :ref:`G.459 <G.459>`, :ref:`G.463 <G.463>`, :ref:`G.468 <G.468>`, :ref:`G.469 <G.469>`, :ref:`G.470 <G.470>`, :ref:`G.471 <G.471>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.520 <G.520>`, :ref:`G.521 <G.521>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
