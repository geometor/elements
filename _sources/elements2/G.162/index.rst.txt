:order: 162
:number: 162
:canonical_id: G.162
:original_id: V.25
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, segment, proportion, equality
:dependencies: G.156
:excerpt: If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

.. _G.162:
.. _V.25:

G.162
=====

.. rubric:: `V.25 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/25/>`_

.. enunciation::

   If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

.. signature:: theorem

   | :fn:`magnitudes_proportional_greatest <G.162>`\ (:g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`, :g:`F <g1:F>`)
   | **given** the four magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`, :g:`F <g1:F>` be proportional so that, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, let :g:`/ A B / <g1:/ A B />` be the greatest of them and :g:`F <g1:F>` the least
   | **prove** :g:`/ A B / <g1:/ A B />`, :g:`F <g1:F>` are greater than :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`

.. picture:: g1.svg
   :alt: Book V, Proposition 25, Line Segments

.. step:: given

   the four magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`, :g:`F <g1:F>` be proportional so that, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, let :g:`/ A B / <g1:/ A B />` be the greatest of them and :g:`F <g1:F>` the least

.. step:: construct

   :fn:`cut_equal_segment <G.9>`\ (:g:`E <g1:E>`, and :g:`/ C H / <g1:/ C H />` :eq:`equal <g1:/ C H / = g1:F>` to :g:`F <g1:F>`) → :g:`/ A G / <g1:/ A G />` (:eq:`equal <g1:/ A G / = g1:E>`)

.. step:: assert

   Since, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, and :g:`E <g1:E>` is :eq:`equal <g1:E = g1:/ A G /; g1:F = g1:/ C H />` to :g:`/ A G / <g1:/ A G />`, and :g:`F <g1:F>` to :g:`/ C H / <g1:/ C H />` → therefore, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`/ A G / <g1:/ A G />` to :g:`/ C H / <g1:/ C H />`.

.. step:: assert ∵ whole_whole_part <G.156>

   Since, as the whole :g:`/ A B / <g1:/ A B />` is to the whole :g:`/ C D / <g1:/ C D />`, so is the part :g:`/ A G / <g1:/ A G />` subtracted to the part :g:`/ C H / <g1:/ C H />` subtracted → the remainder :g:`/ G B / <g1:/ G B />` will also be to the remainder :g:`/ H D / <g1:/ H D />` as the whole :g:`/ A B / <g1:/ A B />` is to the whole :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is greater than :g:`/ C D / <g1:/ C D />`;

.. step:: assert

   Therefore :g:`/ G B / <g1:/ G B />` is also greater than :g:`/ H D / <g1:/ H D />`.

.. step:: assert

   And, since :g:`/ A G / <g1:/ A G />` is :eq:`equal <g1:/ A G / = g1:E; g1:/ C H / = g1:F>` to :g:`E <g1:E>`, and :g:`/ C H / <g1:/ C H />` to :g:`F <g1:F>`,

.. step:: assert

   Therefore :g:`/ A G / <g1:/ A G />`, :g:`F <g1:F>` are equal to :g:`/ C H / <g1:/ C H />`, :g:`E <g1:E>`.

.. step:: assert

   If, :g:`/ G B / <g1:/ G B />`, :g:`/ H D / <g1:/ H D />` being unequal, and :g:`/ G B / <g1:/ G B />` greater, :g:`/ A G / <g1:/ A G />`, :g:`F <g1:F>` be added to :g:`/ G B / <g1:/ G B />` and :g:`/ C H / <g1:/ C H />`, :g:`E <g1:E>` be added to :g:`/ H D / <g1:/ H D />`,

.. step:: conclude

   It follows that :g:`/ A B / <g1:/ A B />`, :g:`F <g1:F>` are greater than :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`.

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
     "G.156" [label="G.156", tooltip="G.156 (V.19): If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder is to the remainder as whole to whole.", fillcolor="#222244", URL="../G.156/index.html", target="_top"];
     "G.162" [label="G.162", tooltip="G.162 (V.25): If four magnitudes be proportional, the greatest and the least are greater than the remaining two.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.162" -> "G.156";
   }

.. toctree::
   :hidden:

   code
   heath
