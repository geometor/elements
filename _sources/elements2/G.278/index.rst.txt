:order: 278
:number: 278
:canonical_id: G.278
:original_id: VII.24
:title: G.278 numbers prime number
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number, prime-to-one-another, multiply, part-aliquot, unit, proportional, in-the-same-ratio, corresponding-magnitudes, prime, reductio-ad-absurdum
:dependencies: G.169, G.180, G.181, G.247, G.248, G.249, G.269, G.270, G.273, G.274, G.275, G.277
:excerpt: If two numbers be prime to any number, their product also is prime to the same.

.. _G.278:
.. _VII.24:

G.278 numbers prime number
==========================

.. rubric:: `VII.24 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/24/>`_

.. enunciation::

   If two :term:`numbers <G.248>` be :term:`prime to <G.249>` any number, their product also is prime to the same.

.. signature:: theorem

   | :fn:`numbers_prime_number_vii_24 <G.278>`\ ()
   | **prove** :g:`C <g1:C>`, :g:`D <g1:D>` are prime to one another

.. picture:: g1.svg
   :alt: Book VII, Proposition 24

.. step:: assert

   Let the two numbers :g:`A <g1:A>`, :g:`B <g1:B>` be prime to any number :g:`C <g1:C>`, and let :g:`A <g1:A>` by :term:`multiplying <G.269>` :g:`B <g1:B>` make :g:`D <g1:D>`

.. step:: assert

   If :g:`C <g1:C>`, :g:`D <g1:D>` are not prime to one another, some number will :term:`measure <G.169>` :g:`C <g1:C>`, :g:`D <g1:D>`

.. step:: assert

   Let a number measure them, and let it be :g:`E <g1:E>`

.. step:: assert

   :g:`C <g1:C>`, :g:`A <g1:A>` are prime to one another, and a certain number :g:`E <g1:E>` measures :g:`C <g1:C>`,

.. step:: assert ∵ numbers_prime_number <G.277>

   :g:`A <g1:A>`, :g:`E <g1:E>` are prime to one another

.. step:: assert

   As many times, then, as :g:`E <g1:E>` measures :g:`D <g1:D>`, so many :term:`units <G.247>` let there be in :g:`F <g1:F>`

.. step:: assert ∵ numbers_multiplying_make <G.270>

   :g:`F <g1:F>` also measures :g:`D <g1:D>` according to the units in :g:`E <g1:E>`

.. step:: assert ∵ number_said_multiply_def <G.269>

   :g:`E <g1:E>` by multiplying :g:`F <g1:F>` has made :g:`D <g1:D>`

.. step:: assert

   But, further, :g:`A <g1:A>` by multiplying :g:`B <g1:B>` has also made :g:`D <g1:D>`

.. step:: assert

   the product of :g:`E <g1:E>`, :g:`F <g1:F>` is equal to the product of :g:`A <g1:A>`, :g:`B <g1:B>`

.. step:: assert ∵ numbers_proportional_number <G.273>

   But, if the product of the extremes be equal to that of the means, the four numbers are :term:`proportional <G.180>`

.. step:: assert

   as :g:`E <g1:E>` is to :g:`A <g1:A>`, so is :g:`B <g1:B>` to :g:`F <g1:F>`

.. step:: assert ∵ numbers_prime_least <G.275>

   :g:`A <g1:A>`, :g:`E <g1:E>` are prime to one another, numbers which are prime to one another are also the least of those which have the same ratio, and the least numbers of those which have the same ratio with them measure those which have the same ratio the same

.. step:: assert ∵ least_numbers_ratio <G.274>

   Number of times, the greater the greater and the less the less, that is, the :term:`antecedent <G.181>` the antecedent and the consequent the consequent

.. step:: assert

   :g:`E <g1:E>` measures :g:`B <g1:B>`

.. step:: assert

   It also measures :g:`C <g1:C>`

.. step:: assert ∵ numbers_prime_measured_def <G.249>

   :g:`E <g1:E>` measures :g:`B <g1:B>`, :g:`C <g1:C>` which are prime to one another ⇒⇐

.. step:: assert

   no number will measure the numbers :g:`C <g1:C>`, :g:`D <g1:D>`

.. step:: conclude

   :g:`C <g1:C>`, :g:`D <g1:D>` are prime to one another

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
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.13): Inverse ratio means taking theconsequent as antecedent in relation to the antecedent as consequent.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (V.def.7): When, of theequimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then th...", fillcolor="#224422", URL="../G.185/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.187" [label="G.187", tooltip="G.187 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.187/index.html", target="_top"];
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
     "G.268" [label="G.268", tooltip="G.268 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.268/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.270" [label="G.270", tooltip="G.270 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced are equal.", fillcolor="#222244", URL="../G.270/index.html", target="_top"];
     "G.271" [label="G.271", tooltip="G.271 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.271/index.html", target="_top"];
     "G.272" [label="G.272", tooltip="G.272 (VII.18): If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", fillcolor="#222244", URL="../G.272/index.html", target="_top"];
     "G.273" [label="G.273", tooltip="G.273 (VII.19): If four numbers be proportional, the number produced from the first and fourth will equals the number produced from the second and third; and, if the number produced from the first...", fillcolor="#222244", URL="../G.273/index.html", target="_top"];
     "G.274" [label="G.274", tooltip="G.274 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.274/index.html", target="_top"];
     "G.275" [label="G.275", tooltip="G.275 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.275/index.html", target="_top"];
     "G.277" [label="G.277", tooltip="G.277 (VII.23): If two numbers be prime to one another, the number which measures the one of them is prime to the remaining number.", fillcolor="#222244", URL="../G.277/index.html", target="_top"];
     "G.278" [label="G.278", tooltip="G.278 (VII.24): If two numbers be prime to any number, their product also is prime to the same.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.3" -> "G.2";
     "G.8" -> "G.3";
     "G.9" -> "G.8";
     "G.187" -> "G.9";
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
     "G.271" -> "G.169";
     "G.274" -> "G.169";
     "G.275" -> "G.169";
     "G.277" -> "G.169";
     "G.278" -> "G.169";
     "G.171" -> "G.170";
     "G.176" -> "G.170";
     "G.183" -> "G.170";
     "G.185" -> "G.170";
     "G.186" -> "G.170";
     "G.257" -> "G.170";
     "G.186" -> "G.171";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.187" -> "G.176";
     "G.271" -> "G.176";
     "G.272" -> "G.176";
     "G.274" -> "G.176";
     "G.275" -> "G.176";
     "G.183" -> "G.180";
     "G.263" -> "G.180";
     "G.266" -> "G.180";
     "G.273" -> "G.180";
     "G.278" -> "G.180";
     "G.182" -> "G.181";
     "G.194" -> "G.181";
     "G.265" -> "G.181";
     "G.268" -> "G.181";
     "G.274" -> "G.181";
     "G.275" -> "G.181";
     "G.278" -> "G.181";
     "G.183" -> "G.182";
     "G.273" -> "G.183";
     "G.186" -> "G.184";
     "G.186" -> "G.185";
     "G.187" -> "G.186";
     "G.273" -> "G.187";
     "G.261" -> "G.194";
     "G.262" -> "G.194";
     "G.266" -> "G.194";
     "G.268" -> "G.194";
     "G.270" -> "G.194";
     "G.271" -> "G.194";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.250" -> "G.247";
     "G.251" -> "G.247";
     "G.255" -> "G.247";
     "G.268" -> "G.247";
     "G.269" -> "G.247";
     "G.270" -> "G.247";
     "G.271" -> "G.247";
     "G.275" -> "G.247";
     "G.278" -> "G.247";
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
     "G.268" -> "G.248";
     "G.269" -> "G.248";
     "G.270" -> "G.248";
     "G.271" -> "G.248";
     "G.272" -> "G.248";
     "G.273" -> "G.248";
     "G.274" -> "G.248";
     "G.275" -> "G.248";
     "G.277" -> "G.248";
     "G.278" -> "G.248";
     "G.250" -> "G.249";
     "G.251" -> "G.249";
     "G.255" -> "G.249";
     "G.275" -> "G.249";
     "G.277" -> "G.249";
     "G.278" -> "G.249";
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
     "G.271" -> "G.263";
     "G.274" -> "G.263";
     "G.268" -> "G.265";
     "G.274" -> "G.265";
     "G.271" -> "G.266";
     "G.274" -> "G.266";
     "G.270" -> "G.268";
     "G.270" -> "G.269";
     "G.271" -> "G.269";
     "G.272" -> "G.269";
     "G.273" -> "G.269";
     "G.278" -> "G.269";
     "G.272" -> "G.270";
     "G.275" -> "G.270";
     "G.278" -> "G.270";
     "G.272" -> "G.271";
     "G.273" -> "G.271";
     "G.273" -> "G.272";
     "G.278" -> "G.273";
     "G.275" -> "G.274";
     "G.278" -> "G.274";
     "G.278" -> "G.275";
     "G.278" -> "G.277";
   }

Required for
------------

:ref:`G.279 <G.279>`, :ref:`G.280 <G.280>`, :ref:`G.281 <G.281>`, :ref:`G.297 <G.297>`, :ref:`G.298 <G.298>`, :ref:`G.303 <G.303>`, :ref:`G.304 <G.304>`, :ref:`G.305 <G.305>`, :ref:`G.306 <G.306>`, :ref:`G.314 <G.314>`, :ref:`G.315 <G.315>`, :ref:`G.316 <G.316>`, :ref:`G.317 <G.317>`, :ref:`G.323 <G.323>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.328 <G.328>`, :ref:`G.329 <G.329>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.332 <G.332>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.337 <G.337>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.345 <G.345>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`, :ref:`G.381 <G.381>`, :ref:`G.383 <G.383>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.584 <G.584>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
