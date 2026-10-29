:order: 260
:number: 260
:canonical_id: G.260
:original_id: VIII.18
:volume: II
:book: VIII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory, proportions
:category: theorem, proof, number-theory, proportions
:tags: book-viii, point, ratio, proportion, mean-proportional, similar, number, plane-number, plane
:dependencies: G.182, G.213, G.217, G.259
:excerpt: Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has to the corresponding side.

.. _G.260:
.. _VIII.18:

G.260
=====

.. rubric:: `VIII.18 <https://geometor.github.io/euclid/heath/volume_II/book_viii/propositions/18/>`_

.. enunciation::

   Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has to the corresponding side.

.. picture:: g1.svg
   :alt: Book VIII, Proposition 18

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>` be two similar plane numbers

.. step:: assert

   Let the numbers :g:`C <g1:C>`, :g:`D <g1:D>` be the sides of :g:`A <g1:A>`, and :g:`E <g1:E>`, :g:`F <g1:F>` of :g:`B <g1:B>`.

.. step:: assert [G.259] <G.259>

   Since similar plane numbers are those which have their sides proportional.

.. step:: assert

   Therefore, as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`.

.. step:: assert

   I say then that between :g:`A <g1:A>`, :g:`B <g1:B>` there is one mean proportional number, and :g:`A <g1:A>` has to :g:`B <g1:B>` the ratio duplicate of that which :g:`C <g1:C>` has to :g:`E <g1:E>`, or :g:`D <g1:D>` to :g:`F <g1:F>`, that is, of that which the corresponding side has to the corresponding side.

.. step:: assert

   Now since, as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`,

.. step:: assert [G.213] <G.213>

   Therefore, alternately, as :g:`C <g1:C>` is to :g:`E <g1:E>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`.

.. step:: assert

   And, since :g:`A <g1:A>` is plane, and :g:`C <g1:C>`, :g:`D <g1:D>` are its sides,

.. step:: assert

   Therefore :g:`D <g1:D>` by multiplying :g:`C <g1:C>` has made :g:`A <g1:A>`.

.. step:: assert

   For the same reason also

.. step:: assert

   :g:`E <g1:E>` by multiplying :g:`F <g1:F>` has made :g:`B <g1:B>`.

.. step:: assert

   Now let :g:`D <g1:D>` by multiplying :g:`E <g1:E>` make :g:`G <g1:G>`.

.. step:: assert

   Since :g:`D <g1:D>` by multiplying :g:`C <g1:C>` has made :g:`A <g1:A>`, and by multiplying :g:`E <g1:E>` has made :g:`G <g1:G>`,

.. step:: assert [G.217] <G.217>

   Therefore, as :g:`C <g1:C>` is to :g:`E <g1:E>`, so is :g:`A <g1:A>` to :g:`G <g1:G>`.

.. step:: assert

   But, as :g:`C <g1:C>` is to :g:`E <g1:E>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`;

.. step:: assert

   Therefore also, as :g:`D <g1:D>` is to :g:`F <g1:F>`, so is :g:`A <g1:A>` to :g:`G <g1:G>`.

.. step:: assert

   Since :g:`E <g1:E>` by multiplying :g:`D <g1:D>` has made :g:`G <g1:G>`, and by multiplying :g:`F <g1:F>` has made :g:`B <g1:B>`,

.. step:: assert [G.217] <G.217>

   Therefore, as :g:`D <g1:D>` is to :g:`F <g1:F>`, so is :g:`G <g1:G>` to :g:`B <g1:B>`.

.. step:: assert

   It was also proved that, as :g:`D <g1:D>` is to :g:`F <g1:F>`, so is :g:`A <g1:A>` to :g:`G <g1:G>`;

.. step:: assert

   Therefore also, as :g:`A <g1:A>` is to :g:`G <g1:G>`, so is :g:`G <g1:G>` to :g:`B <g1:B>`.

.. step:: assert

   Therefore :g:`A <g1:A>`, :g:`G <g1:G>`, :g:`B <g1:B>` are in continued proportion.

.. step:: assert

   Therefore between :g:`A <g1:A>`, :g:`B <g1:B>` there is one mean proportional number.

.. step:: assert

   I say next that :g:`A <g1:A>` also has to :g:`B <g1:B>` the ratio duplicate of that which the corresponding side has to the corresponding side, that is, of that which :g:`C <g1:C>` has to :g:`E <g1:E>` or :g:`D <g1:D>` to :g:`F <g1:F>`.

.. step:: assert

   Since :g:`A <g1:A>`, :g:`G <g1:G>`, :g:`B <g1:B>` are in continued proportion,

.. step:: assert [G.182] <G.182>

   :g:`A <g1:A>` has to :g:`B <g1:B>` the ratio duplicate of that which it has to :g:`G <g1:G>`.

.. step:: assert

   And, as :g:`A <g1:A>` is to :g:`G <g1:G>`, so is :g:`C <g1:C>` to :g:`E <g1:E>`, and so is :g:`D <g1:D>` to :g:`F <g1:F>`.

.. step:: conclude

   Therefore :g:`A <g1:A>` also has to :g:`B <g1:B>` the ratio duplicate of that which :g:`C <g1:C>` has to :g:`E <g1:E>` or :g:`D <g1:D>` to :g:`F <g1:F>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.182" [label="G.182", tooltip="G.182 (V.def.9): When three magnitudes are proportional, the first is said to have to the third theduplicate ratio of that which it has to the second.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.208" [label="G.208", tooltip="G.208 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.208/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** areproportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
     "G.217" [label="G.217", tooltip="G.217 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.217/index.html", target="_top"];
     "G.259" [label="G.259", tooltip="G.259 (VII.def.21): Similar plane and solid numbers are those which have their sides proportional.", fillcolor="#224422", URL="../G.259/index.html", target="_top"];
     "G.260" [label="G.260", tooltip="G.260 (VIII.18): Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has t...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.260" -> "G.182";
     "G.205" -> "G.204";
     "G.208" -> "G.204";
     "G.209" -> "G.204";
     "G.208" -> "G.205";
     "G.209" -> "G.205";
     "G.209" -> "G.208";
     "G.213" -> "G.209";
     "G.213" -> "G.210";
     "G.217" -> "G.210";
     "G.217" -> "G.213";
     "G.260" -> "G.213";
     "G.260" -> "G.217";
     "G.260" -> "G.259";
   }

Required for
------------

:ref:`G.261 <G.261>`, :ref:`G.266 <G.266>`, :ref:`G.267 <G.267>`, :ref:`G.268 <G.268>`, :ref:`G.269 <G.269>`, :ref:`G.270 <G.270>`, :ref:`G.271 <G.271>`, :ref:`G.273 <G.273>`, :ref:`G.274 <G.274>`, :ref:`G.275 <G.275>`, :ref:`G.280 <G.280>`, :ref:`G.322 <G.322>`, :ref:`G.324 <G.324>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.513 <G.513>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
