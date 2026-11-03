:canonical_id: G.147
:original_id: IV.1
:title: G.147 fit chord in circle
:volume: II
:book: IV
:type: prop

G.147 fit chord in circle — Heath
=================================

.. rubric:: `IV.1 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/01/>`_

.. enunciation::

   Into a given :term:`circle <G.10>` to fit a :term:`straight line <G.4>` equal to a given straight line which is not greater than the :term:`diameter <G.61>` of the circle.

Let :g:`( A B C ) <g1:( A B C )>` be the given circle, and :g:`D <g1:D>` the given straight
:term:`line <G.2>` not greater than the diameter
of the circle;
thus it is required to fit into the
circle :g:`( A B C ) <g1:( A B C )>` a straight line :eq:`equal <g1:/ C A / = g1:D>`
to the straight line :g:`D <g1:D>`.

.. picture:: g1.svg
   :alt: Diagram for Proposition 1

Let a diameter :g:`/ B C / <g1:/ B C />` of the
circle :g:`( A B C ) <g1:( A B C )>` be drawn.

Then, if :g:`/ B C / <g1:/ B C />` is :eq:`equal <g1:/ B C / = g1:D>` to :g:`D <g1:D>`,
that which was enjoined will have
been done; for :g:`/ B C / <g1:/ B C />` has been :term:`fitted into the circle <G.146>` :g:`( A B C ) <g1:( A B C )>` :eq:`equal <g1:/ B C / = g1:D>`
to the straight line :g:`D <g1:D>`.

But, if :g:`/ B C / <g1:/ B C />` is greater than :g:`D <g1:D>`,
let :g:`/ C E / <g1:/ C E />` be made :eq:`equal <g1:/ C E / = g1:D>` to :g:`D <g1:D>`, and with :term:`centre <G.11>` :g:`C <g1:C>` and distance
:g:`/ C E / <g1:/ C E />` let the circle :g:`( E A F ) <g1:( E A F )>` be described;
let :g:`/ C A / <g1:/ C A />` be joined.

Then, since the :term:`point <G.1>` :g:`C <g1:C>` is the centre of the circle :g:`( E A F ) <g1:( E A F )>`,

.. assertion::

   :g:`/ C A / <g1:/ C A />` is :eq:`equal <g1:/ C A / = g1:/ C E />` to :g:`/ C E / <g1:/ C E />`.

But :g:`/ C E / <g1:/ C E />` is :eq:`equal <g1:/ C E / = g1:D>` to :g:`D <g1:D>`;

.. assertion::

   therefore :g:`D <g1:D>` is also :eq:`equal <g1:D = g1:/ C A />` to :g:`/ C A / <g1:/ C A />`.

Therefore into the given circle :g:`( A B C ) <g1:( A B C )>` there has been fitted
:g:`/ C A / <g1:/ C A />` :eq:`equal <g1:/ C A / = g1:D>` to the given straight line :g:`D <g1:D>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.def.6): The extremities of a surface are lines or arcs.", fillcolor="#224422", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.def.15): A circle ( A B ) is a plane figure contained by one arc defined by a center A and a point B establishing its defining radius / A B /, such that all segments / A B /, / A C /, / A D...", fillcolor="#224422", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.post.3): Construct a circle ( A B ) with center A and defining radius point B.", fillcolor="#444422", URL="../G.15/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (IV.def.7): Asegment is said to befitted into a circle when itsextremities are on the arc of thecircle.", fillcolor="#224422", URL="../G.146/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (IV.1): Into a given circle to fit a segment equal to a given segment which is not greater than the diameter of the circle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.11" -> "G.1";
     "G.14" -> "G.1";
     "G.15" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.146" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.14" -> "G.4";
     "G.61" -> "G.4";
     "G.146" -> "G.4";
     "G.147" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.146" -> "G.6";
     "G.10" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.61" -> "G.10";
     "G.146" -> "G.10";
     "G.147" -> "G.10";
     "G.15" -> "G.11";
     "G.61" -> "G.11";
     "G.147" -> "G.14";
     "G.147" -> "G.15";
     "G.147" -> "G.61";
     "G.147" -> "G.146";
   }

Required for
------------

:ref:`G.162 <G.162>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.385 <G.385>`, :ref:`G.390 <G.390>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.528 <G.528>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`
