:order: 156
:number: 156
:canonical_id: G.156
:original_id: V.19
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, segment, componendo, separando, convertendo, porism
:dependencies: G.148, G.153, G.154
:excerpt: If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder is to the remainder as whole to whole.

.. _G.156:
.. _V.19:

G.156
=====

.. rubric:: `V.19 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/19/>`_

.. enunciation::

   If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder is to the remainder as whole to whole.

.. picture:: g1.svg
   :alt: Proposition 19

.. step:: assert

   As the whole :g:`/ A B / <g1:/ A B />` is to the whole :g:`/ C D / <g1:/ C D />`, so let the part :g:`/ A E / <g1:/ A E />` subtracted be to the part :g:`/ C F / <g1:/ C F />` subtracted

.. step:: assert

   For since, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`/ A E / <g1:/ A E />` to :g:`/ C F / <g1:/ C F />`,

.. step:: assert [G.153] <G.153>

   Alternately also, as :g:`/ A B / <g1:/ A B />` is to :g:`/ A E / <g1:/ A E />`, so is :g:`/ C D / <g1:/ C D />` to :g:`/ C F / <g1:/ C F />`.

.. step:: assert [G.154] <G.154>

   And, since the magnitudes are proportional :term:`*componendo* <componendo>`, they will also be proportional :term:`*separando* <separando>`.

.. step:: assert

   That is, as :g:`/ E B / <g1:/ E B />` is to :g:`/ A E / <g1:/ A E />`, so is :g:`/ F D / <g1:/ F D />` to :g:`/ C F / <g1:/ C F />`, and, alternately,

.. step:: assert [G.153] <G.153>

   As :g:`/ E B / <g1:/ E B />` is to :g:`/ F D / <g1:/ F D />`, so is :g:`/ A E / <g1:/ A E />` to :g:`/ C F / <g1:/ C F />`.

.. step:: assert

   But, as :g:`/ A E / <g1:/ A E />` is to :g:`/ C F / <g1:/ C F />`, so by hypothesis is the whole :g:`/ A B / <g1:/ A B />` to the whole :g:`/ C D / <g1:/ C D />`.

.. step:: assert [G.148] <G.148>

   Therefore also the remainder :g:`/ E B / <g1:/ E B />` will be to the remainder :g:`/ F D / <g1:/ F D />` as the whole :g:`/ A B / <g1:/ A B />` is to the whole :g:`/ C D / <g1:/ C D />`.

.. step:: conclude

   Therefore etc.

.. porism::

   From this it is manifest that, if magnitudes be proportional :term:`*componendo* <componendo>`, they will also be proportional :term:`*convertendo* <convertendo>`.

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
     "G.149" [label="G.149", tooltip="G.149 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.150/index.html", target="_top"];
     "G.151" [label="G.151", tooltip="G.151 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.151/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.152/index.html", target="_top"];
     "G.153" [label="G.153", tooltip="G.153 (V.16): If four magnitudes be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.153/index.html", target="_top"];
     "G.154" [label="G.154", tooltip="G.154 (V.17): If magnitudes be proportional componendo, they is proportional separando.", fillcolor="#222244", URL="../G.154/index.html", target="_top"];
     "G.156" [label="G.156", tooltip="G.156 (V.19): If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder is to the remainder as whole to whole.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.149" -> "G.135";
     "G.154" -> "G.135";
     "G.154" -> "G.136";
     "G.142" -> "G.138";
     "G.149" -> "G.138";
     "G.150" -> "G.138";
     "G.153" -> "G.138";
     "G.147" -> "G.142";
     "G.152" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.147" -> "G.145";
     "G.151" -> "G.145";
     "G.151" -> "G.147";
     "G.153" -> "G.148";
     "G.156" -> "G.148";
     "G.152" -> "G.149";
     "G.151" -> "G.150";
     "G.153" -> "G.151";
     "G.153" -> "G.152";
     "G.156" -> "G.153";
     "G.156" -> "G.154";
   }

Required for
------------

:ref:`G.162 <G.162>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
