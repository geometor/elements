:order: 359
:number: 359
:canonical_id: G.359
:original_id: IX.28
:title: G.359 odd number multiplying
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, odd-number, multiply, even-number, number, unit
:dependencies: G.248, G.269, G.302, G.351, G.352
:excerpt: If an odd number by multiplying an even number make some number, the product is even.

.. _G.359:
.. _IX.28:

G.359 odd number multiplying
============================

.. rubric:: `IX.28 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/28/>`_

.. enunciation::

   If an :term:`odd number <G.352>` by :term:`multiplying <G.269>` an :term:`even number <G.302>` make some :term:`number <G.248>`, the product is even.

.. signature:: theorem

   | :fn:`odd_number_multiplying <G.359>`\ ()
   | **prove** :g:`C <g1:C>` is even

.. picture:: g1.svg
   :alt: Book IX, Proposition 28

.. step:: assert

   Let the odd number :g:`A <g1:A>` by multiplying the even number :g:`B <g1:B>` make :g:`C <g1:C>`

.. step:: assert

   Since :g:`A <g1:A>` by multiplying :g:`B <g1:B>` has made :g:`C <g1:C>`,

.. step:: assert ∵ number_said_multiply_def <G.269>

   Therefore :g:`C <g1:C>` is made up of as many numbers equal to :g:`B <g1:B>` as there are :term:`units <G.247>` in :g:`A <g1:A>`.

.. step:: assert

   :g:`B <g1:B>` is even ;

.. step:: assert

   Therefore :g:`C <g1:C>` is made up of even numbers.

.. step:: assert ∵ many_even_numbers <G.351>

   But, if as many even numbers as we please be added together, the whole is even.

.. step:: conclude

   Therefore :g:`C <g1:C>` is even.

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
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.351" [label="G.351", tooltip="G.351 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.351/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.359" [label="G.359", tooltip="G.359 (IX.28): If an odd number by multiplying an even number make some number, the product is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.248" -> "G.247";
     "G.269" -> "G.247";
     "G.352" -> "G.247";
     "G.269" -> "G.248";
     "G.351" -> "G.248";
     "G.359" -> "G.248";
     "G.359" -> "G.269";
     "G.351" -> "G.302";
     "G.352" -> "G.302";
     "G.359" -> "G.302";
     "G.359" -> "G.351";
     "G.359" -> "G.352";
   }

.. toctree::
   :hidden:

   code
   heath
