:order: 195
:number: 195
:canonical_id: G.195
:original_id: V.16
:title: G.195 magnitudes proportional proportional
:volume: II
:book: V
:type: prop
:subtype: theorem
:categories: theorem, proof, proportions, magnitudes
:category: theorem, proof, proportions, magnitudes
:tags: book-v, point, proportional, alternando, multiple, in-the-same-ratio, proportion, equality
:dependencies: G.176, G.180, G.189, G.192, G.193, G.194
:excerpt: If four magnitudes be proportional, they is proportional alternately.

.. _G.195:
.. _V.16:

G.195 magnitudes proportional proportional
==========================================

.. rubric:: `V.16 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/16/>`_

.. enunciation::

   If four magnitudes be :term:`proportional <G.180>`, they is proportional :term:`alternately <G.194>`.

.. signature:: theorem

   | :fn:`magnitudes_proportional_proportional <G.195>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`)
   | **given** :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` be four proportional magnitudes, so that, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`C <g1:C>` to :g:`D <g1:D>`
   | **prove** they will also be so alternately, that is, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`B <g1:B>` to :g:`D <g1:D>`

.. picture:: g1.svg
   :alt: Proposition 16 diagram

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` be four proportional magnitudes, so that, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`C <g1:C>` to :g:`D <g1:D>`

.. step:: construct

   Of :g:`A <g1:A>`, :g:`B <g1:B>` let :term:`equimultiples <G.170>` :g:`E <g1:E>`, :g:`F <g1:F>` be taken, and of :g:`C <g1:C>`, :g:`D <g1:D>` other, chance, equimultiples :g:`G <g1:G>`, :g:`H <g1:H>`.

.. step:: assert ∵ parts_ratio_multiples <G.193>

   Since :g:`E <g1:E>` is the same multiple of :g:`A <g1:A>` that :g:`F <g1:F>` is of :g:`B <g1:B>`, and parts have the :term:`same ratio <G.176>` as the same multiples of them.

.. step:: assert

   Therefore, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`.

.. step:: assert

   As :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`C <g1:C>` to :g:`D <g1:D>`

.. step:: assert ∵ ratios_ratio <G.189>

   Therefore also, as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`.

.. step:: assert ∵ parts_ratio_multiples <G.193>

   Since :g:`G <g1:G>`, :g:`H <g1:H>` are equimultiples of :g:`C <g1:C>`, :g:`D <g1:D>` → therefore, as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`G <g1:G>` to :g:`H <g1:H>`.

.. step:: assert

   But, as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`

.. step:: assert ∵ ratios_ratio <G.189>

   Therefore also, as :g:`E <g1:E>` is to :g:`F <g1:F>`, so is :g:`G <g1:G>` to :g:`H <g1:H>`.

.. step:: assert ∵ magnitude_ratio_greater_v_14 <G.192>

   But, if four magnitudes be proportional, and the first be greater than the third, the second will also be greater than the fourth ; if equal, equal ; and if less, less.

.. step:: assert

   Therefore, if :g:`E <g1:E>` is in excess of :g:`G <g1:G>`, :g:`F <g1:F>` is also in excess of :g:`H <g1:H>`, if :eq:`equal <g1:E = g1:G>`, :eq:`equal <g1:F = g1:H>`, and if less, less.

.. step:: assert

   Now :g:`E <g1:E>`, :g:`F <g1:F>` are equimultiples of :g:`A <g1:A>`, :g:`B <g1:B>`, and :g:`G <g1:G>`, :g:`H <g1:H>` other, chance, equimultiples of :g:`C <g1:C>`, :g:`D <g1:D>`

.. step:: conclude ∵ magnitudes_said_ratio_def <G.176>

   Therefore, as :g:`A <g1:A>` is to :g:`C <g1:C>`, so is :g:`B <g1:B>` to :g:`D <g1:D>`.

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
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.171" [label="G.171", tooltip="G.171 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.13): Inverse ratio means taking theconsequent as antecedent in relation to the antecedent as consequent.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (V.def.7): When, of theequimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then th...", fillcolor="#224422", URL="../G.185/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.188" [label="G.188", tooltip="G.188 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.188/index.html", target="_top"];
     "G.189" [label="G.189", tooltip="G.189 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.189/index.html", target="_top"];
     "G.190" [label="G.190", tooltip="G.190 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.190/index.html", target="_top"];
     "G.191" [label="G.191", tooltip="G.191 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.191/index.html", target="_top"];
     "G.192" [label="G.192", tooltip="G.192 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.192/index.html", target="_top"];
     "G.193" [label="G.193", tooltip="G.193 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.193/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.195" [label="G.195", tooltip="G.195 (V.16): If four magnitudes be proportional, they is proportional alternately.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.3" -> "G.2";
     "G.8" -> "G.3";
     "G.9" -> "G.8";
     "G.188" -> "G.9";
     "G.189" -> "G.9";
     "G.170" -> "G.169";
     "G.171" -> "G.170";
     "G.176" -> "G.170";
     "G.185" -> "G.170";
     "G.193" -> "G.170";
     "G.186" -> "G.171";
     "G.190" -> "G.171";
     "G.188" -> "G.173";
     "G.189" -> "G.173";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.189" -> "G.176";
     "G.190" -> "G.176";
     "G.191" -> "G.176";
     "G.192" -> "G.176";
     "G.193" -> "G.176";
     "G.195" -> "G.176";
     "G.183" -> "G.180";
     "G.190" -> "G.180";
     "G.195" -> "G.180";
     "G.182" -> "G.181";
     "G.190" -> "G.181";
     "G.194" -> "G.181";
     "G.183" -> "G.182";
     "G.188" -> "G.183";
     "G.193" -> "G.183";
     "G.186" -> "G.184";
     "G.188" -> "G.184";
     "G.186" -> "G.185";
     "G.188" -> "G.185";
     "G.191" -> "G.185";
     "G.188" -> "G.186";
     "G.192" -> "G.186";
     "G.192" -> "G.188";
     "G.195" -> "G.189";
     "G.193" -> "G.190";
     "G.192" -> "G.191";
     "G.195" -> "G.192";
     "G.195" -> "G.193";
     "G.195" -> "G.194";
   }

Required for
------------

:ref:`G.201 <G.201>`, :ref:`G.206 <G.206>`, :ref:`G.208 <G.208>`, :ref:`G.213 <G.213>`, :ref:`G.214 <G.214>`, :ref:`G.215 <G.215>`, :ref:`G.216 <G.216>`, :ref:`G.218 <G.218>`, :ref:`G.223 <G.223>`, :ref:`G.229 <G.229>`, :ref:`G.231 <G.231>`, :ref:`G.232 <G.232>`, :ref:`G.234 <G.234>`, :ref:`G.236 <G.236>`, :ref:`G.237 <G.237>`, :ref:`G.238 <G.238>`, :ref:`G.239 <G.239>`, :ref:`G.240 <G.240>`, :ref:`G.241 <G.241>`, :ref:`G.243 <G.243>`, :ref:`G.244 <G.244>`, :ref:`G.245 <G.245>`, :ref:`G.377 <G.377>`, :ref:`G.378 <G.378>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.386 <G.386>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.395 <G.395>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.528 <G.528>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.584 <G.584>`, :ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.592 <G.592>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
