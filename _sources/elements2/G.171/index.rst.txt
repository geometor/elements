:order: 171
:number: 171
:canonical_id: G.171
:original_id: V.1
:title: G.171 there number magnitudes
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, segment, multiple, number, equality
:dependencies: G.170
:excerpt: If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, that multiple also will all be of all.

.. _G.171:
.. _V.1:

G.171 there number magnitudes
=============================

.. rubric:: `V.1 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/01/>`_

.. enunciation::

   If there be any number of magnitudes whatever which are, respectively, :term:`equimultiples <G.170>` of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, that multiple also will all be of all.

.. signature:: theorem

   | :fn:`there_number_magnitudes <G.171>`\ (:g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, :g:`E <g1:E>`, :g:`F <g1:F>`)
   | **given** any number of magnitudes whatever :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` be respectively equimultiples of any magnitudes :g:`E <g1:E>`, :g:`F <g1:F>` equal in multitude
   | **prove** whatever multiple :g:`/ A B / <g1:/ A B />` is of :g:`E <g1:E>`, that multiple will :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` also be of :g:`E <g1:E>`, :g:`F <g1:F>`

.. picture:: g1.svg
   :alt: Proposition 1 diagram

.. step:: given

   any number of magnitudes whatever :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` be respectively equimultiples of any magnitudes :g:`E <g1:E>`, :g:`F <g1:F>` equal in multitude

.. step:: assert

   I say that, whatever multiple :g:`/ A B / <g1:/ A B />` is of :g:`E <g1:E>`, that multiple will :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` also be of :g:`E <g1:E>`, :g:`F <g1:F>`.

.. step:: assert

   Since :g:`/ A B / <g1:/ A B />` is the same multiple of :g:`E <g1:E>` that :g:`/ C D / <g1:/ C D />` is of :g:`F <g1:F>`, as many magnitudes as there are in :g:`/ A B / <g1:/ A B />` equal to :g:`E <g1:E>`, so many also are there in :g:`/ C D / <g1:/ C D />` equal to :g:`F <g1:F>`.

.. step:: assert

   Let :g:`/ A B / <g1:/ A B />` be divided into the magnitudes :g:`/ A G / <g1:/ A G />`, :g:`/ G B / <g1:/ G B />` :eq:`equal <g1:/ A G / = g1:/ G B / = g1:E>` to :g:`E <g1:E>`, and :g:`/ C D / <g1:/ C D />` into :g:`/ C H / <g1:/ C H />`, :g:`/ H D / <g1:/ H D />` :eq:`equal <g1:/ C H / = g1:/ H D / = g1:F>` to :g:`F <g1:F>`

.. step:: assert

   Then the multitude of the magnitudes :g:`/ A G / <g1:/ A G />`, :g:`/ G B / <g1:/ G B />` will be equal to the multitude of the magnitudes :g:`/ C H / <g1:/ C H />`, :g:`/ H D / <g1:/ H D />`.

.. step:: assert

   Since :g:`/ A G / <g1:/ A G />` is :eq:`equal <g1:/ A G / = g1:E; g1:/ C H / = g1:F>` to :g:`E <g1:E>`, and :g:`/ C H / <g1:/ C H />` to :g:`F <g1:F>` → therefore :g:`/ A G / <g1:/ A G />` is :eq:`equal <g1:/ A G / = g1:E>` to :g:`E <g1:E>`, and :g:`/ A G / <g1:/ A G />`, :g:`/ C H / <g1:/ C H />` to :g:`E <g1:E>`, :g:`F <g1:F>`.

.. step:: assert

   The same reason

.. step:: assert

   :g:`/ G B / <g1:/ G B />` is :eq:`equal <g1:/ G B / = g1:E>` to :g:`E <g1:E>`, and :g:`/ G B / <g1:/ G B />`, :g:`/ H D / <g1:/ H D />` to :g:`E <g1:E>`, :g:`F <g1:F>`;

.. step:: assert

   Therefore, as many magnitudes as there are in :g:`/ A B / <g1:/ A B />` equal to :g:`E <g1:E>`, so many also are there in :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` equal to :g:`E <g1:E>`, :g:`F <g1:F>`;

.. step:: conclude

   Therefore, whatever multiple :g:`/ A B / <g1:/ A B />` is of :g:`E <g1:E>`, that multiple will :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` also be of :g:`E <g1:E>`, :g:`F <g1:F>`.

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
     "G.171" [label="G.171", tooltip="G.171 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.171" -> "G.170";
   }

Required for
------------

:ref:`G.178 <G.178>`, :ref:`G.186 <G.186>`, :ref:`G.187 <G.187>`, :ref:`G.188 <G.188>`, :ref:`G.190 <G.190>`, :ref:`G.192 <G.192>`, :ref:`G.193 <G.193>`, :ref:`G.195 <G.195>`, :ref:`G.198 <G.198>`, :ref:`G.199 <G.199>`, :ref:`G.201 <G.201>`, :ref:`G.202 <G.202>`, :ref:`G.204 <G.204>`, :ref:`G.205 <G.205>`, :ref:`G.206 <G.206>`, :ref:`G.207 <G.207>`, :ref:`G.208 <G.208>`, :ref:`G.210 <G.210>`, :ref:`G.211 <G.211>`, :ref:`G.212 <G.212>`, :ref:`G.213 <G.213>`, :ref:`G.214 <G.214>`, :ref:`G.215 <G.215>`, :ref:`G.216 <G.216>`, :ref:`G.218 <G.218>`, :ref:`G.219 <G.219>`, :ref:`G.220 <G.220>`, :ref:`G.221 <G.221>`, :ref:`G.222 <G.222>`, :ref:`G.223 <G.223>`, :ref:`G.225 <G.225>`, :ref:`G.226 <G.226>`, :ref:`G.227 <G.227>`, :ref:`G.228 <G.228>`, :ref:`G.229 <G.229>`, :ref:`G.231 <G.231>`, :ref:`G.232 <G.232>`, :ref:`G.234 <G.234>`, :ref:`G.235 <G.235>`, :ref:`G.236 <G.236>`, :ref:`G.237 <G.237>`, :ref:`G.238 <G.238>`, :ref:`G.239 <G.239>`, :ref:`G.240 <G.240>`, :ref:`G.241 <G.241>`, :ref:`G.243 <G.243>`, :ref:`G.244 <G.244>`, :ref:`G.245 <G.245>`, :ref:`G.273 <G.273>`, :ref:`G.278 <G.278>`, :ref:`G.279 <G.279>`, :ref:`G.280 <G.280>`, :ref:`G.281 <G.281>`, :ref:`G.285 <G.285>`, :ref:`G.289 <G.289>`, :ref:`G.290 <G.290>`, :ref:`G.292 <G.292>`, :ref:`G.295 <G.295>`, :ref:`G.297 <G.297>`, :ref:`G.298 <G.298>`, :ref:`G.299 <G.299>`, :ref:`G.301 <G.301>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`, :ref:`G.305 <G.305>`, :ref:`G.306 <G.306>`, :ref:`G.314 <G.314>`, :ref:`G.315 <G.315>`, :ref:`G.316 <G.316>`, :ref:`G.317 <G.317>`, :ref:`G.322 <G.322>`, :ref:`G.323 <G.323>`, :ref:`G.324 <G.324>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.328 <G.328>`, :ref:`G.329 <G.329>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.332 <G.332>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.337 <G.337>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`, :ref:`G.376 <G.376>`, :ref:`G.377 <G.377>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.386 <G.386>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.395 <G.395>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.520 <G.520>`, :ref:`G.528 <G.528>`, :ref:`G.536 <G.536>`, :ref:`G.541 <G.541>`, :ref:`G.542 <G.542>`, :ref:`G.543 <G.543>`, :ref:`G.544 <G.544>`, :ref:`G.546 <G.546>`, :ref:`G.547 <G.547>`, :ref:`G.550 <G.550>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.554 <G.554>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.560 <G.560>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.579 <G.579>`, :ref:`G.580 <G.580>`, :ref:`G.582 <G.582>`, :ref:`G.583 <G.583>`, :ref:`G.584 <G.584>`, :ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.592 <G.592>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
