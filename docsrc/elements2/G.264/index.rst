:order: 264
:number: 264
:canonical_id: G.264
:original_id: VII.11
:title: G.264 whole whole number
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, segment, number, part-aliquot, parts-non-aliquot
:dependencies: G.248, G.259, G.260, G.263
:excerpt: If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder is to the remainder as whole to whole.

.. _G.264:
.. _VII.11:

G.264 whole whole number
========================

.. rubric:: `VII.11 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/11/>`_

.. enunciation::

   If, as whole is to whole, so is a :term:`number <G.248>` subtracted to a number subtracted, the remainder is to the remainder as whole to whole.

.. signature:: theorem

   | :fn:`whole_whole_number <G.264>`\ ()
   | **prove** the remainder :g:`/ E B / <g1:/ E B />` is also to the remainder :g:`/ F D / <g1:/ F D />` as the whole :g:`/ A B / <g1:/ A B />` to the whole :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Book VII, Proposition 11

.. step:: assert

   As the whole :g:`/ A B / <g1:/ A B />` is to the whole :g:`/ C D / <g1:/ C D />`, so let :g:`/ A E / <g1:/ A E />` subtracted be to :g:`/ C F / <g1:/ C F />` subtracted

.. step:: assert

   Since, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`/ A E / <g1:/ A E />` to :g:`/ C F / <g1:/ C F />`,

.. step:: assert ∵ numbers_proportional_multiple_def <G.263>

   Whatever part or parts :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`, the :term:`same part <G.253>` or the :term:`same parts <G.254>` is :g:`/ A E / <g1:/ A E />` of :g:`/ C F / <g1:/ C F />` also.

.. step:: assert ∵ number_part_number_vii_7, number_parts_number_vii_8 <G.259, G.260>

   Therefore also the remainder :g:`/ E B / <g1:/ E B />` is the same part or parts of :g:`/ F D / <g1:/ F D />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`.

.. step:: conclude ∵ numbers_proportional_multiple_def <G.263>

   Therefore, as :g:`/ E B / <g1:/ E B />` is to :g:`/ F D / <g1:/ F D />`, so is :g:`/ A B / <g1:/ A B />` to :g:`/ C D / <g1:/ C D />`.

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
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.259" [label="G.259", tooltip="G.259 (VII.7): If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.", fillcolor="#222244", URL="../G.259/index.html", target="_top"];
     "G.260" [label="G.260", tooltip="G.260 (VII.8): If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.", fillcolor="#222244", URL="../G.260/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VII.def.20): Numbers areproportional when the first is thesame multiple, or thesame part, or thesame parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.263/index.html", target="_top"];
     "G.264" [label="G.264", tooltip="G.264 (VII.11): If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder is to the remainder as whole to whole.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.257" -> "G.170";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.259" -> "G.248";
     "G.260" -> "G.248";
     "G.264" -> "G.248";
     "G.257" -> "G.253";
     "G.259" -> "G.253";
     "G.263" -> "G.253";
     "G.260" -> "G.254";
     "G.263" -> "G.254";
     "G.257" -> "G.256";
     "G.263" -> "G.256";
     "G.259" -> "G.257";
     "G.260" -> "G.259";
     "G.264" -> "G.259";
     "G.264" -> "G.260";
     "G.264" -> "G.263";
   }

Required for
------------

:ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`

.. toctree::
   :hidden:

   code
   heath
