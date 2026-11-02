:order: 365
:number: 365
:canonical_id: G.365
:original_id: VII.def.9
:title: G.365 even-times odd number
:volume: II
:book: VII
:type: def
:categories: definition, number-theory
:category: definition, number-theory
:tags: book-vii, even-times-odd-number, part-aliquot, even-number, odd-number, number
:dependencies: G.169, G.302, G.352
:excerpt: Aneven-times odd number is that which ismeasured by aneven number according to anodd number.

.. _G.365:
.. _VII.def.9:

G.365 even-times odd number
===========================

.. rubric:: `VII.def.9 <https://geometor.github.io/euclid/heath/volume_II/book_vii/definitions/#vii-def-9>`_

.. enunciation::

   An:term:`**even-times odd number** <even-times-odd-number>` is that which is:term:`measured <G.253>` by an:term:`even number <G.302>` according to an:term:`odd number <G.352>`.

.. signature:: def

   | :fn:`even_times_odd_def <G.365>`

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
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.365" [label="G.365", tooltip="G.365 (VII.def.9): Aneven-times odd number is that which ismeasured by aneven number according to anodd number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.365" -> "G.169";
     "G.352" -> "G.247";
     "G.352" -> "G.302";
     "G.365" -> "G.302";
     "G.365" -> "G.352";
   }

Required for
------------

:ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`

.. toctree::
   :hidden:

   heath
