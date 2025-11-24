:order: 14
:number: 351
:type: prop
:dependencies: VII.30




.. figure:: IX.14.graphic.inverted.png

.. _IX.14:

IX.14
=====

   If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

For let the number A be the least that is measured by the prime numbers B, C, D; I say that A will not be measured by any other prime number except B, C, D.

For, if possible, let it be measured by the prime number E, and let E not be the same with any one of the numbers B, C, D.

Now, since E measures A, let it measure it according to F;


.. container:: center

   therefore E by multiplying F has made A.


And A is measured by the prime numbers B, C, D.

But, if two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers; [:ref:`VII.30`] therefore B, C, D will measure one of the numbers E, F.

Now they will not measure E; for E is prime and not the same with any one of the numbers B, C, D.

Therefore they will measure F, which is less than A: which is impossible, for A is by hypothesis the least number measured by B, C, D.

Therefore no prime number will measure A except B, C, D. Q. E. D.


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
     "VII.30" [URL="/heath/VII/30/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VII.18" [URL="/heath/VII/18/", target="_top"];
     "VII.29" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/29/", target="_top"];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "IX.14" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/14/", target="_top"];
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
     "IX.14" -> "VII.30";
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
