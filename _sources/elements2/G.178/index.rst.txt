:order: 178
:number: 178
:canonical_id: G.178
:original_id: V.5
:title: G.178 magnitude multiple magnitude
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, segment, multiple, equality
:dependencies: G.170, G.171
:excerpt: If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder is the same multiple of the remainder that the whole is of the whole.

.. _G.178:
.. _V.5:

G.178 magnitude multiple magnitude
==================================

.. rubric:: `V.5 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/05/>`_

.. enunciation::

   If a magnitude be the same :term:`multiple <G.170>` of a magnitude that a part subtracted is of a part subtracted, the remainder is the same multiple of the remainder that the whole is of the whole.

.. signature:: theorem

   | :fn:`magnitude_multiple_magnitude <G.178>`\ ()
   | **prove** :g:`/ E B / <g1:/ E B />` is also the same multiple of :g:`/ F D / <g1:/ F D />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`

.. picture:: g1.svg
   :alt: Proposition 5 Diagram

.. step:: assert

   Let the magnitude :g:`/ A B / <g1:/ A B />` be the same multiple of the magnitude :g:`/ C D / <g1:/ C D />` that the part :g:`/ A E / <g1:/ A E />` subtracted is of the part :g:`/ C F / <g1:/ C F />` subtracted

.. step:: construct

   Whatever multiple :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, let :g:`/ E B / <g1:/ E B />` be made that multiple of :g:`/ C G / <g1:/ C G />`.

.. step:: assert ∵ there_number_magnitudes <G.171>

   :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ E B / <g1:/ E B />` is of :g:`/ C G / <g1:/ C G />` → therefore :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ G F / <g1:/ G F />`

.. step:: assert

   But, by the assumption, :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is the same multiple of each of the magnitudes :g:`/ G F / <g1:/ G F />`, :g:`/ C D / <g1:/ C D />`

.. step:: assert

   :g:`/ G F / <g1:/ G F />` :eq:`= <g1:/ G F / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`

.. step:: construct

   Let :g:`/ C F / <g1:/ C F />` be subtracted from each;

.. step:: assert

   :g:`/ C G / <g1:/ C G />` :eq:`= <g1:/ C G / = g1:/ F D />` :g:`/ F D / <g1:/ F D />`

.. step:: assert

   since :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ E B / <g1:/ E B />` is of :g:`/ C G / <g1:/ C G />`,

.. step:: assert

   :g:`/ C G / <g1:/ C G />` :eq:`= <g1:/ C G / = g1:/ F D />` :g:`/ F D / <g1:/ F D />`,

.. step:: assert

   :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ E B / <g1:/ E B />` is of :g:`/ F D / <g1:/ F D />`

.. step:: assert

   But, by hypothesis,

.. step:: assert

   :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`

.. step:: assert

   :g:`/ E B / <g1:/ E B />` is the same multiple of :g:`/ F D / <g1:/ F D />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`

.. step:: conclude

   That is, :g:`/ E B / <g1:/ E B />` will be the same multiple of :g:`/ F D / <g1:/ F D />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`

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
     "G.171" [label="G.171", tooltip="G.171 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.178" [label="G.178", tooltip="G.178 (V.5): If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder is the same multiple of the remainder that the whole is of the whol...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.171" -> "G.170";
     "G.178" -> "G.170";
     "G.178" -> "G.171";
   }

.. toctree::
   :hidden:

   code
   heath
