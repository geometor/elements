:order: 363
:number: 363
:canonical_id: G.363
:original_id: VII.def.8
:title: G.363 even-times even number
:volume: II
:book: VII
:type: def
:categories: definition, number-theory
:category: definition, number-theory
:tags: book-vii, even-times-even-number, part-aliquot, even-number, number
:dependencies: G.169, G.253, G.302
:excerpt: Aneven-times even number is that which ismeasured by aneven number according to an even number.

.. _G.363:
.. _VII.def.8:

G.363 even-times even number
============================

.. rubric:: `VII.def.8 <https://geometor.github.io/euclid/heath/volume_II/book_vii/definitions/#vii-def-8>`_

.. enunciation::

   An:term:`**even-times even number** <even-times-even-number>` is that which is:term:`measured <G.253>` by an:term:`even number <G.302>` according to an even number.

.. signature:: def

   | :fn:`even_times_even_def <G.363>`

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
     "G.363" [label="G.363", tooltip="G.363 (VII.def.8): Aneven-times even number is that which ismeasured by aneven number according to an even number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.253" -> "G.169";
     "G.363" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.363" -> "G.253";
     "G.363" -> "G.302";
   }

Required for
------------

:ref:`G.364 <G.364>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`

.. toctree::
   :hidden:

   heath
