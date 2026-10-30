:order: 207
:number: 207
:canonical_id: G.207
:original_id: VII.8
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, segment, number, equality
:dependencies: G.206
:excerpt: If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.

.. _G.207:
.. _VII.8:

G.207
=====

.. rubric:: `VII.8 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/08/>`_

.. enunciation::

   If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.

.. signature:: theorem

   | :fn:`number_parts_number_vii_8 <G.207>`\ ()
   | **prove** the remainder :g:`/ E B / <g1:/ E B />` is also the same parts of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ A B / <g1:/ A B />` is of the whole :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Book VII, Proposition 8

.. step:: assert

   Let the number :g:`/ A B / <g1:/ A B />` be the same parts of the number :g:`/ C D / <g1:/ C D />` that :g:`/ A E / <g1:/ A E />` subtracted is of :g:`/ C F / <g1:/ C F />` subtracted

.. step:: construct

   :fn:`cut_equal_segment <G.9>`\ (:g:`/ A B / <g1:/ A B />`) → :g:`/ G H / <g1:/ G H />` (:eq:`equal <g1:/ G H / = g1:/ A B />`)

.. step:: assert

   Therefore, whatever parts :g:`/ G H / <g1:/ G H />` is of :g:`/ C D / <g1:/ C D />`, the same parts also is :g:`/ A E / <g1:/ A E />` of :g:`/ C F / <g1:/ C F />`.

.. step:: assert

   Let :g:`/ G H / <g1:/ G H />` be divided into the parts of :g:`/ C D / <g1:/ C D />`, namely :g:`/ G K / <g1:/ G K />`, :g:`/ K H / <g1:/ K H />`, and :g:`/ A E / <g1:/ A E />` into the parts of :g:`/ C F / <g1:/ C F />`, namely :g:`/ A L / <g1:/ A L />`, :g:`/ L E / <g1:/ L E />`

.. step:: assert

   Thus the multitude of :g:`/ G K / <g1:/ G K />`, :g:`/ K H / <g1:/ K H />` will be equal to the multitude of :g:`/ A L / <g1:/ A L />`, :g:`/ L E / <g1:/ L E />`.

.. step:: assert

   Now since, whatever part :g:`/ G K / <g1:/ G K />` is of :g:`/ C D / <g1:/ C D />`, the same part also is :g:`/ A L / <g1:/ A L />` of :g:`/ C F / <g1:/ C F />`, while :g:`/ C D / <g1:/ C D />` is greater than :g:`/ C F / <g1:/ C F />`,

.. step:: assert

   Therefore :g:`/ G K / <g1:/ G K />` is also greater than :g:`/ A L / <g1:/ A L />`.

.. step:: construct

   :fn:`cut_equal_segment <G.9>`\ (:g:`/ A L / <g1:/ A L />`) → :g:`/ G M / <g1:/ G M />` (:eq:`equal <g1:/ G M / = g1:/ A L />`)

.. step:: assert

   Therefore, whatever part :g:`/ G K / <g1:/ G K />` is of :g:`/ C D / <g1:/ C D />`, the same part also is :g:`/ G M / <g1:/ G M />` of :g:`/ C F / <g1:/ C F />`;

.. step:: assert ∵ number_part_number_vii_7 <G.206>

   Therefore also the remainder :g:`/ M K / <g1:/ M K />` is the same part of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ G K / <g1:/ G K />` is of the whole :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   Since, whatever part :g:`/ K H / <g1:/ K H />` is of :g:`/ C D / <g1:/ C D />`, the same part also is :g:`/ L E / <g1:/ L E />` of :g:`/ C F / <g1:/ C F />`, while :g:`/ C D / <g1:/ C D />` is greater than :g:`/ C F / <g1:/ C F />`,

.. step:: assert

   Therefore :g:`/ K H / <g1:/ K H />` is also greater than :g:`/ L E / <g1:/ L E />`.

.. step:: construct

   :fn:`cut_equal_segment <G.9>`\ (:g:`/ L E / <g1:/ L E />`) → :g:`/ K N / <g1:/ K N />` (:eq:`equal <g1:/ K N / = g1:/ L E />`)

.. step:: assert

   Therefore, whatever part :g:`/ K H / <g1:/ K H />` is of :g:`/ C D / <g1:/ C D />`, the same part also is :g:`/ K N / <g1:/ K N />` of :g:`/ C F / <g1:/ C F />`;

.. step:: assert ∵ number_part_number_vii_7 <G.206>

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
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.206" [label="G.206", tooltip="G.206 (VII.7): If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.", fillcolor="#222244", URL="../G.206/index.html", target="_top"];
     "G.207" [label="G.207", tooltip="G.207 (VII.8): If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.206" -> "G.204";
     "G.207" -> "G.206";
   }

Required for
------------

:ref:`G.211 <G.211>`, :ref:`G.310 <G.310>`, :ref:`G.312 <G.312>`

.. toctree::
   :hidden:

   code
   heath
