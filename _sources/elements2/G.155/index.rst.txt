:order: 155
:number: 155
:canonical_id: G.155
:original_id: V.18
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, segment, separando, componendo, proportion, reductio-ad-absurdum
:dependencies: G.148, G.151, G.154
:excerpt: If magnitudes be proportional separando, they is proportional componendo.

.. _G.155:
.. _V.18:

G.155
=====

.. rubric:: `V.18 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/18/>`_

.. enunciation::

   If magnitudes be proportional separando, they is proportional componendo.

.. signature:: theorem

   | :fn:`magnitudes_proportional_separando <G.155>`\ (:g:`/ A E / <g1:/ A E />`, :g:`/ E B / <g1:/ E B />`, :g:`/ C F / <g1:/ C F />`, :g:`/ F D / <g1:/ F D />`)
   | **given** :g:`/ A E / <g1:/ A E />`, :g:`/ E B / <g1:/ E B />`, :g:`/ C F / <g1:/ C F />`, :g:`/ F D / <g1:/ F D />` be magnitudes proportional :term:`*separando* <separando>`, so that, as :g:`/ A E / <g1:/ A E />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C F / <g1:/ C F />` to :g:`/ F D / <g1:/ F D />`
   | **prove** they will also be proportional :term:`*componendo* <componendo>`, that is, as :g:`/ A B / <g1:/ A B />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C D / <g1:/ C D />` to :g:`/ F D / <g1:/ F D />`

.. picture:: g1.svg
   :alt: Proposition 18 diagram of line segments

.. step:: given

   :g:`/ A E / <g1:/ A E />`, :g:`/ E B / <g1:/ E B />`, :g:`/ C F / <g1:/ C F />`, :g:`/ F D / <g1:/ F D />` be magnitudes proportional :term:`*separando* <separando>`, so that, as :g:`/ A E / <g1:/ A E />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C F / <g1:/ C F />` to :g:`/ F D / <g1:/ F D />`

.. step:: assert

   If :g:`/ C D / <g1:/ C D />` be not to :g:`/ F D / <g1:/ F D />` as :g:`/ A B / <g1:/ A B />` to :g:`/ E B / <g1:/ E B />`, then, as :g:`/ A B / <g1:/ A B />` is to :g:`/ E B / <g1:/ E B />`, so will :g:`/ C D / <g1:/ C D />` be either to some magnitude less than :g:`/ F D / <g1:/ F D />` or to a greater.

.. step:: assert

   First, let it be in that ratio to a less magnitude :g:`/ G D / <g1:/ G D />`.

.. step:: assert

   Since, as :g:`/ A B / <g1:/ A B />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C D / <g1:/ C D />` to :g:`/ G D / <g1:/ G D />`, they are magnitudes proportional :term:`*componendo* <componendo>`

.. step:: assert ∵ magnitudes_proportional_componendo <G.154>

   So that they will also be proportional :term:`*separando* <separando>`.

.. step:: assert

   Therefore, as :g:`/ A E / <g1:/ A E />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C G / <g1:/ C G />` to :g:`/ G D / <g1:/ G D />`.

.. step:: assert

   Also, by hypothesis,

.. step:: assert

   As :g:`/ A E / <g1:/ A E />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C F / <g1:/ C F />` to :g:`/ F D / <g1:/ F D />`.

.. step:: assert ∵ ratios_ratio <G.148>

   Therefore also, as :g:`/ C G / <g1:/ C G />` is to :g:`/ G D / <g1:/ G D />`, so is :g:`/ C F / <g1:/ C F />` to :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   The first :g:`/ C G / <g1:/ C G />` is greater than the third :g:`/ C F / <g1:/ C F />`

.. step:: assert ∵ magnitude_ratio_greater_v_14 <G.151>

   Therefore the second :g:`/ G D / <g1:/ G D />` is also greater than the fourth :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   It is also less: which is impossible.

.. step:: assert

   Therefore, as :g:`/ A B / <g1:/ A B />` is to :g:`/ E B / <g1:/ E B />`, so is not :g:`/ C D / <g1:/ C D />` to a less magnitude than :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   Similarly we can prove that neither is it in that ratio to a greater

.. step:: conclude

   It is therefore in that ratio to :g:`/ F D / <g1:/ F D />` itself.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.136" [label="G.136", tooltip="G.136 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.136/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.150/index.html", target="_top"];
     "G.151" [label="G.151", tooltip="G.151 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.151/index.html", target="_top"];
     "G.154" [label="G.154", tooltip="G.154 (V.17): If magnitudes be proportional componendo, they is proportional separando.", fillcolor="#222244", URL="../G.154/index.html", target="_top"];
     "G.155" [label="G.155", tooltip="G.155 (V.18): If magnitudes be proportional separando, they is proportional componendo.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.154" -> "G.135";
     "G.154" -> "G.136";
     "G.142" -> "G.138";
     "G.150" -> "G.138";
     "G.147" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.147" -> "G.145";
     "G.151" -> "G.145";
     "G.151" -> "G.147";
     "G.155" -> "G.148";
     "G.151" -> "G.150";
     "G.155" -> "G.151";
     "G.155" -> "G.154";
   }

Required for
------------

:ref:`G.161 <G.161>`, :ref:`G.189 <G.189>`, :ref:`G.191 <G.191>`, :ref:`G.192 <G.192>`, :ref:`G.193 <G.193>`, :ref:`G.194 <G.194>`, :ref:`G.195 <G.195>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.392 <G.392>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.492 <G.492>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
