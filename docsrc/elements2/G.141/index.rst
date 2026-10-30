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

.. signature:: theorem

   | :fn:`magnitudes_equimultiples_magnitudes <G.141>`\ ()
   | **prove** the remainders also, :g:`/ G B / <g1:/ G B />`, :g:`/ H D / <g1:/ H D />`, are either :eq:`equal <g1:/ G B / = g1:E; g1:/ H D / = g1:F>` to :g:`E <g1:E>`, :g:`F <g1:F>` or equimultiples of them; :g:`/ H D / <g1:/ H D />` is also :eq:`equal <g1:/ H D / = g1:F>` to :g:`F <g1:F>`

.. picture:: g1.svg
   :alt: Proposition 6 Diagram

.. step:: assert

   Let two magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` be equimultiples of two magnitudes :g:`E <g1:E>`, :g:`F <g1:F>`, and let :g:`/ A G / <g1:/ A G />`, :g:`/ C H / <g1:/ C H />` subtracted from them be equimultiples of the same two :g:`E <g1:E>`, :g:`F <g1:F>`

.. step:: assert

   First, let :g:`/ G B / <g1:/ G B />` be :eq:`equal <g1:/ G B / = g1:E>` to :g:`E <g1:E>`

.. step:: construct

   :fn:`cut_equal_segment <G.9>`\ (:g:`F <g1:F>`) → :g:`/ C K / <g1:/ C K />` (:eq:`equal <g1:/ C K / = g1:F>`)

.. step:: assert

   Since :g:`/ A G / <g1:/ A G />` is the same multiple of :g:`E <g1:E>` that :g:`/ C H / <g1:/ C H />` is of :g:`F <g1:F>` → while :g:`/ G B / <g1:/ G B />` is :eq:`equal <g1:/ G B / = g1:E; g1:/ C K / = g1:F>` to :g:`E <g1:E>` and :g:`/ C K / <g1:/ C K />` to :g:`F <g1:F>`,

.. step:: assert ∵ magnitude_multiple_fifth <G.136>

   Therefore :g:`/ A B / <g1:/ A B />` is the same multiple of :g:`E <g1:E>` that :g:`/ K H / <g1:/ K H />` is of :g:`F <g1:F>`.

.. step:: assert

   But, by hypothesis, :g:`/ A B / <g1:/ A B />` is the same multiple of :g:`E <g1:E>` that :g:`/ C D / <g1:/ C D />` is of :g:`F <g1:F>`

.. step:: assert

   Therefore :g:`/ K H / <g1:/ K H />` is the same multiple of :g:`F <g1:F>` that :g:`/ C D / <g1:/ C D />` is of :g:`F <g1:F>`.

.. step:: assert

   Since then each of the magnitudes :g:`/ K H / <g1:/ K H />`, :g:`/ C D / <g1:/ C D />` is the same multiple of :g:`F <g1:F>` → therefore :g:`/ K H / <g1:/ K H />` is :eq:`equal <g1:/ K H / = g1:/ C D />` to :g:`/ C D / <g1:/ C D />`.

.. step:: construct

   Let :g:`/ C H / <g1:/ C H />` be subtracted from each;

.. step:: assert

   Therefore the remainder :g:`/ C K / <g1:/ C K />` is :eq:`equal <g1:/ C K / = g1:/ H D />` to the remainder :g:`/ H D / <g1:/ H D />`.

.. step:: assert

   :g:`F <g1:F>` is :eq:`equal <g1:F = g1:/ C K />` to :g:`/ C K / <g1:/ C K />`

.. step:: assert

   Therefore :g:`/ H D / <g1:/ H D />` is also :eq:`equal <g1:/ H D / = g1:F>` to :g:`F <g1:F>`.

.. step:: assert

   Hence, if :g:`/ G B / <g1:/ G B />` is :eq:`equal <g1:/ G B / = g1:E>` to :g:`E <g1:E>`, :g:`/ H D / <g1:/ H D />` is also :eq:`equal <g1:/ H D / = g1:F>` to :g:`F <g1:F>`.

.. step:: conclude

   Similarly we can prove that, even if :g:`/ G B / <g1:/ G B />` be a multiple of :g:`E <g1:E>`, :g:`/ H D / <g1:/ H D />` is also the same multiple of :g:`F <g1:F>`.

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

.. toctree::
   :hidden:

   code
   heath
