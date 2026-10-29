:order: 295
:number: 295
:canonical_id: G.295
:original_id: IX.22
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, segment, number, even-number, odd-number
:dependencies: G.293, G.294
:excerpt: If as many odd numbers as we please be added together, and their multitude be even, the whole is even.

.. _G.295:
.. _IX.22:

G.295
=====

.. rubric:: `IX.22 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/22/>`_

.. enunciation::

   If as many odd numbers as we please be added together, and their multitude be even, the whole is even.

.. picture:: g1.svg
   :alt: Book IX, Proposition 22

.. step:: assert

   For let as many odd numbers as we please, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, even in multitude, be added together

.. step:: assert [G.294] <G.294>

   Since each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />` is odd, if an unit be subtracted from each, each of the remainders will be even .

.. step:: assert [G.293] <G.293>

   So that the sum of them will be even.

.. step:: assert

   The multitude of the units is also even.

.. step:: conclude [G.293] <G.293>

   Therefore the whole :g:`/ A E / <g1:/ A E />` is also even.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.292" [label="G.292", tooltip="G.292 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.292/index.html", target="_top"];
     "G.293" [label="G.293", tooltip="G.293 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.293/index.html", target="_top"];
     "G.294" [label="G.294", tooltip="G.294 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by an unit from an even number.", fillcolor="#224422", URL="../G.294/index.html", target="_top"];
     "G.295" [label="G.295", tooltip="G.295 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.293" -> "G.292";
     "G.295" -> "G.293";
     "G.295" -> "G.294";
   }

Required for
------------

:ref:`G.296 <G.296>`, :ref:`G.302 <G.302>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`

.. toctree::
   :hidden:

   code
   heath
