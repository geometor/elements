:order: 311
:number: 311
:canonical_id: G.311
:original_id: VII.def.19
:title: G.311 square number
:volume: II
:book: VII
:type: def
:categories: definition, number-theory
:category: definition, number-theory
:tags: book-vii, cube-number, multiply, number, cube
:dependencies: G.248, G.269
:excerpt: And acube is equalmultiplied by equal and again by equal, or anumber which is contained by three equal numbers.

.. _G.311:
.. _VII.def.19:

G.311 square number
===================

.. rubric:: `VII.def.19 <https://geometor.github.io/euclid/heath/volume_II/book_vii/definitions/#vii-def-19>`_

.. enunciation::

   And a:term:`**cube** <cube-number>` is equal:term:`multiplied <G.269>` by equal and again by equal, or a:term:`number <G.248>` which is contained by three equal numbers.

.. signature:: def

   | :fn:`cube_equal_multiplied_def <G.311>`

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
     "G.311" [label="G.311", tooltip="G.311 (VII.def.19): And acube is equalmultiplied by equal and again by equal, or anumber which is contained by three equal numbers.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.248" -> "G.247";
     "G.269" -> "G.247";
     "G.269" -> "G.248";
     "G.311" -> "G.248";
     "G.311" -> "G.269";
   }

Required for
------------

:ref:`G.312 <G.312>`, :ref:`G.315 <G.315>`, :ref:`G.317 <G.317>`, :ref:`G.327 <G.327>`, :ref:`G.329 <G.329>`, :ref:`G.332 <G.332>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`

.. toctree::
   :hidden:

   heath
