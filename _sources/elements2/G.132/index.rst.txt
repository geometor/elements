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

Let :g:`< A B C D E > <0112.g1:< A B C D E >>` be the given pentagon, which is equilateral
and equiangular;
thus it is required to circumscribe a circle
about the pentagon :g:`< A B C D E > <0112.g1:< A B C D E >>`.

Let the angles :g:`< B C D ) <0112.g1:< B C D )>`, :g:`< C D E ) <0112.g1:< C D E )>` be bisected
by the straight lines :g:`/ F C / <0112.g1:/ F C />`, :g:`/ F D / <0112.g1:/ F D />` respectively,
and from the point :g:`F <0112.g1:F>`, at which the straight
lines meet, let the straight lines :g:`/ F B / <0112.g1:/ F B />`, :g:`/ F A / <0112.g1:/ F A />`,
:g:`/ F E / <0112.g1:/ F E />` be joined to the points :g:`B <0112.g1:B>`, :g:`A <0112.g1:A>`, :g:`E <0112.g1:E>`.

.. picture:: 0112.g1.svg
   :alt: Book IV Proposition 14: Circle circumscribed about regular pentagon ABCDE

Then in manner similar to the preceding
it can be proved that the angles
:g:`< C B A ) <0112.g1:< C B A )>`, :g:`< B A E ) <0112.g1:< B A E )>`, :g:`< A E D ) <0112.g1:< A E D )>` have also been bisected by the straight
lines :g:`/ F B / <0112.g1:/ F B />`, :g:`/ F A / <0112.g1:/ F A />`, :g:`/ F E / <0112.g1:/ F E />` respectively.

Now, since the angle :g:`< B C D ) <0112.g1:< B C D )>` is :eq:`equal <0112.g1:< B C D ) = 0112.g1:< C D E )>` to the angle :g:`< C D E ) <0112.g1:< C D E )>`,
and the angle :g:`< F C D ) <0112.g1:< F C D )>` is half of the angle :g:`< B C D ) <0112.g1:< B C D )>`,
and the angle :g:`< C D F ) <0112.g1:< C D F )>` half of the angle :g:`< C D E ) <0112.g1:< C D E )>`,

.. assertion::

   therefore the angle :g:`< F C D ) <0112.g1:< F C D )>` is also :eq:`equal <0112.g1:< F C D ) = 0112.g1:< C D F )>` to the angle :g:`< C D F ) <0112.g1:< C D F )>`,

.. assertion:: [G.13] <G.13>

   so that the side :g:`/ F C / <0112.g1:/ F C />` is also :eq:`equal <0112.g1:/ F C / = 0112.g1:/ F D />` to the side :g:`/ F D / <0112.g1:/ F D />`.

Similarly it can be proved that
each of the straight lines :g:`/ F B / <0112.g1:/ F B />`, :g:`/ F A / <0112.g1:/ F A />`, :g:`/ F E / <0112.g1:/ F E />` is also :eq:`equal <0112.g1:/ F B / = 0112.g1:/ F A / = 0112.g1:/ F E / = 0112.g1:/ F C / = 0112.g1:/ F D />` to each
of the straight lines :g:`/ F C / <0112.g1:/ F C />`, :g:`/ F D / <0112.g1:/ F D />`;

.. assertion::

   therefore the five straight lines :g:`/ F A / <0112.g1:/ F A />`, :g:`/ F B / <0112.g1:/ F B />`, :g:`/ F C / <0112.g1:/ F C />`, :g:`/ F D / <0112.g1:/ F D />`, :g:`/ F E / <0112.g1:/ F E />` are :eq:`equal <0112.g1:/ F A / = 0112.g1:/ F B / = 0112.g1:/ F C / = 0112.g1:/ F D / = 0112.g1:/ F E />` to one another.

Therefore the circle described with centre :g:`F <0112.g1:F>` and distance
one of the straight lines :g:`/ F A / <0112.g1:/ F A />`, :g:`/ F B / <0112.g1:/ F B />`, :g:`/ F C / <0112.g1:/ F C />`, :g:`/ F D / <0112.g1:/ F D />`, :g:`/ F E / <0112.g1:/ F E />` will pass
also through the remaining points, and will have been
circumscribed.

Let it be circumscribed, and let it be :g:`( A B C D E ) <0112.g1:( A B C D E )>`.

.. qed::

   Therefore about the given pentagon, which is equilateral and equiangular, a circle has been circumscribed. :just:`Q. E. F.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.13" [label="G.13", tooltip="G.13 (I.6): If in a triangle two angles be equal to one another, the sides which subtend the equal angles will also be equal to one another.", fillcolor="#222244", URL="../G.13/index.html", target="_top"];
     "G.132" [label="G.132", tooltip="G.132 (IV.14): About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.132" -> "G.13";
   }

Required for
------------

:ref:`G.515 <G.515>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`
