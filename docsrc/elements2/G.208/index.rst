:order: 208
:number: 208
:canonical_id: G.208
:original_id: V.25
:title: G.208 magnitudes proportional greatest
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, segment, proportional, proportion, equality
:dependencies: G.180, G.201
:excerpt: If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

.. _G.208:
.. _V.25:

G.208 magnitudes proportional greatest
======================================

.. rubric:: `V.25 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/25/>`_

.. enunciation::

   If four magnitudes be :term:`proportional <G.180>`, the greatest and the least are greater than the remaining two.

.. signature:: theorem

   | :fn:`magnitudes_proportional_greatest <G.208>`\ (:g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`, :g:`F <g1:F>`)
   | **given** the four magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`, :g:`F <g1:F>` be proportional so that, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, let :g:`/ A B / <g1:/ A B />` be the greatest of them and :g:`F <g1:F>` the least
   | **prove** :g:`/ A B / <g1:/ A B />`, :g:`F <g1:F>` are greater than :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`

.. picture:: g1.svg
   :alt: Book V, Proposition 25, Line Segments

.. step:: given

   the four magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`, :g:`F <g1:F>` be proportional so that, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, let :g:`/ A B / <g1:/ A B />` be the greatest of them and :g:`F <g1:F>` the least

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`E <g1:E>`, and :g:`/ C H / <g1:/ C H />` :eq:`equal <g1:/ C H / = g1:F>` to :g:`F <g1:F>`) → :g:`/ A G / <g1:/ A G />` (:eq:`equal <g1:/ A G / = g1:E>`)

.. step:: assert

   Since, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, and :g:`E <g1:E>` is :eq:`equal <g1:E = g1:/ A G /; g1:F = g1:/ C H />` to :g:`/ A G / <g1:/ A G />`, and :g:`F <g1:F>` to :g:`/ C H / <g1:/ C H />` → therefore, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C D / <g1:/ C D />`, so is :g:`/ A G / <g1:/ A G />` to :g:`/ C H / <g1:/ C H />`.

.. step:: assert ∵ whole_whole_part <G.201>

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
     "G.190" [label="G.190", tooltip="G.190 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.190/index.html", target="_top"];
     "G.191" [label="G.191", tooltip="G.191 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.191/index.html", target="_top"];
     "G.192" [label="G.192", tooltip="G.192 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.192/index.html", target="_top"];
     "G.193" [label="G.193", tooltip="G.193 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.193/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.195" [label="G.195", tooltip="G.195 (V.16): If four magnitudes be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.195/index.html", target="_top"];
     "G.196" [label="G.196", tooltip="G.196 (V.def.14): Composition of a ratio means taking theantecedent together with the consequent as one in relation to the consequent by itself.", fillcolor="#224422", URL="../G.196/index.html", target="_top"];
     "G.197" [label="G.197", tooltip="G.197 (V.def.15): Separation of a ratio means taking the excess by which theantecedent exceeds the consequent in relation to the consequent by itself.", fillcolor="#224422", URL="../G.197/index.html", target="_top"];
     "G.198" [label="G.198", tooltip="G.198 (V.17): If magnitudes be proportional componendo, they is proportional separando.", fillcolor="#222244", URL="../G.198/index.html", target="_top"];
     "G.200" [label="G.200", tooltip="G.200 (V.def.16): Conversion of a ratio means taking theantecedent in relation to the excess by which the antecedent exceeds the consequent.", fillcolor="#224422", URL="../G.200/index.html", target="_top"];
     "G.201" [label="G.201", tooltip="G.201 (V.19): If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder is to the remainder as whole to whole.", fillcolor="#222244", URL="../G.201/index.html", target="_top"];
     "G.208" [label="G.208", tooltip="G.208 (V.25): If four magnitudes be proportional, the greatest and the least are greater than the remaining two.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.193" -> "G.170";
     "G.186" -> "G.171";
     "G.190" -> "G.171";
     "G.198" -> "G.171";
     "G.198" -> "G.172";
     "G.188" -> "G.173";
     "G.189" -> "G.173";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.189" -> "G.176";
     "G.190" -> "G.176";
     "G.191" -> "G.176";
     "G.192" -> "G.176";
     "G.193" -> "G.176";
     "G.195" -> "G.176";
     "G.183" -> "G.180";
     "G.190" -> "G.180";
     "G.195" -> "G.180";
     "G.198" -> "G.180";
     "G.208" -> "G.180";
     "G.182" -> "G.181";
     "G.190" -> "G.181";
     "G.194" -> "G.181";
     "G.196" -> "G.181";
     "G.197" -> "G.181";
     "G.200" -> "G.181";
     "G.183" -> "G.182";
     "G.188" -> "G.183";
     "G.193" -> "G.183";
     "G.186" -> "G.184";
     "G.188" -> "G.184";
     "G.186" -> "G.185";
     "G.188" -> "G.185";
     "G.191" -> "G.185";
     "G.188" -> "G.186";
     "G.192" -> "G.186";
     "G.192" -> "G.188";
     "G.195" -> "G.189";
     "G.201" -> "G.189";
     "G.193" -> "G.190";
     "G.192" -> "G.191";
     "G.195" -> "G.192";
     "G.195" -> "G.193";
     "G.195" -> "G.194";
     "G.201" -> "G.195";
     "G.198" -> "G.196";
     "G.198" -> "G.197";
     "G.201" -> "G.198";
     "G.201" -> "G.200";
     "G.208" -> "G.201";
   }

.. toctree::
   :hidden:

   code
   heath
