:canonical_id: G.357
:original_id: IX.26
:title: G.357 odd number odd
:volume: II
:book: IX
:type: prop

G.357 odd number odd — Heath
============================

.. rubric:: `IX.26 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/26/>`_

.. enunciation::

   If from an :term:`odd number <G.352>` an odd number be subtracted, the remainder will be :term:`even <G.302>`.

For from the odd number :g:`/ A B / <g1:/ A B />` let the odd number :g:`/ B C / <g1:/ B C />` be subtracted ;

I say that the remainder :g:`/ A C / <g1:/ A C />` is even.

.. picture:: g1.svg
   :alt: Book IX, Proposition 26

.. subclause::

   For, since :g:`/ A B / <g1:/ A B />` is odd, let the :term:`unit <G.247>` :g:`/ B D / <g1:/ B D />` be subtracted ;

.. assertion:: [G.352] <G.352>

   therefore the remainder :g:`/ A D / <g1:/ A D />` is even.

.. subclause:: [G.352] <G.352>

   For the same reason :g:`/ C D / <g1:/ C D />` is also even ;

.. assertion:: [G.355] <G.355>

   so that the remainder :g:`/ A C / <g1:/ A C />` is also even.

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
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.355" [label="G.355", tooltip="G.355 (IX.24): If from an even number an even number be subtracted, the remainder is even.", fillcolor="#222244", URL="../G.355/index.html", target="_top"];
     "G.357" [label="G.357", tooltip="G.357 (IX.26): If from an odd number an odd number be subtracted, the remainder is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.352" -> "G.247";
     "G.352" -> "G.302";
     "G.355" -> "G.302";
     "G.357" -> "G.302";
     "G.357" -> "G.352";
     "G.357" -> "G.355";
   }
