:order: 199
:number: 199
:canonical_id: G.199
:original_id: V.18
:title: G.199 magnitudes proportional separando
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, segment, proportional, separando, componendo, ratio, proportion, reductio-ad-absurdum
:dependencies: G.180, G.189, G.192, G.196, G.197, G.198
:excerpt: If magnitudes be proportional separando, they is proportional componendo.

.. _G.199:
.. _V.18:

G.199 magnitudes proportional separando
=======================================

.. rubric:: `V.18 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/18/>`_

.. enunciation::

   If magnitudes be :term:`proportional <G.180>` :term:`separando <G.197>`, they is proportional :term:`componendo <G.196>`.

.. signature:: theorem

   | :fn:`magnitudes_proportional_separando <G.199>`\ (:g:`/ A E / <g1:/ A E />`, :g:`/ E B / <g1:/ E B />`, :g:`/ C F / <g1:/ C F />`, :g:`/ F D / <g1:/ F D />`)
   | **given** :g:`/ A E / <g1:/ A E />`, :g:`/ E B / <g1:/ E B />`, :g:`/ C F / <g1:/ C F />`, :g:`/ F D / <g1:/ F D />` be magnitudes proportional *separando*, so that, as :g:`/ A E / <g1:/ A E />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C F / <g1:/ C F />` to :g:`/ F D / <g1:/ F D />`
   | **prove** they will also be proportional *componendo*, that is, as :g:`/ A B / <g1:/ A B />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C D / <g1:/ C D />` to :g:`/ F D / <g1:/ F D />`

.. picture:: g1.svg
   :alt: Proposition 18 diagram of line segments

.. step:: given

   :g:`/ A E / <g1:/ A E />`, :g:`/ E B / <g1:/ E B />`, :g:`/ C F / <g1:/ C F />`, :g:`/ F D / <g1:/ F D />` be magnitudes proportional *separando*, so that, as :g:`/ A E / <g1:/ A E />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C F / <g1:/ C F />` to :g:`/ F D / <g1:/ F D />`

.. step:: assert

   If :g:`/ C D / <g1:/ C D />` be not to :g:`/ F D / <g1:/ F D />` as :g:`/ A B / <g1:/ A B />` to :g:`/ E B / <g1:/ E B />`, then, as :g:`/ A B / <g1:/ A B />` is to :g:`/ E B / <g1:/ E B />`, so will :g:`/ C D / <g1:/ C D />` be either to some magnitude less than :g:`/ F D / <g1:/ F D />` or to a greater.

.. step:: assert

   First, let it be in that :term:`ratio <G.173>` to a less magnitude :g:`/ G D / <g1:/ G D />`.

.. step:: assert

   Since, as :g:`/ A B / <g1:/ A B />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C D / <g1:/ C D />` to :g:`/ G D / <g1:/ G D />`, they are magnitudes proportional *componendo*

.. step:: assert ∵ magnitudes_proportional_componendo <G.198>

   So that they will also be proportional *separando*.

.. step:: assert

   Therefore, as :g:`/ A E / <g1:/ A E />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C G / <g1:/ C G />` to :g:`/ G D / <g1:/ G D />`.

.. step:: assert

   Also, by hypothesis,

.. step:: assert

   As :g:`/ A E / <g1:/ A E />` is to :g:`/ E B / <g1:/ E B />`, so is :g:`/ C F / <g1:/ C F />` to :g:`/ F D / <g1:/ F D />`.

.. step:: assert ∵ ratios_ratio <G.189>

   Therefore also, as :g:`/ C G / <g1:/ C G />` is to :g:`/ G D / <g1:/ G D />`, so is :g:`/ C F / <g1:/ C F />` to :g:`/ F D / <g1:/ F D />`.

.. step:: assert

   The first :g:`/ C G / <g1:/ C G />` is greater than the third :g:`/ C F / <g1:/ C F />`

.. step:: assert ∵ magnitude_ratio_greater_v_14 <G.192>

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
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.171" [label="G.171", tooltip="G.171 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.172" [label="G.172", tooltip="G.172 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.172/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.13): Inverse ratio means taking theconsequent as antecedent in relation to the antecedent as consequent.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (V.def.7): When, of theequimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then th...", fillcolor="#224422", URL="../G.185/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.188" [label="G.188", tooltip="G.188 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.188/index.html", target="_top"];
     "G.189" [label="G.189", tooltip="G.189 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.189/index.html", target="_top"];
     "G.191" [label="G.191", tooltip="G.191 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.191/index.html", target="_top"];
     "G.192" [label="G.192", tooltip="G.192 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.192/index.html", target="_top"];
     "G.196" [label="G.196", tooltip="G.196 (V.def.14): Composition of a ratio means taking theantecedent together with the consequent as one in relation to the consequent by itself.", fillcolor="#224422", URL="../G.196/index.html", target="_top"];
     "G.197" [label="G.197", tooltip="G.197 (V.def.15): Separation of a ratio means taking the excess by which theantecedent exceeds the consequent in relation to the consequent by itself.", fillcolor="#224422", URL="../G.197/index.html", target="_top"];
     "G.198" [label="G.198", tooltip="G.198 (V.17): If magnitudes be proportional componendo, they is proportional separando.", fillcolor="#222244", URL="../G.198/index.html", target="_top"];
     "G.199" [label="G.199", tooltip="G.199 (V.18): If magnitudes be proportional separando, they is proportional componendo.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.3" -> "G.2";
     "G.198" -> "G.2";
     "G.8" -> "G.3";
     "G.9" -> "G.8";
     "G.188" -> "G.9";
     "G.189" -> "G.9";
     "G.170" -> "G.169";
     "G.171" -> "G.170";
     "G.172" -> "G.170";
     "G.176" -> "G.170";
     "G.185" -> "G.170";
     "G.186" -> "G.171";
     "G.198" -> "G.171";
     "G.198" -> "G.172";
     "G.188" -> "G.173";
     "G.189" -> "G.173";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.189" -> "G.176";
     "G.191" -> "G.176";
     "G.192" -> "G.176";
     "G.183" -> "G.180";
     "G.198" -> "G.180";
     "G.199" -> "G.180";
     "G.182" -> "G.181";
     "G.196" -> "G.181";
     "G.197" -> "G.181";
     "G.183" -> "G.182";
     "G.188" -> "G.183";
     "G.186" -> "G.184";
     "G.188" -> "G.184";
     "G.186" -> "G.185";
     "G.188" -> "G.185";
     "G.191" -> "G.185";
     "G.188" -> "G.186";
     "G.192" -> "G.186";
     "G.192" -> "G.188";
     "G.199" -> "G.189";
     "G.192" -> "G.191";
     "G.199" -> "G.192";
     "G.198" -> "G.196";
     "G.199" -> "G.196";
     "G.198" -> "G.197";
     "G.199" -> "G.197";
     "G.199" -> "G.198";
   }

Required for
------------

:ref:`G.207 <G.207>`, :ref:`G.236 <G.236>`, :ref:`G.238 <G.238>`, :ref:`G.239 <G.239>`, :ref:`G.240 <G.240>`, :ref:`G.241 <G.241>`, :ref:`G.243 <G.243>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.451 <G.451>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.557 <G.557>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
