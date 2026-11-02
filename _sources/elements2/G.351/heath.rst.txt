:canonical_id: G.351
:original_id: IX.21
:title: G.351 many even numbers
:volume: II
:book: IX
:type: prop

G.351 many even numbers — Heath
===============================

.. rubric:: `IX.21 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/21/>`_

.. enunciation::

   If as many :term:`even numbers <G.302>` as we please be added together, the whole is even.

For let as many even numbers as we please, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, be added together ;

I say that the whole :g:`/ A E / <g1:/ A E />` is even.

.. picture:: g1.svg
   :alt: Book IX, Proposition 21

.. subclause::

   For, since each of the :term:`numbers <G.248>` :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />` is even, it has a half part ; :just:`[G.302] <G.302>`

.. assertion::

   so that the whole :g:`/ A E / <g1:/ A E />` also has a half part.

.. subclause::

   But an even number is that which is divisible into two equal parts ; :just:`[G.302] <G.302>`

.. assertion::

   therefore :g:`/ A E / <g1:/ A E />` is even.

.. qed::

   :just:`Q. E. D.`

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
     "G.351" [label="G.351", tooltip="G.351 (IX.21): If as many even numbers as we please be added together, the whole is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.248" -> "G.247";
     "G.351" -> "G.248";
     "G.351" -> "G.302";
   }

Required for
------------

:ref:`G.353 <G.353>`, :ref:`G.354 <G.354>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`
