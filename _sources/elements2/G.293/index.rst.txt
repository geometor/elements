:order: 293
:number: 293
:canonical_id: G.293
:original_id: IX.21
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, segment, number, even-number
:dependencies: G.292
:excerpt: If as many even numbers as we please be added together, the whole is even.

.. _G.293:
.. _IX.21:

G.293
=====

.. rubric:: `IX.21 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/21/>`_

.. enunciation::

   If as many even numbers as we please be added together, the whole is even.

.. picture:: g1.svg
   :alt: Book IX, Proposition 21

.. step:: assert

   For let as many even numbers as we please, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, be added together

.. step:: assert [G.292] <G.292>

   Since each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />` is even, it has a half part .

.. step:: assert

   So that the whole :g:`/ A E / <g1:/ A E />` also has a half part.

.. step:: assert [G.292] <G.292>

   An even number is that which is divisible into two equal parts .

.. step:: conclude

   Therefore :g:`/ A E / <g1:/ A E />` is even.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.292" [label="G.292", tooltip="G.292 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.292/index.html", target="_top"];
     "G.293" [label="G.293", tooltip="G.293 (IX.21): If as many even numbers as we please be added together, the whole is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.293" -> "G.292";
   }

Required for
------------

:ref:`G.295 <G.295>`, :ref:`G.296 <G.296>`, :ref:`G.301 <G.301>`, :ref:`G.302 <G.302>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`

.. toctree::
   :hidden:

   code
   heath
