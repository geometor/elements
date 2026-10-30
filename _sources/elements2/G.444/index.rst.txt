:order: 444
:number: 444
:canonical_id: G.444
:original_id: XI.2
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, triangle, quadrilateral, plane
:dependencies: G.443
:excerpt: If two straight lines cut one another, they are in one plane, and every triangle is in one plane.

.. _G.444:
.. _XI.2:

G.444
=====

.. rubric:: `XI.2 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/02/>`_

.. enunciation::

   If two straight lines cut one another, they are in one plane, and every triangle is in one plane.

.. signature:: theorem

   | :fn:`straight_lines_cut <G.444>`\ ()
   | **prove** :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are in one plane, and every triangle is in one plane

.. picture:: g1.svg
   :alt: Book XI, Proposition 2

.. step:: intersect

   Let :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` cut one another at :g:`E <g1:E>`

.. step:: construct

   :fn:`segment <G.3>`\ () → :g:`F <g1:F>`, :fn:`segment <G.3>`\ () → :g:`G <g1:G>`, :fn:`segment <G.3>`\ (:g:`E <g1:E>`, :g:`C <g1:C>`) → :g:`/ E C / <g1:/ E C />`, :fn:`segment <G.3>`\ (:g:`E <g1:E>`, :g:`B <g1:B>`) → :g:`/ E B / <g1:/ E B />`, :fn:`segment <G.3>`\ (:g:`C <g1:C>`, :g:`B <g1:B>`) → :g:`/ C B / <g1:/ C B />`, :fn:`segment <G.3>`\ (:g:`F <g1:F>`, :g:`G <g1:G>`) → :g:`/ F G / <g1:/ F G />`

.. step:: construct

   Let :g:`/ F H / <g1:/ F H />`, :g:`/ G K / <g1:/ G K />` be drawn across

.. step:: assert

   I say first that :g:`< E C B > <g1:< E C B >>` is in one plane.

.. step:: assert

   If part of :g:`< E C B > <g1:< E C B >>`, either :g:`< F H C > <g1:< F H C >>` or :g:`< G B K > <g1:< G B K >>`, is in the plane of reference, and the rest in another,

.. step:: assert

   A part also of one of :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />` will be in the plane of reference, and a part in another.

.. step:: assert

   But, if the part :g:`< F C B G > <g1:< F C B G >>` of :g:`< E C B > <g1:< E C B >>` be in the plane of reference, and the rest in another,

.. step:: assert

   A part also of both :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />` will be in the plane of reference and a part in another:

.. step:: assert ∵ part_straight_line <G.443>

   Which was proved absurd.

.. step:: assert

   Therefore :g:`< E C B > <g1:< E C B >>` is in one plane.

.. step:: assert ∵ part_straight_line <G.443>

   But, in whatever plane :g:`< E C B > <g1:< E C B >>` is, in that plane also is each of :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />`, and, in whatever plane each of :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />` is, in that plane are :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` also.

.. step:: conclude

   Therefore :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are in one plane, and every triangle is in one plane.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.444" -> "G.443";
   }

Required for
------------

:ref:`G.449 <G.449>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.454 <G.454>`, :ref:`G.455 <G.455>`, :ref:`G.459 <G.459>`, :ref:`G.463 <G.463>`, :ref:`G.468 <G.468>`, :ref:`G.469 <G.469>`, :ref:`G.470 <G.470>`, :ref:`G.471 <G.471>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.520 <G.520>`, :ref:`G.521 <G.521>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
