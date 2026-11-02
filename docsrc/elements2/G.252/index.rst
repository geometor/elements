:order: 252
:number: 252
:canonical_id: G.252
:original_id: VII.3
:title: G.252 numbers prime find
:volume: II
:book: VII
:type: prop
:subtype: problem
:categories: problem, finding, number-theory
:category: problem, finding, number-theory
:tags: book-vii, point, number, prime-to-one-another, part-aliquot, prime, reductio-ad-absurdum
:dependencies: G.169, G.248, G.249, G.251
:excerpt: Given three numbers not prime to one another, to find their greatest common measure.

.. _G.252:
.. _VII.3:

G.252 numbers prime find
========================

.. rubric:: `VII.3 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/03/>`_

.. enunciation::

   Given three :term:`numbers <G.248>` not :term:`prime to one another <G.249>`, to find their greatest common :term:`measure <G.169>`.

.. signature:: problem

   | :fn:`numbers_prime_find_vii_3 <G.252>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`E <g1:E>`
   | **given** :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` be the three given numbers not prime to one another
   | **construct** :g:`E <g1:E>` is the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`

.. picture:: g1.svg
   :alt: Proposition 3 Diagram

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` be the three given numbers not prime to one another

.. step:: construct

   :fn:`numbers_prime_find <G.251>`: Let the greatest common measure, :g:`D <g1:D>`, of the two numbers :g:`A <g1:A>`, :g:`B <g1:B>` be taken

.. step:: assert

   Then :g:`D <g1:D>` either measures, or does not measure, :g:`C <g1:C>`.

.. step:: assert

   First, let it measure it.

.. step:: assert

   It measures :g:`A <g1:A>`, :g:`B <g1:B>` also ;

.. step:: assert

   Therefore :g:`D <g1:D>` measures :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` ;

.. step:: assert

   Therefore :g:`D <g1:D>` is a common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. step:: assert

   If :g:`D <g1:D>` is not the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, some number which is greater than :g:`D <g1:D>` will measure the numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. step:: assert

   Let such a number measure them, and let it be :g:`E <g1:E>`.

.. step:: assert

   Since then :g:`E <g1:E>` measures :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, it will also measure :g:`A <g1:A>`, :g:`B <g1:B>` ;

.. step:: assert ∵ numbers_prime_find <G.251>

   Therefore it will also measure the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`.

.. step:: assert

   The greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>` is :g:`D <g1:D>` ;

.. step:: assert

   Therefore :g:`E <g1:E>` measures :g:`D <g1:D>`, the greater the less : which is impossible.

.. step:: assert

   Therefore no number which is greater than :g:`D <g1:D>` will measure the numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` ;

.. step:: assert

   Therefore :g:`D <g1:D>` is the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. step:: assert

   Next, let :g:`D <g1:D>` not measure :g:`C <g1:C>`

.. step:: assert

   I say first that :g:`C <g1:C>`, :g:`D <g1:D>` are not prime to one another.

.. step:: assert

   Since :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` are not prime to one another, some number will measure them.

.. step:: assert ∵ numbers_prime_find <G.251>

   Now that which measures :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` will also measure :g:`A <g1:A>`, :g:`B <g1:B>`, and will measure :g:`D <g1:D>`, the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`.

.. step:: assert

   It measures :g:`C <g1:C>` also ;

.. step:: assert

   Therefore some number will measure the numbers :g:`D <g1:D>`, :g:`C <g1:C>` ;

.. step:: assert

   Therefore :g:`D <g1:D>`, :g:`C <g1:C>` are not prime to one another.

.. step:: construct

   :fn:`numbers_prime_find <G.251>`: Let then their greatest common measure :g:`E <g1:E>` be taken.

.. step:: assert

   Since :g:`E <g1:E>` measures :g:`D <g1:D>`, and :g:`D <g1:D>` measures :g:`A <g1:A>`, :g:`B <g1:B>`,

.. step:: assert

   Therefore :g:`E <g1:E>` also measures :g:`A <g1:A>`, :g:`B <g1:B>`.

.. step:: assert

   It measures :g:`C <g1:C>` also ;

.. step:: assert

   Therefore :g:`E <g1:E>` measures :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` ;

.. step:: assert

   Therefore :g:`E <g1:E>` is a common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. step:: assert

   I say next that it is also the greatest.

.. step:: assert

   If :g:`E <g1:E>` is not the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, some number which is greater than :g:`E <g1:E>` will measure the numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. step:: assert

   Let such a number measure them, and let it be :g:`F <g1:F>`.

.. step:: assert

   Since :g:`F <g1:F>` measures :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, it also measures :g:`A <g1:A>`, :g:`B <g1:B>` ;

.. step:: assert ∵ numbers_prime_find <G.251>

   Therefore it will also measure the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`.

.. step:: assert

   The greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>` is :g:`D <g1:D>` ;

.. step:: assert

   Therefore :g:`F <g1:F>` measures :g:`D <g1:D>`.

.. step:: assert

   It measures :g:`C <g1:C>` also ;

.. step:: assert

   Therefore :g:`F <g1:F>` measures :g:`D <g1:D>`, :g:`C <g1:C>` ;

.. step:: assert ∵ numbers_prime_find <G.251>

   Therefore it will also measure the greatest common measure of :g:`D <g1:D>`, :g:`C <g1:C>`.

.. step:: assert

   The greatest common measure of :g:`D <g1:D>`, :g:`C <g1:C>` is :g:`E <g1:E>` ;

.. step:: assert

   Therefore :g:`F <g1:F>` measures :g:`E <g1:E>`, the greater the less : which is impossible.

.. step:: assert

   Therefore no number which is greater than :g:`E <g1:E>` will measure the numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` ;

.. step:: conclude

   Therefore :g:`E <g1:E>` is the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.249" [label="G.249", tooltip="G.249 (VII.def.12): Numbers prime to one another are those which aremeasured by anunit alone as a common measure.", fillcolor="#224422", URL="../G.249/index.html", target="_top"];
     "G.250" [label="G.250", tooltip="G.250 (VII.1): Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is...", fillcolor="#222244", URL="../G.250/index.html", target="_top"];
     "G.251" [label="G.251", tooltip="G.251 (VII.2): Given two numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.251/index.html", target="_top"];
     "G.252" [label="G.252", tooltip="G.252 (VII.3): Given three numbers not prime to one another, to find their greatest common measure.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.249" -> "G.169";
     "G.250" -> "G.169";
     "G.251" -> "G.169";
     "G.252" -> "G.169";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.250" -> "G.247";
     "G.250" -> "G.248";
     "G.251" -> "G.248";
     "G.252" -> "G.248";
     "G.250" -> "G.249";
     "G.251" -> "G.249";
     "G.252" -> "G.249";
     "G.251" -> "G.250";
     "G.252" -> "G.251";
   }

Required for
------------

:ref:`G.289 <G.289>`, :ref:`G.290 <G.290>`, :ref:`G.292 <G.292>`, :ref:`G.295 <G.295>`, :ref:`G.298 <G.298>`, :ref:`G.299 <G.299>`, :ref:`G.301 <G.301>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`, :ref:`G.305 <G.305>`, :ref:`G.314 <G.314>`, :ref:`G.315 <G.315>`, :ref:`G.316 <G.316>`, :ref:`G.317 <G.317>`, :ref:`G.322 <G.322>`, :ref:`G.323 <G.323>`, :ref:`G.324 <G.324>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.328 <G.328>`, :ref:`G.329 <G.329>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.332 <G.332>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.337 <G.337>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`, :ref:`G.381 <G.381>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
