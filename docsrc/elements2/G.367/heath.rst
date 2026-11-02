:canonical_id: G.367
:original_id: IX.34
:title: G.367 number continually doubled
:volume: II
:book: IX
:type: prop

G.367 number continually doubled — Heath
========================================

.. rubric:: `IX.34 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/34/>`_

.. enunciation::

   If a :term:`number <G.248>` neither be one of those which are continually doubled from a dyad, nor have its half :term:`odd <G.352>`, it is both :term:`even-times even <G.363>` and :term:`even-times odd <G.365>`.

For let the number :g:`A <g1:A>` neither be one of those doubled from a dyad, nor have its half odd;

I say that :g:`A <g1:A>` is both even-times even and even-times odd.

.. picture:: g1.svg
   :alt: Proposition 34 Diagram

.. assertion::

   Now that :g:`A <g1:A>` is even-times even is manifest; for it has not its half odd. :just:`[G.363] <G.363>`

I say next that it is also even-times odd.

.. subclause::

   For, if we bisect :g:`A <g1:A>`, then bisect its half, and do this continually, we shall come upon some odd number which will :term:`measure <G.253>` :g:`A <g1:A>` according to an :term:`even number <G.302>`.

.. subclause::

   For, if not, we shall come upon a dyad, and :g:`A <g1:A>` will be among those which are doubled from a dyad: which is contrary to the hypothesis.

.. assertion::

   Thus :g:`A <g1:A>` is even-times odd.

.. subclause::

   But it was also proved even-times even.

.. assertion::

   Therefore :g:`A <g1:A>` is both even-times even and even-times odd.

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
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.363" [label="G.363", tooltip="G.363 (VII.def.8): Aneven-times even number is that which ismeasured by aneven number according to an even number.", fillcolor="#224422", URL="../G.363/index.html", target="_top"];
     "G.365" [label="G.365", tooltip="G.365 (VII.def.9): Aneven-times odd number is that which ismeasured by aneven number according to anodd number.", fillcolor="#224422", URL="../G.365/index.html", target="_top"];
     "G.367" [label="G.367", tooltip="G.367 (IX.34): If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.363" -> "G.169";
     "G.365" -> "G.169";
     "G.248" -> "G.247";
     "G.352" -> "G.247";
     "G.367" -> "G.248";
     "G.352" -> "G.302";
     "G.363" -> "G.302";
     "G.365" -> "G.302";
     "G.365" -> "G.352";
     "G.367" -> "G.352";
     "G.367" -> "G.363";
     "G.367" -> "G.365";
   }
