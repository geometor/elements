:order: 214
:number: 214
:canonical_id: G.214
:original_id: VII.14
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, ex-aequali, ratio, number
:dependencies: G.213
:excerpt: If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they is in the same ratio ex aequali.

.. _G.214:
.. _VII.14:

G.214
=====

.. rubric:: `VII.14 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/14/>`_

.. enunciation::

   If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they is in the same ratio ex aequali.

.. signature:: theorem

   | :fn:`there_many_numbers_vii_14 <G.214>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`)
   | **given** there be as many numbers as we please :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, others equal to them in multitude :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>`, which taken two and two are in the same ratio, so that, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`, and, as :g:`B <g1:B>` is to :g:`C <g1:C>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`
   | **prove** alternately, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`

.. picture:: g1.svg
   :alt: Proposition 14 Diagram

.. step:: given

   there be as many numbers as we please :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, others equal to them in multitude :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>`, which taken two and two are in the same ratio, so that, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`, and, as :g:`B <g1:B>` is to :g:`C <g1:C>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`

.. step:: assert

   I say that, :term:`*ex aequali* <ex-aequali>`, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so also is :g:`D <g1:D>` to :g:`F <g1:F>`.

.. step:: assert

   Since, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`,

.. step:: assert ∵ numbers_proportional_proportional <G.213>

   Therefore, alternately, as :g:`A <g1:A>` is to :g:`D <g1:D>`, so is :g:`B <g1:B>` to :g:`E <g1:E>`.

.. step:: assert

   Since, as :g:`B <g1:B>` is to :g:`C <g1:C>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`,

.. step:: assert ∵ numbers_proportional_proportional <G.213>

   Therefore, alternately, as :g:`B <g1:B>` is to :g:`E <g1:E>`, so is :g:`C <g1:C>` to :g:`F <g1:F>`.

.. step:: assert

   But, as :g:`B <g1:B>` is to :g:`E <g1:E>`, so is :g:`A <g1:A>` to :g:`D <g1:D>`;

.. step:: assert

   Therefore also, as :g:`A <g1:A>` is to :g:`D <g1:D>`, so is :g:`C <g1:C>` to :g:`F <g1:F>`.

.. step:: conclude ∵ numbers_proportional_proportional <G.213>

   Therefore, alternately, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.208" [label="G.208", tooltip="G.208 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.208/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** areproportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
     "G.214" [label="G.214", tooltip="G.214 (VII.14): If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they is in the same ratio ex aequali.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.205" -> "G.204";
     "G.208" -> "G.204";
     "G.209" -> "G.204";
     "G.208" -> "G.205";
     "G.209" -> "G.205";
     "G.209" -> "G.208";
     "G.213" -> "G.209";
     "G.213" -> "G.210";
     "G.214" -> "G.213";
   }

Required for
------------

:ref:`G.241 <G.241>`, :ref:`G.242 <G.242>`, :ref:`G.243 <G.243>`, :ref:`G.245 <G.245>`, :ref:`G.246 <G.246>`, :ref:`G.247 <G.247>`, :ref:`G.248 <G.248>`, :ref:`G.249 <G.249>`, :ref:`G.254 <G.254>`, :ref:`G.255 <G.255>`, :ref:`G.256 <G.256>`, :ref:`G.257 <G.257>`, :ref:`G.258 <G.258>`, :ref:`G.263 <G.263>`, :ref:`G.265 <G.265>`, :ref:`G.266 <G.266>`, :ref:`G.267 <G.267>`, :ref:`G.268 <G.268>`, :ref:`G.269 <G.269>`, :ref:`G.270 <G.270>`, :ref:`G.271 <G.271>`, :ref:`G.272 <G.272>`, :ref:`G.273 <G.273>`, :ref:`G.274 <G.274>`, :ref:`G.275 <G.275>`, :ref:`G.278 <G.278>`, :ref:`G.279 <G.279>`, :ref:`G.280 <G.280>`, :ref:`G.283 <G.283>`, :ref:`G.284 <G.284>`, :ref:`G.286 <G.286>`, :ref:`G.290 <G.290>`, :ref:`G.306 <G.306>`, :ref:`G.312 <G.312>`, :ref:`G.322 <G.322>`, :ref:`G.324 <G.324>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.513 <G.513>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
