:canonical_id: G.360
:original_id: IX.29
:title: G.360 odd number multiplying
:volume: II
:book: IX
:type: prop

G.360 odd number multiplying — Heath
====================================

.. rubric:: `IX.29 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/29/>`_

.. enunciation::

   If an :term:`odd number <G.352>` by :term:`multiplying <G.269>` an odd number make some :term:`number <G.248>`, the product will be odd.

For let the odd number :g:`A <g1:A>` by multiplying the odd number :g:`B <g1:B>` make :g:`C <g1:C>` ;

I say that :g:`C <g1:C>` is odd.

.. picture:: g1.svg
   :alt: Book IX, Proposition 29

.. subclause::

   For, since :g:`A <g1:A>` by multiplying :g:`B <g1:B>` has made :g:`C <g1:C>`,

.. assertion::

   therefore :g:`C <g1:C>` is made up of as many numbers equal to :g:`B <g1:B>` as there are :term:`units <G.247>` in :g:`A <g1:A>`. :just:`[G.269] <G.269>`

.. subclause::

   And each of the numbers :g:`A <g1:A>`, :g:`B <g1:B>` is odd;

.. assertion::

   therefore :g:`C <g1:C>` is made up of odd numbers the multitude of which is odd.

.. assertion:: [G.354] <G.354>

   Thus :g:`C <g1:C>` is odd.

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
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.351" [label="G.351", tooltip="G.351 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.351/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.353" [label="G.353", tooltip="G.353 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", fillcolor="#222244", URL="../G.353/index.html", target="_top"];
     "G.354" [label="G.354", tooltip="G.354 (IX.23): If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.", fillcolor="#222244", URL="../G.354/index.html", target="_top"];
     "G.360" [label="G.360", tooltip="G.360 (IX.29): If an odd number by multiplying an odd number make some number, the product is odd.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.248" -> "G.247";
     "G.269" -> "G.247";
     "G.352" -> "G.247";
     "G.269" -> "G.248";
     "G.351" -> "G.248";
     "G.360" -> "G.248";
     "G.360" -> "G.269";
     "G.351" -> "G.302";
     "G.352" -> "G.302";
     "G.353" -> "G.302";
     "G.353" -> "G.351";
     "G.354" -> "G.351";
     "G.353" -> "G.352";
     "G.354" -> "G.352";
     "G.360" -> "G.352";
     "G.354" -> "G.353";
     "G.360" -> "G.354";
   }
