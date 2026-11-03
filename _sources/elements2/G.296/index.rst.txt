:order: 296
:number: 296
:canonical_id: G.296
:original_id: VIII.1
:title: G.296 there many numbers
:volume: II
:book: VIII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory, proportions
:category: theorem, proof, number-theory, proportions
:tags: book-viii, point, number, proportional, prime-to-one-another, in-the-same-ratio, ex-aequali, prime-number, part-aliquot, corresponding-magnitudes, ratio, proportion, prime, continued-proportion, reductio-ad-absurdum
:dependencies: G.174, G.176, G.180, G.248, G.249, G.267, G.274, G.275, G.283
:excerpt: If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio with them.

.. _G.296:
.. _VIII.1:

G.296 there many numbers
========================

.. rubric:: `VIII.1 <https://geometor.github.io/euclid/heath/volume_II/book_viii/propositions/01/>`_

.. enunciation::

   If there be as many :term:`numbers <G.248>` as we please in :term:`continued proportion <G.180>`, and the extremes of them be :term:`prime to one another <G.249>`, the numbers are the least of those which have the :term:`same ratio <G.176>` with them.

.. signature:: theorem

   | :fn:`there_many_numbers_viii_1 <G.296>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`)
   | **given** there be as many numbers as we please, :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, in continued proportion, let the extremes of them :g:`A <g1:A>`, :g:`D <g1:D>` be prime to one another
   | **prove** :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` are the least of those which have the same ratio with them

.. picture:: g1.svg
   :alt: Proposition 1 Diagram

.. step:: given

   there be as many numbers as we please, :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, in continued proportion, let the extremes of them :g:`A <g1:A>`, :g:`D <g1:D>` be prime to one another

.. step:: assert

   If not, let :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`G <g1:G>`, :g:`H <g1:H>` be less than :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, and in the same ratio with them

.. step:: assert

   :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` are in the same ratio with :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`G <g1:G>`, :g:`H <g1:H>`, and the multitude of the numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` is equal to the multitude of the numbers :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`G <g1:G>`, :g:`H <g1:H>`,

.. step:: assert ∵ there_many_numbers_vii_14 <G.267>

   *:term:`ex aequali <G.174>`*, as :g:`A <g1:A>` is to :g:`D <g1:D>`, so is :g:`E <g1:E>` to :g:`H <g1:H>`

.. step:: assert ∵ numbers_prime_least, least_numbers_ratio <G.275, G.274>

   :g:`A <g1:A>`, :g:`D <g1:D>` are prime, primes are also least, and the least numbers measure those which have the same ratio the same number of times, the greater the greater and the less the less, that is, the antecedent the antecedent and the consequent the consequent

.. step:: assert

   :g:`A <g1:A>` measures :g:`E <g1:E>`, the greater the less ⇒⇐

.. step:: assert

   :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`G <g1:G>`, :g:`H <g1:H>` which are less than :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` are not in the same ratio with them

.. step:: conclude

   :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` are the least of those which have the same ratio with them

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
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.174" [label="G.174", tooltip="G.174 (V.def.17): Aratioex aequali arises when, there being several magnitudes and another set equal to them in multitude which taken two and two are in the same proportion, as the first is to the l...", fillcolor="#224422", URL="../G.174/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.249" [label="G.249", tooltip="G.249 (VII.def.12): Numbers prime to one another are those which aremeasured by anunit alone as a common measure.", fillcolor="#224422", URL="../G.249/index.html", target="_top"];
     "G.250" [label="G.250", tooltip="G.250 (VII.1): Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is...", fillcolor="#222244", URL="../G.250/index.html", target="_top"];
     "G.251" [label="G.251", tooltip="G.251 (VII.2): Given two numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.251/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.255" [label="G.255", tooltip="G.255 (VII.4): Any number is either a part or parts of any number, the less of the greater.", fillcolor="#222244", URL="../G.255/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.258" [label="G.258", tooltip="G.258 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.258/index.html", target="_top"];
     "G.261" [label="G.261", tooltip="G.261 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.261/index.html", target="_top"];
     "G.262" [label="G.262", tooltip="G.262 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.262/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VII.def.20): Numbers areproportional when the first is thesame multiple, or thesame part, or thesame parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.263/index.html", target="_top"];
     "G.265" [label="G.265", tooltip="G.265 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.265/index.html", target="_top"];
     "G.266" [label="G.266", tooltip="G.266 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.266/index.html", target="_top"];
     "G.267" [label="G.267", tooltip="G.267 (VII.14): If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.267/index.html", target="_top"];
     "G.268" [label="G.268", tooltip="G.268 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.268/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.270" [label="G.270", tooltip="G.270 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced are equal.", fillcolor="#222244", URL="../G.270/index.html", target="_top"];
     "G.274" [label="G.274", tooltip="G.274 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.274/index.html", target="_top"];
     "G.275" [label="G.275", tooltip="G.275 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.275/index.html", target="_top"];
     "G.283" [label="G.283", tooltip="G.283 (VII.def.11): Aprime number is that which ismeasured by anunit alone.", fillcolor="#224422", URL="../G.283/index.html", target="_top"];
     "G.296" [label="G.296", tooltip="G.296 (VIII.1): If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio wit...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.249" -> "G.169";
     "G.250" -> "G.169";
     "G.251" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.255" -> "G.169";
     "G.256" -> "G.169";
     "G.268" -> "G.169";
     "G.270" -> "G.169";
     "G.274" -> "G.169";
     "G.275" -> "G.169";
     "G.283" -> "G.169";
     "G.176" -> "G.170";
     "G.257" -> "G.170";
     "G.174" -> "G.173";
     "G.267" -> "G.174";
     "G.296" -> "G.174";
     "G.180" -> "G.176";
     "G.267" -> "G.176";
     "G.274" -> "G.176";
     "G.275" -> "G.176";
     "G.296" -> "G.176";
     "G.263" -> "G.180";
     "G.266" -> "G.180";
     "G.296" -> "G.180";
     "G.194" -> "G.181";
     "G.265" -> "G.181";
     "G.268" -> "G.181";
     "G.274" -> "G.181";
     "G.275" -> "G.181";
     "G.261" -> "G.194";
     "G.262" -> "G.194";
     "G.266" -> "G.194";
     "G.267" -> "G.194";
     "G.268" -> "G.194";
     "G.270" -> "G.194";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.250" -> "G.247";
     "G.251" -> "G.247";
     "G.255" -> "G.247";
     "G.268" -> "G.247";
     "G.269" -> "G.247";
     "G.270" -> "G.247";
     "G.275" -> "G.247";
     "G.283" -> "G.247";
     "G.250" -> "G.248";
     "G.251" -> "G.248";
     "G.253" -> "G.248";
     "G.255" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.258" -> "G.248";
     "G.261" -> "G.248";
     "G.262" -> "G.248";
     "G.265" -> "G.248";
     "G.266" -> "G.248";
     "G.267" -> "G.248";
     "G.268" -> "G.248";
     "G.269" -> "G.248";
     "G.270" -> "G.248";
     "G.274" -> "G.248";
     "G.275" -> "G.248";
     "G.296" -> "G.248";
     "G.250" -> "G.249";
     "G.251" -> "G.249";
     "G.255" -> "G.249";
     "G.275" -> "G.249";
     "G.296" -> "G.249";
     "G.251" -> "G.250";
     "G.255" -> "G.251";
     "G.254" -> "G.253";
     "G.255" -> "G.253";
     "G.256" -> "G.253";
     "G.257" -> "G.253";
     "G.258" -> "G.253";
     "G.261" -> "G.253";
     "G.262" -> "G.253";
     "G.263" -> "G.253";
     "G.265" -> "G.253";
     "G.266" -> "G.253";
     "G.283" -> "G.253";
     "G.255" -> "G.254";
     "G.258" -> "G.254";
     "G.261" -> "G.254";
     "G.262" -> "G.254";
     "G.263" -> "G.254";
     "G.265" -> "G.254";
     "G.266" -> "G.254";
     "G.274" -> "G.254";
     "G.274" -> "G.255";
     "G.257" -> "G.256";
     "G.263" -> "G.256";
     "G.258" -> "G.257";
     "G.261" -> "G.257";
     "G.262" -> "G.257";
     "G.265" -> "G.257";
     "G.261" -> "G.258";
     "G.262" -> "G.258";
     "G.265" -> "G.258";
     "G.262" -> "G.261";
     "G.266" -> "G.262";
     "G.265" -> "G.263";
     "G.266" -> "G.263";
     "G.274" -> "G.263";
     "G.268" -> "G.265";
     "G.274" -> "G.265";
     "G.267" -> "G.266";
     "G.274" -> "G.266";
     "G.296" -> "G.267";
     "G.270" -> "G.268";
     "G.270" -> "G.269";
     "G.275" -> "G.270";
     "G.275" -> "G.274";
     "G.296" -> "G.274";
     "G.296" -> "G.275";
     "G.296" -> "G.283";
   }

Required for
------------

:ref:`G.297 <G.297>`, :ref:`G.298 <G.298>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`, :ref:`G.305 <G.305>`, :ref:`G.306 <G.306>`, :ref:`G.314 <G.314>`, :ref:`G.315 <G.315>`, :ref:`G.316 <G.316>`, :ref:`G.317 <G.317>`, :ref:`G.323 <G.323>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.328 <G.328>`, :ref:`G.329 <G.329>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.332 <G.332>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.337 <G.337>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.345 <G.345>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`, :ref:`G.381 <G.381>`, :ref:`G.383 <G.383>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
