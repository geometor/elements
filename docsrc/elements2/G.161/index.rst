:order: 161
:number: 161
:canonical_id: G.161
:original_id: V.24
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, segment, ex-aequali, separando, componendo, ratio
:dependencies: G.155, G.159
:excerpt: If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth added together will have to the second the same ratio as the third and sixth have to the fourth.

.. _G.161:
.. _V.24:

G.161
=====

.. rubric:: `V.24 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/24/>`_

.. enunciation::

   If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth added together will have to the second the same ratio as the third and sixth have to the fourth.

.. picture:: g1.svg
   :alt: Book V, Proposition 24, Line Segments

.. step:: given

   a first magnitude :g:`/ A B / <g1:/ A B />` have to a second :g:`C <g1:C>` the same ratio as a third :g:`/ D E / <g1:/ D E />` has to a fourth :g:`F <g1:F>`

.. step:: assert

   And let also a fifth :g:`/ B G / <g1:/ B G />` have to the second :g:`C <g1:C>` the same ratio as a sixth :g:`/ E H / <g1:/ E H />` has to the fourth :g:`F <g1:F>`

.. step:: assert

   For since, as :g:`/ B G / <g1:/ B G />` is to :g:`C <g1:C>`, so is :g:`/ E H / <g1:/ E H />` to :g:`F <g1:F>`,

.. step:: assert

   Inversely, as :g:`C <g1:C>` is to :g:`/ B G / <g1:/ B G />`, so is :g:`F <g1:F>` to :g:`/ E H / <g1:/ E H />`.

.. step:: assert

   Since, then, as :g:`/ A B / <g1:/ A B />` is to :g:`C <g1:C>`, so is :g:`/ D E / <g1:/ D E />` to :g:`F <g1:F>`, and, as :g:`C <g1:C>` is to :g:`/ B G / <g1:/ B G />`, so is :g:`F <g1:F>` to :g:`/ E H / <g1:/ E H />`,

.. step:: assert [G.159] <G.159>

   Therefore, :term:`*ex aequali* <ex-aequali>`, as :g:`/ A B / <g1:/ A B />` is to :g:`/ B G / <g1:/ B G />`, so is :g:`/ D E / <g1:/ D E />` to :g:`/ E H / <g1:/ E H />`.

.. step:: assert [G.155] <G.155>

   And, since the magnitudes are proportional :term:`*separando* <separando>`, they will also be proportional :term:`*componendo* <componendo>`

.. step:: assert

   Therefore, as :g:`/ A G / <g1:/ A G />` is to :g:`/ B G / <g1:/ B G />`, so is :g:`/ D H / <g1:/ D H />` to :g:`/ E H / <g1:/ E H />`.

.. step:: assert

   Also, as :g:`/ B G / <g1:/ B G />` is to :g:`C <g1:C>`, so is :g:`/ E H / <g1:/ E H />` to :g:`F <g1:F>`

.. step:: conclude [G.159] <G.159>

   Therefore, :term:`*ex aequali* <ex-aequali>`, as :g:`/ A G / <g1:/ A G />` is to :g:`C <g1:C>`, so is :g:`/ D H / <g1:/ D H />` to :g:`F <g1:F>`.

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
     "G.137" [label="G.137", tooltip="G.137 (V.3): If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then alsoex aequali the magnitudes taken is...", fillcolor="#222244", URL="../G.137/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (V.4): If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples wh...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.150/index.html", target="_top"];
     "G.151" [label="G.151", tooltip="G.151 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.151/index.html", target="_top"];
     "G.154" [label="G.154", tooltip="G.154 (V.17): If magnitudes be proportional componendo, they is proportional separando.", fillcolor="#222244", URL="../G.154/index.html", target="_top"];
     "G.155" [label="G.155", tooltip="G.155 (V.18): If magnitudes be proportional separando, they is proportional componendo.", fillcolor="#222244", URL="../G.155/index.html", target="_top"];
     "G.157" [label="G.157", tooltip="G.157 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and ifex aequali the first be greater than the third, the fourth...", fillcolor="#222244", URL="../G.157/index.html", target="_top"];
     "G.159" [label="G.159", tooltip="G.159 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.159/index.html", target="_top"];
     "G.161" [label="G.161", tooltip="G.161 (V.24): If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth ad...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.154" -> "G.135";
     "G.137" -> "G.136";
     "G.154" -> "G.136";
     "G.139" -> "G.137";
     "G.139" -> "G.138";
     "G.142" -> "G.138";
     "G.150" -> "G.138";
     "G.159" -> "G.138";
     "G.159" -> "G.139";
     "G.147" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.147" -> "G.145";
     "G.151" -> "G.145";
     "G.157" -> "G.145";
     "G.151" -> "G.147";
     "G.157" -> "G.147";
     "G.155" -> "G.148";
     "G.151" -> "G.150";
     "G.157" -> "G.150";
     "G.155" -> "G.151";
     "G.155" -> "G.154";
     "G.161" -> "G.155";
     "G.159" -> "G.157";
     "G.161" -> "G.159";
   }

.. toctree::
   :hidden:

   code
   heath
