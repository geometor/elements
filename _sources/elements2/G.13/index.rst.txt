:order: 13
:number: 13
:canonical_id: G.13
:original_id: I.6
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, angle, triangle, equality, reductio-ad-absurdum
:dependencies: 
:excerpt: If two angles of a triangle are equal, the sides subtending the equal angles are also equal.

.. _G.13:
.. _I.6:

G.13
====

.. rubric:: `I.6 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/06/>`_

.. enunciation::

   If two angles of a triangle are equal, the sides subtending the equal angles are also equal.

.. picture:: g1.svg
   :alt: Proposition 6 figure

.. step:: given

   :g:`< A B C > <g1:< A B C >>` be a triangle having :g:`< A B C ) <g1:< A B C )>` :eq:`equal <g1:< A B C ) = g1:< A C B )>` to :g:`< A C B ) <g1:< A C B )>`

.. step:: assert

   The side :g:`/ A B / <g1:/ A B />` is also :eq:`equal <g1:/ A B / = g1:/ A C />` to the side :g:`/ A C / <g1:/ A C />`.

.. step:: assert

   If :g:`/ A B / <g1:/ A B />` is unequal to :g:`/ A C / <g1:/ A C />`, one of them is greater.

.. step:: assert

   Let :g:`/ A B / <g1:/ A B />` be greater

.. step:: construct

   And from :g:`/ A B / <g1:/ A B />` the greater let :g:`/ D B / <g1:/ D B />` be cut off :eq:`equal <g1:/ D B / = g1:/ A C />` to :g:`/ A C / <g1:/ A C />` the less

.. step:: construct

   **segment** :g:`/ D C / <g1:/ D C />`

.. step:: assert

   Since :g:`/ D B / <g1:/ D B />` is :eq:`equal <g1:/ D B / = g1:/ A C />` to :g:`/ A C / <g1:/ A C />`, and :g:`/ B C / <g1:/ B C />` is common → the two sides :g:`/ D B / <g1:/ D B />`, :g:`/ B C / <g1:/ B C />` are :eq:`equal <g1:/ D B / = g1:/ A C />` to the two sides :g:`/ A C / <g1:/ A C />`, :g:`/ C B / <g1:/ C B />` respectively;

.. step:: assert

   And :g:`< D B C ) <g1:< D B C )>` is :eq:`equal <g1:< D B C ) = g1:< A C B )>` to :g:`< A C B ) <g1:< A C B )>`

.. step:: assert

   Therefore the base :g:`/ D C / <g1:/ D C />` is :eq:`equal <g1:/ D C / = g1:/ A B />` to the base :g:`/ A B / <g1:/ A B />`,

.. step:: assert

   And :g:`< D B C > <g1:< D B C >>` will be :eq:`equal <g1:< D B C > = g1:< A C B >>` to :g:`< A C B > <g1:< A C B >>`,

.. step:: assert

   The less to the greater: which is absurd.

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is not unequal to :g:`/ A C / <g1:/ A C />`

.. step:: conclude

   It is therefore :eq:`equal <g1:/ A B / = g1:/ A C />` to it.

Required for
------------

:ref:`G.65 <G.65>`, :ref:`G.70 <G.70>`, :ref:`G.71 <G.71>`, :ref:`G.73 <G.73>`, :ref:`G.104 <G.104>`, :ref:`G.127 <G.127>`, :ref:`G.128 <G.128>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.132 <G.132>`, :ref:`G.165 <G.165>`, :ref:`G.286 <G.286>`, :ref:`G.341 <G.341>`, :ref:`G.351 <G.351>`, :ref:`G.352 <G.352>`, :ref:`G.353 <G.353>`, :ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.372 <G.372>`, :ref:`G.374 <G.374>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.418 <G.418>`, :ref:`G.435 <G.435>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.514 <G.514>`, :ref:`G.515 <G.515>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
