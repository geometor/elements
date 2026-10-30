:order: 230
:number: 230
:canonical_id: G.230
:original_id: VII.29
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number, prime, reductio-ad-absurdum
:dependencies: 
:excerpt: Any prime number is prime to any number which it does not measure.

.. _G.230:
.. _VII.29:

G.230
=====

.. rubric:: `VII.29 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/29/>`_

.. enunciation::

   Any prime number is prime to any number which it does not measure.

.. signature:: theorem

   | :fn:`prime_number_prime <G.230>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`)
   | **given** :g:`A <g1:A>` be a prime number, let it not measure :g:`B <g1:B>`
   | **prove** :g:`B <g1:B>`, :g:`A <g1:A>` are prime to one another

.. picture:: g1.svg
   :alt: Book VII, Proposition 29

.. step:: given

   :g:`A <g1:A>` be a prime number, let it not measure :g:`B <g1:B>`

.. step:: assert

   If :g:`B <g1:B>`, :g:`A <g1:A>` are not prime to one another, some number will measure them.

.. step:: assert

   Let :g:`C <g1:C>` measure them.

.. step:: assert

   Since :g:`C <g1:C>` measures :g:`B <g1:B>`, and :g:`A <g1:A>` does not measure :g:`B <g1:B>`,

.. step:: assert

   Therefore :g:`C <g1:C>` is not the same with :g:`A <g1:A>`.

.. step:: assert

   Since :g:`C <g1:C>` measures :g:`B <g1:B>`, :g:`A <g1:A>`,

.. step:: assert

   Therefore it also measures :g:`A <g1:A>` which is prime, though it is not the same with it : which is impossible.

.. step:: assert

   Therefore no number will measure :g:`B <g1:B>`, :g:`A <g1:A>`.

.. step:: conclude

   Therefore :g:`A <g1:A>`, :g:`B <g1:B>` are prime to one another.

Required for
------------

:ref:`G.231 <G.231>`, :ref:`G.283 <G.283>`, :ref:`G.284 <G.284>`, :ref:`G.285 <G.285>`, :ref:`G.306 <G.306>`, :ref:`G.312 <G.312>`

.. toctree::
   :hidden:

   code
   heath
