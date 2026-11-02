:order: 388
:number: 388
:canonical_id: G.388
:original_id: X.16
:title: G.388 incommensurable magnitudes added
:volume: III
:book: X
:type: prop
:subtype: theorem
:categories: theorem, proof, incommensurables, magnitudes
:category: theorem, proof, incommensurables, magnitudes
:tags: book-x, point, segment, quadrilateral, incommensurable, part-aliquot, straight-line, square, figure, contained-rectangle, equality, reductio-ad-absurdum, lemma
:dependencies: G.4, G.9, G.63, G.81, G.372
:excerpt: If two incommensurable magnitudes be added together, the whole is incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes is incommensurable.

.. _G.388:
.. _X.16:

G.388 incommensurable magnitudes added
======================================

.. rubric:: `X.16 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/016/>`_

.. enunciation::

   If two :term:`incommensurable <G.372>` magnitudes be added together, the whole is incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes is incommensurable.

.. signature:: theorem

   | :fn:`incommensurable_magnitudes_added <G.388>`\ ()
   | **prove** the whole :g:`/ A C / <g1:/ A C />` is also incommensurable with each of the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`; :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are also incommensurable; :g:`< A C D E > <g2:< A C D E >>` is equal to the rectangle contained by :g:`/ A C / <g2:/ A C />`, :g:`/ C B / <g2:/ C B />`

.. picture:: g1.svg
   :alt: Proposition 16 Diagram

.. picture:: g2.svg
   :alt: Lemma Diagram

.. step:: construct

   Let the two incommensurable magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` be added together

.. step:: assert

   If :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are not incommensurable, some magnitude will :term:`measure <G.169>` them

.. step:: assert

   Let it measure them, if possible, and let it be :g:`D <g1:D>`.

.. step:: assert

   Since then :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`,

.. step:: assert

   Therefore it will also measure the remainder :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   It measures :g:`/ A B / <g1:/ A B />` also;

.. step:: assert

   Therefore :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are commensurable;

.. step:: assert

   But they were also, by hypothesis, incommensurable:

.. step:: assert

   Which is impossible.

.. step:: assert ∵ magnitudes_said_commensurable_def <G.372>

   Therefore no magnitude will measure :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`; therefore :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are incommensurable.

.. step:: assert

   Similarly we can prove that :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` are also incommensurable.

.. step:: assert

   Therefore :g:`/ A C / <g1:/ A C />` is incommensurable with each of the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   Next, let :g:`/ A C / <g1:/ A C />` be incommensurable with one of the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   First, let it be incommensurable with :g:`/ A B / <g1:/ A B />`

.. step:: assert

   If they are commensurable, some magnitude will measure them

.. step:: assert

   Let it measure them, and let it be :g:`D <g1:D>`.

.. step:: assert

   Since then :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`,

.. step:: assert

   Therefore it will also measure the whole :g:`/ A C / <g1:/ A C />`.

.. step:: assert

   It measures :g:`/ A B / <g1:/ A B />` also;

.. step:: assert

   Therefore :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`.

.. step:: assert

   Therefore :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are commensurable;

.. step:: assert

   But they were also, by hypothesis, incommensurable:

.. step:: assert

   Which is impossible.

.. step:: assert ∵ magnitudes_said_commensurable_def <G.372>

   Therefore no magnitude will measure :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`; therefore :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are incommensurable.

.. step:: assert

   LEMMA. ~~~~~~

.. step:: construct

   Let there be applied to :g:`/ A B / <g2:/ A B />` the parallelogram :g:`< A C D E > <g2:< A C D E >>` deficient by the :term:`square <G.63>` :term:`figure <G.9>` :g:`< C B F D > <g2:< C B F D >>`

.. step:: assert

   This is indeed at once manifest

.. step:: assert

   For, since :g:`< C B F D > <g2:< C B F D >>` is a square,

.. step:: assert

   :g:`/ C D / <g2:/ C D />` is :eq:`equal <g2:/ C D / = g2:/ C B />` to :g:`/ C B / <g2:/ C B />`;

.. step:: conclude

   And :g:`< A C D E > <g2:< A C D E >>` is the :term:`rectangle <G.81>` :g:`/ A C / <g2:/ A C />`, :g:`/ C D / <g2:/ C D />`, that is, the rectangle :g:`/ A C / <g2:/ A C />`, :g:`/ C B / <g2:/ C B />`.

.. enunciation::

   If to any :term:`straight line <G.4>` there be applied a parallelogram deficient by a square figure, the applied parallelogram is equal to the rectangle contained by the segments of the straight line resulting from the application.

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
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.81" [label="G.81", tooltip="G.81 (II.def.1): Any rectangular parallelogram is said to becontained by the twosegments containing theright angle.", fillcolor="#224422", URL="../G.81/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.372" [label="G.372", tooltip="G.372 (X.def.1): Those magnitudes are said to becommensurable which aremeasured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.372/index.html", target="_top"];
     "G.388" [label="G.388", tooltip="G.388 (X.16): If two incommensurable magnitudes be added together, the whole is incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.11" -> "G.4";
     "G.22" -> "G.4";
     "G.32" -> "G.4";
     "G.81" -> "G.4";
     "G.388" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.388" -> "G.9";
     "G.12" -> "G.11";
     "G.63" -> "G.11";
     "G.63" -> "G.12";
     "G.32" -> "G.22";
     "G.63" -> "G.22";
     "G.81" -> "G.32";
     "G.388" -> "G.63";
     "G.388" -> "G.81";
     "G.372" -> "G.169";
     "G.388" -> "G.372";
   }

Required for
------------

:ref:`G.390 <G.390>`, :ref:`G.400 <G.400>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.455 <G.455>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
