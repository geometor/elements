:order: 387
:number: 387
:canonical_id: G.387
:original_id: X.15
:title: G.387 commensurable magnitudes added
:volume: III
:book: X
:type: prop
:subtype: theorem
:categories: theorem, proof, incommensurables, magnitudes
:category: theorem, proof, incommensurables, magnitudes
:tags: book-x, point, segment, commensurable, part-aliquot
:dependencies: G.169, G.372
:excerpt: If two commensurable magnitudes be added together, the whole is commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes is commensurable.

.. _G.387:
.. _X.15:

G.387 commensurable magnitudes added
====================================

.. rubric:: `X.15 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/015/>`_

.. enunciation::

   If two :term:`commensurable <G.372>` magnitudes be added together, the whole is commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes is commensurable.

.. signature:: theorem

   | :fn:`commensurable_magnitudes_added <G.387>`\ ()
   | **prove** :g:`/ A C / <g1:/ A C />` is also commensurable with each of the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`; :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are also commensurable

.. picture:: g1.svg
   :alt: Proposition 15 Diagram

.. step:: construct

   Let the two commensurable magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` be added together

.. step:: assert

   :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are commensurable, some magnitude will measure them

.. step:: assert

   Let it :term:`measure <G.169>` them, and let it be :g:`D <g1:D>`

.. step:: assert

   then :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, it will also measure :g:`/ A C / <g1:/ A C />`

.. step:: assert

   It measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` also

.. step:: assert ∵ magnitudes_said_commensurable_def <G.372>

   :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ A C / <g1:/ A C />`; therefore :g:`/ A C / <g1:/ A C />` is commensurable with each of the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`

.. step:: assert

   Next, let :g:`/ A C / <g1:/ A C />` be commensurable with :g:`/ A B / <g1:/ A B />`

.. step:: assert

   :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are commensurable, some magnitude will measure them

.. step:: assert

   Let it measure them, and let it be :g:`D <g1:D>`

.. step:: assert

   then :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`, it will also measure :g:`/ B C / <g1:/ B C />`

.. step:: assert

   It measures :g:`/ A B / <g1:/ A B />` also

.. step:: conclude ∵ magnitudes_said_commensurable_def <G.372>

   :g:`D <g1:D>` will measure :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`; therefore :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are commensurable

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
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.372" [label="G.372", tooltip="G.372 (X.def.1): Those magnitudes are said to becommensurable which aremeasured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.372/index.html", target="_top"];
     "G.387" [label="G.387", tooltip="G.387 (X.15): If two commensurable magnitudes be added together, the whole is commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes is com...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.253" -> "G.169";
     "G.372" -> "G.169";
     "G.387" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.372" -> "G.253";
     "G.387" -> "G.372";
   }

Required for
------------

:ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
