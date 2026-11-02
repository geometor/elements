:order: 320
:number: 320
:canonical_id: G.320
:original_id: VII.def.17
:title: G.320 square and cube numbers
:volume: II
:book: VII
:type: def
:categories: definition, number-theory
:category: definition, number-theory
:tags: book-vii, number, multiply, solid-number, side-of-number
:dependencies: G.248, G.269
:excerpt: And, when threenumbers havingmultiplied one another make some number, the number so produced issolid, and itssides are the numbers which have multiplied one another.

.. _G.320:
.. _VII.def.17:

G.320 square and cube numbers
=============================

.. rubric:: `VII.def.17 <https://geometor.github.io/euclid/heath/volume_II/book_vii/definitions/#vii-def-17>`_

.. enunciation::

   And, when three:term:`numbers <G.248>` having:term:`multiplied <G.269>` one another make some number, the number so produced is:term:`**solid** <solid-number>`, and its:term:`**sides** <side-of-number>` are the numbers which have multiplied one another.

.. signature:: def

   | :fn:`numbers_multiplied_make_def_vii_def_17 <G.320>`

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
     "G.320" [label="G.320", tooltip="G.320 (VII.def.17): And, when threenumbers havingmultiplied one another make some number, the number so produced issolid, and itssides are the numbers which have multiplied one another.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.248" -> "G.247";
     "G.269" -> "G.247";
     "G.269" -> "G.248";
     "G.320" -> "G.248";
     "G.320" -> "G.269";
   }

Required for
------------

:ref:`G.321 <G.321>`, :ref:`G.327 <G.327>`, :ref:`G.329 <G.329>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.339 <G.339>`

.. toctree::
   :hidden:

   heath
