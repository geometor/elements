:order: 259
:number: 259
:canonical_id: G.259
:original_id: VII.7
:title: G.259 number part number
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, segment, number, part-aliquot, equality
:dependencies: G.248, G.253, G.257
:excerpt: If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.

.. _G.259:
.. _VII.7:

G.259 number part number
========================

.. rubric:: `VII.7 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/07/>`_

.. enunciation::

   If a :term:`number <G.248>` be that :term:`part of <G.253>` a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.

.. signature:: theorem

   | :fn:`number_part_number_vii_7 <G.259>`\ ()
   | **prove** the remainder :g:`/ E B / <g1:/ E B />` is also the same part of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ A B / <g1:/ A B />` is of the whole :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Book VII, Proposition 7

.. step:: assert

   Let the number :g:`/ A B / <g1:/ A B />` be that part of the number :g:`/ C D / <g1:/ C D />` which :g:`/ A E / <g1:/ A E />` subtracted is of :g:`/ C F / <g1:/ C F />` subtracted

.. step:: assert

   Whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also let :g:`/ E B / <g1:/ E B />` be of :g:`/ G C / <g1:/ G C />`.

.. step:: assert

   Now since, whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also is :g:`/ E B / <g1:/ E B />` of :g:`/ G C / <g1:/ G C />`,

.. step:: assert ∵ number_part_number <G.257>

   Therefore, whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also is :g:`/ A B / <g1:/ A B />` of :g:`/ G F / <g1:/ G F />`.

.. step:: assert

   But, whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also, by hypothesis, is :g:`/ A B / <g1:/ A B />` of :g:`/ C D / <g1:/ C D />`;

.. step:: assert

   Therefore, whatever part :g:`/ A B / <g1:/ A B />` is of :g:`/ G F / <g1:/ G F />`, the same part is it of :g:`/ C D / <g1:/ C D />` also;

.. step:: assert

   Therefore :g:`/ G F / <g1:/ G F />` is :eq:`equal <g1:/ G F / = g1:/ C D />` to :g:`/ C D / <g1:/ C D />`.

.. step:: construct

   Let :g:`/ C F / <g1:/ C F />` be subtracted from each

.. step:: assert

   Therefore the remainder :g:`/ G C / <g1:/ G C />` is :eq:`equal <g1:/ G C / = g1:/ F D />` to the remainder :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   Now since, whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also is :g:`/ E B / <g1:/ E B />` of :g:`/ G C / <g1:/ G C />`, while :g:`/ G C / <g1:/ G C />` is :eq:`equal <g1:/ G C / = g1:/ F D />` to :g:`/ F D / <g1:/ F D />`,

.. step:: assert

   Therefore, whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also is :g:`/ E B / <g1:/ E B />` of :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   But, whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also is :g:`/ A B / <g1:/ A B />` of :g:`/ C D / <g1:/ C D />`;

.. step:: conclude

   Therefore also the remainder :g:`/ E B / <g1:/ E B />` is the same part of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ A B / <g1:/ A B />` is of the whole :g:`/ C D / <g1:/ C D />`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.259" [label="G.259", tooltip="G.259 (VII.7): If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.256" -> "G.169";
     "G.257" -> "G.170";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.259" -> "G.248";
     "G.257" -> "G.253";
     "G.259" -> "G.253";
     "G.257" -> "G.256";
     "G.259" -> "G.257";
   }

Required for
------------

:ref:`G.260 <G.260>`, :ref:`G.264 <G.264>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`

.. toctree::
   :hidden:

   code
   heath
