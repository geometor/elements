:order: 301
:number: 301
:canonical_id: G.301
:original_id: IX.28
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, number, even-number, odd-number
:dependencies: G.222, G.293
:excerpt: If an odd number by multiplying an even number make some number, the product is even.

.. _G.301:
.. _IX.28:

G.301
=====

.. rubric:: `IX.28 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/28/>`_

.. enunciation::

   If an odd number by multiplying an even number make some number, the product is even.

.. picture:: g1.svg
   :alt: Book IX, Proposition 28

.. step:: assert

   For let the odd number :g:`A <g1:A>` by multiplying the even number :g:`B <g1:B>` make :g:`C <g1:C>`

.. step:: assert

   Since :g:`A <g1:A>` by multiplying :g:`B <g1:B>` has made :g:`C <g1:C>`,

.. step:: assert [G.222] <G.222>

   Therefore :g:`C <g1:C>` is made up of as many numbers equal to :g:`B <g1:B>` as there are units in :g:`A <g1:A>`.

.. step:: assert

   :g:`B <g1:B>` is even ;

.. step:: assert

   Therefore :g:`C <g1:C>` is made up of even numbers.

.. step:: assert [G.293] <G.293>

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
     "G.222" [label="G.222", tooltip="G.222 (VII.def.15): A number is said tomultiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.222/index.html", target="_top"];
     "G.292" [label="G.292", tooltip="G.292 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.292/index.html", target="_top"];
     "G.293" [label="G.293", tooltip="G.293 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.293/index.html", target="_top"];
     "G.301" [label="G.301", tooltip="G.301 (IX.28): If an odd number by multiplying an even number make some number, the product is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.301" -> "G.222";
     "G.293" -> "G.292";
     "G.301" -> "G.293";
   }

.. toctree::
   :hidden:

   code
   heath
