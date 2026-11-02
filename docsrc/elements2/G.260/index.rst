:order: 260
:number: 260
:canonical_id: G.260
:original_id: VII.8
:title: G.260 number parts number
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, segment, number, parts-non-aliquot, part-aliquot, equality
:dependencies: G.248, G.254, G.259
:excerpt: If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.

.. _G.260:
.. _VII.8:

G.260 number parts number
=========================

.. rubric:: `VII.8 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/08/>`_

.. enunciation::

   If a :term:`number <G.248>` be the :term:`same parts <G.254>` of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.

.. signature:: theorem

   | :fn:`number_parts_number_vii_8 <G.260>`\ ()
   | **prove** the remainder :g:`/ E B / <g1:/ E B />` is also the same parts of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ A B / <g1:/ A B />` is of the whole :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Book VII, Proposition 8

.. step:: assert

   Let the number :g:`/ A B / <g1:/ A B />` be the same parts of the number :g:`/ C D / <g1:/ C D />` that :g:`/ A E / <g1:/ A E />` subtracted is of :g:`/ C F / <g1:/ C F />` subtracted

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ A B / <g1:/ A B />`) → :g:`/ G H / <g1:/ G H />` (:eq:`equal <g1:/ G H / = g1:/ A B />`)

.. step:: assert

   Therefore, whatever parts :g:`/ G H / <g1:/ G H />` is of :g:`/ C D / <g1:/ C D />`, the same parts also is :g:`/ A E / <g1:/ A E />` of :g:`/ C F / <g1:/ C F />`.

.. step:: assert

   Let :g:`/ G H / <g1:/ G H />` be divided into the parts of :g:`/ C D / <g1:/ C D />`, namely :g:`/ G K / <g1:/ G K />`, :g:`/ K H / <g1:/ K H />`, and :g:`/ A E / <g1:/ A E />` into the parts of :g:`/ C F / <g1:/ C F />`, namely :g:`/ A L / <g1:/ A L />`, :g:`/ L E / <g1:/ L E />`

.. step:: assert

   Thus the multitude of :g:`/ G K / <g1:/ G K />`, :g:`/ K H / <g1:/ K H />` will be equal to the multitude of :g:`/ A L / <g1:/ A L />`, :g:`/ L E / <g1:/ L E />`.

.. step:: assert

   Now since, whatever part :g:`/ G K / <g1:/ G K />` is of :g:`/ C D / <g1:/ C D />`, the :term:`same part <G.253>` also is :g:`/ A L / <g1:/ A L />` of :g:`/ C F / <g1:/ C F />`, while :g:`/ C D / <g1:/ C D />` is greater than :g:`/ C F / <g1:/ C F />`,

.. step:: assert

   Therefore :g:`/ G K / <g1:/ G K />` is also greater than :g:`/ A L / <g1:/ A L />`.

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ A L / <g1:/ A L />`) → :g:`/ G M / <g1:/ G M />` (:eq:`equal <g1:/ G M / = g1:/ A L />`)

.. step:: assert

   Therefore, whatever part :g:`/ G K / <g1:/ G K />` is of :g:`/ C D / <g1:/ C D />`, the same part also is :g:`/ G M / <g1:/ G M />` of :g:`/ C F / <g1:/ C F />`;

.. step:: assert ∵ number_part_number_vii_7 <G.259>

   Therefore also the remainder :g:`/ M K / <g1:/ M K />` is the same part of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ G K / <g1:/ G K />` is of the whole :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   Since, whatever part :g:`/ K H / <g1:/ K H />` is of :g:`/ C D / <g1:/ C D />`, the same part also is :g:`/ L E / <g1:/ L E />` of :g:`/ C F / <g1:/ C F />`, while :g:`/ C D / <g1:/ C D />` is greater than :g:`/ C F / <g1:/ C F />`,

.. step:: assert

   Therefore :g:`/ K H / <g1:/ K H />` is also greater than :g:`/ L E / <g1:/ L E />`.

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ L E / <g1:/ L E />`) → :g:`/ K N / <g1:/ K N />` (:eq:`equal <g1:/ K N / = g1:/ L E />`)

.. step:: assert

   Therefore, whatever part :g:`/ K H / <g1:/ K H />` is of :g:`/ C D / <g1:/ C D />`, the same part also is :g:`/ K N / <g1:/ K N />` of :g:`/ C F / <g1:/ C F />`;

.. step:: assert ∵ number_part_number_vii_7 <G.259>

   Therefore also the remainder :g:`/ N H / <g1:/ N H />` is the same part of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ K H / <g1:/ K H />` is of the whole :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   The remainder :g:`/ M K / <g1:/ M K />` was also proved to be the same part of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ G K / <g1:/ G K />` is of the whole :g:`/ C D / <g1:/ C D />`;

.. step:: assert

   Therefore also the sum of :g:`/ M K / <g1:/ M K />`, :g:`/ N H / <g1:/ N H />` is the same parts of :g:`/ F D / <g1:/ F D />` that the whole :g:`/ G H / <g1:/ G H />` is of the whole :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   The sum of :g:`/ M K / <g1:/ M K />`, :g:`/ N H / <g1:/ N H />` is equal to :g:`/ E B / <g1:/ E B />`, and :g:`/ G H / <g1:/ G H />` is :eq:`equal <g1:/ G H / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />`;

.. step:: conclude

   Therefore the remainder :g:`/ E B / <g1:/ E B />` is the same parts of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ A B / <g1:/ A B />` is of the whole :g:`/ C D / <g1:/ C D />`.

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
     "G.260" [label="G.260", tooltip="G.260 (VII.8): If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.257" -> "G.253";
     "G.259" -> "G.253";
     "G.260" -> "G.254";
     "G.257" -> "G.256";
     "G.259" -> "G.257";
     "G.260" -> "G.259";
   }

Required for
------------

:ref:`G.264 <G.264>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`

.. toctree::
   :hidden:

   code
   heath
