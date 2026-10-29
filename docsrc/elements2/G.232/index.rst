:order: 232
:number: 232
:canonical_id: G.232
:original_id: VII.31
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number, prime, composite, reductio-ad-absurdum
:dependencies: 
:excerpt: Any composite number is measured by some prime number.

.. _G.232:
.. _VII.31:

G.232
=====

.. rubric:: `VII.31 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/31/>`_

.. enunciation::

   Any composite number is measured by some prime number.

.. picture:: g1.svg
   :alt: Proposition 31 diagram

.. step:: given

   :g:`A <g1:A>` be a composite number

.. step:: assert

   Since :g:`A <g1:A>` is composite, some number will measure it.

.. step:: assert

   Let a number measure it

.. step:: assert

   Let it be :g:`B <g1:B>`.

.. step:: assert

   If :g:`B <g1:B>` is prime, what was enjoined will have been done.

.. step:: assert

   If it is composite, some number will measure it.

.. step:: assert

   Let a number measure it

.. step:: assert

   Let it be :g:`C <g1:C>`.

.. step:: assert

   Since :g:`C <g1:C>` measures :g:`B <g1:B>`, and :g:`B <g1:B>` measures :g:`A <g1:A>`,

.. step:: assert

   Therefore :g:`C <g1:C>` also measures :g:`A <g1:A>`.

.. step:: assert

   And, if :g:`C <g1:C>` is prime, what was enjoined will have been done.

.. step:: assert

   If it is composite, some number will measure it.

.. step:: assert

   Thus, if the investigation be continued in this way, some prime number will be found which will measure the number before it, which will also measure :g:`A <g1:A>`.

.. step:: assert

   If it is not found, an infinite series of numbers will measure the number :g:`A <g1:A>`, each of which is less than the other: which is impossible in numbers.

.. step:: assert

   Therefore some prime number will be found which will measure the one before it, which will also measure :g:`A <g1:A>`.

.. step:: conclude

   Therefore any composite number is measured by some prime number.

Required for
------------

:ref:`G.233 <G.233>`, :ref:`G.284 <G.284>`, :ref:`G.291 <G.291>`, :ref:`G.306 <G.306>`, :ref:`G.312 <G.312>`

.. toctree::
   :hidden:

   code
   heath
