:order: 321
:number: 321
:canonical_id: G.321
:original_id: VIII.19
:title: G.321 similar solid numbers
:volume: II
:book: VIII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory, proportions
:category: theorem, proof, number-theory, proportions
:tags: book-viii, point, similar-plane-and-solid-numbers, proportional, number, solid-number, ratio, multiply, in-the-same-ratio, alternando, proportion, similar, plane
:dependencies: G.173, G.180, G.194, G.248, G.266, G.269, G.271, G.272, G.310, G.318, G.319, G.320
:excerpt: Between two similar solid numbers there fall two mean proportional numbers; and the solid number has to the similar solid number the ratio triplicate of that which the corresponding side has to the corresponding side.

.. _G.321:
.. _VIII.19:

G.321 similar solid numbers
===========================

.. rubric:: `VIII.19 <https://geometor.github.io/euclid/heath/volume_II/book_viii/propositions/19/>`_

.. enunciation::

   Between two :term:`similar solid numbers <G.318>` there fall two mean :term:`proportional <G.180>` :term:`numbers <G.248>`; and the :term:`solid number <G.320>` has to the similar solid number the :term:`ratio <G.173>` triplicate of that which the corresponding side has to the corresponding side.

.. signature:: theorem

   | :fn:`similar_solid_numbers <G.321>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`)
   | **given** :g:`A <g1:A>`, :g:`B <g1:B>` be two similar solid numbers, let :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>` be the sides of :g:`A <g1:A>`, :g:`F <g1:F>`, :g:`G <g1:G>`, :g:`H <g1:H>` of :g:`B <g1:B>`
   | **prove** between :g:`A <g1:A>`, :g:`B <g1:B>` there fall two mean proportional numbers, and :g:`A <g1:A>` has to :g:`B <g1:B>` the ratio triplicate of that which :g:`C <g1:C>` has to :g:`F <g1:F>`, :g:`D <g1:D>` to :g:`G <g1:G>`, and also :g:`E <g1:E>` to :g:`H <g1:H>`; :g:`A <g1:A>` also has to :g:`B <g1:B>` the ratio triplicate of that which the corresponding side has to the corresponding side, that is, of the ratio which the number :g:`C <g1:C>` has to :g:`F <g1:F>`, or :g:`D <g1:D>` to :g:`G <g1:G>`, and also :g:`E <g1:E>` to :g:`H <g1:H>`

.. picture:: g1.svg
   :alt: Book VIII, Proposition 19

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>` be two similar solid numbers, let :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>` be the sides of :g:`A <g1:A>`, :g:`F <g1:F>`, :g:`G <g1:G>`, :g:`H <g1:H>` of :g:`B <g1:B>`

.. step:: assert ∵ similar_plane_solid_def <G.318>

   similar solid numbers are those which have their sides proportional

.. step:: assert

   as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`F <g1:F>` to :g:`G <g1:G>`, and, as :g:`D <g1:D>` is to :g:`E <g1:E>`, so is :g:`G <g1:G>` to :g:`H <g1:H>`

.. step:: assert

   Let :g:`C <g1:C>` by :term:`multiplying <G.269>` :g:`D <g1:D>` make :g:`K <g1:K>`, and let :g:`F <g1:F>` by multiplying :g:`G <g1:G>` make :g:`L <g1:L>`

.. step:: assert ∵ similar_plane_solid_def <G.318>

   :g:`C <g1:C>`, :g:`D <g1:D>` are in the same ratio with :g:`F <g1:F>`, :g:`G <g1:G>`, and :g:`K <g1:K>` is the product of :g:`C <g1:C>`, :g:`D <g1:D>`, and :g:`L <g1:L>` the product of :g:`F <g1:F>`, :g:`G <g1:G>`, :g:`K <g1:K>`, :g:`L <g1:L>` are similar plane numbers

.. step:: assert ∵ similar_plane_numbers <G.319>

   between :g:`K <g1:K>`, :g:`L <g1:L>` there is one mean proportional number

.. step:: assert

   Let it be :g:`M <g1:M>`

.. step:: assert ∵ similar_plane_numbers <G.319>

   :g:`M <g1:M>` is the product of :g:`D <g1:D>`, :g:`F <g1:F>`, as was proved in the theorem preceding this

.. step:: assert

   :g:`D <g1:D>` by multiplying :g:`C <g1:C>` has made :g:`K <g1:K>`, and by multiplying :g:`F <g1:F>` has made :g:`M <g1:M>`,

.. step:: assert ∵ number_multiplying_numbers <G.271>

   as :g:`C <g1:C>` is to :g:`F <g1:F>`, so is :g:`K <g1:K>` to :g:`M <g1:M>`

.. step:: assert

   But, as :g:`K <g1:K>` is to :g:`M <g1:M>`, so is :g:`M <g1:M>` to :g:`L <g1:L>`

.. step:: assert

   :g:`K <g1:K>`, :g:`M <g1:M>`, :g:`L <g1:L>` are continuously proportional in the ratio of :g:`C <g1:C>` to :g:`F <g1:F>`

.. step:: assert

   Since, as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`F <g1:F>` to :g:`G <g1:G>`,

.. step:: assert ∵ numbers_proportional_proportional <G.266>

   :term:`Alternately <G.194>` therefore, as :g:`C <g1:C>` is to :g:`F <g1:F>`, so is :g:`D <g1:D>` to :g:`G <g1:G>`

.. step:: assert

   For the same reason also,

.. step:: assert

   As :g:`D <g1:D>` is to :g:`G <g1:G>`, so is :g:`E <g1:E>` to :g:`H <g1:H>`

.. step:: assert

   :g:`K <g1:K>`, :g:`M <g1:M>`, :g:`L <g1:L>` are continuously proportional in the ratio of :g:`C <g1:C>` to :g:`F <g1:F>`, in the ratio of :g:`D <g1:D>` to :g:`G <g1:G>`, and also in the ratio of :g:`E <g1:E>` to :g:`H <g1:H>`

.. step:: assert

   Next, let :g:`E <g1:E>`, :g:`H <g1:H>` by multiplying :g:`M <g1:M>` make :g:`N <g1:N>`, :g:`O <g1:O>`

.. step:: assert

   :g:`A <g1:A>` is a solid number, and :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>` are its sides,

.. step:: assert

   :g:`E <g1:E>` by multiplying the product of :g:`C <g1:C>`, :g:`D <g1:D>` has made :g:`A <g1:A>`

.. step:: assert

   The product of :g:`C <g1:C>`, :g:`D <g1:D>` is :g:`K <g1:K>`

.. step:: assert

   :g:`E <g1:E>` by multiplying :g:`K <g1:K>` has made :g:`A <g1:A>`

.. step:: assert

   For the same reason also

.. step:: assert

   :g:`H <g1:H>` by multiplying :g:`L <g1:L>` has made :g:`B <g1:B>`

.. step:: assert

   :g:`E <g1:E>` by multiplying :g:`K <g1:K>` has made :g:`A <g1:A>`, and further also by multiplying :g:`M <g1:M>` has made :g:`N <g1:N>`,

.. step:: assert ∵ number_multiplying_numbers <G.271>

   as :g:`K <g1:K>` is to :g:`M <g1:M>`, so is :g:`A <g1:A>` to :g:`N <g1:N>`

.. step:: assert

   But, as :g:`K <g1:K>` is to :g:`M <g1:M>`, so is :g:`C <g1:C>` to :g:`F <g1:F>`, :g:`D <g1:D>` to :g:`G <g1:G>`, and also :g:`E <g1:E>` to :g:`H <g1:H>`

.. step:: assert

   also, as :g:`C <g1:C>` is to :g:`F <g1:F>`, :g:`D <g1:D>` to :g:`G <g1:G>`, and :g:`E <g1:E>` to :g:`H <g1:H>`, so is :g:`A <g1:A>` to :g:`N <g1:N>`

.. step:: assert

   :g:`E <g1:E>`, :g:`H <g1:H>` by multiplying :g:`M <g1:M>` have made :g:`N <g1:N>`, :g:`O <g1:O>`,

.. step:: assert ∵ numbers_multiplying_number <G.272>

   as :g:`E <g1:E>` is to :g:`H <g1:H>`, so is :g:`N <g1:N>` to :g:`O <g1:O>`

.. step:: assert

   But, as :g:`E <g1:E>` is to :g:`H <g1:H>`, so is :g:`C <g1:C>` to :g:`F <g1:F>` and :g:`D <g1:D>` to :g:`G <g1:G>`

.. step:: assert

   also, as :g:`C <g1:C>` is to :g:`F <g1:F>`, :g:`D <g1:D>` to :g:`G <g1:G>`, and :g:`E <g1:E>` to :g:`H <g1:H>`, so is :g:`A <g1:A>` to :g:`N <g1:N>` and :g:`N <g1:N>` to :g:`O <g1:O>`

.. step:: assert

   :g:`H <g1:H>` by multiplying :g:`M <g1:M>` has made :g:`O <g1:O>`, and further also by multiplying :g:`L <g1:L>` has made :g:`B <g1:B>`,

.. step:: assert ∵ number_multiplying_numbers <G.271>

   as :g:`M <g1:M>` is to :g:`L <g1:L>`, so is :g:`O <g1:O>` to :g:`B <g1:B>`

.. step:: assert

   But, as :g:`M <g1:M>` is to :g:`L <g1:L>`, so is :g:`C <g1:C>` to :g:`F <g1:F>`, :g:`D <g1:D>` to :g:`G <g1:G>`, and :g:`E <g1:E>` to :g:`H <g1:H>`

.. step:: assert

   also, as :g:`C <g1:C>` is to :g:`F <g1:F>`, :g:`D <g1:D>` to :g:`G <g1:G>`, and :g:`E <g1:E>` to :g:`H <g1:H>`, so not only is :g:`O <g1:O>` to :g:`B <g1:B>`, but also :g:`A <g1:A>` to :g:`N <g1:N>` and :g:`N <g1:N>` to :g:`O <g1:O>`

.. step:: assert

   :g:`A <g1:A>`, :g:`N <g1:N>`, :g:`O <g1:O>`, :g:`B <g1:B>` are continuously proportional in the aforesaid ratios of the sides

.. step:: assert

   :g:`A <g1:A>`, :g:`N <g1:N>`, :g:`O <g1:O>`, :g:`B <g1:B>` are four numbers in continued proportion,

.. step:: assert ∵ magnitudes_proportional_said_def_v_def_10 <G.310>

   :g:`A <g1:A>` has to :g:`B <g1:B>` the ratio triplicate of that which :g:`A <g1:A>` has to :g:`N <g1:N>`

.. step:: assert

   But, as :g:`A <g1:A>` is to :g:`N <g1:N>`, so it was proved that :g:`C <g1:C>` is to :g:`F <g1:F>`, :g:`D <g1:D>` to :g:`G <g1:G>`, and also :g:`E <g1:E>` to :g:`H <g1:H>`

.. step:: conclude

   :g:`A <g1:A>` also has to :g:`B <g1:B>` the ratio triplicate of that which the corresponding side has to the corresponding side, that is, of the ratio which the number :g:`C <g1:C>` has to :g:`F <g1:F>`, :g:`D <g1:D>` to :g:`G <g1:G>`, and also :g:`E <g1:E>` to :g:`H <g1:H>`

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
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.230" [label="G.230", tooltip="G.230 (V.def.9): When three magnitudes areproportional, the first is said to have to the third theduplicate ratio of that which it has to the second.", fillcolor="#224422", URL="../G.230/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
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
     "G.300" [label="G.300", tooltip="G.300 (VII.def.16): And, when twonumbers havingmultiplied one another make some number, the number so produced is calledplane, and itssides are the numbers which have multiplied one another.", fillcolor="#224422", URL="../G.300/index.html", target="_top"];
     "G.310" [label="G.310", tooltip="G.310 (V.def.10): When four magnitudes are < continuously >proportional, the first is said to have to the fourth thetriplicate ratio of that which it has to the second, and so on continually, whatev...", fillcolor="#224422", URL="../G.310/index.html", target="_top"];
     "G.318" [label="G.318", tooltip="G.318 (VII.def.21): Similar plane and solid numbers are those which have their sidesproportional.", fillcolor="#224422", URL="../G.318/index.html", target="_top"];
     "G.319" [label="G.319", tooltip="G.319 (VIII.18): Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has t...", fillcolor="#222244", URL="../G.319/index.html", target="_top"];
     "G.320" [label="G.320", tooltip="G.320 (VII.def.17): And, when threenumbers havingmultiplied one another make some number, the number so produced issolid, and itssides are the numbers which have multiplied one another.", fillcolor="#224422", URL="../G.320/index.html", target="_top"];
     "G.321" [label="G.321", tooltip="G.321 (VIII.19): Between two similar solid numbers there fall two mean proportional numbers; and the solid number has to the similar solid number the ratio triplicate of that which the correspondin...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.7" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.7" -> "G.5";
     "G.319" -> "G.7";
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.268" -> "G.169";
     "G.270" -> "G.169";
     "G.271" -> "G.169";
     "G.176" -> "G.170";
     "G.257" -> "G.170";
     "G.319" -> "G.173";
     "G.321" -> "G.173";
     "G.180" -> "G.176";
     "G.271" -> "G.176";
     "G.272" -> "G.176";
     "G.230" -> "G.180";
     "G.263" -> "G.180";
     "G.266" -> "G.180";
     "G.310" -> "G.180";
     "G.318" -> "G.180";
     "G.319" -> "G.180";
     "G.321" -> "G.180";
     "G.194" -> "G.181";
     "G.265" -> "G.181";
     "G.268" -> "G.181";
     "G.261" -> "G.194";
     "G.262" -> "G.194";
     "G.266" -> "G.194";
     "G.268" -> "G.194";
     "G.270" -> "G.194";
     "G.271" -> "G.194";
     "G.319" -> "G.194";
     "G.321" -> "G.194";
     "G.319" -> "G.230";
     "G.248" -> "G.247";
     "G.268" -> "G.247";
     "G.269" -> "G.247";
     "G.270" -> "G.247";
     "G.271" -> "G.247";
     "G.253" -> "G.248";
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
     "G.300" -> "G.248";
     "G.319" -> "G.248";
     "G.320" -> "G.248";
     "G.321" -> "G.248";
     "G.254" -> "G.253";
     "G.256" -> "G.253";
     "G.257" -> "G.253";
     "G.258" -> "G.253";
     "G.261" -> "G.253";
     "G.262" -> "G.253";
     "G.263" -> "G.253";
     "G.265" -> "G.253";
     "G.266" -> "G.253";
     "G.258" -> "G.254";
     "G.261" -> "G.254";
     "G.262" -> "G.254";
     "G.263" -> "G.254";
     "G.265" -> "G.254";
     "G.266" -> "G.254";
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
     "G.268" -> "G.265";
     "G.271" -> "G.266";
     "G.319" -> "G.266";
     "G.321" -> "G.266";
     "G.270" -> "G.268";
     "G.270" -> "G.269";
     "G.271" -> "G.269";
     "G.272" -> "G.269";
     "G.300" -> "G.269";
     "G.319" -> "G.269";
     "G.320" -> "G.269";
     "G.321" -> "G.269";
     "G.272" -> "G.270";
     "G.272" -> "G.271";
     "G.319" -> "G.271";
     "G.321" -> "G.271";
     "G.321" -> "G.272";
     "G.319" -> "G.300";
     "G.321" -> "G.310";
     "G.319" -> "G.318";
     "G.321" -> "G.318";
     "G.321" -> "G.319";
     "G.321" -> "G.320";
   }

Required for
------------

:ref:`G.327 <G.327>`, :ref:`G.329 <G.329>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.339 <G.339>`

.. toctree::
   :hidden:

   code
   heath
