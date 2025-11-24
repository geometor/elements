:order: 17
:number: 354
:type: prop
:dependencies: VII.13, VII.20, VII.21




.. figure:: IX.17.graphic.inverted.png

.. _IX.17:

IX.17
=====

   If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the last will not be to any other number as the first to the second.

For let there be as many numbers as we please, A, B, C, D, in continued proportion, and let the extremes of them, A, D, be prime to one another; I say that D is not to any other number as A is to B.

For, if possible, as A is to B, so let D be to E; therefore, alternately, as A is to D, so is B to E. [:ref:`VII.13`]

But A, D are prime, primes are also least, [:ref:`VII.21`] and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent. [:ref:`VII.20`]

Therefore A measures B.

And, as A is to B, so is B to C.

Therefore B also measures C; so that A also measures C.

And since, as B is to C, so is C to D, and B measures C, therefore C also measures D.

But A measured C; so that A also measures D.

But it also measures itself; therefore A measures A, D which are prime to one another : which is impossible.

Therefore D will not be to any other number as A is to B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "VII.4" [URL="/heath/VII/4/", target="_top"];
     "VII.def.12" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.12/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "IX.17" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/17/", target="_top"];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "VII.13" [URL="/heath/VII/13/", target="_top"];
     "VII.1" [URL="/heath/VII/1/", target="_top"];
     "VII.10" [URL="/heath/VII/10/", target="_top"];
     "VII.21" [URL="/heath/VII/21/", target="_top"];
     "VII.21" -> "VII.20";
     "IX.17" -> "VII.20";
     "VII.20" -> "VII.4";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.16" -> "VII.15";
     "VII.4" -> "VII.2";
     "VII.10" -> "VII.9";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VII.21" -> "VII.16";
     "VII.20" -> "VII.13";
     "IX.17" -> "VII.13";
     "VII.2" -> "VII.1";
     "VII.13" -> "VII.10";
     "IX.17" -> "VII.21";
   }



Required for
------------

:ref:`IX.19`