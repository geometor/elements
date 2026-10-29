:order: 285
:number: 285
:canonical_id: G.285
:original_id: IX.14
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, number, prime, reductio-ad-absurdum
:dependencies: G.231
:excerpt: If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

.. _G.285:
.. _IX.14:

G.285
=====

.. rubric:: `IX.14 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/14/>`_

.. enunciation::

   If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

.. picture:: g1.svg
   :alt: Proposition 14 diagram

.. step:: assert

   For let the number :g:`A <g1:A>` be the least that is measured by the prime numbers :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`

.. step:: assert

   If possible, let it be measured by the prime number :g:`E <g1:E>`

.. step:: assert

   Let :g:`E <g1:E>` not be the same with any one of the numbers :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`.

.. step:: assert

   Since :g:`E <g1:E>` measures :g:`A <g1:A>`, let it measure it according to :g:`F <g1:F>` ;

.. step:: assert

   Therefore :g:`E <g1:E>` by multiplying :g:`F <g1:F>` has made :g:`A <g1:A>`.

.. step:: assert

   :g:`A <g1:A>` is measured by the prime numbers :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`.

.. step:: assert [G.231] <G.231>

   But, if two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers .

.. step:: assert

   Therefore :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` will measure one of the numbers :g:`E <g1:E>`, :g:`F <g1:F>`.

.. step:: assert

   Now they will not measure :g:`E <g1:E>` ; for :g:`E <g1:E>` is prime and not the same with any one of the numbers :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`.

.. step:: assert

   Therefore they will measure :g:`F <g1:F>`, which is less than :g:`A <g1:A>` : which is impossible, for :g:`A <g1:A>` is by hypothesis the least number measured by :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`.

.. step:: conclude

   Therefore no prime number will measure :g:`A <g1:A>` except :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`.

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
     "G.146" [label="G.146", tooltip="G.146 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.146/index.html", target="_top"];
     "G.199" [label="G.199", tooltip="G.199 (VII.def.12): Numbers prime to one another are those which are measured by an unit alone as a common measure.", fillcolor="#224422", URL="../G.199/index.html", target="_top"];
     "G.200" [label="G.200", tooltip="G.200 (VII.1): Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is...", fillcolor="#222244", URL="../G.200/index.html", target="_top"];
     "G.201" [label="G.201", tooltip="G.201 (VII.2): Given two numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.201/index.html", target="_top"];
     "G.203" [label="G.203", tooltip="G.203 (VII.4): Any number is either a part or parts of any number, the less of the greater.", fillcolor="#222244", URL="../G.203/index.html", target="_top"];
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.208" [label="G.208", tooltip="G.208 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.208/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** areproportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.212" [label="G.212", tooltip="G.212 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.212/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
     "G.215" [label="G.215", tooltip="G.215 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.215/index.html", target="_top"];
     "G.216" [label="G.216", tooltip="G.216 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced are equal.", fillcolor="#222244", URL="../G.216/index.html", target="_top"];
     "G.217" [label="G.217", tooltip="G.217 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.217/index.html", target="_top"];
     "G.218" [label="G.218", tooltip="G.218 (VII.18): If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", fillcolor="#222244", URL="../G.218/index.html", target="_top"];
     "G.219" [label="G.219", tooltip="G.219 (VII.19): If four numbers be proportional, the number produced from the first and fourth will equals the number produced from the second and third; and, if the number produced from the first...", fillcolor="#222244", URL="../G.219/index.html", target="_top"];
     "G.220" [label="G.220", tooltip="G.220 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.220/index.html", target="_top"];
     "G.221" [label="G.221", tooltip="G.221 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.221/index.html", target="_top"];
     "G.222" [label="G.222", tooltip="G.222 (VII.def.15): A number is said tomultiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.222/index.html", target="_top"];
     "G.230" [label="G.230", tooltip="G.230 (VII.29): Any prime number is prime to any number which it does not measure.", fillcolor="#222244", URL="../G.230/index.html", target="_top"];
     "G.231" [label="G.231", tooltip="G.231 (VII.30): If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.", fillcolor="#222244", URL="../G.231/index.html", target="_top"];
     "G.285" [label="G.285", tooltip="G.285 (IX.14): If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.142" -> "G.138";
     "G.219" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.146" -> "G.145";
     "G.219" -> "G.146";
     "G.200" -> "G.199";
     "G.221" -> "G.199";
     "G.201" -> "G.200";
     "G.203" -> "G.201";
     "G.220" -> "G.203";
     "G.205" -> "G.204";
     "G.208" -> "G.204";
     "G.209" -> "G.204";
     "G.212" -> "G.204";
     "G.208" -> "G.205";
     "G.209" -> "G.205";
     "G.212" -> "G.205";
     "G.209" -> "G.208";
     "G.213" -> "G.209";
     "G.212" -> "G.210";
     "G.213" -> "G.210";
     "G.217" -> "G.210";
     "G.220" -> "G.210";
     "G.215" -> "G.212";
     "G.220" -> "G.212";
     "G.217" -> "G.213";
     "G.220" -> "G.213";
     "G.216" -> "G.215";
     "G.218" -> "G.216";
     "G.221" -> "G.216";
     "G.218" -> "G.217";
     "G.219" -> "G.217";
     "G.219" -> "G.218";
     "G.231" -> "G.219";
     "G.221" -> "G.220";
     "G.231" -> "G.220";
     "G.231" -> "G.221";
     "G.231" -> "G.222";
     "G.231" -> "G.230";
     "G.285" -> "G.231";
   }

.. toctree::
   :hidden:

   code
   heath
