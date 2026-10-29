:canonical_id: G.140
:original_id: V.5
:volume: II
:book: V
:type: prop

G.140 — Heath
=============

.. rubric:: `V.5 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/05/>`_

.. enunciation::

   If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

For let the magnitude :g:`/ A B / <g1:/ A B />` be the same multiple of the magnitude :g:`/ C D / <g1:/ C D />` that the part :g:`/ A E / <g1:/ A E />` subtracted is of the part :g:`/ C F / <g1:/ C F />` subtracted;

I say that the remainder :g:`/ E B / <g1:/ E B />` is also the same multiple of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ A B / <g1:/ A B />` is of the whole :g:`/ C D / <g1:/ C D />`.

.. picture:: g1.svg
   :alt: Proposition 5 Diagram

For, whatever multiple :g:`/ A E / <g1:/ A E />` is of :g:`/ C F / <g1:/ C F />`, let :g:`/ E B / <g1:/ E B />` be made that multiple of :g:`/ C G / <g1:/ C G />`.

Then, since :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ E B / <g1:/ E B />` is of :g:`/ C G / <g1:/ C G />`,

.. assertion:: [G.135] <G.135>

   therefore :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ G F / <g1:/ G F />`.

But, by the assumption, :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`.

.. assertion::

   Therefore :g:`/ A B / <g1:/ A B />` is the same multiple of each of the magnitudes :g:`/ G F / <g1:/ G F />`, :g:`/ C D / <g1:/ C D />`;

.. assertion::

   therefore :g:`/ G F / <g1:/ G F />` is :eq:`equal <g1:/ G F / = g1:/ C D />` to :g:`/ C D / <g1:/ C D />`.

.. subclause::

   Let :g:`/ C F / <g1:/ C F />` be subtracted from each;

.. assertion::

   therefore the remainder :g:`/ C G / <g1:/ C G />` is :eq:`equal <g1:/ C G / = g1:/ F D />` to the remainder :g:`/ F D / <g1:/ F D />`.

And, since :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ E B / <g1:/ E B />` is of :g:`/ C G / <g1:/ C G />`,

.. subclause::

   and :g:`/ C G / <g1:/ C G />` is :eq:`equal <g1:/ C G / = g1:/ F D />` to :g:`/ F D / <g1:/ F D />`,

.. assertion::

   therefore :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ E B / <g1:/ E B />` is of :g:`/ F D / <g1:/ F D />`.

But, by hypothesis,

.. subclause::

   :g:`/ A E / <g1:/ A E />` is the same multiple of :g:`/ C F / <g1:/ C F />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`;

.. assertion::

   therefore :g:`/ E B / <g1:/ E B />` is the same multiple of :g:`/ F D / <g1:/ F D />` that :g:`/ A B / <g1:/ A B />` is of :g:`/ C D / <g1:/ C D />`.

That is, the remainder :g:`/ E B / <g1:/ E B />` will be the same multiple of the remainder :g:`/ F D / <g1:/ F D />` that the whole :g:`/ A B / <g1:/ A B />` is of the whole :g:`/ C D / <g1:/ C D />`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.140" [label="G.140", tooltip="G.140 (V.5): If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder is the same multiple of the remainder that the whole is of the whol...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.140" -> "G.135";
   }
