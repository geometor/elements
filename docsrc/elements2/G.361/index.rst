:order: 361
:number: 361
:canonical_id: G.361
:original_id: IX.30
:title: G.361 odd number measure
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, odd-number, part-aliquot, even-number, multiply, number, reductio-ad-absurdum
:dependencies: G.169, G.269, G.302, G.352, G.354
:excerpt: If an odd number measure an even number, it will also measure the half of it.

.. _G.361:
.. _IX.30:

G.361 odd number measure
========================

.. rubric:: `IX.30 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/30/>`_

.. enunciation::

   If an :term:`odd number <G.352>` :term:`measure <G.169>` an :term:`even number <G.302>`, it will also measure the half of it.

.. signature:: theorem

   | :fn:`odd_number_measure <G.361>`\ ()
   | **prove** it will also measure the half of it; :g:`C <g1:C>` is not odd

.. picture:: g1.svg
   :alt: Book IX, Proposition 30

.. step:: assert

   Let the odd number :g:`A <g1:A>` measure the even number :g:`B <g1:B>`

.. step:: assert

   :g:`A <g1:A>` measures :g:`B <g1:B>`, let it measure it according to :g:`C <g1:C>`

.. step:: assert

   If possible, let it be so

.. step:: assert

   :g:`A <g1:A>` measures :g:`B <g1:B>` according to :g:`C <g1:C>`,

.. step:: assert

   :g:`A <g1:A>` by multiplying :g:`C <g1:C>` has made :g:`B <g1:B>`

.. step:: assert

   :g:`B <g1:B>` is made up of odd numbers the multitude of which is odd

.. step:: assert ∵ many_odd_numbers_ix_23 <G.354>

   :g:`B <g1:B>` is odd ⇒⇐, for by hypothesis it is even

.. step:: assert

   :g:`C <g1:C>` is not odd; therefore :g:`C <g1:C>` is even

.. step:: assert

   :g:`A <g1:A>` measures :g:`B <g1:B>` an even number of times

.. step:: conclude

   For this reason then it also measures the half of it

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.351" [label="G.351", tooltip="G.351 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.351/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.353" [label="G.353", tooltip="G.353 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", fillcolor="#222244", URL="../G.353/index.html", target="_top"];
     "G.354" [label="G.354", tooltip="G.354 (IX.23): If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.", fillcolor="#222244", URL="../G.354/index.html", target="_top"];
     "G.361" [label="G.361", tooltip="G.361 (IX.30): If an odd number measure an even number, it will also measure the half of it.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.361" -> "G.169";
     "G.248" -> "G.247";
     "G.269" -> "G.247";
     "G.352" -> "G.247";
     "G.353" -> "G.247";
     "G.354" -> "G.247";
     "G.269" -> "G.248";
     "G.351" -> "G.248";
     "G.353" -> "G.248";
     "G.361" -> "G.269";
     "G.351" -> "G.302";
     "G.352" -> "G.302";
     "G.353" -> "G.302";
     "G.361" -> "G.302";
     "G.353" -> "G.351";
     "G.354" -> "G.351";
     "G.353" -> "G.352";
     "G.354" -> "G.352";
     "G.361" -> "G.352";
     "G.354" -> "G.353";
     "G.361" -> "G.354";
   }

Required for
------------

:ref:`G.362 <G.362>`

.. toctree::
   :hidden:

   code
   heath
