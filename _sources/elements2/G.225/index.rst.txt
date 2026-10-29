:order: 225
:number: 225
:canonical_id: G.225
:original_id: VII.24
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number, prime, reductio-ad-absurdum
:dependencies: G.199, G.216, G.219, G.220, G.221, G.222, G.224
:excerpt: If two numbers be prime to any number, their product also is prime to the same.

.. _G.225:
.. _VII.24:

G.225
=====

.. rubric:: `VII.24 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/24/>`_

.. enunciation::

   If two numbers be prime to any number, their product also is prime to the same.

.. picture:: g1.svg
   :alt: Book VII, Proposition 24

.. step:: assert

   For let the two numbers :g:`A <g1:A>`, :g:`B <g1:B>` be prime to any number :g:`C <g1:C>`

.. step:: assert

   Let :g:`A <g1:A>` by multiplying :g:`B <g1:B>` make :g:`D <g1:D>`

.. step:: assert

   If :g:`C <g1:C>`, :g:`D <g1:D>` are not prime to one another, some number will measure :g:`C <g1:C>`, :g:`D <g1:D>`.

.. step:: assert

   Let a number measure them

.. step:: assert

   Let it be :g:`E <g1:E>`.

.. step:: assert

   Since :g:`C <g1:C>`, :g:`A <g1:A>` are prime to one another, and a certain number :g:`E <g1:E>` measures :g:`C <g1:C>`,

.. step:: assert [G.224] <G.224>

   Therefore :g:`A <g1:A>`, :g:`E <g1:E>` are prime to one another.

.. step:: assert

   As many times, then, as :g:`E <g1:E>` measures :g:`D <g1:D>`, so many units let there be in :g:`F <g1:F>`

.. step:: assert [G.216] <G.216>

   Therefore :g:`F <g1:F>` also measures :g:`D <g1:D>` according to the units in :g:`E <g1:E>`.

.. step:: assert [G.222] <G.222>

   Therefore :g:`E <g1:E>` by multiplying :g:`F <g1:F>` has made :g:`D <g1:D>`.

.. step:: assert

   But, further, :g:`A <g1:A>` by multiplying :g:`B <g1:B>` has also made :g:`D <g1:D>` ;

.. step:: assert

   Therefore the product of :g:`E <g1:E>`, :g:`F <g1:F>` is equal to the product of :g:`A <g1:A>`, :g:`B <g1:B>`.

.. step:: assert [G.219] <G.219>

   But, if the product of the extremes be equal to that of the means, the four numbers are proportional .

.. step:: assert

   Therefore, as :g:`E <g1:E>` is to :g:`A <g1:A>`, so is :g:`B <g1:B>` to :g:`F <g1:F>`.

.. step:: assert [G.221] <G.221>

   :g:`A <g1:A>`, :g:`E <g1:E>` are prime to one another, numbers which are prime to one another are also the least of those which have the same ratio, and the least numbers of those which have the same ratio with them measure those which have the same ratio the same

.. step:: assert [G.220] <G.220>

   Number of times, the greater the greater and the less the less, that is, the antecedent the antecedent and the consequent the consequent .

.. step:: assert

   Therefore :g:`E <g1:E>` measures :g:`B <g1:B>`.

.. step:: assert

   It also measures :g:`C <g1:C>` ;

.. step:: assert [G.199] <G.199>

   Therefore :g:`E <g1:E>` measures :g:`B <g1:B>`, :g:`C <g1:C>` which are prime to one another : which is impossible.

.. step:: assert

   Therefore no number will measure the numbers :g:`C <g1:C>`, :g:`D <g1:D>`.

.. step:: conclude

   Therefore :g:`C <g1:C>`, :g:`D <g1:D>` are prime to one another.

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
     "G.224" [label="G.224", tooltip="G.224 (VII.23): If two numbers be prime to one another, the number which measures the one of them is prime to the remaining number.", fillcolor="#222244", URL="../G.224/index.html", target="_top"];
     "G.225" [label="G.225", tooltip="G.225 (VII.24): If two numbers be prime to any number, their product also is prime to the same.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.225" -> "G.216";
     "G.218" -> "G.217";
     "G.219" -> "G.217";
     "G.219" -> "G.218";
     "G.225" -> "G.219";
     "G.221" -> "G.220";
     "G.225" -> "G.220";
     "G.225" -> "G.221";
     "G.225" -> "G.222";
     "G.225" -> "G.224";
   }

Required for
------------

:ref:`G.226 <G.226>`, :ref:`G.227 <G.227>`, :ref:`G.228 <G.228>`, :ref:`G.242 <G.242>`, :ref:`G.243 <G.243>`, :ref:`G.246 <G.246>`, :ref:`G.247 <G.247>`, :ref:`G.248 <G.248>`, :ref:`G.249 <G.249>`, :ref:`G.255 <G.255>`, :ref:`G.256 <G.256>`, :ref:`G.257 <G.257>`, :ref:`G.258 <G.258>`, :ref:`G.263 <G.263>`, :ref:`G.265 <G.265>`, :ref:`G.266 <G.266>`, :ref:`G.267 <G.267>`, :ref:`G.268 <G.268>`, :ref:`G.269 <G.269>`, :ref:`G.270 <G.270>`, :ref:`G.271 <G.271>`, :ref:`G.272 <G.272>`, :ref:`G.273 <G.273>`, :ref:`G.274 <G.274>`, :ref:`G.275 <G.275>`, :ref:`G.278 <G.278>`, :ref:`G.279 <G.279>`, :ref:`G.280 <G.280>`, :ref:`G.283 <G.283>`, :ref:`G.284 <G.284>`, :ref:`G.286 <G.286>`, :ref:`G.306 <G.306>`, :ref:`G.312 <G.312>`, :ref:`G.322 <G.322>`, :ref:`G.324 <G.324>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.513 <G.513>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
