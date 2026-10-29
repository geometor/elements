:order: 251
:number: 251
:canonical_id: G.251
:original_id: VIII.11
:volume: II
:book: VIII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory, proportions
:category: theorem, proof, number-theory, proportions
:tags: book-viii, point, square, ratio, proportion, mean-proportional, number, square-number
:dependencies: G.182, G.217, G.218
:excerpt: Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.

.. _G.251:
.. _VIII.11:

G.251
=====

.. rubric:: `VIII.11 <https://geometor.github.io/euclid/heath/volume_II/book_viii/propositions/11/>`_

.. enunciation::

   Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.

Let :g:`A <0369.g1:A>`, :g:`B <0369.g1:B>` be square numbers, and let :g:`C <0369.g1:C>` be the side of :g:`A <0369.g1:A>`, and :g:`D <0369.g1:D>` of :g:`B <0369.g1:B>`;

I say that between :g:`A <0369.g1:A>`, :g:`B <0369.g1:B>` there is one mean proportional number, and :g:`A <0369.g1:A>` has to :g:`B <0369.g1:B>` the ratio duplicate of that which :g:`C <0369.g1:C>` has to :g:`D <0369.g1:D>`.

For let :g:`C <0369.g1:C>` by multiplying :g:`D <0369.g1:D>` make :g:`E <0369.g1:E>`.

.. picture:: 0369.g1.svg
   :alt: Book VIII, Proposition 11

.. subclause::

   Now, since :g:`A <0369.g1:A>` is a square and :g:`C <0369.g1:C>` is its side,

.. assertion::

   therefore :g:`C <0369.g1:C>` by multiplying itself has made :g:`A <0369.g1:A>`.

.. subclause::

   For the same reason also

.. assertion::

   :g:`D <0369.g1:D>` by multiplying itself has made :g:`B <0369.g1:B>`.

.. subclause::

   Since then :g:`C <0369.g1:C>` by multiplying the numbers :g:`C <0369.g1:C>`, :g:`D <0369.g1:D>` has made :g:`A <0369.g1:A>`, :g:`E <0369.g1:E>` respectively,

.. assertion:: [G.217] <G.217>

   therefore, as :g:`C <0369.g1:C>` is to :g:`D <0369.g1:D>`, so is :g:`A <0369.g1:A>` to :g:`E <0369.g1:E>`.

.. subclause::

   For the same reason also,

.. assertion:: [G.218] <G.218>

   as :g:`C <0369.g1:C>` is to :g:`D <0369.g1:D>`, so is :g:`E <0369.g1:E>` to :g:`B <0369.g1:B>`.

.. assertion::

   Therefore also, as :g:`A <0369.g1:A>` is to :g:`E <0369.g1:E>`, so is :g:`E <0369.g1:E>` to :g:`B <0369.g1:B>`.

.. assertion::

   Therefore between :g:`A <0369.g1:A>`, :g:`B <0369.g1:B>` there is one mean proportional number.

I say next that :g:`A <0369.g1:A>` also has to :g:`B <0369.g1:B>` the ratio duplicate of that which :g:`C <0369.g1:C>` has to :g:`D <0369.g1:D>`.

.. subclause::

   For, since :g:`A <0369.g1:A>`, :g:`E <0369.g1:E>`, :g:`B <0369.g1:B>` are three numbers in proportion,

.. assertion::

   therefore :g:`A <0369.g1:A>` has to :g:`B <0369.g1:B>` the ratio duplicate of that which :g:`A <0369.g1:A>` has to :g:`E <0369.g1:E>`. :just:`[G.182] <G.182>`

.. subclause::

   But, as :g:`A <0369.g1:A>` is to :g:`E <0369.g1:E>`, so is :g:`C <0369.g1:C>` to :g:`D <0369.g1:D>`.

.. assertion::

   Therefore :g:`A <0369.g1:A>` has to :g:`B <0369.g1:B>` the ratio duplicate of that which the side :g:`C <0369.g1:C>` has to :g:`D <0369.g1:D>`.

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
     "G.182" [label="G.182", tooltip="G.182 (V.def.9): When three magnitudes are proportional, the first is said to have to the third the duplicate ratio of that which it has to the second.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
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
     "G.251" [label="G.251", tooltip="G.251 (VIII.11): Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.251" -> "G.182";
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
     "G.215" -> "G.212";
     "G.217" -> "G.213";
     "G.216" -> "G.215";
     "G.218" -> "G.216";
     "G.218" -> "G.217";
     "G.251" -> "G.217";
     "G.251" -> "G.218";
   }

Required for
------------

:ref:`G.255 <G.255>`, :ref:`G.256 <G.256>`, :ref:`G.257 <G.257>`, :ref:`G.258 <G.258>`, :ref:`G.322 <G.322>`, :ref:`G.324 <G.324>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.513 <G.513>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`
