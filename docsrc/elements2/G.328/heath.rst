:canonical_id: G.328
:original_id: X.15
:volume: III
:book: X
:type: prop

G.328 — Heath
=============

.. rubric:: `X.15 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/015/>`_

.. enunciation::

   If two commensurable magnitudes be added together, the whole will also be commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes will also be commensurable.

For let the two commensurable magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` be added together; I say that the whole :g:`/ A C / <g1:/ A C />` is also commensurable with each of the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. picture:: g1.svg
   :alt: Proposition 15 Diagram

For, since :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are commensurable, some magnitude will measure them. Let it measure them, and let it be :g:`D <g1:D>`.

.. assertion::

   Since then :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, it will also measure the whole :g:`/ A C / <g1:/ A C />`.

.. subclause::

   But it measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` also;

.. assertion::

   therefore :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ A C / <g1:/ A C />`; therefore :g:`/ A C / <g1:/ A C />` is commensurable with each of the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`. :just:`[G.314] <G.314>`

Next, let :g:`/ A C / <g1:/ A C />` be commensurable with :g:`/ A B / <g1:/ A B />`; I say that :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are also commensurable.

For, since :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are commensurable, some magnitude will measure them. Let it measure them, and let it be :g:`D <g1:D>`.

.. assertion::

   Since then :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`, it will also measure the remainder :g:`/ B C / <g1:/ B C />`.

.. subclause::

   But it measures :g:`/ A B / <g1:/ A B />` also;

.. assertion::

   therefore :g:`D <g1:D>` will measure :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`; therefore :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are commensurable. :just:`[G.314] <G.314>`

.. qed::

   Therefore etc.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.314" [label="G.314", tooltip="G.314 (X.def.1): Those magnitudes are said to becommensurable which are measured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.314/index.html", target="_top"];
     "G.328" [label="G.328", tooltip="G.328 (X.15): If two commensurable magnitudes be added together, the whole is commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes is com...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.328" -> "G.314";
   }

Required for
------------

:ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.351 <G.351>`, :ref:`G.352 <G.352>`, :ref:`G.353 <G.353>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.372 <G.372>`, :ref:`G.374 <G.374>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.424 <G.424>`, :ref:`G.425 <G.425>`, :ref:`G.426 <G.426>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.430 <G.430>`, :ref:`G.431 <G.431>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.513 <G.513>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`
