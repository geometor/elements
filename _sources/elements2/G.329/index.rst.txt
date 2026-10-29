:order: 329
:number: 329
:canonical_id: G.329
:original_id: X.16
:volume: III
:book: X
:type: prop
:subtype: theorem
:categories: theorem, proof, incommensurables, magnitudes
:category: theorem, proof, incommensurables, magnitudes
:tags: book-x, point, segment, quadrilateral, incommensurable, equality, reductio-ad-absurdum, lemma
:dependencies: G.314
:excerpt: If two incommensurable magnitudes be added together, the whole is incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes is incommensurable.

.. _G.329:
.. _X.16:

G.329
=====

.. rubric:: `X.16 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/016/>`_

.. enunciation::

   If two incommensurable magnitudes be added together, the whole is incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes is incommensurable.

.. picture:: g1.svg
   :alt: Proposition 16 Diagram

.. enunciation::

   If to any straight line there be applied a parallelogram deficient by a square figure, the applied parallelogram is equal to the rectangle contained by the segments of the straight line resulting from the application.

.. picture:: g2.svg
   :alt: Lemma Diagram

.. step:: assert

   For let the two incommensurable magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` be added together

.. step:: assert

   If :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are not incommensurable, some magnitude will measure them. Let it measure them, if possible

.. step:: assert

   Let it be :g:`D <g1:D>`.

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

.. step:: assert [G.314] <G.314>

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

   If they are commensurable, some magnitude will measure them. Let it measure them

.. step:: assert

   Let it be :g:`D <g1:D>`.

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

.. step:: assert [G.314] <G.314>

   Therefore no magnitude will measure :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`; therefore :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are incommensurable.

.. step:: assert

   LEMMA. ~~~~~~

.. step:: construct

   For let there be applied to :g:`/ A B / <g2:/ A B />` the parallelogram :g:`< A C D E > <g2:< A C D E >>` deficient by the square figure :g:`< C B F D > <g2:< C B F D >>`

.. step:: assert

   This is indeed at once manifest

.. step:: assert

   For, since :g:`< C B F D > <g2:< C B F D >>` is a square,

.. step:: assert

   :g:`/ C D / <g2:/ C D />` is :eq:`equal <g2:/ C D / = g2:/ C B />` to :g:`/ C B / <g2:/ C B />`;

.. step:: conclude

   And :g:`< A C D E > <g2:< A C D E >>` is the rectangle :g:`/ A C / <g2:/ A C />`, :g:`/ C D / <g2:/ C D />`, that is, the rectangle :g:`/ A C / <g2:/ A C />`, :g:`/ C B / <g2:/ C B />`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.314" [label="G.314", tooltip="G.314 (X.def.1): Those magnitudes are said to becommensurable which are measured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.314/index.html", target="_top"];
     "G.329" [label="G.329", tooltip="G.329 (X.16): If two incommensurable magnitudes be added together, the whole is incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.329" -> "G.314";
   }

Required for
------------

:ref:`G.331 <G.331>`, :ref:`G.341 <G.341>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.351 <G.351>`, :ref:`G.352 <G.352>`, :ref:`G.353 <G.353>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.372 <G.372>`, :ref:`G.374 <G.374>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.395 <G.395>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.424 <G.424>`, :ref:`G.425 <G.425>`, :ref:`G.426 <G.426>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.430 <G.430>`, :ref:`G.431 <G.431>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.513 <G.513>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`

.. toctree::
   :hidden:

   code
   heath
