:canonical_id: G.354
:original_id: IX.23
:title: G.354 many odd numbers
:volume: II
:book: IX
:type: prop

G.354 many odd numbers — Heath
==============================

.. rubric:: `IX.23 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/23/>`_

.. enunciation::

   If as many :term:`odd numbers <G.352>` as we please be added together, and their multitude be odd, the whole will also be odd.

For let as many odd numbers as we please, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, the multitude of which is odd, be added together ;

I say that the whole :g:`/ A D / <g1:/ A D />` is also odd.

.. picture:: g1.svg
   :alt: Book IX, Proposition 23

Let the :term:`unit <G.247>` :g:`/ D E / <g1:/ D E />` be subtracted from :g:`/ C D / <g1:/ C D />` ;

.. assertion:: [G.352] <G.352>

   therefore the remainder :g:`/ C E / <g1:/ C E />` is :term:`even <G.302>`.

.. subclause:: [G.353] <G.353>

   But :g:`/ A C / <g1:/ A C />` is also even ;

.. assertion:: [G.351] <G.351>

   therefore the whole :g:`/ A E / <g1:/ A E />` is also even.

.. subclause::

   And :g:`/ D E / <g1:/ D E />` is an unit.

.. assertion:: [G.352] <G.352>

   Therefore :g:`/ A D / <g1:/ A D />` is odd.

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
     "G.351" [label="G.351", tooltip="G.351 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.351/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.353" [label="G.353", tooltip="G.353 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", fillcolor="#222244", URL="../G.353/index.html", target="_top"];
     "G.354" [label="G.354", tooltip="G.354 (IX.23): If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.248" -> "G.247";
     "G.352" -> "G.247";
     "G.353" -> "G.247";
     "G.354" -> "G.247";
     "G.351" -> "G.248";
     "G.353" -> "G.248";
     "G.351" -> "G.302";
     "G.352" -> "G.302";
     "G.353" -> "G.302";
     "G.353" -> "G.351";
     "G.354" -> "G.351";
     "G.353" -> "G.352";
     "G.354" -> "G.352";
     "G.354" -> "G.353";
   }

Required for
------------

:ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`
