:order: 341
:number: 341
:canonical_id: G.341
:original_id: VII.def.14
:title: G.341 numbers composite to one another
:volume: II
:book: VII
:type: def
:categories: definition, number-theory
:category: definition, number-theory
:tags: book-vii, composite-to-one-another, part-aliquot, number, composite
:dependencies: G.169, G.248, G.253
:excerpt: Numbers composite to one another are those which aremeasured by somenumber as a common measure.

.. _G.341:
.. _VII.def.14:

G.341 numbers composite to one another
======================================

.. rubric:: `VII.def.14 <https://geometor.github.io/euclid/heath/volume_II/book_vii/definitions/#vii-def-14>`_

.. enunciation::

   :term:`**Numbers composite to one another** <composite-to-one-another>` are those which are:term:`measured <G.253>` by some:term:`number <G.248>` as a common measure.

.. signature:: def

   | :fn:`numbers_composite_measured_def <G.341>`

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
     "G.341" [label="G.341", tooltip="G.341 (VII.def.14): Numbers composite to one another are those which aremeasured by somenumber as a common measure.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.253" -> "G.169";
     "G.341" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.341" -> "G.248";
     "G.341" -> "G.253";
   }

Required for
------------

:ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`

.. toctree::
   :hidden:

   heath
