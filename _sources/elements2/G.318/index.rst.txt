:order: 318
:number: 318
:canonical_id: G.318
:original_id: X.5
:volume: III
:book: X
:type: prop
:subtype: theorem
:categories: theorem, proof, incommensurables, magnitudes
:category: theorem, proof, incommensurables, magnitudes
:tags: book-x, point, ex-aequali, ratio, commensurable, number
:dependencies: G.142, G.159, G.210
:excerpt: Commensurable magnitudes have to one another the ratio which a number has to a number.

.. _G.318:
.. _X.5:

G.318
=====

.. rubric:: `X.5 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/005/>`_

.. enunciation::

   Commensurable magnitudes have to one another the ratio which a number has to a number.

.. signature:: theorem

   | :fn:`commensurable_magnitudes_ratio <G.318>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`)
   | **given** :g:`A <g1:A>`, :g:`B <g1:B>` be commensurable magnitudes
   | **prove** :g:`A <g1:A>` has to :g:`B <g1:B>` the ratio which a number has to a number

.. picture:: g1.svg
   :alt: Proposition 5 diagram

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>` be commensurable magnitudes

.. step:: assert

   Since :g:`A <g1:A>`, :g:`B <g1:B>` are commensurable, some magnitude will measure them

.. step:: assert

   Let it measure them, and let it be :g:`C <g1:C>`.

.. step:: assert

   And, as many times as :g:`C <g1:C>` measures :g:`A <g1:A>`, so many units let there be in :g:`D <g1:D>`

.. step:: assert

   And, as many times as :g:`C <g1:C>` measures :g:`B <g1:B>`, so many units let there be in :g:`E <g1:E>`.

.. step:: assert

   Since then :g:`C <g1:C>` measures :g:`A <g1:A>` according to the units in :g:`D <g1:D>`, while the unit also measures :g:`D <g1:D>` according to the units in it,

.. step:: assert

   Therefore the unit measures the number :g:`D <g1:D>` the same number of times as the magnitude :g:`C <g1:C>` measures :g:`A <g1:A>`;

.. step:: assert ∵ numbers_proportional_multiple_def <G.210>

   Therefore, as :g:`C <g1:C>` is to :g:`A <g1:A>`, so is the unit to :g:`D <g1:D>`;

.. step:: assert ∵ equal_magnitudes_ratio <G.142>

   Therefore, inversely, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to the unit.

.. step:: assert

   Since :g:`C <g1:C>` measures :g:`B <g1:B>` according to the units in :g:`E <g1:E>`, while the unit also measures :g:`E <g1:E>` according to the units in it,

.. step:: assert

   Therefore the unit measures :g:`E <g1:E>` the same number of times as :g:`C <g1:C>` measures :g:`B <g1:B>`;

.. step:: assert

   Therefore, as :g:`C <g1:C>` is to :g:`B <g1:B>`, so is the unit to :g:`E <g1:E>`.

.. step:: assert

   It was also proved that, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to the unit;

.. step:: conclude ∵ there_number_magnitudes_v_22 <G.159>

   Therefore, :term:`*ex aequali* <ex-aequali>`, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is the number :g:`D <g1:D>` to :g:`E <g1:E>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.136" [label="G.136", tooltip="G.136 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.136/index.html", target="_top"];
     "G.137" [label="G.137", tooltip="G.137 (V.3): If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then alsoex aequali the magnitudes taken is...", fillcolor="#222244", URL="../G.137/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (V.4): If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples wh...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.150/index.html", target="_top"];
     "G.157" [label="G.157", tooltip="G.157 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and ifex aequali the first be greater than the third, the fourth...", fillcolor="#222244", URL="../G.157/index.html", target="_top"];
     "G.159" [label="G.159", tooltip="G.159 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.159/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** areproportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.318" [label="G.318", tooltip="G.318 (X.5): Commensurable magnitudes have to one another the ratio which a number has to a number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.137" -> "G.136";
     "G.139" -> "G.137";
     "G.139" -> "G.138";
     "G.142" -> "G.138";
     "G.150" -> "G.138";
     "G.159" -> "G.138";
     "G.159" -> "G.139";
     "G.147" -> "G.142";
     "G.318" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.147" -> "G.145";
     "G.157" -> "G.145";
     "G.157" -> "G.147";
     "G.157" -> "G.150";
     "G.159" -> "G.157";
     "G.318" -> "G.159";
     "G.318" -> "G.210";
   }

Required for
------------

:ref:`G.321 <G.321>`, :ref:`G.322 <G.322>`, :ref:`G.323 <G.323>`, :ref:`G.324 <G.324>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.336 <G.336>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.340 <G.340>`, :ref:`G.341 <G.341>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.351 <G.351>`, :ref:`G.352 <G.352>`, :ref:`G.353 <G.353>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.372 <G.372>`, :ref:`G.374 <G.374>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.424 <G.424>`, :ref:`G.425 <G.425>`, :ref:`G.426 <G.426>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.430 <G.430>`, :ref:`G.431 <G.431>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.513 <G.513>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
