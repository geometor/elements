:order: 231
:number: 231
:canonical_id: G.231
:original_id: VII.30
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number, prime
:dependencies: G.219, G.220, G.221, G.222, G.230
:excerpt: If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.

.. _G.231:
.. _VII.30:

G.231
=====

.. rubric:: `VII.30 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/30/>`_

.. enunciation::

   If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.

For let the two numbers :g:`A <0337.g1:A>`, :g:`B <0337.g1:B>` by multiplying one another make :g:`C <0337.g1:C>`, and let any prime number :g:`D <0337.g1:D>` measure :g:`C <0337.g1:C>`;

I say that :g:`D <0337.g1:D>` measures one of the numbers :g:`A <0337.g1:A>`, :g:`B <0337.g1:B>`.

.. picture:: 0337.g1.svg
   :alt: Book VII, Proposition 30

For let it not measure :g:`A <0337.g1:A>`.

.. subclause::

   Now :g:`D <0337.g1:D>` is prime ;

.. assertion::

   therefore :g:`A <0337.g1:A>`, :g:`D <0337.g1:D>` are prime to one another. :just:`[G.230] <G.230>`

And, as many times as :g:`D <0337.g1:D>` measures :g:`C <0337.g1:C>`, so many units let there be in :g:`E <0337.g1:E>`.

.. subclause::

   Since then :g:`D <0337.g1:D>` measures :g:`C <0337.g1:C>` according to the units in :g:`E <0337.g1:E>`,

.. assertion:: [G.222] <G.222>

   therefore :g:`D <0337.g1:D>` by multiplying :g:`E <0337.g1:E>` has made :g:`C <0337.g1:C>`.

.. subclause::

   Further, :g:`A <0337.g1:A>` by multiplying :g:`B <0337.g1:B>` has also made :g:`C <0337.g1:C>` ;

.. assertion::

   therefore the product of :g:`D <0337.g1:D>`, :g:`E <0337.g1:E>` is equal to the product of :g:`A <0337.g1:A>`, :g:`B <0337.g1:B>`.

.. assertion:: [G.219] <G.219>

   Therefore, as :g:`D <0337.g1:D>` is to :g:`A <0337.g1:A>`, so is :g:`B <0337.g1:B>` to :g:`E <0337.g1:E>`.

.. subclause::

   But :g:`D <0337.g1:D>`, :g:`A <0337.g1:A>` are prime to one another, primes are also least, :just:`[G.221] <G.221>` and the least measure the numbers which have the same ratio the same number of times, the greater the greater and the less the less, that is, the antecedent the antecedent and the consequent the consequent ; :just:`[G.220] <G.220>`

.. assertion::

   therefore :g:`D <0337.g1:D>` measures :g:`B <0337.g1:B>`.

.. assertion::

   Similarly we can also show that, if :g:`D <0337.g1:D>` do not measure :g:`B <0337.g1:B>`, it will measure :g:`A <0337.g1:A>`.

.. assertion::

   Therefore :g:`D <0337.g1:D>` measures one of the numbers :g:`A <0337.g1:A>`, :g:`B <0337.g1:B>`.

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
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said to be in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equim...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said to have a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (V.9): Magnitudes which have the same ratio to the same are equal to one another ; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.146/index.html", target="_top"];
     "G.199" [label="G.199", tooltip="G.199 (VII.def.12): Numbers prime to one another are those which are measured by an unit alone as a common measure.", fillcolor="#224422", URL="../G.199/index.html", target="_top"];
     "G.200" [label="G.200", tooltip="G.200 (VII.1): Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is...", fillcolor="#222244", URL="../G.200/index.html", target="_top"];
     "G.201" [label="G.201", tooltip="G.201 (VII.2): Given two numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.201/index.html", target="_top"];
     "G.203" [label="G.203", tooltip="G.203 (VII.4): Any number is either a part or parts of any number, the less of the greater.", fillcolor="#222244", URL="../G.203/index.html", target="_top"];
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.208" [label="G.208", tooltip="G.208 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.208/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.212" [label="G.212", tooltip="G.212 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.212/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VII.13): If four numbers be proportional, they will also be proportional alternately.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
     "G.215" [label="G.215", tooltip="G.215 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.215/index.html", target="_top"];
     "G.216" [label="G.216", tooltip="G.216 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.", fillcolor="#222244", URL="../G.216/index.html", target="_top"];
     "G.217" [label="G.217", tooltip="G.217 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.217/index.html", target="_top"];
     "G.218" [label="G.218", tooltip="G.218 (VII.18): If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", fillcolor="#222244", URL="../G.218/index.html", target="_top"];
     "G.219" [label="G.219", tooltip="G.219 (VII.19): If four numbers be proportional, the number produced from the first and fourth will be equal to the number produced from the second and third; and, if the number produced from the ...", fillcolor="#222244", URL="../G.219/index.html", target="_top"];
     "G.220" [label="G.220", tooltip="G.220 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.220/index.html", target="_top"];
     "G.221" [label="G.221", tooltip="G.221 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.221/index.html", target="_top"];
     "G.222" [label="G.222", tooltip="G.222 (VII.def.15): A number is said to multiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.222/index.html", target="_top"];
     "G.230" [label="G.230", tooltip="G.230 (VII.29): Any prime number is prime to any number which it does not measure.", fillcolor="#222244", URL="../G.230/index.html", target="_top"];
     "G.231" [label="G.231", tooltip="G.231 (VII.30): If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
   }

Required for
------------

:ref:`G.285 <G.285>`
