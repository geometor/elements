:order: 81
:number: 81
:canonical_id: G.81
:original_id: III.6
:volume: II
:book: III
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, circles
:category: theorem, proof, plane-geometry, circles
:tags: book-iii, point, segment, circle, tangent, equality, reductio-ad-absurdum
:dependencies: 
:excerpt: If two circles touch one another, they will not have the same centre.

.. _G.81:
.. _III.6:

G.81
====

.. rubric:: `III.6 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/06/>`_

.. enunciation::

   If two circles touch one another, they will not have the same centre.

.. picture:: g1.svg
   :alt: Proposition 6 Diagram

.. step:: assert

   For let the two circles :g:`( A B C ) <g1:( A B C )>`, :g:`( C D E ) <g1:( C D E )>` touch one another at :g:`C <g1:C>`

.. step:: assert

   If possible, let it be :g:`F <g1:F>`

.. step:: construct

   **segment** :g:`/ F C / <g1:/ F C />`

.. step:: construct

   Let :g:`/ F E B / <g1:/ F E B />` be drawn through at random.

.. step:: assert

   Since :g:`F <g1:F>` is the center of :g:`( A B C ) <g1:( A B C )>` → :g:`/ F C / <g1:/ F C />` is :eq:`equal <g1:/ F C / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`.

.. step:: assert

   Since :g:`F <g1:F>` is the center of :g:`( C D E ) <g1:( C D E )>` → :g:`/ F C / <g1:/ F C />` is :eq:`equal <g1:/ F C / = g1:/ F E />` to :g:`/ F E / <g1:/ F E />`.

.. step:: assert

   :g:`/ F C / <g1:/ F C />` was proved :eq:`equal <g1:/ F C / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`

.. step:: assert

   Therefore :g:`/ F E / <g1:/ F E />` is also :eq:`equal <g1:/ F E / = g1:/ F B />` to :g:`/ F B / <g1:/ F B />`, the less to the greater: which is impossible.

.. step:: conclude

   Therefore :g:`F <g1:F>` is not the center of :g:`( A B C ) <g1:( A B C )>`, :g:`( C D E ) <g1:( C D E )>`.

.. toctree::
   :hidden:

   code
   heath
