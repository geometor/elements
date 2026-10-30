:order: 160
:number: 160
:canonical_id: G.160
:original_id: V.23
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, ex-aequali, ratio, proportion, equality
:dependencies: G.148, G.152, G.153, G.158
:excerpt: If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they is in the same ratio ex aequali.

.. _G.160:
.. _V.23:

G.160
=====

.. rubric:: `V.23 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/23/>`_

.. enunciation::

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they is in the same ratio ex aequali.

.. signature:: theorem

   | :fn:`there_magnitudes_others_v_23 <G.160>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`)
   | **given** there be three magnitudes :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, others equal to them in multitude, which, taken two and two together, are in the same proportion, namely :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>`
   | **prove** as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`

.. picture:: g1.svg
   :alt: Book V, Proposition 23, Line Segments

.. step:: given

   there be three magnitudes :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, others equal to them in multitude, which, taken two and two together, are in the same proportion, namely :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>`

.. step:: assert

   And let the proportion of them be perturbed, so that,

.. step:: assert

   As :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`,

.. step:: assert

   And, as :g:`B <g1:B>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`;

.. step:: assert

   I say that, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`.

.. step:: construct

   Of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`D <g1:D>` let equimultiples :g:`G <g1:G>`, :g:`H <g1:H>`, :g:`K <g1:K>` be taken, and of :g:`C <g1:C>`, :g:`E <g1:E>`, :g:`F <g1:F>` other, chance, equimultiples :g:`L <g1:L>`, :g:`M <g1:M>`, :g:`N <g1:N>`.

.. step:: assert ∵ parts_ratio_multiples <G.152>

   Since :g:`G <g1:G>`, :g:`H <g1:H>` are equimultiples of :g:`A <g1:A>`, :g:`B <g1:B>`, and parts have the same ratio as the same multiples of them.

.. step:: assert

   Therefore, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`G <g1:G>` to :g:`H <g1:H>`.

.. step:: assert

   The same reason also,

.. step:: assert

   As :g:`E <g1:E>` is to :g:`F <g1:F>`, so is :g:`M <g1:M>` to :g:`N <g1:N>`.

.. step:: assert

   And, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`

.. step:: assert ∵ ratios_ratio <G.148>

   Therefore also, as :g:`G <g1:G>` is to :g:`H <g1:H>`, so is :g:`M <g1:M>` to :g:`N <g1:N>`.

.. step:: assert

   Next, since, as :g:`B <g1:B>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`,

.. step:: assert ∵ magnitudes_proportional_proportional <G.153>

   Alternately, also, as :g:`B <g1:B>` is to :g:`D <g1:D>`, so is :g:`C <g1:C>` to :g:`E <g1:E>`.

.. step:: assert

   And, since :g:`H <g1:H>`, :g:`K <g1:K>` are equimultiples of :g:`B <g1:B>`, :g:`D <g1:D>`, and parts have the same ratio as their equimultiples,

.. step:: assert ∵ parts_ratio_multiples <G.152>

   Therefore, as :g:`B <g1:B>` is to :g:`D <g1:D>`, so is :g:`H <g1:H>` to :g:`K <g1:K>`.

.. step:: assert

   But, as :g:`B <g1:B>` is to :g:`D <g1:D>`, so is :g:`C <g1:C>` to :g:`E <g1:E>`

.. step:: assert ∵ ratios_ratio <G.148>

   Therefore also, as :g:`H <g1:H>` is to :g:`K <g1:K>`, so is :g:`C <g1:C>` to :g:`E <g1:E>`.

.. step:: assert ∵ parts_ratio_multiples <G.152>

   Since :g:`L <g1:L>`, :g:`M <g1:M>` are equimultiples of :g:`C <g1:C>`, :g:`E <g1:E>` → therefore, as :g:`C <g1:C>` is to :g:`E <g1:E>`, so is :g:`L <g1:L>` to :g:`M <g1:M>`.

.. step:: assert

   But, as :g:`C <g1:C>` is to :g:`E <g1:E>`, so is :g:`H <g1:H>` to :g:`K <g1:K>`

.. step:: assert ∵ ratios_ratio, magnitudes_proportional_proportional <G.148, G.153>

   Therefore also, as :g:`H <g1:H>` is to :g:`K <g1:K>`, so is :g:`L <g1:L>` to :g:`M <g1:M>`, and, alternately, as :g:`H <g1:H>` is to :g:`L <g1:L>`, so is :g:`K <g1:K>` to :g:`M <g1:M>`.

.. step:: assert

   It was also proved that,

.. step:: assert

   As :g:`G <g1:G>` is to :g:`H <g1:H>`, so is :g:`M <g1:M>` to :g:`N <g1:N>`.

.. step:: assert

   Since, then, there are three magnitudes :g:`G <g1:G>`, :g:`H <g1:H>`, :g:`L <g1:L>`, and others equal to them in multitude :g:`K <g1:K>`, :g:`M <g1:M>`, :g:`N <g1:N>`, which taken two and two together are in the same ratio, and the proportion of them is perturbed,

.. step:: assert ∵ there_magnitudes_others_v_21 <G.158>

   Therefore, :term:`*ex aequali* <ex-aequali>`, if :g:`G <g1:G>` is in excess of :g:`L <g1:L>`, :g:`K <g1:K>` is also in excess of :g:`N <g1:N>`; if :eq:`equal <g1:G = g1:L>`, :eq:`equal <g1:K = g1:N>`; and if less, less.

.. step:: assert

   :g:`G <g1:G>`, :g:`K <g1:K>` are equimultiples of :g:`A <g1:A>`, :g:`D <g1:D>`, and :g:`L <g1:L>`, :g:`N <g1:N>` of :g:`C <g1:C>`, :g:`F <g1:F>`.

.. step:: conclude

   Therefore, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
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
     "G.158" [label="G.158", tooltip="G.158 (V.21): If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex ae...", fillcolor="#222244", URL="../G.158/index.html", target="_top"];
     "G.160" [label="G.160", tooltip="G.160 (V.23): If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they is in the...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.149" -> "G.135";
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
     "G.158" -> "G.145";
     "G.151" -> "G.147";
     "G.158" -> "G.147";
     "G.153" -> "G.148";
     "G.160" -> "G.148";
     "G.152" -> "G.149";
     "G.151" -> "G.150";
     "G.158" -> "G.150";
     "G.153" -> "G.151";
     "G.153" -> "G.152";
     "G.160" -> "G.152";
     "G.160" -> "G.153";
     "G.160" -> "G.158";
   }

.. toctree::
   :hidden:

   code
   heath
