:order: 460
:number: 460
:canonical_id: G.460
:original_id: XI.16
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, quadrilateral, polygon, parallel, plane, reductio-ad-absurdum
:dependencies: G.38, G.443
:excerpt: If two parallel planes be cut by any plane, their common sections are parallel.

.. _G.460:
.. _XI.16:

G.460
=====

.. rubric:: `XI.16 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/16/>`_

.. enunciation::

   If two parallel planes be cut by any plane, their common sections are parallel.

For let the two parallel planes :g:`< A B > <0304.g1:< A B >>`, :g:`< C D > <0304.g1:< C D >>` be cut by the plane :g:`< E F G H > <0304.g1:< E F G H >>`, and let :g:`/ E F / <0304.g1:/ E F />`, :g:`/ G H / <0304.g1:/ G H />` be their common sections ; I say that :g:`/ E F / <0304.g1:/ E F />` is parallel to :g:`/ G H / <0304.g1:/ G H />`.

.. picture:: 0304.g1.svg
   :alt: Book XI, Proposition 16

.. subclause::

   For, if not, :g:`/ E F / <0304.g1:/ E F />`, :g:`/ G H / <0304.g1:/ G H />` will, when produced, meet either in the direction of :g:`F <0304.g1:F>`, :g:`H <0304.g1:H>` or of :g:`E <0304.g1:E>`, :g:`G <0304.g1:G>`. Let them be produced, as in the direction of :g:`F <0304.g1:F>`, :g:`H <0304.g1:H>`, and let them, first, meet at :g:`K <0304.g1:K>`.

.. subclause::

   Now, since :g:`/ E F K / <0304.g1:/ E F K />` is in the plane :g:`< A B > <0304.g1:< A B >>`,

.. assertion::

   therefore all the points on :g:`/ E F K / <0304.g1:/ E F K />` are also in the plane :g:`< A B > <0304.g1:< A B >>`. :just:`[G.443] <G.443>`

.. subclause::

   But :g:`K <0304.g1:K>` is one of the points on the straight line :g:`/ E F K / <0304.g1:/ E F K />`;

.. assertion::

   therefore :g:`K <0304.g1:K>` is in the plane :g:`< A B > <0304.g1:< A B >>`.

.. subclause::

   For the same reason :g:`K <0304.g1:K>` is also in the plane :g:`< C D > <0304.g1:< C D >>`;

.. assertion::

   therefore the planes :g:`< A B > <0304.g1:< A B >>`, :g:`< C D > <0304.g1:< C D >>` will meet when produced.

.. subclause::

   But they do not meet, because they are, by hypothesis, parallel;

.. assertion::

   therefore the straight lines :g:`/ E F / <0304.g1:/ E F />`, :g:`/ G H / <0304.g1:/ G H />` will not meet when produced in the direction of :g:`F <0304.g1:F>`, :g:`H <0304.g1:H>`.

.. assertion::

   Similarly we can prove that neither will the straight lines :g:`/ E F / <0304.g1:/ E F />`, :g:`/ G H / <0304.g1:/ G H />` meet when produced in the direction of :g:`E <0304.g1:E>`, :g:`G <0304.g1:G>`.

.. subclause::

   But straight lines which do not meet in either direction are parallel. :just:`[G.38] <G.38>`

.. assertion::

   Therefore :g:`/ E F / <0304.g1:/ E F />` is parallel to :g:`/ G H / <0304.g1:/ G H />`.

.. assertion::

   Therefore etc.

.. qed::

   :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.460" [label="G.460", tooltip="G.460 (XI.16): If two parallel planes be cut by any plane, their common sections are parallel.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.460" -> "G.38";
     "G.460" -> "G.443";
   }

Required for
------------

:ref:`G.461 <G.461>`, :ref:`G.469 <G.469>`, :ref:`G.470 <G.470>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.486 <G.486>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`
