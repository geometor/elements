:order: 353
:number: 353
:canonical_id: G.353
:original_id: IX.22
:title: G.353 many odd numbers
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, segment, odd-number, even-number, number, unit
:dependencies: G.247, G.248, G.302, G.351, G.352
:excerpt: If as many odd numbers as we please be added together, and their multitude be even, the whole is even.

.. _G.353:
.. _IX.22:

G.353 many odd numbers
======================

.. rubric:: `IX.22 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/22/>`_

.. enunciation::

   If as many :term:`odd numbers <G.352>` as we please be added together, and their multitude be :term:`even <G.302>`, the whole is even.

.. signature:: theorem

   | :fn:`many_odd_numbers <G.353>`\ ()
   | **prove** :g:`/ A E / <g1:/ A E />` is even

.. picture:: g1.svg
   :alt: Book IX, Proposition 22

.. step:: construct

   Let as many odd numbers as we please, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, even in multitude, be added together

.. step:: assert ∵ odd_number_divisible_def <G.352>

   each of the :term:`numbers <G.248>` :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />` is odd, if an :term:`unit <G.247>` be subtracted from each, each of the remainders will be even

.. step:: assert ∵ many_even_numbers <G.351>

   So that the sum of them will be even

.. step:: assert

   The multitude of the units is also even

.. step:: conclude ∵ many_even_numbers <G.351>

   :g:`/ A E / <g1:/ A E />` is also even

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.351" [label="G.351", tooltip="G.351 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.351/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.353" [label="G.353", tooltip="G.353 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.248" -> "G.247";
     "G.352" -> "G.247";
     "G.353" -> "G.247";
     "G.351" -> "G.248";
     "G.353" -> "G.248";
     "G.351" -> "G.302";
     "G.352" -> "G.302";
     "G.353" -> "G.302";
     "G.353" -> "G.351";
     "G.353" -> "G.352";
   }

Required for
------------

:ref:`G.354 <G.354>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`

.. toctree::
   :hidden:

   code
   heath
