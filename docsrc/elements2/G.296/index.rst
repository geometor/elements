:order: 296
:number: 296
:canonical_id: G.296
:original_id: IX.23
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, segment, number, odd-number
:dependencies: G.293, G.294, G.295
:excerpt: If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.

.. _G.296:
.. _IX.23:

G.296
=====

.. rubric:: `IX.23 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/23/>`_

.. enunciation::

   If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.

.. signature:: theorem

   | :fn:`many_odd_numbers_ix_23 <G.296>`\ ()
   | **prove** the whole :g:`/ A D / <g1:/ A D />` is also odd

.. picture:: g1.svg
   :alt: Book IX, Proposition 23

.. step:: construct

   Let as many odd numbers as we please, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, the multitude of which is odd, be added together

.. step:: construct

   Let the unit :g:`/ D E / <g1:/ D E />` be subtracted from :g:`/ C D / <g1:/ C D />`

.. step:: assert ∵ odd_number_divisible_def <G.294>

   Therefore the remainder :g:`/ C E / <g1:/ C E />` is even.

.. step:: assert ∵ many_odd_numbers <G.295>

   :g:`/ A C / <g1:/ A C />` is also even ;

.. step:: assert ∵ many_even_numbers <G.293>

   Therefore the whole :g:`/ A E / <g1:/ A E />` is also even.

.. step:: assert

   :g:`/ D E / <g1:/ D E />` is an unit.

.. step:: conclude ∵ odd_number_divisible_def <G.294>

   Therefore :g:`/ A D / <g1:/ A D />` is odd.

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
     "G.295" [label="G.295", tooltip="G.295 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", fillcolor="#222244", URL="../G.295/index.html", target="_top"];
     "G.296" [label="G.296", tooltip="G.296 (IX.23): If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.293" -> "G.292";
     "G.295" -> "G.293";
     "G.296" -> "G.293";
     "G.295" -> "G.294";
     "G.296" -> "G.294";
     "G.296" -> "G.295";
   }

Required for
------------

:ref:`G.302 <G.302>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`

.. toctree::
   :hidden:

   code
   heath
