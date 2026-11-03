:order: 319
:number: 319
:canonical_id: G.319
:original_id: VIII.18
:title: G.319 similar plane numbers
:volume: II
:book: VIII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory, proportions
:category: theorem, proof, number-theory, proportions
:tags: book-viii, point, similar-plane-and-solid-numbers, proportional, number, plane-number, ratio, alternando, plane-surface, multiply, proportion, similar, plane
:dependencies: G.7, G.173, G.180, G.194, G.230, G.248, G.266, G.269, G.271, G.300, G.318
:excerpt: Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has to the corresponding side.

.. _G.319:
.. _VIII.18:

G.319 similar plane numbers
===========================

.. rubric:: `VIII.18 <https://geometor.github.io/euclid/heath/volume_II/book_viii/propositions/18/>`_

.. enunciation::

   Between two :term:`similar plane numbers <G.318>` there is one mean :term:`proportional <G.180>` :term:`number <G.248>`; and the :term:`plane number <G.300>` has to the plane number the :term:`ratio <G.173>` duplicate of that which the corresponding side has to the corresponding side.

.. signature:: theorem

   | :fn:`similar_plane_numbers <G.319>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`)
   | **given** :g:`A <g1:A>`, :g:`B <g1:B>` be two similar plane numbers, let the numbers :g:`C <g1:C>`, :g:`D <g1:D>` be the sides of :g:`A <g1:A>`, :g:`E <g1:E>`, :g:`F <g1:F>` of :g:`B <g1:B>`
   | **prove** :g:`A <g1:A>` also has to :g:`B <g1:B>` the ratio duplicate of that which :g:`C <g1:C>` has to :g:`E <g1:E>` or :g:`D <g1:D>` to :g:`F <g1:F>`

.. picture:: g1.svg
   :alt: Book VIII, Proposition 18

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>` be two similar plane numbers, let the numbers :g:`C <g1:C>`, :g:`D <g1:D>` be the sides of :g:`A <g1:A>`, :g:`E <g1:E>`, :g:`F <g1:F>` of :g:`B <g1:B>`

.. step:: assert ∵ similar_plane_solid_def <G.318>

   similar plane numbers are those which have their sides proportional

.. step:: assert

   as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`

.. step:: assert

   I say then that between :g:`A <g1:A>`, :g:`B <g1:B>` there is one mean proportional number, and :g:`A <g1:A>` has to :g:`B <g1:B>` the ratio duplicate of that which :g:`C <g1:C>` has to :g:`E <g1:E>`, or :g:`D <g1:D>` to :g:`F <g1:F>`, that is, of that which the corresponding side has to the corresponding side

.. step:: assert

   Now since, as :g:`C <g1:C>` is to :g:`D <g1:D>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`,

.. step:: assert ∵ numbers_proportional_proportional <G.266>

   :term:`alternately <G.194>`, as :g:`C <g1:C>` is to :g:`E <g1:E>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`

.. step:: assert

   since :g:`A <g1:A>` is :term:`plane <G.7>`, and :g:`C <g1:C>`, :g:`D <g1:D>` are its sides,

.. step:: assert

   :g:`D <g1:D>` by multiplying :g:`C <g1:C>` has made :g:`A <g1:A>`

.. step:: assert

   For the same reason also

.. step:: assert

   :g:`E <g1:E>` by multiplying :g:`F <g1:F>` has made :g:`B <g1:B>`

.. step:: assert

   Now let :g:`D <g1:D>` by :term:`multiplying <G.269>` :g:`E <g1:E>` make :g:`G <g1:G>`

.. step:: assert

   :g:`D <g1:D>` by multiplying :g:`C <g1:C>` has made :g:`A <g1:A>`, and by multiplying :g:`E <g1:E>` has made :g:`G <g1:G>`,

.. step:: assert ∵ number_multiplying_numbers <G.271>

   as :g:`C <g1:C>` is to :g:`E <g1:E>`, so is :g:`A <g1:A>` to :g:`G <g1:G>`

.. step:: assert

   But, as :g:`C <g1:C>` is to :g:`E <g1:E>`, so is :g:`D <g1:D>` to :g:`F <g1:F>`

.. step:: assert

   also, as :g:`D <g1:D>` is to :g:`F <g1:F>`, so is :g:`A <g1:A>` to :g:`G <g1:G>`

.. step:: assert

   :g:`E <g1:E>` by multiplying :g:`D <g1:D>` has made :g:`G <g1:G>`, and by multiplying :g:`F <g1:F>` has made :g:`B <g1:B>`,

.. step:: assert ∵ number_multiplying_numbers <G.271>

   as :g:`D <g1:D>` is to :g:`F <g1:F>`, so is :g:`G <g1:G>` to :g:`B <g1:B>`

.. step:: assert

   It was also proved that, as :g:`D <g1:D>` is to :g:`F <g1:F>`, so is :g:`A <g1:A>` to :g:`G <g1:G>`

.. step:: assert

   also, as :g:`A <g1:A>` is to :g:`G <g1:G>`, so is :g:`G <g1:G>` to :g:`B <g1:B>`

.. step:: assert

   :g:`A <g1:A>`, :g:`G <g1:G>`, :g:`B <g1:B>` are in continued proportion

.. step:: assert

   between :g:`A <g1:A>`, :g:`B <g1:B>` there is one mean proportional number

.. step:: assert

   I say next that :g:`A <g1:A>` also has to :g:`B <g1:B>` the ratio duplicate of that which the corresponding side has to the corresponding side, that is, of that which :g:`C <g1:C>` has to :g:`E <g1:E>` or :g:`D <g1:D>` to :g:`F <g1:F>`

.. step:: assert

   :g:`A <g1:A>`, :g:`G <g1:G>`, :g:`B <g1:B>` are in continued proportion,

.. step:: assert ∵ magnitudes_proportional_said_def <G.230>

   :g:`A <g1:A>` has to :g:`B <g1:B>` the ratio duplicate of that which it has to :g:`G <g1:G>`

.. step:: assert

   as :g:`A <g1:A>` is to :g:`G <g1:G>`, so is :g:`C <g1:C>` to :g:`E <g1:E>`, and so is :g:`D <g1:D>` to :g:`F <g1:F>`

.. step:: conclude

   :g:`A <g1:A>` also has to :g:`B <g1:B>` the ratio duplicate of that which :g:`C <g1:C>` has to :g:`E <g1:E>` or :g:`D <g1:D>` to :g:`F <g1:F>`

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
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.230" [label="G.230", tooltip="G.230 (V.def.9): When three magnitudes areproportional, the first is said to have to the third theduplicate ratio of that which it has to the second.", fillcolor="#224422", URL="../G.230/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.258" [label="G.258", tooltip="G.258 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.258/index.html", target="_top"];
     "G.261" [label="G.261", tooltip="G.261 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.261/index.html", target="_top"];
     "G.262" [label="G.262", tooltip="G.262 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.262/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VII.def.20): Numbers areproportional when the first is thesame multiple, or thesame part, or thesame parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.263/index.html", target="_top"];
     "G.266" [label="G.266", tooltip="G.266 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.266/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.271" [label="G.271", tooltip="G.271 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.271/index.html", target="_top"];
     "G.300" [label="G.300", tooltip="G.300 (VII.def.16): And, when twonumbers havingmultiplied one another make some number, the number so produced is calledplane, and itssides are the numbers which have multiplied one another.", fillcolor="#224422", URL="../G.300/index.html", target="_top"];
     "G.318" [label="G.318", tooltip="G.318 (VII.def.21): Similar plane and solid numbers are those which have their sidesproportional.", fillcolor="#224422", URL="../G.318/index.html", target="_top"];
     "G.319" [label="G.319", tooltip="G.319 (VIII.18): Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has t...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.7" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.7" -> "G.5";
     "G.319" -> "G.7";
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.271" -> "G.169";
     "G.176" -> "G.170";
     "G.257" -> "G.170";
     "G.319" -> "G.173";
     "G.180" -> "G.176";
     "G.271" -> "G.176";
     "G.230" -> "G.180";
     "G.263" -> "G.180";
     "G.266" -> "G.180";
     "G.318" -> "G.180";
     "G.319" -> "G.180";
     "G.194" -> "G.181";
     "G.261" -> "G.194";
     "G.262" -> "G.194";
     "G.266" -> "G.194";
     "G.271" -> "G.194";
     "G.319" -> "G.194";
     "G.319" -> "G.230";
     "G.248" -> "G.247";
     "G.269" -> "G.247";
     "G.271" -> "G.247";
     "G.253" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.258" -> "G.248";
     "G.261" -> "G.248";
     "G.262" -> "G.248";
     "G.266" -> "G.248";
     "G.269" -> "G.248";
     "G.271" -> "G.248";
     "G.300" -> "G.248";
     "G.319" -> "G.248";
     "G.254" -> "G.253";
     "G.256" -> "G.253";
     "G.257" -> "G.253";
     "G.258" -> "G.253";
     "G.261" -> "G.253";
     "G.262" -> "G.253";
     "G.263" -> "G.253";
     "G.266" -> "G.253";
     "G.258" -> "G.254";
     "G.261" -> "G.254";
     "G.262" -> "G.254";
     "G.263" -> "G.254";
     "G.266" -> "G.254";
     "G.257" -> "G.256";
     "G.263" -> "G.256";
     "G.258" -> "G.257";
     "G.261" -> "G.257";
     "G.262" -> "G.257";
     "G.261" -> "G.258";
     "G.262" -> "G.258";
     "G.262" -> "G.261";
     "G.266" -> "G.262";
     "G.266" -> "G.263";
     "G.271" -> "G.263";
     "G.271" -> "G.266";
     "G.319" -> "G.266";
     "G.271" -> "G.269";
     "G.300" -> "G.269";
     "G.319" -> "G.269";
     "G.319" -> "G.271";
     "G.319" -> "G.300";
     "G.319" -> "G.318";
   }

Required for
------------

:ref:`G.321 <G.321>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.328 <G.328>`, :ref:`G.329 <G.329>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.339 <G.339>`, :ref:`G.381 <G.381>`, :ref:`G.383 <G.383>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
