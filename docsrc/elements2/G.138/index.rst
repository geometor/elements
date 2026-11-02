:order: 138
:number: 138
:canonical_id: G.138
:original_id: III.def.8
:title: G.138 angle in a circle segment
:volume: II
:book: III
:type: def
:categories: definition, plane-geometry, circles
:category: definition, plane-geometry, circles
:tags: book-iii, angle-in-segment, plane-angle, point, straight-line, extremity, base-of-segment, arc, plane
:dependencies: G.1, G.3, G.4, G.22
:excerpt: Anangle in a segment is theangle which, when apoint is taken on the arc of the segment andsegments are joined from it to theextremities of the segment which is thebase of the segment, is contained by the segments so joined.

.. _G.138:
.. _III.def.8:

G.138 angle in a circle segment
===============================

.. rubric:: `III.def.8 <https://geometor.github.io/euclid/heath/volume_II/book_iii/definitions/#iii-def-8>`_

.. enunciation::

   An:term:`**angle in a segment** <angle-in-segment>` is the:term:`angle <G.22>` which, when a:term:`point <G.1>` is taken on the arc of the segment and:term:`segments <G.4>` are joined from it to the:term:`extremities <G.6>` of the segment which is the:term:`**base of the segment** <base-of-segment>`, is contained by the segments so joined.

.. signature:: def

   | :fn:`angle_segment_angle_def <G.138>`

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
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (III.def.8): Anangle in a segment is theangle which, when apoint is taken on the arc of the segment andsegments are joined from it to theextremities of the segment which is thebase of the segme...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.138" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.138" -> "G.3";
     "G.7" -> "G.4";
     "G.22" -> "G.4";
     "G.138" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.138" -> "G.22";
   }

Required for
------------

:ref:`G.139 <G.139>`, :ref:`G.140 <G.140>`, :ref:`G.141 <G.141>`, :ref:`G.142 <G.142>`, :ref:`G.149 <G.149>`, :ref:`G.157 <G.157>`, :ref:`G.158 <G.158>`, :ref:`G.162 <G.162>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.223 <G.223>`, :ref:`G.237 <G.237>`, :ref:`G.240 <G.240>`, :ref:`G.241 <G.241>`, :ref:`G.243 <G.243>`, :ref:`G.385 <G.385>`, :ref:`G.390 <G.390>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.528 <G.528>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.590 <G.590>`, :ref:`G.592 <G.592>`, :ref:`G.594 <G.594>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   heath
