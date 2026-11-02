:order: 336
:number: 336
:canonical_id: G.336
:original_id: IX.7
:title: G.336 composite number multiplying
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, composite-number, multiply, number, part-aliquot, unit, composite
:dependencies: G.248, G.269, G.286
:excerpt: If a composite number by multiplying any number make some number, the product is solid.

.. _G.336:
.. _IX.7:

G.336 composite number multiplying
==================================

.. rubric:: `IX.7 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/07/>`_

.. enunciation::

   If a :term:`composite number <G.286>` by :term:`multiplying <G.269>` any :term:`number <G.248>` make some number, the product is solid.

.. signature:: theorem

   | :fn:`composite_number_multiplying <G.336>`\ ()
   | **prove** :g:`C <g1:C>` is solid

.. picture:: g1.svg
   :alt: Proposition 7 Diagram

.. step:: assert

   Let the composite number :g:`A <g1:A>` by multiplying any number :g:`B <g1:B>` make :g:`C <g1:C>`

.. step:: assert

   Since :g:`A <g1:A>` is composite,

.. step:: assert ∵ composite_number_measured_def <G.286>

   It will be :term:`measured <G.169>` by some number.

.. step:: construct

   Let it be measured by :g:`D <g1:D>`

.. step:: assert

   And, as many times as :g:`D <g1:D>` measures :g:`A <g1:A>`, so many :term:`units <G.247>` let there be in :g:`E <g1:E>`.

.. step:: assert

   Since then :g:`D <g1:D>` measures :g:`A <g1:A>` according to the units in :g:`E <g1:E>`,

.. step:: assert ∵ number_said_multiply_def <G.269>

   Therefore :g:`E <g1:E>` by multiplying :g:`D <g1:D>` has made :g:`A <g1:A>`.

.. step:: assert

   And, since :g:`A <g1:A>` by multiplying :g:`B <g1:B>` has made :g:`C <g1:C>`, and :g:`A <g1:A>` is the product of :g:`D <g1:D>`, :g:`E <g1:E>`,

.. step:: assert

   Therefore the product of :g:`D <g1:D>`, :g:`E <g1:E>` by multiplying :g:`B <g1:B>` has made :g:`C <g1:C>`.

.. step:: conclude

   Therefore :g:`C <g1:C>` is solid, and :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`B <g1:B>` are its sides.

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
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.286" [label="G.286", tooltip="G.286 (VII.def.13): Acomposite number is that which ismeasured by somenumber.", fillcolor="#224422", URL="../G.286/index.html", target="_top"];
     "G.336" [label="G.336", tooltip="G.336 (IX.7): If a composite number by multiplying any number make some number, the product is solid.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.286" -> "G.169";
     "G.248" -> "G.247";
     "G.269" -> "G.247";
     "G.269" -> "G.248";
     "G.286" -> "G.248";
     "G.336" -> "G.248";
     "G.336" -> "G.269";
     "G.336" -> "G.286";
   }

.. toctree::
   :hidden:

   code
   heath
