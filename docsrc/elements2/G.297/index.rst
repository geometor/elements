:order: 297
:number: 297
:canonical_id: G.297
:original_id: IX.24
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, segment, number, even-number
:dependencies: G.292
:excerpt: If from an even number an even number be subtracted, the remainder is even.

.. _G.297:
.. _IX.24:

G.297
=====

.. rubric:: `IX.24 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/24/>`_

.. enunciation::

   If from an even number an even number be subtracted, the remainder is even.

.. picture:: g1.svg
   :alt: Book IX, Proposition 24

.. step:: assert

   For from the even number :g:`/ A B / <g1:/ A B />` let the even number :g:`/ B C / <g1:/ B C />` be subtracted :

.. step:: assert [G.292] <G.292>

   Since :g:`/ A B / <g1:/ A B />` is even, it has a half part.

.. step:: assert

   For the same reason :g:`/ B C / <g1:/ B C />` also has a half part ;

.. step:: conclude

   So that the remainder [:g:`/ A C / <g1:/ A C />` also has a half part, and] :g:`/ A C / <g1:/ A C />` is therefore even.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.292" [label="G.292", tooltip="G.292 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.292/index.html", target="_top"];
     "G.297" [label="G.297", tooltip="G.297 (IX.24): If from an even number an even number be subtracted, the remainder is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.297" -> "G.292";
   }

Required for
------------

:ref:`G.298 <G.298>`, :ref:`G.299 <G.299>`, :ref:`G.300 <G.300>`

.. toctree::
   :hidden:

   code
   heath
