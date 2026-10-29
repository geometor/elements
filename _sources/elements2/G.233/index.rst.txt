:order: 233
:number: 233
:canonical_id: G.233
:original_id: VII.32
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number, prime
:dependencies: G.232
:excerpt: Any number either is prime or is measured by some prime number.

.. _G.233:
.. _VII.32:

G.233
=====

.. rubric:: `VII.32 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/32/>`_

.. enunciation::

   Any number either is prime or is measured by some prime number.

.. picture:: g1.svg
   :alt: Proposition 32 diagram

.. step:: given

   :g:`A <g1:A>` be a number

.. step:: assert

   If now :g:`A <g1:A>` is prime, that which was enjoined will have been done.

.. step:: assert [G.232] <G.232>

   If it is composite, some prime number will measure it.

.. step:: conclude

   Therefore any number either is prime or is measured by some prime number.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.232" [label="G.232", tooltip="G.232 (VII.31): Any composite number is measured by some prime number.", fillcolor="#222244", URL="../G.232/index.html", target="_top"];
     "G.233" [label="G.233", tooltip="G.233 (VII.32): Any number either is prime or is measured by some prime number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.233" -> "G.232";
   }

.. toctree::
   :hidden:

   code
   heath
