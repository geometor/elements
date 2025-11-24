:order: 30
:number: 301
:type: prop
:dependencies: VII.19, VII.20, VII.21, VII.29, VII.def.15




.. figure:: VII.30.graphic.inverted.png

.. _VII.30:

VII.30
======

   If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.

For let the two numbers A, B by multiplying one another make C, and let any prime number D measure C; I say that D measures one of the numbers A, B.

For let it not measure A.

Now D is prime; therefore A, D are prime to one another. [:ref:`VII.29`]

And, as many times as D measures C, so many units let there be in E.

Since then D measures C according to the units in E, therefore D by multiplying E has made C. [:ref:`VII.def.15`]

Further, A by multiplying B has also made C; therefore the product of D, E is equal to the product of A, B.

Therefore, as D is to A, so is B to E. [:ref:`VII.19`]

But D, A are prime to one another, primes are also least, [:ref:`VII.21`] and the least measure the numbers which have the same ratio the same number of times, the greater the greater and the less the less, that is, the antecedent the antecedent and the consequent the consequent; [:ref:`VII.20`] therefore D measures B.

Similarly we can also show that, if D do not measure B, it will measure A.

Therefore D measures one of the numbers A, B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.def.12" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.12/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "VII.1" [URL="/heath/VII/1/", target="_top"];
     "VII.10" [URL="/heath/VII/10/", target="_top"];
     "VII.30" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VII/30/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VII.18" [URL="/heath/VII/18/", target="_top"];
     "VII.29" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/29/", target="_top"];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "VII.4" [URL="/heath/VII/4/", target="_top"];
     "VII.21" [URL="/heath/VII/21/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "VII.17" [URL="/heath/VII/17/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "VII.13" [URL="/heath/VII/13/", target="_top"];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "V.9" -> "V.8";
     "VII.2" -> "VII.1";
     "VII.13" -> "VII.10";
     "VII.10" -> "VII.9";
     "VII.30" -> "VII.def.15";
     "V.7" -> "V.def.5";
     "VII.30" -> "VII.19";
     "VII.19" -> "VII.18";
     "VII.30" -> "VII.29";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.20" -> "VII.4";
     "VII.30" -> "VII.21";
     "V.8" -> "V.1";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VII.21" -> "VII.20";
     "VII.30" -> "VII.20";
     "VII.19" -> "V.7";
     "VII.19" -> "V.9";
     "V.8" -> "V.def.4";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VII.4" -> "VII.2";
     "V.8" -> "V.def.7";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.16" -> "VII.15";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
   }



Required for
------------

:ref:`IX.14`