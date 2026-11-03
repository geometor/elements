:canonical_id: G.366
:original_id: IX.33
:title: G.366 number half odd
:volume: II
:book: IX
:type: prop

G.366 number half odd — Heath
=============================

.. rubric:: `IX.33 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/33/>`_

.. enunciation::

   If a :term:`number <G.248>` have its half :term:`odd <G.352>`, it is :term:`even-times odd <G.365>` only.

For let the number :g:`A <g1:A>` have its half odd;

I say that :g:`A <g1:A>` is even-times odd only.

.. picture:: g1.svg
   :alt: Proposition 33 Diagram

.. assertion::

   Now that it is even-times odd is manifest; for the half of it, being odd, :term:`measures <G.253>` it an :term:`even number <G.302>` of times. :just:`[G.365] <G.365>`

I say next that it is also even-times odd only.

.. subclause::

   For, if :g:`A <g1:A>` is :term:`even-times even <G.363>` also,

.. assertion::

   it will be measured by an even number according to an even number; :just:`[G.363] <G.363>`

.. assertion::

   so that the half of it will also be measured by an even number though it is odd: which is absurd.

.. assertion::

   Therefore :g:`A <g1:A>` is even-times odd only.

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
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.363" [label="G.363", tooltip="G.363 (VII.def.8): Aneven-times even number is that which ismeasured by aneven number according to an even number.", fillcolor="#224422", URL="../G.363/index.html", target="_top"];
     "G.365" [label="G.365", tooltip="G.365 (VII.def.9): Aneven-times odd number is that which ismeasured by aneven number according to anodd number.", fillcolor="#224422", URL="../G.365/index.html", target="_top"];
     "G.366" [label="G.366", tooltip="G.366 (IX.33): If a number have its half odd, it is even-times odd only.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.253" -> "G.169";
     "G.363" -> "G.169";
     "G.365" -> "G.169";
     "G.366" -> "G.169";
     "G.248" -> "G.247";
     "G.352" -> "G.247";
     "G.253" -> "G.248";
     "G.366" -> "G.248";
     "G.363" -> "G.253";
     "G.365" -> "G.253";
     "G.352" -> "G.302";
     "G.363" -> "G.302";
     "G.365" -> "G.302";
     "G.366" -> "G.302";
     "G.365" -> "G.352";
     "G.366" -> "G.352";
     "G.366" -> "G.363";
     "G.366" -> "G.365";
   }
