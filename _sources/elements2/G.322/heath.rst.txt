:canonical_id: G.322
:original_id: VIII.20
:title: G.322 mean proportional number
:volume: II
:book: VIII
:type: prop

G.322 mean proportional number — Heath
======================================

.. rubric:: `VIII.20 <https://geometor.github.io/euclid/heath/volume_II/book_viii/propositions/20/>`_

.. enunciation::

   If one mean :term:`proportional <G.180>` :term:`number <G.248>` fall between two numbers, the numbers will be :term:`similar plane numbers <G.318>`.

For let one mean proportional number :g:`C <g1:C>` fall between the two numbers :g:`A <g1:A>`, :g:`B <g1:B>`;

I say that :g:`A <g1:A>`, :g:`B <g1:B>` are similar plane numbers.

Let :g:`D <g1:D>`, :g:`E <g1:E>`, the least numbers of those which have the :term:`same ratio <G.176>` with :g:`A <g1:A>`, :g:`C <g1:C>`, be taken; :just:`[G.289] <G.289>`

.. assertion::

   therefore :g:`D <g1:D>` :term:`measures <G.253>` :g:`A <g1:A>` the same number of times that :g:`E <g1:E>` measures :g:`C <g1:C>`. :just:`[G.274] <G.274>`

Now, as many times as :g:`D <g1:D>` measures :g:`A <g1:A>`, so many :term:`units <G.247>` let there be in :g:`F <g1:F>`;

.. assertion::

   therefore :g:`F <g1:F>` by :term:`multiplying <G.269>` :g:`D <g1:D>` has made :g:`A <g1:A>`, so that :g:`A <g1:A>` is :term:`plane <G.7>`, and :g:`D <g1:D>`, :g:`F <g1:F>` are its sides.

.. subclause::

   Again, since :g:`D <g1:D>`, :g:`E <g1:E>` are the least of the numbers which have the same ratio with :g:`C <g1:C>`, :g:`B <g1:B>`,

.. assertion::

   therefore :g:`D <g1:D>` measures :g:`C <g1:C>` the same number of times that :g:`E <g1:E>` measures :g:`B <g1:B>`. :just:`[G.274] <G.274>`

.. picture:: g1.svg
   :alt: Book VIII, Proposition 20

As many times, then, as :g:`E <g1:E>` measures :g:`B <g1:B>`, so many units let there be in :g:`G <g1:G>`;

.. assertion::

   therefore :g:`E <g1:E>` measures :g:`B <g1:B>` according to the units in :g:`G <g1:G>`; therefore :g:`G <g1:G>` by multiplying :g:`E <g1:E>` has made :g:`B <g1:B>`.

.. assertion::

   Therefore :g:`B <g1:B>` is plane, and :g:`E <g1:E>`, :g:`G <g1:G>` are its sides.

.. assertion::

   Therefore :g:`A <g1:A>`, :g:`B <g1:B>` are :term:`plane numbers <G.300>`.

I say next that they are also similar.

.. subclause::

   For, † since :g:`F <g1:F>` by multiplying :g:`D <g1:D>` has made :g:`A <g1:A>`, and by multiplying :g:`E <g1:E>` has made :g:`C <g1:C>`,

.. assertion:: [G.271] <G.271>

   therefore, as :g:`D <g1:D>` is to :g:`E <g1:E>`, so is :g:`A <g1:A>` to :g:`C <g1:C>`, that is, :g:`C <g1:C>` to :g:`B <g1:B>`.

.. subclause::

   Again,† since :g:`E <g1:E>` by multiplying :g:`F <g1:F>`, :g:`G <g1:G>` has made :g:`C <g1:C>`, :g:`B <g1:B>` respectively,

.. assertion:: [G.271] <G.271>

   therefore, as :g:`F <g1:F>` is to :g:`G <g1:G>`, so is :g:`C <g1:C>` to :g:`B <g1:B>`.

.. subclause::

   But, as :g:`C <g1:C>` is to :g:`B <g1:B>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`;

.. assertion::

   therefore also, as :g:`D <g1:D>` is to :g:`E <g1:E>`, so is :g:`F <g1:F>` to :g:`G <g1:G>`.

.. assertion:: [G.266] <G.266>

   And :term:`alternately <G.194>`, as :g:`D <g1:D>` is to :g:`F <g1:F>`, so is :g:`E <g1:E>` to :g:`G <g1:G>`.

.. assertion::

   Therefore :g:`A <g1:A>`, :g:`B <g1:B>` are similar plane numbers; for their sides are proportional.

.. qed::

   :just:`Q. E. D.`

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
     "G.289" [label="G.289", tooltip="G.289 (VII.33): Given as many numbers as we please, to find the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.289/index.html", target="_top"];
     "G.300" [label="G.300", tooltip="G.300 (VII.def.16): And, when twonumbers havingmultiplied one another make some number, the number so produced is calledplane, and itssides are the numbers which have multiplied one another.", fillcolor="#224422", URL="../G.300/index.html", target="_top"];
     "G.318" [label="G.318", tooltip="G.318 (VII.def.21): Similar plane and solid numbers are those which have their sidesproportional.", fillcolor="#224422", URL="../G.318/index.html", target="_top"];
     "G.322" [label="G.322", tooltip="G.322 (VIII.20): If one mean proportional number fall between two numbers, the numbers is similar plane numbers.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.7" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.7" -> "G.5";
     "G.322" -> "G.7";
     "G.9" -> "G.8";
     "G.187" -> "G.9";
     "G.170" -> "G.169";
     "G.249" -> "G.169";
     "G.250" -> "G.169";
     "G.251" -> "G.169";
     "G.252" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.255" -> "G.169";
     "G.256" -> "G.169";
     "G.268" -> "G.169";
     "G.270" -> "G.169";
     "G.271" -> "G.169";
     "G.274" -> "G.169";
     "G.275" -> "G.169";
     "G.289" -> "G.169";
     "G.322" -> "G.169";
     "G.171" -> "G.170";
     "G.176" -> "G.170";
     "G.183" -> "G.170";
     "G.185" -> "G.170";
     "G.186" -> "G.170";
     "G.257" -> "G.170";
     "G.186" -> "G.171";
     "G.289" -> "G.173";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.187" -> "G.176";
     "G.271" -> "G.176";
     "G.272" -> "G.176";
     "G.274" -> "G.176";
     "G.275" -> "G.176";
     "G.289" -> "G.176";
     "G.183" -> "G.180";
     "G.263" -> "G.180";
     "G.266" -> "G.180";
     "G.273" -> "G.180";
     "G.318" -> "G.180";
     "G.322" -> "G.180";
     "G.182" -> "G.181";
     "G.194" -> "G.181";
     "G.265" -> "G.181";
     "G.268" -> "G.181";
     "G.274" -> "G.181";
     "G.275" -> "G.181";
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
     "G.270" -> "G.194";
     "G.271" -> "G.194";
     "G.322" -> "G.194";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.250" -> "G.247";
     "G.251" -> "G.247";
     "G.255" -> "G.247";
     "G.268" -> "G.247";
     "G.269" -> "G.247";
     "G.270" -> "G.247";
     "G.271" -> "G.247";
     "G.275" -> "G.247";
     "G.289" -> "G.247";
     "G.322" -> "G.247";
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
     "G.300" -> "G.248";
     "G.322" -> "G.248";
     "G.250" -> "G.249";
     "G.251" -> "G.249";
     "G.252" -> "G.249";
     "G.255" -> "G.249";
     "G.275" -> "G.249";
     "G.289" -> "G.249";
     "G.251" -> "G.250";
     "G.252" -> "G.251";
     "G.255" -> "G.251";
     "G.289" -> "G.252";
     "G.254" -> "G.253";
     "G.255" -> "G.253";
     "G.256" -> "G.253";
     "G.257" -> "G.253";
     "G.258" -> "G.253";
     "G.261" -> "G.253";
     "G.262" -> "G.253";
     "G.263" -> "G.253";
     "G.265" -> "G.253";
     "G.266" -> "G.253";
     "G.255" -> "G.254";
     "G.258" -> "G.254";
     "G.261" -> "G.254";
     "G.262" -> "G.254";
     "G.263" -> "G.254";
     "G.265" -> "G.254";
     "G.266" -> "G.254";
     "G.274" -> "G.254";
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
     "G.268" -> "G.265";
     "G.274" -> "G.265";
     "G.271" -> "G.266";
     "G.274" -> "G.266";
     "G.322" -> "G.266";
     "G.270" -> "G.268";
     "G.270" -> "G.269";
     "G.271" -> "G.269";
     "G.272" -> "G.269";
     "G.273" -> "G.269";
     "G.289" -> "G.269";
     "G.300" -> "G.269";
     "G.322" -> "G.269";
     "G.272" -> "G.270";
     "G.275" -> "G.270";
     "G.289" -> "G.270";
     "G.272" -> "G.271";
     "G.273" -> "G.271";
     "G.322" -> "G.271";
     "G.273" -> "G.272";
     "G.289" -> "G.273";
     "G.275" -> "G.274";
     "G.322" -> "G.274";
     "G.289" -> "G.275";
     "G.322" -> "G.289";
     "G.322" -> "G.300";
     "G.322" -> "G.318";
   }

Required for
------------

:ref:`G.323 <G.323>`, :ref:`G.324 <G.324>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.332 <G.332>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.337 <G.337>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`
