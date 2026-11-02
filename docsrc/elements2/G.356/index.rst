:order: 356
:number: 356
:canonical_id: G.356
:original_id: IX.25
:title: G.356 even number odd
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, segment, even-number, odd-number, unit, number
:dependencies: G.302, G.352, G.355
:excerpt: If from an even number an odd number be subtracted, the remainder is odd.

.. _G.356:
.. _IX.25:

G.356 even number odd
=====================

.. rubric:: `IX.25 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/25/>`_

.. enunciation::

   If from an :term:`even number <G.302>` an :term:`odd number <G.352>` be subtracted, the remainder is odd.

.. signature:: theorem

   | :fn:`even_number_odd <G.356>`\ ()
   | **prove** the remainder :g:`/ A C / <g1:/ A C />` is odd

.. picture:: g1.svg
   :alt: Book IX, Proposition 25

.. step:: construct

   From the even number :g:`/ A B / <g1:/ A B />` let the odd number :g:`/ B C / <g1:/ B C />` be subtracted

.. step:: construct

   Let the :term:`unit <G.247>` :g:`/ C D / <g1:/ C D />` be subtracted from :g:`/ B C / <g1:/ B C />`

.. step:: assert ∵ odd_number_divisible_def <G.352>

   Therefore :g:`/ B D / <g1:/ B D />` is even.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is also even ;

.. step:: assert ∵ even_number_even <G.355>

   Therefore the remainder :g:`/ A D / <g1:/ A D />` is also even.

.. step:: assert

   :g:`/ C D / <g1:/ C D />` is an unit ;

.. step:: conclude ∵ odd_number_divisible_def <G.352>

   Therefore :g:`/ A C / <g1:/ A C />` is odd.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.355" [label="G.355", tooltip="G.355 (IX.24): If from an even number an even number be subtracted, the remainder is even.", fillcolor="#222244", URL="../G.355/index.html", target="_top"];
     "G.356" [label="G.356", tooltip="G.356 (IX.25): If from an even number an odd number be subtracted, the remainder is odd.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.352" -> "G.247";
     "G.352" -> "G.302";
     "G.355" -> "G.302";
     "G.356" -> "G.302";
     "G.356" -> "G.352";
     "G.356" -> "G.355";
   }

.. toctree::
   :hidden:

   code
   heath
