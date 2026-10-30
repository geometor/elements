:order: 211
:number: 211
:canonical_id: G.211
:original_id: VII.11
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, segment, number
:dependencies: G.206, G.207, G.210
:excerpt: If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder is to the remainder as whole to whole.

.. _G.211:
.. _VII.11:

G.211
=====

.. rubric:: `VII.11 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/11/>`_

.. enunciation::

   If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder is to the remainder as whole to whole.

.. signature:: theorem

   | :fn:`whole_whole_number <G.211>`\ ()
   | **prove** the remainder :g:`/ E B / <g1:/ E B />` is also to the remainder :g:`/ F D / <g1:/ F D />` as the whole :g:`/ A B / <g1:/ A B />` to the whole :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Book VII, Proposition 11

.. step:: assert

   As the whole :g:`/ A B / <g1:/ A B />` is to the whole :g:`/ C D / <g1:/ C D />`, so let :g:`/ A E / <g1:/ A E />` subtracted be to :g:`/ C F / <g1:/ C F />` subtracted

.. step:: assert

   Since, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`/ A E / <g1:/ A E />` to :g:`/ C F / <g1:/ C F />`,

.. step:: assert ∵ numbers_proportional_multiple_def <G.210>

   Whatever part or parts :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`, the same part or the same parts is :g:`/ A E / <g1:/ A E />` of :g:`/ C F / <g1:/ C F />` also.

.. step:: assert ∵ number_part_number_vii_7, number_parts_number_vii_8 <G.206, G.207>

   Therefore also the remainder :g:`/ E B / <g1:/ E B />` is the same part or parts of :g:`/ F D / <g1:/ F D />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`.

.. step:: conclude ∵ numbers_proportional_multiple_def <G.210>

   Therefore, as :g:`/ E B / <g1:/ E B />` is to :g:`/ F D / <g1:/ F D />`, so is :g:`/ A B / <g1:/ A B />` to :g:`/ C D / <g1:/ C D />`.

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
     "G.207" [label="G.207", tooltip="G.207 (VII.8): If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.", fillcolor="#222244", URL="../G.207/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** areproportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.211" [label="G.211", tooltip="G.211 (VII.11): If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder is to the remainder as whole to whole.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.206" -> "G.204";
     "G.207" -> "G.206";
     "G.211" -> "G.206";
     "G.211" -> "G.207";
     "G.211" -> "G.210";
   }

Required for
------------

:ref:`G.310 <G.310>`, :ref:`G.312 <G.312>`

.. toctree::
   :hidden:

   code
   heath
