:order: 177
:number: 177
:canonical_id: G.177
:original_id: V.4
:title: G.177 magnitude ratio equimultiples
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, in-the-same-ratio, multiple, ratio, equality
:dependencies: G.170, G.175, G.176
:excerpt: If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples whatever of the second and fourth respectively, taken in corresponding order.

.. _G.177:
.. _V.4:

G.177 magnitude ratio equimultiples
===================================

.. rubric:: `V.4 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/04/>`_

.. enunciation::

   If a first magnitude have to a second the :term:`same ratio <G.176>` as a third to a fourth, any :term:`equimultiples <G.170>` whatever of the first and third will also have the same ratio to any equimultiples whatever of the second and fourth respectively, taken in corresponding order.

.. signature:: theorem

   | :fn:`magnitude_ratio_equimultiples <G.177>`\ ()
   | **prove** as :g:`E <g1:E>` is to :g:`G <g1:G>`, so is :g:`F <g1:F>` to :g:`H <g1:H>`

.. picture:: g1.svg
   :alt: Proposition 4 diagram

.. step:: assert

   Let a first magnitude :g:`A <g1:A>` have to a second :g:`B <g1:B>` the same ratio as a third :g:`C <g1:C>` to a fourth :g:`D <g1:D>`

.. step:: construct

   And let equimultiples :g:`E <g1:E>`, :g:`F <g1:F>` be taken of :g:`A <g1:A>`, :g:`C <g1:C>`, and :g:`G <g1:G>`, :g:`H <g1:H>` other, chance, equimultiples of :g:`B <g1:B>`, :g:`D <g1:D>`

.. step:: assert

   I say that, as :g:`E <g1:E>` is to :g:`G <g1:G>`, so is :g:`F <g1:F>` to :g:`H <g1:H>`

.. step:: construct

   Let equimultiples :g:`K <g1:K>`, :g:`L <g1:L>` be taken of :g:`E <g1:E>`, :g:`F <g1:F>`, and other, chance, equimultiples :g:`M <g1:M>`, :g:`N <g1:N>` of :g:`G <g1:G>`, :g:`H <g1:H>`.

.. step:: assert ∵ magnitude_multiple_equimultiples <G.175>

   :g:`E <g1:E>` is the same multiple of :g:`A <g1:A>` that :g:`F <g1:F>` is of :g:`C <g1:C>`, and equimultiples :g:`K <g1:K>`, :g:`L <g1:L>` of :g:`E <g1:E>`, :g:`F <g1:F>` have been taken → therefore :g:`K <g1:K>` is the same multiple of :g:`A <g1:A>` that :g:`L <g1:L>` is of :g:`C <g1:C>`

.. step:: assert

   The same reason

.. step:: assert

   :g:`M <g1:M>` is the same multiple of :g:`B <g1:B>` that :g:`N <g1:N>` is of :g:`D <g1:D>`

.. step:: assert

   since, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`C <g1:C>` to :g:`D <g1:D>`, and of :g:`A <g1:A>`, :g:`C <g1:C>` equimultiples :g:`K <g1:K>`, :g:`L <g1:L>` have been taken, and of :g:`B <g1:B>`, :g:`D <g1:D>` other, chance, equimultiples :g:`M <g1:M>`, :g:`N <g1:N>`,

.. step:: assert ∵ magnitudes_said_ratio_def <G.176>

   if :g:`K <g1:K>` is in excess of :g:`M <g1:M>`, :g:`L <g1:L>` also is in excess of :g:`N <g1:N>`, if it is :eq:`= <g1:K = g1:M>`, :eq:`= <g1:L = g1:N>`, and if less, less

.. step:: assert

   :g:`K <g1:K>`, :g:`L <g1:L>` are equimultiples of :g:`E <g1:E>`, :g:`F <g1:F>`, and :g:`M <g1:M>`, :g:`N <g1:N>` other, chance, equimultiples of :g:`G <g1:G>`, :g:`H <g1:H>`

.. step:: conclude ∵ magnitudes_said_ratio_def <G.176>

   as :g:`E <g1:E>` is to :g:`G <g1:G>`, so is :g:`F <g1:F>` to :g:`H <g1:H>`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.172" [label="G.172", tooltip="G.172 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.172/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.174" [label="G.174", tooltip="G.174 (V.def.17): Aratioex aequali arises when, there being several magnitudes and another set equal to them in multitude which taken two and two are in the same proportion, as the first is to the l...", fillcolor="#224422", URL="../G.174/index.html", target="_top"];
     "G.175" [label="G.175", tooltip="G.175 (V.3): If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then also ex aequali the magnitudes taken i...", fillcolor="#222244", URL="../G.175/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.177" [label="G.177", tooltip="G.177 (V.4): If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples wh...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.172" -> "G.170";
     "G.175" -> "G.170";
     "G.176" -> "G.170";
     "G.177" -> "G.170";
     "G.175" -> "G.172";
     "G.174" -> "G.173";
     "G.175" -> "G.174";
     "G.177" -> "G.175";
     "G.177" -> "G.176";
   }

Required for
------------

:ref:`G.205 <G.205>`, :ref:`G.207 <G.207>`, :ref:`G.213 <G.213>`, :ref:`G.214 <G.214>`, :ref:`G.215 <G.215>`, :ref:`G.216 <G.216>`, :ref:`G.218 <G.218>`, :ref:`G.223 <G.223>`, :ref:`G.229 <G.229>`, :ref:`G.232 <G.232>`, :ref:`G.234 <G.234>`, :ref:`G.236 <G.236>`, :ref:`G.237 <G.237>`, :ref:`G.238 <G.238>`, :ref:`G.239 <G.239>`, :ref:`G.240 <G.240>`, :ref:`G.241 <G.241>`, :ref:`G.243 <G.243>`, :ref:`G.244 <G.244>`, :ref:`G.245 <G.245>`, :ref:`G.376 <G.376>`, :ref:`G.377 <G.377>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.386 <G.386>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.395 <G.395>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.528 <G.528>`, :ref:`G.536 <G.536>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.584 <G.584>`, :ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.592 <G.592>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
