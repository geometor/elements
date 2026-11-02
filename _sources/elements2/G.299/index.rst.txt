:order: 299
:number: 299
:canonical_id: G.299
:original_id: VIII.4
:title: G.299 many ratios please
:volume: II
:book: VIII
:type: prop
:subtype: problem
:categories: problem, finding, number-theory, proportions
:category: problem, finding, number-theory, proportions
:tags: book-viii, point, ratio, number, proportional, part-aliquot, in-the-same-ratio, corresponding-magnitudes, proportion, continued-proportion, reductio-ad-absurdum
:dependencies: G.173, G.180, G.248, G.263, G.266, G.274, G.290, G.291
:excerpt: Given as many ratios as we please in least numbers, to find numbers in continued proportion which are the least in the given ratios.

.. _G.299:
.. _VIII.4:

G.299 many ratios please
========================

.. rubric:: `VIII.4 <https://geometor.github.io/euclid/heath/volume_II/book_viii/propositions/04/>`_

.. enunciation::

   Given as many :term:`ratios <G.173>` as we please in least :term:`numbers <G.248>`, to find numbers in :term:`continued proportion <G.180>` which are the least in the given ratios.

.. signature:: problem

   | :fn:`many_ratios_please <G.299>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`) → :g:`N <g2:N>`, :g:`O <g2:O>`
   | **given** the given ratios in least numbers be that of :g:`A <g1:A>` to :g:`B <g1:B>`, that of :g:`C <g1:C>` to :g:`D <g1:D>`, that of :g:`E <g1:E>` to :g:`F <g1:F>`
   | **construct** :g:`N <g2:N>`, :g:`O <g2:O>`, :g:`M <g2:M>`, :g:`P <g2:P>` are the least numbers continuously proportional in the ratios :g:`A <g2:A>` : :g:`B <g2:B>`, :g:`C <g2:C>` : :g:`D <g2:D>`, :g:`E <g2:E>` : :g:`F <g2:F>`

.. picture:: g1.svg
   :alt: Proposition 4 Diagram 1

.. picture:: g2.svg
   :alt: Proposition 4 Diagram 2

.. step:: given

   the given ratios in least numbers be that of :g:`A <g1:A>` to :g:`B <g1:B>`, that of :g:`C <g1:C>` to :g:`D <g1:D>`, that of :g:`E <g1:E>` to :g:`F <g1:F>`

.. step:: construct

   :fn:`numbers_find_least <G.290>`: Let :g:`G <g1:G>`, the least number measured by :g:`B <g1:B>`, :g:`C <g1:C>`, be taken.

.. step:: assert

   And, as many times as :g:`B <g1:B>` :term:`measures <G.169>` :g:`G <g1:G>`, so many times also let :g:`A <g1:A>` measure :g:`H <g1:H>`, and, as many times as :g:`C <g1:C>` measures :g:`G <g1:G>`, so many times also let :g:`D <g1:D>` measure :g:`K <g1:K>`.

.. step:: assert

   Now :g:`E <g1:E>` either measures or does not measure :g:`K <g1:K>`.

.. step:: assert

   First, let it measure it.

.. step:: assert

   And, as many times as :g:`E <g1:E>` measures :g:`K <g1:K>`, so many times let :g:`F <g1:F>` measure :g:`L <g1:L>` also.

.. step:: assert

   Since :g:`A <g1:A>` measures :g:`H <g1:H>` the same number of times that :g:`B <g1:B>` measures :g:`G <g1:G>`,

.. step:: assert ∵ numbers_proportional_multiple_def, numbers_proportional_proportional <G.263, G.266>

   Therefore, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`H <g1:H>` to :g:`G <g1:G>`.

.. step:: assert

   For the same reason also, as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`G <g1:G>` to :g:`K <g1:K>`, and further, as :g:`E <g1:E>` is to :g:`F <g1:F>`, so is :g:`K <g1:K>` to :g:`L <g1:L>`;

.. step:: assert

   Therefore :g:`H <g1:H>`, :g:`G <g1:G>`, :g:`K <g1:K>`, :g:`L <g1:L>` are continuously proportional in the ratio of :g:`A <g1:A>` to :g:`B <g1:B>`, in the ratio of :g:`C <g1:C>` to :g:`D <g1:D>`, and in the ratio of :g:`E <g1:E>` to :g:`F <g1:F>`.

.. step:: assert

   I say next that they are also the least that have this property.

.. step:: assert

   If :g:`H <g1:H>`, :g:`G <g1:G>`, :g:`K <g1:K>`, :g:`L <g1:L>` are not the least numbers continuously proportional in the ratios of :g:`A <g1:A>` to :g:`B <g1:B>`, of :g:`C <g1:C>` to :g:`D <g1:D>`, and of :g:`E <g1:E>` to :g:`F <g1:F>`, let them be :g:`N <g1:N>`, :g:`O <g1:O>`, :g:`M <g1:M>`, :g:`P <g1:P>`.

.. step:: assert

   Then since, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`N <g1:N>` to :g:`O <g1:O>`, while :g:`A <g1:A>`, :g:`B <g1:B>` are least, and the least numbers measure those which have the :term:`same ratio <G.176>` the same number of times, the greater the greater and the less the less, that is, the :term:`antecedent <G.181>` the antecedent and the consequent the consequent;

.. step:: assert ∵ least_numbers_ratio <G.274>

   Therefore :g:`B <g1:B>` measures :g:`O <g1:O>`.

.. step:: assert

   For the same reason :g:`C <g1:C>` also measures :g:`O <g1:O>`;

.. step:: assert

   Therefore :g:`B <g1:B>`, :g:`C <g1:C>` measure :g:`O <g1:O>`;

.. step:: assert ∵ numbers_measure_number <G.291>

   Therefore the least number measured by :g:`B <g1:B>`, :g:`C <g1:C>` will also measure :g:`O <g1:O>`.

.. step:: assert

   :g:`G <g1:G>` is the least number measured by :g:`B <g1:B>`, :g:`C <g1:C>`;

.. step:: assert

   Therefore :g:`G <g1:G>` measures :g:`O <g1:O>`, the greater the less : which is impossible.

.. step:: assert

   Therefore there will be no numbers less than :g:`H <g1:H>`, :g:`G <g1:G>`, :g:`K <g1:K>`, :g:`L <g1:L>` which are continuously in the ratio of :g:`A <g1:A>` to :g:`B <g1:B>`, of :g:`C <g1:C>` to :g:`D <g1:D>`, and of :g:`E <g1:E>` to :g:`F <g1:F>`.

.. step:: assert

   Next, let :g:`E <g2:E>` not measure :g:`K <g2:K>`.

.. step:: construct

   Let :g:`M <g2:M>`, the least number measured by :g:`E <g2:E>`, :g:`K <g2:K>`, be taken.

.. step:: assert

   And, as many times as :g:`K <g2:K>` measures :g:`M <g2:M>`, so many times let :g:`H <g2:H>`, :g:`G <g2:G>` measure :g:`N <g2:N>`, :g:`O <g2:O>` respectively, and, as many times as :g:`E <g2:E>` measures :g:`M <g2:M>`, so many times let :g:`F <g2:F>` measure :g:`P <g2:P>` also.

.. step:: assert

   Since :g:`H <g2:H>` measures :g:`N <g2:N>` the same number of times that :g:`G <g2:G>` measures :g:`O <g2:O>`,

.. step:: assert ∵ numbers_proportional_proportional, numbers_proportional_multiple_def <G.266, G.263>

   Therefore, as :g:`H <g2:H>` is to :g:`G <g2:G>`, so is :g:`N <g2:N>` to :g:`O <g2:O>`.

.. step:: assert

   But, as :g:`H <g2:H>` is to :g:`G <g2:G>`, so is :g:`A <g2:A>` to :g:`B <g2:B>`;

.. step:: assert

   Therefore also, as :g:`A <g2:A>` is to :g:`B <g2:B>`, so is :g:`N <g2:N>` to :g:`O <g2:O>`.

.. step:: assert

   For the same reason also, as :g:`C <g2:C>` is to :g:`D <g2:D>`, so is :g:`O <g2:O>` to :g:`M <g2:M>`.

.. step:: assert

   Since :g:`E <g2:E>` measures :g:`M <g2:M>` the same number of times that :g:`F <g2:F>` measures :g:`P <g2:P>`,

.. step:: assert ∵ numbers_proportional_proportional, numbers_proportional_multiple_def <G.266, G.263>

   Therefore, as :g:`E <g2:E>` is to :g:`F <g2:F>`, so is :g:`M <g2:M>` to :g:`P <g2:P>`;

.. step:: assert

   Therefore :g:`N <g2:N>`, :g:`O <g2:O>`, :g:`M <g2:M>`, :g:`P <g2:P>` are continuously proportional in the ratios of :g:`A <g2:A>` to :g:`B <g2:B>`, of :g:`C <g2:C>` to :g:`D <g2:D>`, and of :g:`E <g2:E>` to :g:`F <g2:F>`.

.. step:: assert

   I say next that they are also the least that are in the ratios :g:`A <g2:A>` : :g:`B <g2:B>`, :g:`C <g2:C>` : :g:`D <g2:D>`, :g:`E <g2:E>` : :g:`F <g2:F>`.

.. step:: assert

   If not, there will be some numbers less than :g:`N <g2:N>`, :g:`O <g2:O>`, :g:`M <g2:M>`, :g:`P <g2:P>` continuously proportional in the ratios :g:`A <g2:A>` : :g:`B <g2:B>`, :g:`C <g2:C>` : :g:`D <g2:D>`, :g:`E <g2:E>` : :g:`F <g2:F>`.

.. step:: assert

   Let them be :g:`Q <g2:Q>`, :g:`R <g2:R>`, :g:`S <g2:S>`, :g:`T <g2:T>`.

.. step:: assert ∵ least_numbers_ratio <G.274>

   Now since, as :g:`Q <g2:Q>` is to :g:`R <g2:R>`, so is :g:`A <g2:A>` to :g:`B <g2:B>`, while :g:`A <g2:A>`, :g:`B <g2:B>` are least, and the least numbers measure those which have the same ratio with them the same number of times, the antecedent the antecedent and the consequent the consequent.

.. step:: assert

   Therefore :g:`B <g2:B>` measures :g:`R <g2:R>`.

.. step:: assert

   For the same reason :g:`C <g2:C>` also measures :g:`R <g2:R>`;

.. step:: assert

   Therefore :g:`B <g2:B>`, :g:`C <g2:C>` measure :g:`R <g2:R>`.

.. step:: assert ∵ numbers_measure_number <G.291>

   Therefore the least number measured by :g:`B <g2:B>`, :g:`C <g2:C>` will also measure :g:`R <g2:R>`.

.. step:: assert

   :g:`G <g2:G>` is the least number measured by :g:`B <g2:B>`, :g:`C <g2:C>`;

.. step:: assert

   Therefore :g:`G <g2:G>` measures :g:`R <g2:R>`.

.. step:: assert ∵ numbers_proportional_proportional <G.266>

   And, as :g:`G <g2:G>` is to :g:`R <g2:R>`, so is :g:`K <g2:K>` to :g:`S <g2:S>` :

.. step:: assert

   Therefore :g:`K <g2:K>` also measures :g:`S <g2:S>`.

.. step:: assert

   :g:`E <g2:E>` also measures :g:`S <g2:S>`;

.. step:: assert

   Therefore :g:`E <g2:E>`, :g:`K <g2:K>` measure :g:`S <g2:S>`.

.. step:: assert ∵ numbers_measure_number <G.291>

   Therefore the least number measured by :g:`E <g2:E>`, :g:`K <g2:K>` will also measure :g:`S <g2:S>`.

.. step:: assert

   :g:`M <g2:M>` is the least number measured by :g:`E <g2:E>`, :g:`K <g2:K>`;

.. step:: assert

   Therefore :g:`M <g2:M>` measures :g:`S <g2:S>`, the greater the less : which is impossible.

.. step:: assert

   Therefore there will not be any numbers less than :g:`N <g2:N>`, :g:`O <g2:O>`, :g:`M <g2:M>`, :g:`P <g2:P>` continuously proportional in the ratios of :g:`A <g2:A>` to :g:`B <g2:B>`, of :g:`C <g2:C>` to :g:`D <g2:D>`, and of :g:`E <g2:E>` to :g:`F <g2:F>`;

.. step:: conclude

   Therefore :g:`N <g2:N>`, :g:`O <g2:O>`, :g:`M <g2:M>`, :g:`P <g2:P>` are the least numbers continuously proportional in the ratios :g:`A <g2:A>` : :g:`B <g2:B>`, :g:`C <g2:C>` : :g:`D <g2:D>`, :g:`E <g2:E>` : :g:`F <g2:F>`.

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
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.13): Inverse ratio means taking theconsequent as antecedent in relation to the antecedent as consequent.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (V.def.7): When, of theequimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then th...", fillcolor="#224422", URL="../G.185/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.187" [label="G.187", tooltip="G.187 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.187/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.249" [label="G.249", tooltip="G.249 (VII.def.12): Numbers prime to one another are those which aremeasured by anunit alone as a common measure.", fillcolor="#224422", URL="../G.249/index.html", target="_top"];
     "G.250" [label="G.250", tooltip="G.250 (VII.1): Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is...", fillcolor="#222244", URL="../G.250/index.html", target="_top"];
     "G.251" [label="G.251", tooltip="G.251 (VII.2): Given two numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.251/index.html", target="_top"];
     "G.252" [label="G.252", tooltip="G.252 (VII.3): Given three numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.252/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.255" [label="G.255", tooltip="G.255 (VII.4): Any number is either a part or parts of any number, the less of the greater.", fillcolor="#222244", URL="../G.255/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.258" [label="G.258", tooltip="G.258 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.258/index.html", target="_top"];
     "G.261" [label="G.261", tooltip="G.261 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.261/index.html", target="_top"];
     "G.262" [label="G.262", tooltip="G.262 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.262/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VII.def.20): Numbers areproportional when the first is thesame multiple, or thesame part, or thesame parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.263/index.html", target="_top"];
     "G.265" [label="G.265", tooltip="G.265 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.265/index.html", target="_top"];
     "G.266" [label="G.266", tooltip="G.266 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.266/index.html", target="_top"];
     "G.268" [label="G.268", tooltip="G.268 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.268/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.270" [label="G.270", tooltip="G.270 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced are equal.", fillcolor="#222244", URL="../G.270/index.html", target="_top"];
     "G.271" [label="G.271", tooltip="G.271 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.271/index.html", target="_top"];
     "G.272" [label="G.272", tooltip="G.272 (VII.18): If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", fillcolor="#222244", URL="../G.272/index.html", target="_top"];
     "G.273" [label="G.273", tooltip="G.273 (VII.19): If four numbers be proportional, the number produced from the first and fourth will equals the number produced from the second and third; and, if the number produced from the first...", fillcolor="#222244", URL="../G.273/index.html", target="_top"];
     "G.274" [label="G.274", tooltip="G.274 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.274/index.html", target="_top"];
     "G.275" [label="G.275", tooltip="G.275 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.275/index.html", target="_top"];
     "G.283" [label="G.283", tooltip="G.283 (VII.def.11): Aprime number is that which ismeasured by anunit alone.", fillcolor="#224422", URL="../G.283/index.html", target="_top"];
     "G.289" [label="G.289", tooltip="G.289 (VII.33): Given as many numbers as we please, to find the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.289/index.html", target="_top"];
     "G.290" [label="G.290", tooltip="G.290 (VII.34): Given two numbers, to find the least number which they measure.", fillcolor="#222244", URL="../G.290/index.html", target="_top"];
     "G.291" [label="G.291", tooltip="G.291 (VII.35): If two numbers measure any number, the least number measured by them will also measure the same.", fillcolor="#222244", URL="../G.291/index.html", target="_top"];
     "G.299" [label="G.299", tooltip="G.299 (VIII.4): Given as many ratios as we please in least numbers, to find numbers in continued proportion which are the least in the given ratios.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.3" -> "G.2";
     "G.8" -> "G.3";
     "G.9" -> "G.8";
     "G.187" -> "G.9";
     "G.170" -> "G.169";
     "G.249" -> "G.169";
     "G.250" -> "G.169";
     "G.251" -> "G.169";
     "G.252" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.268" -> "G.169";
     "G.274" -> "G.169";
     "G.283" -> "G.169";
     "G.290" -> "G.169";
     "G.291" -> "G.169";
     "G.171" -> "G.170";
     "G.176" -> "G.170";
     "G.185" -> "G.170";
     "G.257" -> "G.170";
     "G.186" -> "G.171";
     "G.289" -> "G.173";
     "G.299" -> "G.173";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.187" -> "G.176";
     "G.271" -> "G.176";
     "G.272" -> "G.176";
     "G.274" -> "G.176";
     "G.275" -> "G.176";
     "G.289" -> "G.176";
     "G.183" -> "G.180";
     "G.266" -> "G.180";
     "G.273" -> "G.180";
     "G.299" -> "G.180";
     "G.182" -> "G.181";
     "G.194" -> "G.181";
     "G.265" -> "G.181";
     "G.183" -> "G.182";
     "G.273" -> "G.183";
     "G.186" -> "G.184";
     "G.186" -> "G.185";
     "G.187" -> "G.186";
     "G.273" -> "G.187";
     "G.261" -> "G.194";
     "G.262" -> "G.194";
     "G.266" -> "G.194";
     "G.268" -> "G.194";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.250" -> "G.247";
     "G.268" -> "G.247";
     "G.269" -> "G.247";
     "G.283" -> "G.247";
     "G.250" -> "G.248";
     "G.251" -> "G.248";
     "G.252" -> "G.248";
     "G.253" -> "G.248";
     "G.255" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.258" -> "G.248";
     "G.261" -> "G.248";
     "G.262" -> "G.248";
     "G.265" -> "G.248";
     "G.266" -> "G.248";
     "G.268" -> "G.248";
     "G.269" -> "G.248";
     "G.270" -> "G.248";
     "G.271" -> "G.248";
     "G.272" -> "G.248";
     "G.273" -> "G.248";
     "G.274" -> "G.248";
     "G.275" -> "G.248";
     "G.289" -> "G.248";
     "G.290" -> "G.248";
     "G.291" -> "G.248";
     "G.299" -> "G.248";
     "G.250" -> "G.249";
     "G.251" -> "G.249";
     "G.252" -> "G.249";
     "G.275" -> "G.249";
     "G.251" -> "G.250";
     "G.252" -> "G.251";
     "G.255" -> "G.251";
     "G.289" -> "G.252";
     "G.255" -> "G.253";
     "G.257" -> "G.253";
     "G.261" -> "G.253";
     "G.262" -> "G.253";
     "G.263" -> "G.253";
     "G.255" -> "G.254";
     "G.258" -> "G.254";
     "G.261" -> "G.254";
     "G.262" -> "G.254";
     "G.263" -> "G.254";
     "G.274" -> "G.255";
     "G.257" -> "G.256";
     "G.263" -> "G.256";
     "G.258" -> "G.257";
     "G.261" -> "G.257";
     "G.262" -> "G.257";
     "G.265" -> "G.257";
     "G.261" -> "G.258";
     "G.262" -> "G.258";
     "G.265" -> "G.258";
     "G.262" -> "G.261";
     "G.266" -> "G.262";
     "G.265" -> "G.263";
     "G.266" -> "G.263";
     "G.271" -> "G.263";
     "G.274" -> "G.263";
     "G.289" -> "G.263";
     "G.299" -> "G.263";
     "G.268" -> "G.265";
     "G.274" -> "G.265";
     "G.271" -> "G.266";
     "G.274" -> "G.266";
     "G.299" -> "G.266";
     "G.270" -> "G.268";
     "G.270" -> "G.269";
     "G.271" -> "G.269";
     "G.272" -> "G.269";
     "G.289" -> "G.269";
     "G.290" -> "G.269";
     "G.272" -> "G.270";
     "G.275" -> "G.270";
     "G.289" -> "G.270";
     "G.290" -> "G.270";
     "G.272" -> "G.271";
     "G.273" -> "G.271";
     "G.290" -> "G.271";
     "G.273" -> "G.272";
     "G.289" -> "G.273";
     "G.290" -> "G.273";
     "G.275" -> "G.274";
     "G.290" -> "G.274";
     "G.299" -> "G.274";
     "G.289" -> "G.275";
     "G.290" -> "G.275";
     "G.290" -> "G.283";
     "G.290" -> "G.289";
     "G.299" -> "G.290";
     "G.299" -> "G.291";
   }

Required for
------------

:ref:`G.301 <G.301>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
