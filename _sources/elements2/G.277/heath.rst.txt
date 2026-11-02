:canonical_id: G.277
:original_id: VII.23
:title: G.277 numbers prime number
:volume: II
:book: VII
:type: prop

G.277 numbers prime number — Heath
==================================

.. rubric:: `VII.23 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/23/>`_

.. enunciation::

   If two :term:`numbers <G.248>` be :term:`prime to one another <G.249>`, the number which :term:`measures <G.253>` the one of them will be prime to the remaining number.

Let :g:`A <g1:A>`, :g:`B <g1:B>` be two numbers prime to one another, and let any number :g:`C <g1:C>` measure :g:`A <g1:A>`;

I say that :g:`C <g1:C>`, :g:`B <g1:B>` are also prime to one another.

.. picture:: g1.svg
   :alt: Book VII, Proposition 23

.. subclause::

   For, if :g:`C <g1:C>`, :g:`B <g1:B>` are not prime to one another, some number will measure :g:`C <g1:C>`, :g:`B <g1:B>`.

Let a number measure them, and let it be :g:`D <g1:D>`.

.. subclause::

   Since :g:`D <g1:D>` measures :g:`C <g1:C>`, and :g:`C <g1:C>` measures :g:`A <g1:A>`,

.. assertion::

   therefore :g:`D <g1:D>` also measures :g:`A <g1:A>`.

.. subclause::

   But it also measures :g:`B <g1:B>` ;

.. assertion::

   therefore :g:`D <g1:D>` measures :g:`A <g1:A>`, :g:`B <g1:B>` which are prime to one another : which is impossible. :just:`[G.249] <G.249>`

.. assertion::

   Therefore no number will measure the numbers :g:`C <g1:C>`, :g:`B <g1:B>`.

.. assertion::

   Therefore :g:`C <g1:C>`, :g:`B <g1:B>` are prime to one another.

.. qed::

   :just:`Q. E. D.`

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
     "G.277" [label="G.277", tooltip="G.277 (VII.23): If two numbers be prime to one another, the number which measures the one of them is prime to the remaining number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.249" -> "G.169";
     "G.277" -> "G.169";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.277" -> "G.248";
     "G.277" -> "G.249";
   }

Required for
------------

:ref:`G.278 <G.278>`, :ref:`G.279 <G.279>`, :ref:`G.280 <G.280>`, :ref:`G.281 <G.281>`, :ref:`G.297 <G.297>`, :ref:`G.298 <G.298>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`, :ref:`G.305 <G.305>`, :ref:`G.306 <G.306>`, :ref:`G.314 <G.314>`, :ref:`G.315 <G.315>`, :ref:`G.316 <G.316>`, :ref:`G.317 <G.317>`, :ref:`G.323 <G.323>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.328 <G.328>`, :ref:`G.329 <G.329>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.332 <G.332>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.337 <G.337>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.345 <G.345>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`, :ref:`G.381 <G.381>`, :ref:`G.383 <G.383>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`
