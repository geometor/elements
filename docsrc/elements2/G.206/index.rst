:order: 206
:number: 206
:canonical_id: G.206
:original_id: VII.7
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, segment, number, equality
:dependencies: G.204
:excerpt: If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.

.. _G.206:
.. _VII.7:

G.206
=====

.. rubric:: `VII.7 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/07/>`_

.. enunciation::

   If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.

.. signature:: theorem

   | :fn:`number_part_number_vii_7 <G.206>`\ ()
   | **prove** the remainder :g:`/ E B / <g1:/ E B />` is also the same part of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ A B / <g1:/ A B />` is of the whole :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Book VII, Proposition 7

.. step:: assert

   Let the number :g:`/ A B / <g1:/ A B />` be that part of the number :g:`/ C D / <g1:/ C D />` which :g:`/ A E / <g1:/ A E />` subtracted is of :g:`/ C F / <g1:/ C F />` subtracted

.. step:: assert

   Whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also let :g:`/ E B / <g1:/ E B />` be of :g:`/ G C / <g1:/ G C />`.

.. step:: assert

   Now since, whatever part :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, the same part also is :g:`/ E B / <g1:/ E B />` of :g:`/ G C / <g1:/ G C />`,

.. step:: assert ∵ number_part_number <G.204>

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
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.206" [label="G.206", tooltip="G.206 (VII.7): If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.206" -> "G.204";
   }

Required for
------------

:ref:`G.207 <G.207>`, :ref:`G.211 <G.211>`, :ref:`G.310 <G.310>`, :ref:`G.312 <G.312>`

.. toctree::
   :hidden:

   code
   heath
