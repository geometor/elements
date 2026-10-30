:order: 147
:number: 147
:canonical_id: G.147
:original_id: V.10
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, ratio, equality, reductio-ad-absurdum
:dependencies: G.142, G.145
:excerpt: Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.

.. _G.147:
.. _V.10:

G.147
=====

.. rubric:: `V.10 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/10/>`_

.. enunciation::

   Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.

.. signature:: theorem

   | :fn:`magnitudes_ratio_greater <G.147>`\ ()
   | **prove** :g:`A <g1:A>` is greater than :g:`B <g1:B>`; :g:`B <g1:B>` is less than :g:`A <g1:A>`

.. picture:: g1.svg
   :alt: Folio 0161 Figure 1

.. step:: assert

   Let :g:`A <g1:A>` have to :g:`C <g1:C>` a greater ratio than :g:`B <g1:B>` has to :g:`C <g1:C>`

.. step:: assert

   If not, :g:`A <g1:A>` is either :eq:`equal <g1:A = g1:B>` to :g:`B <g1:B>` or less.

.. step:: assert

   Now :g:`A <g1:A>` is not :eq:`equal <g1:A = g1:B>` to :g:`B <g1:B>`

.. step:: assert ∵ equal_magnitudes_ratio <G.142>

   For in that case each of the magnitudes :g:`A <g1:A>`, :g:`B <g1:B>` would have had the same ratio to :g:`C <g1:C>`

.. step:: assert

   But they have not

.. step:: assert

   Therefore :g:`A <g1:A>` is not :eq:`equal <g1:A = g1:B>` to :g:`B <g1:B>`.

.. step:: assert

   Nor again is :g:`A <g1:A>` less than :g:`B <g1:B>`

.. step:: assert ∵ unequal_magnitudes_greater <G.145>

   For in that case :g:`A <g1:A>` would have had to :g:`C <g1:C>` a less ratio than :g:`B <g1:B>` has to :g:`C <g1:C>`

.. step:: assert

   But it has not

.. step:: assert

   Therefore :g:`A <g1:A>` is not less than :g:`B <g1:B>`.

.. step:: assert

   It was proved not to be :eq:`equal <g1:A = g1:B>` either

.. step:: assert

   Therefore :g:`A <g1:A>` is greater than :g:`B <g1:B>`.

.. step:: assert

   Let :g:`C <g1:C>` have to :g:`B <g1:B>` a greater ratio than :g:`C <g1:C>` has to :g:`A <g1:A>`

.. step:: assert

   If not, it is either :eq:`equal <g1:B = g1:A>` or greater.

.. step:: assert

   Now :g:`B <g1:B>` is not :eq:`equal <g1:B = g1:A>` to :g:`A <g1:A>`

.. step:: assert ∵ equal_magnitudes_ratio <G.142>

   For in that case :g:`C <g1:C>` would have had the same ratio to each of the magnitudes :g:`A <g1:A>`, :g:`B <g1:B>`

.. step:: assert

   But it has not

.. step:: assert

   Therefore :g:`A <g1:A>` is not :eq:`equal <g1:A = g1:B>` to :g:`B <g1:B>`.

.. step:: assert

   Nor again is :g:`B <g1:B>` greater than :g:`A <g1:A>`

.. step:: assert ∵ unequal_magnitudes_greater <G.145>

   For in that case :g:`C <g1:C>` would have had to :g:`B <g1:B>` a less ratio than it has to :g:`A <g1:A>`

.. step:: assert

   But it has not

.. step:: assert

   Therefore :g:`B <g1:B>` is not greater than :g:`A <g1:A>`.

.. step:: assert

   It was proved that it is not :eq:`equal <g1:B = g1:A>` either

.. step:: conclude

   Therefore :g:`B <g1:B>` is less than :g:`A <g1:A>`.

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
     "G.147" [label="G.147", tooltip="G.147 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.142" -> "G.138";
     "G.147" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.147" -> "G.145";
   }

Required for
------------

:ref:`G.151 <G.151>`, :ref:`G.153 <G.153>`, :ref:`G.155 <G.155>`, :ref:`G.156 <G.156>`, :ref:`G.157 <G.157>`, :ref:`G.158 <G.158>`, :ref:`G.159 <G.159>`, :ref:`G.160 <G.160>`, :ref:`G.161 <G.161>`, :ref:`G.162 <G.162>`, :ref:`G.166 <G.166>`, :ref:`G.167 <G.167>`, :ref:`G.168 <G.168>`, :ref:`G.169 <G.169>`, :ref:`G.171 <G.171>`, :ref:`G.176 <G.176>`, :ref:`G.181 <G.181>`, :ref:`G.184 <G.184>`, :ref:`G.185 <G.185>`, :ref:`G.187 <G.187>`, :ref:`G.189 <G.189>`, :ref:`G.190 <G.190>`, :ref:`G.191 <G.191>`, :ref:`G.192 <G.192>`, :ref:`G.193 <G.193>`, :ref:`G.194 <G.194>`, :ref:`G.195 <G.195>`, :ref:`G.196 <G.196>`, :ref:`G.197 <G.197>`, :ref:`G.318 <G.318>`, :ref:`G.319 <G.319>`, :ref:`G.320 <G.320>`, :ref:`G.321 <G.321>`, :ref:`G.322 <G.322>`, :ref:`G.323 <G.323>`, :ref:`G.324 <G.324>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.336 <G.336>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.340 <G.340>`, :ref:`G.341 <G.341>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.351 <G.351>`, :ref:`G.352 <G.352>`, :ref:`G.353 <G.353>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.372 <G.372>`, :ref:`G.374 <G.374>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.424 <G.424>`, :ref:`G.425 <G.425>`, :ref:`G.426 <G.426>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.430 <G.430>`, :ref:`G.431 <G.431>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.468 <G.468>`, :ref:`G.473 <G.473>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.512 <G.512>`, :ref:`G.513 <G.513>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
