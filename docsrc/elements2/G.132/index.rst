:order: 132
:number: 132
:canonical_id: G.132
:original_id: IV.14
:volume: II
:book: IV
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry, circles, polygons
:category: problem, construction, plane-geometry, circles, polygons
:tags: book-iv, point, segment, circle, angle, polygon, equilateral, circumscribed, pentagon, equality
:dependencies: G.13
:excerpt: About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.

.. _G.132:
.. _IV.14:

G.132
=====

.. rubric:: `IV.14 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/14/>`_

.. enunciation::

   About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.

.. picture:: g1.svg
   :alt: Book IV Proposition 14: Circle circumscribed about regular pentagon ABCDE

.. step:: given

   :g:`< A B C D E > <g1:< A B C D E >>` be the given pentagon, which is equilateral and equiangular

.. step:: construct

   Let :g:`< B C D ) <g1:< B C D )>`, :g:`< C D E ) <g1:< C D E )>` be bisected by :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />` respectively

.. step:: construct

   From :g:`F <g1:F>`, at which the straight lines meet, let :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` be joined to :g:`B <g1:B>`, :g:`A <g1:A>`, :g:`E <g1:E>`.

.. step:: assert

   Then in manner similar to the preceding it can be proved that :g:`< C B A ) <g1:< C B A )>`, :g:`< B A E ) <g1:< B A E )>`, :g:`< A E D ) <g1:< A E D )>` have also been bisected by :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` respectively.

.. step:: assert

   Since :g:`< B C D ) <g1:< B C D )>` is :eq:`equal <g1:< B C D ) = g1:< C D E )>` to :g:`< C D E ) <g1:< C D E )>`, and :g:`< F C D ) <g1:< F C D )>` is half of :g:`< B C D ) <g1:< B C D )>`, and :g:`< C D F ) <g1:< C D F )>` half of :g:`< C D E ) <g1:< C D E )>` → therefore :g:`< F C D ) <g1:< F C D )>` is also :eq:`equal <g1:< F C D ) = g1:< C D F )>` to :g:`< C D F ) <g1:< C D F )>`,

.. step:: assert [G.13] <G.13>

   So that the side :g:`/ F C / <g1:/ F C />` is also :eq:`equal <g1:/ F C / = g1:/ F D />` to the side :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   Similarly it can be proved that each of :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` is also :eq:`equal <g1:/ F B / = g1:/ F A / = g1:/ F E / = g1:/ F C / = g1:/ F D />` to each of :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />`

.. step:: assert

   Therefore the five straight lines :g:`/ F A / <g1:/ F A />`, :g:`/ F B / <g1:/ F B />`, :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />`, :g:`/ F E / <g1:/ F E />` are :eq:`equal <g1:/ F A / = g1:/ F B / = g1:/ F C / = g1:/ F D / = g1:/ F E />` to one another.

.. step:: assert

   Therefore the circle described with center :g:`F <g1:F>` and distance one of :g:`/ F A / <g1:/ F A />`, :g:`/ F B / <g1:/ F B />`, :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />`, :g:`/ F E / <g1:/ F E />` will pass also through the remaining points, and will have been circumscribed.

.. step:: assert

   Let it be circumscribed

.. step:: conclude

   Let it be :g:`( A B C D E ) <g1:( A B C D E )>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.13" [label="G.13", tooltip="G.13 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", fillcolor="#222244", URL="../G.13/index.html", target="_top"];
     "G.132" [label="G.132", tooltip="G.132 (IV.14): About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.132" -> "G.13";
   }

Required for
------------

:ref:`G.515 <G.515>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
