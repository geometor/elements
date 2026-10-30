:order: 279
:number: 279
:canonical_id: G.279
:original_id: IX.9
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, square, proportion, unit, number, continued-proportion, cube
:dependencies: G.264, G.265, G.272, G.278
:excerpt: If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest is square. And, if the number after the unit be cube, all the rest is cube.

.. _G.279:
.. _IX.9:

G.279
=====

.. rubric:: `IX.9 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/09/>`_

.. enunciation::

   If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest is square. And, if the number after the unit be cube, all the rest is cube.

.. signature:: theorem

   | :fn:`many_numbers_please_ix_9 <G.279>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`)
   | **given** there be as many numbers as we please, :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>`, beginning from an unit and in continued proportion, let :g:`A <g1:A>`, the number after the unit, be square
   | **prove** all the rest will also be square; all the rest are also square; all the rest are also cube; all the rest are also cube

.. picture:: g1.svg
   :alt: Proposition 9 Diagram

.. step:: given

   there be as many numbers as we please, :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>`, beginning from an unit and in continued proportion, let :g:`A <g1:A>`, the number after the unit, be square

.. step:: assert ∵ many_numbers_please_ix_8 <G.278>

   Now it has been proved that :g:`B <g1:B>`, the third from the unit, is square, as are also all those which leave out one .

.. step:: assert

   Since :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` are in continued proportion, and :g:`A <g1:A>` is square,

.. step:: assert ∵ numbers_continued_proportion <G.264>

   Therefore :g:`C <g1:C>` is also square.

.. step:: assert

   Since :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` are in continued proportion, and :g:`B <g1:B>` is square,

.. step:: assert ∵ numbers_continued_proportion <G.264>

   :g:`D <g1:D>` is also square.

.. step:: assert

   Similarly we can prove that all the rest are also square.

.. step:: assert

   Next, let :g:`A <g1:A>` be cube

.. step:: assert ∵ many_numbers_please_ix_8 <G.278>

   Now it has been proved that :g:`C <g1:C>`, the fourth from the unit, is cube, as also are all those which leave out two .

.. step:: assert

   Since, as the unit is to :g:`A <g1:A>`, so is :g:`A <g1:A>` to :g:`B <g1:B>`,

.. step:: assert

   Therefore the unit measures :g:`A <g1:A>` the same number of times as :g:`A <g1:A>` measures :g:`B <g1:B>`.

.. step:: assert

   The unit measures :g:`A <g1:A>` according to the units in it ;

.. step:: assert

   Therefore :g:`A <g1:A>` also measures :g:`B <g1:B>` according to the units in itself ;

.. step:: assert

   Therefore :g:`A <g1:A>` by multiplying itself has made :g:`B <g1:B>`.

.. step:: assert

   :g:`A <g1:A>` is cube.

.. step:: assert ∵ cube_number_multiplying <G.272>

   But, if a cube number by multiplying itself make some number, the product is cube.

.. step:: assert

   Therefore :g:`B <g1:B>` is also cube.

.. step:: assert

   And, since the four numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` are in continued proportion, and :g:`A <g1:A>` is cube,

.. step:: assert ∵ numbers_continued_proportion_viii_23 <G.265>

   :g:`D <g1:D>` also is cube.

.. step:: assert

   For the same reason

.. step:: conclude

   :g:`E <g1:E>` is also cube, and similarly all the rest are cube.

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
     "G.202" [label="G.202", tooltip="G.202 (VII.3): Given three numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.202/index.html", target="_top"];
     "G.203" [label="G.203", tooltip="G.203 (VII.4): Any number is either a part or parts of any number, the less of the greater.", fillcolor="#222244", URL="../G.203/index.html", target="_top"];
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.208" [label="G.208", tooltip="G.208 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.208/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** areproportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.212" [label="G.212", tooltip="G.212 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.212/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
     "G.214" [label="G.214", tooltip="G.214 (VII.14): If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.214/index.html", target="_top"];
     "G.215" [label="G.215", tooltip="G.215 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.215/index.html", target="_top"];
     "G.216" [label="G.216", tooltip="G.216 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced are equal.", fillcolor="#222244", URL="../G.216/index.html", target="_top"];
     "G.217" [label="G.217", tooltip="G.217 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.217/index.html", target="_top"];
     "G.218" [label="G.218", tooltip="G.218 (VII.18): If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", fillcolor="#222244", URL="../G.218/index.html", target="_top"];
     "G.219" [label="G.219", tooltip="G.219 (VII.19): If four numbers be proportional, the number produced from the first and fourth will equals the number produced from the second and third; and, if the number produced from the first...", fillcolor="#222244", URL="../G.219/index.html", target="_top"];
     "G.220" [label="G.220", tooltip="G.220 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.220/index.html", target="_top"];
     "G.221" [label="G.221", tooltip="G.221 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.221/index.html", target="_top"];
     "G.222" [label="G.222", tooltip="G.222 (VII.def.15): A number is said tomultiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.222/index.html", target="_top"];
     "G.223" [label="G.223", tooltip="G.223 (VII.22): The least numbers of those which have the same ratio with them are prime to one another.", fillcolor="#222244", URL="../G.223/index.html", target="_top"];
     "G.224" [label="G.224", tooltip="G.224 (VII.23): If two numbers be prime to one another, the number which measures the one of them is prime to the remaining number.", fillcolor="#222244", URL="../G.224/index.html", target="_top"];
     "G.225" [label="G.225", tooltip="G.225 (VII.24): If two numbers be prime to any number, their product also is prime to the same.", fillcolor="#222244", URL="../G.225/index.html", target="_top"];
     "G.226" [label="G.226", tooltip="G.226 (VII.25): If two numbers be prime to one another, the product of one of them into itself is prime to the remaining one.", fillcolor="#222244", URL="../G.226/index.html", target="_top"];
     "G.227" [label="G.227", tooltip="G.227 (VII.26): If two numbers be prime to two numbers, both to each, their products also is prime to one another.", fillcolor="#222244", URL="../G.227/index.html", target="_top"];
     "G.228" [label="G.228", tooltip="G.228 (VII.27): If two numbers be prime to one another, and each by multiplying itself make a certain number, the products is prime to one another; and, if the original numbers by multiplying the ...", fillcolor="#222244", URL="../G.228/index.html", target="_top"];
     "G.234" [label="G.234", tooltip="G.234 (VII.33): Given as many numbers as we please, to find the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.234/index.html", target="_top"];
     "G.241" [label="G.241", tooltip="G.241 (VIII.1): If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio wit...", fillcolor="#222244", URL="../G.241/index.html", target="_top"];
     "G.242" [label="G.242", tooltip="G.242 (VIII.2): Find numbers in continued proportion, as many as may be prescribed, and the least that are in a given ratio.", fillcolor="#222244", URL="../G.242/index.html", target="_top"];
     "G.243" [label="G.243", tooltip="G.243 (VIII.3): If as many numbers as we please in continued proportion be the least of those which have the same ratio with them, the extremes of them are prime to one another.", fillcolor="#222244", URL="../G.243/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VIII.8): If between two numbers there fall numbers in continued proportion with them, then, however many numbers fall between them in continued proportion, so many will also fall in continu...", fillcolor="#222244", URL="../G.248/index.html", target="_top"];
     "G.262" [label="G.262", tooltip="G.262 (VIII.20): If one mean proportional number fall between two numbers, the numbers is similar plane numbers.", fillcolor="#222244", URL="../G.262/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VIII.21): If two mean proportional numbers fall between two numbers, the numbers are similar solid numbers.", fillcolor="#222244", URL="../G.263/index.html", target="_top"];
     "G.264" [label="G.264", tooltip="G.264 (VIII.22): If three numbers be in continued proportion, and the first be square, the third is square.", fillcolor="#222244", URL="../G.264/index.html", target="_top"];
     "G.265" [label="G.265", tooltip="G.265 (VIII.23): If four numbers be in continued proportion, and the first be cube, the fourth is cube.", fillcolor="#222244", URL="../G.265/index.html", target="_top"];
     "G.272" [label="G.272", tooltip="G.272 (IX.3): If a cube number by multiplying itself make some number, the product is cube.", fillcolor="#222244", URL="../G.272/index.html", target="_top"];
     "G.278" [label="G.278", tooltip="G.278 (IX.8): If as many numbers as we please beginning from an unit be in continued proportion, the third from the unit is square, as will also those which successively leave out one; the fourt...", fillcolor="#222244", URL="../G.278/index.html", target="_top"];
     "G.279" [label="G.279", tooltip="G.279 (IX.9): If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest is square. And, if the number after the uni...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.142" -> "G.138";
     "G.219" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.146" -> "G.145";
     "G.219" -> "G.146";
     "G.200" -> "G.199";
     "G.221" -> "G.199";
     "G.224" -> "G.199";
     "G.225" -> "G.199";
     "G.201" -> "G.200";
     "G.202" -> "G.201";
     "G.203" -> "G.201";
     "G.234" -> "G.202";
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
     "G.234" -> "G.210";
     "G.248" -> "G.210";
     "G.272" -> "G.210";
     "G.278" -> "G.210";
     "G.215" -> "G.212";
     "G.220" -> "G.212";
     "G.214" -> "G.213";
     "G.217" -> "G.213";
     "G.220" -> "G.213";
     "G.262" -> "G.213";
     "G.241" -> "G.214";
     "G.248" -> "G.214";
     "G.263" -> "G.214";
     "G.216" -> "G.215";
     "G.218" -> "G.216";
     "G.221" -> "G.216";
     "G.225" -> "G.216";
     "G.234" -> "G.216";
     "G.218" -> "G.217";
     "G.219" -> "G.217";
     "G.223" -> "G.217";
     "G.242" -> "G.217";
     "G.262" -> "G.217";
     "G.219" -> "G.218";
     "G.242" -> "G.218";
     "G.263" -> "G.218";
     "G.225" -> "G.219";
     "G.234" -> "G.219";
     "G.221" -> "G.220";
     "G.225" -> "G.220";
     "G.241" -> "G.220";
     "G.248" -> "G.220";
     "G.262" -> "G.220";
     "G.263" -> "G.220";
     "G.225" -> "G.221";
     "G.234" -> "G.221";
     "G.241" -> "G.221";
     "G.248" -> "G.221";
     "G.263" -> "G.221";
     "G.223" -> "G.222";
     "G.225" -> "G.222";
     "G.234" -> "G.222";
     "G.242" -> "G.223";
     "G.243" -> "G.223";
     "G.225" -> "G.224";
     "G.226" -> "G.225";
     "G.227" -> "G.225";
     "G.228" -> "G.226";
     "G.228" -> "G.227";
     "G.242" -> "G.228";
     "G.243" -> "G.228";
     "G.243" -> "G.234";
     "G.248" -> "G.234";
     "G.262" -> "G.234";
     "G.263" -> "G.234";
     "G.242" -> "G.241";
     "G.243" -> "G.242";
     "G.263" -> "G.242";
     "G.248" -> "G.243";
     "G.263" -> "G.243";
     "G.272" -> "G.248";
     "G.263" -> "G.262";
     "G.264" -> "G.262";
     "G.265" -> "G.263";
     "G.278" -> "G.264";
     "G.279" -> "G.264";
     "G.272" -> "G.265";
     "G.278" -> "G.265";
     "G.279" -> "G.265";
     "G.279" -> "G.272";
     "G.279" -> "G.278";
   }

.. toctree::
   :hidden:

   code
   heath
