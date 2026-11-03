:order: 261
:number: 261
:canonical_id: G.261
:original_id: VII.9
:title: G.261 number part number
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, segment, number, part-aliquot, alternando, parts-non-aliquot, equality
:dependencies: G.194, G.248, G.253, G.254, G.257, G.258
:excerpt: If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, will the second also be of the fourth.

.. _G.261:
.. _VII.9:

G.261 number part number
========================

.. rubric:: `VII.9 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/09/>`_

.. enunciation::

   If a :term:`number <G.248>` be a :term:`part of <G.253>` a number, and another be the same part of another, :term:`alternately <G.194>` also, whatever part or parts the first is of the third, the same part, or the :term:`same parts <G.254>`, will the second also be of the fourth.

.. signature:: theorem

   | :fn:`number_part_number_vii_9 <G.261>`\ ()
   | **prove** whatever part or parts :g:`A <g1:A>` is of :g:`D <g1:D>`, the same part or the same parts is :g:`/ B C / <g1:/ B C />` of :g:`/ E F / <g1:/ E F />` also

.. picture:: g1.svg
   :alt: Book VII, Proposition 9

.. step:: assert

   Let the number :g:`A <g1:A>` be a part of the number :g:`/ B C / <g1:/ B C />`, and another, :g:`D <g1:D>`, the same part of another, :g:`/ E F / <g1:/ E F />`, that :g:`A <g1:A>` is of :g:`/ B C / <g1:/ B C />`

.. step:: assert

   I say that, alternately also, whatever part or parts :g:`A <g1:A>` is of :g:`D <g1:D>`, the same part or parts is :g:`/ B C / <g1:/ B C />` of :g:`/ E F / <g1:/ E F />` also

.. step:: assert

   For since, whatever part :g:`A <g1:A>` is of :g:`/ B C / <g1:/ B C />`, the same part also is :g:`D <g1:D>` of :g:`/ E F / <g1:/ E F />`,

.. step:: assert

   as many numbers as there are in :g:`/ B C / <g1:/ B C />` equal to :g:`A <g1:A>`, so many also are there in :g:`/ E F / <g1:/ E F />` equal to :g:`D <g1:D>`

.. step:: assert

   Let :g:`/ B C / <g1:/ B C />` be divided into the numbers :eq:`= <g1:/ B G / = g1:/ G C / = g1:A>` to :g:`A <g1:A>`, namely :g:`/ B G / <g1:/ B G />`, :g:`/ G C / <g1:/ G C />`, and :g:`/ E F / <g1:/ E F />` into those :eq:`= <g1:/ E H / = g1:/ H F / = g1:D>` to :g:`D <g1:D>`, namely :g:`/ E H / <g1:/ E H />`, :g:`/ H F / <g1:/ H F />`

.. step:: assert

   the multitude of :g:`/ B G / <g1:/ B G />`, :g:`/ G C / <g1:/ G C />` will be equal to the multitude of :g:`/ E H / <g1:/ E H />`, :g:`/ H F / <g1:/ H F />`

.. step:: assert

   the numbers :g:`/ B G / <g1:/ B G />`, :g:`/ G C / <g1:/ G C />` :eq:`= <g1:/ B G / = g1:/ G C />`, and the numbers :g:`/ E H / <g1:/ E H />`, :g:`/ H F / <g1:/ H F />` :eq:`= <g1:/ E H / = g1:/ H F />`, while the multitude of :g:`/ B G / <g1:/ B G />`, :g:`/ G C / <g1:/ G C />` is equal to the multitude of :g:`/ E H / <g1:/ E H />`, :g:`/ H F / <g1:/ H F />`,

.. step:: assert

   whatever part or parts :g:`/ B G / <g1:/ B G />` is of :g:`/ E H / <g1:/ E H />`, the same part or the same parts is :g:`/ G C / <g1:/ G C />` of :g:`/ H F / <g1:/ H F />` also

.. step:: assert ∵ number_part_number, number_parts_number <G.257, G.258>

   So that, in addition, whatever part or parts :g:`/ B G / <g1:/ B G />` is of :g:`/ E H / <g1:/ E H />`, the same part also, or the same parts, is the sum :g:`/ B C / <g1:/ B C />` of the sum :g:`/ E F / <g1:/ E F />`

.. step:: assert

   :g:`/ B G / <g1:/ B G />` :eq:`= <g1:/ B G / = g1:A; g1:/ E H / = g1:D>` :g:`A <g1:A>`, and :g:`/ E H / <g1:/ E H />` to :g:`D <g1:D>`

.. step:: conclude

   whatever part or parts :g:`A <g1:A>` is of :g:`D <g1:D>`, the same part or the same parts is :g:`/ B C / <g1:/ B C />` of :g:`/ E F / <g1:/ E F />` also

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
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.258" [label="G.258", tooltip="G.258 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.258/index.html", target="_top"];
     "G.261" [label="G.261", tooltip="G.261 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.257" -> "G.170";
     "G.194" -> "G.181";
     "G.261" -> "G.194";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.258" -> "G.248";
     "G.261" -> "G.248";
     "G.254" -> "G.253";
     "G.256" -> "G.253";
     "G.257" -> "G.253";
     "G.258" -> "G.253";
     "G.261" -> "G.253";
     "G.258" -> "G.254";
     "G.261" -> "G.254";
     "G.257" -> "G.256";
     "G.258" -> "G.257";
     "G.261" -> "G.257";
     "G.261" -> "G.258";
   }

Required for
------------

:ref:`G.262 <G.262>`, :ref:`G.266 <G.266>`, :ref:`G.267 <G.267>`, :ref:`G.271 <G.271>`, :ref:`G.272 <G.272>`, :ref:`G.273 <G.273>`, :ref:`G.274 <G.274>`, :ref:`G.275 <G.275>`, :ref:`G.276 <G.276>`, :ref:`G.278 <G.278>`, :ref:`G.279 <G.279>`, :ref:`G.280 <G.280>`, :ref:`G.281 <G.281>`, :ref:`G.285 <G.285>`, :ref:`G.289 <G.289>`, :ref:`G.290 <G.290>`, :ref:`G.292 <G.292>`, :ref:`G.295 <G.295>`, :ref:`G.296 <G.296>`, :ref:`G.297 <G.297>`, :ref:`G.298 <G.298>`, :ref:`G.299 <G.299>`, :ref:`G.301 <G.301>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`, :ref:`G.305 <G.305>`, :ref:`G.306 <G.306>`, :ref:`G.307 <G.307>`, :ref:`G.309 <G.309>`, :ref:`G.312 <G.312>`, :ref:`G.313 <G.313>`, :ref:`G.314 <G.314>`, :ref:`G.315 <G.315>`, :ref:`G.316 <G.316>`, :ref:`G.317 <G.317>`, :ref:`G.319 <G.319>`, :ref:`G.321 <G.321>`, :ref:`G.322 <G.322>`, :ref:`G.323 <G.323>`, :ref:`G.324 <G.324>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.328 <G.328>`, :ref:`G.329 <G.329>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.332 <G.332>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.337 <G.337>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.364 <G.364>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.381 <G.381>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
