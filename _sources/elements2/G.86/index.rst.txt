:order: 86
:number: 86
:canonical_id: G.86
:original_id: III.11
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, tangent, equality, reductio-ad-absurdum
:dependencies: 
:excerpt: If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the circles.

.. _G.86:
.. _III.11:

G.86
====

.. rubric:: `III.11 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/11/>`_

.. enunciation::

   If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the circles.

.. picture:: g1.svg
   :alt: Diagram for Proposition 11 showing circles ABC and ADE touching internally at A

.. step:: assert

   For let the two circles :g:`( A B C ) <g1:( A B C )>`, :g:`( A D E ) <g1:( A D E )>` touch one another internally at :g:`A <g1:A>`

.. step:: construct

   Let the center :g:`F <g1:F>` of :g:`( A B C ) <g1:( A B C )>`, and the center :g:`G <g1:G>` of :g:`( A D E ) <g1:( A D E )>`, be taken

.. step:: assert

   For suppose it does not, but, if possible, let it fall as :g:`/ F G H / <g1:/ F G H />`

.. step:: construct

   **segment** :g:`/ A F / <g1:/ A F />`, :g:`/ A G / <g1:/ A G />`

.. step:: assert

   Since :g:`/ A G / <g1:/ A G />`, :g:`/ G F / <g1:/ G F />` are greater than :g:`/ F A / <g1:/ F A />`, that is, than :g:`/ F H / <g1:/ F H />` → let :g:`/ F G / <g1:/ F G />` be subtracted from each;

.. step:: assert

   Therefore the remainder :g:`/ A G / <g1:/ A G />` is greater than the remainder :g:`/ G H / <g1:/ G H />`.

.. step:: assert

   :g:`/ A G / <g1:/ A G />` is :eq:`equal <g1:/ A G / = g1:/ G D />` to :g:`/ G D / <g1:/ G D />`

.. step:: assert

   Therefore :g:`/ G D / <g1:/ G D />` is also greater than :g:`/ G H / <g1:/ G H />`,

.. step:: assert

   The less than the greater: which is impossible.

.. step:: assert

   Therefore the straight line joined from :g:`F <g1:F>` to :g:`G <g1:G>` will not fall outside;

.. step:: conclude

   Therefore it will fall at :g:`A <g1:A>` on the point of contact.

Required for
------------

:ref:`G.89 <G.89>`

.. toctree::
   :hidden:

   code
   heath
