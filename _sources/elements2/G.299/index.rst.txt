:order: 299
:number: 299
:canonical_id: G.299
:original_id: IX.26
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, segment, number, even-number, odd-number
:dependencies: G.294, G.297
:excerpt: If from an odd number an odd number be subtracted, the remainder is even.

.. _G.299:
.. _IX.26:

G.299
=====

.. rubric:: `IX.26 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/26/>`_

.. enunciation::

   If from an odd number an odd number be subtracted, the remainder is even.

.. signature:: theorem

   | :fn:`odd_number_odd <G.299>`\ ()
   | **prove** the remainder :g:`/ A C / <g1:/ A C />` is even

.. picture:: g1.svg
   :alt: Book IX, Proposition 26

.. step:: construct

   From the odd number :g:`/ A B / <g1:/ A B />` let the odd number :g:`/ B C / <g1:/ B C />` be subtracted

.. step:: construct

   Since :g:`/ A B / <g1:/ A B />` is odd, let the unit :g:`/ B D / <g1:/ B D />` be subtracted ;

.. step:: assert ∵ odd_number_divisible_def <G.294>

   Therefore the remainder :g:`/ A D / <g1:/ A D />` is even.

.. step:: assert ∵ odd_number_divisible_def <G.294>

   For the same reason :g:`/ C D / <g1:/ C D />` is also even ;

.. step:: conclude ∵ even_number_even <G.297>

   So that the remainder :g:`/ A C / <g1:/ A C />` is also even.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.292" [label="G.292", tooltip="G.292 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.292/index.html", target="_top"];
     "G.294" [label="G.294", tooltip="G.294 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by an unit from an even number.", fillcolor="#224422", URL="../G.294/index.html", target="_top"];
     "G.297" [label="G.297", tooltip="G.297 (IX.24): If from an even number an even number be subtracted, the remainder is even.", fillcolor="#222244", URL="../G.297/index.html", target="_top"];
     "G.299" [label="G.299", tooltip="G.299 (IX.26): If from an odd number an odd number be subtracted, the remainder is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.297" -> "G.292";
     "G.299" -> "G.294";
     "G.299" -> "G.297";
   }

.. toctree::
   :hidden:

   code
   heath
