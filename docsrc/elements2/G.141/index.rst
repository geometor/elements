:order: 141
:number: 141
:canonical_id: G.141
:original_id: V.6
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, segment, equality
:dependencies: G.136
:excerpt: If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equimultiples of them.

.. _G.141:
.. _V.6:

G.141
=====

.. rubric:: `V.6 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/06/>`_

.. enunciation::

   If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equimultiples of them.

For let two magnitudes :g:`/ A B / <0153.g1:/ A B />`, :g:`/ C D / <0153.g1:/ C D />` be equimultiples of two magnitudes :g:`E <0153.g1:E>`, :g:`F <0153.g1:F>`, and let :g:`/ A G / <0153.g1:/ A G />`, :g:`/ C H / <0153.g1:/ C H />` subtracted from them be equimultiples of the same two :g:`E <0153.g1:E>`, :g:`F <0153.g1:F>`;

I say that the remainders also, :g:`/ G B / <0153.g1:/ G B />`, :g:`/ H D / <0153.g1:/ H D />`, are either :eq:`equal <0153.g1:/ G B / = 0153.g1:E; 0153.g1:/ H D / = 0153.g1:F>` to :g:`E <0153.g1:E>`, :g:`F <0153.g1:F>` or equimultiples of them.

.. picture:: 0153.g1.svg
   :alt: Proposition 6 Diagram

For, first, let :g:`/ G B / <0153.g1:/ G B />` be :eq:`equal <0153.g1:/ G B / = 0153.g1:E>` to :g:`E <0153.g1:E>`;

I say that :g:`/ H D / <0153.g1:/ H D />` is also :eq:`equal <0153.g1:/ H D / = 0153.g1:F>` to :g:`F <0153.g1:F>`.

For let :g:`/ C K / <0153.g1:/ C K />` be made :eq:`equal <0153.g1:/ C K / = 0153.g1:F>` to :g:`F <0153.g1:F>`.

Since :g:`/ A G / <0153.g1:/ A G />` is the same multiple of :g:`E <0153.g1:E>` that :g:`/ C H / <0153.g1:/ C H />` is of :g:`F <0153.g1:F>`,

.. subclause::

   while :g:`/ G B / <0153.g1:/ G B />` is :eq:`equal <0153.g1:/ G B / = 0153.g1:E; 0153.g1:/ C K / = 0153.g1:F>` to :g:`E <0153.g1:E>` and :g:`/ C K / <0153.g1:/ C K />` to :g:`F <0153.g1:F>`,

therefore :g:`/ A B / <0153.g1:/ A B />` is the same multiple of :g:`E <0153.g1:E>` that :g:`/ K H / <0153.g1:/ K H />` is of :g:`F <0153.g1:F>`. :just:`[G.136] <G.136>`

But, by hypothesis, :g:`/ A B / <0153.g1:/ A B />` is the same multiple of :g:`E <0153.g1:E>` that :g:`/ C D / <0153.g1:/ C D />` is of :g:`F <0153.g1:F>`;

.. assertion::

   therefore :g:`/ K H / <0153.g1:/ K H />` is the same multiple of :g:`F <0153.g1:F>` that :g:`/ C D / <0153.g1:/ C D />` is of :g:`F <0153.g1:F>`.

Since then each of the magnitudes :g:`/ K H / <0153.g1:/ K H />`, :g:`/ C D / <0153.g1:/ C D />` is the same multiple of :g:`F <0153.g1:F>`,

.. assertion::

   therefore :g:`/ K H / <0153.g1:/ K H />` is :eq:`equal <0153.g1:/ K H / = 0153.g1:/ C D />` to :g:`/ C D / <0153.g1:/ C D />`.

.. subclause::

   Let :g:`/ C H / <0153.g1:/ C H />` be subtracted from each;

.. assertion::

   therefore the remainder :g:`/ C K / <0153.g1:/ C K />` is :eq:`equal <0153.g1:/ C K / = 0153.g1:/ H D />` to the remainder :g:`/ H D / <0153.g1:/ H D />`.

But :g:`F <0153.g1:F>` is :eq:`equal <0153.g1:F = 0153.g1:/ C K />` to :g:`/ C K / <0153.g1:/ C K />`;

.. assertion::

   therefore :g:`/ H D / <0153.g1:/ H D />` is also :eq:`equal <0153.g1:/ H D / = 0153.g1:F>` to :g:`F <0153.g1:F>`.

Hence, if :g:`/ G B / <0153.g1:/ G B />` is :eq:`equal <0153.g1:/ G B / = 0153.g1:E>` to :g:`E <0153.g1:E>`, :g:`/ H D / <0153.g1:/ H D />` is also :eq:`equal <0153.g1:/ H D / = 0153.g1:F>` to :g:`F <0153.g1:F>`.

Similarly we can prove that, even if :g:`/ G B / <0153.g1:/ G B />` be a multiple of :g:`E <0153.g1:E>`, :g:`/ H D / <0153.g1:/ H D />` is also the same multiple of :g:`F <0153.g1:F>`.

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
     "G.136" [label="G.136", tooltip="G.136 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.136/index.html", target="_top"];
     "G.141" [label="G.141", tooltip="G.141 (V.6): If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equi...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.141" -> "G.136";
   }
