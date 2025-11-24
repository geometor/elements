:order: 8
:number: 318
:type: prop
:dependencies: VII.14, VII.20, VII.21, VII.33, VII.def.20, VIII.3




.. figure:: VIII.8.graphic.inverted.png

.. _VIII.8:

VIII.8
======

   If between two numbers there fall numbers in continued proportion with them, then, however many numbers fall between them in continued proportion, so many will also fall in continued proportion between the numbers which have the same ratio with the original numbers.

Let the numbers C, D fall between the two numbers A, B in continued proportion with them, and let E be made in the same ratio to F as A is to B; I say that, as many numbers as have fallen between A, B in continued proportion, so many will also fall between E, F in continued proportion.

For, as many as A, B, C, D are in multitude, let so many numbers G, H, K, L, the least of those which have the same ratio with A, C, D, B, be taken; [:ref:`VII.33`] therefore the extremes of them G, L are prime to one another. [:ref:`VIII.3`]

Now, since A, C, D, B are in the same ratio with G, H, K, L, and the multitude of the numbers A, C, D, B is equal to the multitude of the numbers G, H, K, L, therefore, ex aequali, as A is to B, so is G to L. [:ref:`VII.14`]

But, as A is to B, so is E to F; therefore also, as G is to L, so is E to F.

But G, L are prime, primes are also least, [:ref:`VII.21`] and the least numbers measure those which have the same ratio the same number of times, the greater the greater and the less the less, that is, the antecedent the antecedent and the consequent the consequent. [:ref:`VII.20`]

Therefore G measures E the same number of times as L measures F.

Next, as many times as G measures E, so many times let H, K also measure M, N respectively; therefore G, H, K, L measure E, M, N, F the same number of times.

Therefore G, H, K, L are in the same ratio with E, M, N, F. [:ref:`VII.def.20`]

But G, H, K, L are in the same ratio with A, C, D, B; therefore A, C, D, B are also in the same ratio with E, M, N, F.

But A, C, D, B are in continued proportion; therefore E, M, N, F are also in continued proportion.

Therefore, as many numbers as have fallen between A, B in continued proportion with them, so many numbers have also fallen between E, F in continued proportion. Q. E. D.
1. fall. The Greek word is ἐμπίπτειν, fall in
=can be interpolated.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "VII.14" [URL="/heath/VII/14/", target="_top"];
     "VII.13" [URL="/heath/VII/13/", target="_top"];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "VII.18" [URL="/heath/VII/18/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "VII.21" [URL="/heath/VII/21/", target="_top"];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "VII.def.12" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.12/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "VII.3" [URL="/heath/VII/3/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "elem.8.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.10" [URL="/heath/VII/10/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "VIII.1" [URL="/heath/VIII/1/", target="_top"];
     "VII.25" [URL="/heath/VII/25/", target="_top"];
     "VII.23" [URL="/heath/VII/23/", target="_top"];
     "VIII.8" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VIII/8/", target="_top"];
     "VII.27" [URL="/heath/VII/27/", target="_top"];
     "VIII.2" [URL="/heath/VIII/2/", target="_top"];
     "VII.24" [URL="/heath/VII/24/", target="_top"];
     "VIII.3" [URL="/heath/VIII/3/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VII.4" [URL="/heath/VII/4/", target="_top"];
     "elem.7.2.p.1" [style="rounded,filled", fillcolor=orange];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "VII.26" [URL="/heath/VII/26/", target="_top"];
     "VII.1" [URL="/heath/VII/1/", target="_top"];
     "VII.22" [URL="/heath/VII/22/", target="_top"];
     "VII.33" [URL="/heath/VII/33/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "VII.17" [URL="/heath/VII/17/", target="_top"];
     "V.8" -> "V.1";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VIII.1" -> "VII.14";
     "VIII.8" -> "VII.14";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.24" -> "VII.16";
     "VII.33" -> "VII.16";
     "V.8" -> "V.def.4";
     "VII.22" -> "VII.def.15";
     "VII.24" -> "VII.def.15";
     "VII.33" -> "VII.def.15";
     "VII.19" -> "VII.18";
     "VIII.2" -> "VII.18";
     "V.9" -> "V.8";
     "VII.24" -> "VII.21";
     "VII.33" -> "VII.21";
     "VIII.1" -> "VII.21";
     "VIII.8" -> "VII.21";
     "VII.19" -> "V.7";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.23" -> "VII.def.12";
     "VII.24" -> "VII.def.12";
     "VII.16" -> "VII.15";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VIII.8" -> "VII.def.20";
     "VII.33" -> "VII.3";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VIII.3" -> "elem.8.2.p.1";
     "VII.13" -> "VII.10";
     "V.8" -> "V.def.7";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VIII.1" -> "VII.20";
     "VIII.8" -> "VII.20";
     "VII.10" -> "VII.9";
     "VIII.2" -> "VIII.1";
     "VII.27" -> "VII.25";
     "VII.24" -> "VII.23";
     "VIII.2" -> "VII.27";
     "VIII.3" -> "VII.27";
     "VIII.3" -> "VIII.2";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VIII.8" -> "VIII.3";
     "VII.24" -> "VII.19";
     "VII.33" -> "VII.19";
     "VII.20" -> "VII.4";
     "VII.3" -> "elem.7.2.p.1";
     "VII.19" -> "V.9";
     "VII.27" -> "VII.26";
     "VII.2" -> "VII.1";
     "VIII.2" -> "VII.22";
     "VIII.3" -> "VII.22";
     "VIII.3" -> "VII.33";
     "VIII.8" -> "VII.33";
     "V.7" -> "V.def.5";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VIII.2" -> "VII.17";
   }



Required for
------------

:ref:`IX.1`, :ref:`IX.10`, :ref:`IX.3`, :ref:`IX.4`, :ref:`IX.5`, :ref:`IX.6`, :ref:`IX.9`, :ref:`VIII.24`, :ref:`VIII.25`, :ref:`X.110`, :ref:`X.28`, :ref:`X.75`, :ref:`X.81`, :ref:`X.93`, :ref:`X.99`