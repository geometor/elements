:order: 8
:number: 345
:type: prop
:dependencies: VII.def.20, VIII.22, VIII.23




.. figure:: IX.8.graphic.inverted.png

.. _IX.8:

IX.8
====

   If as many numbers as we please beginning from an unit be in continued proportion, the third from the unit will be square, as will also those which successively leave out one; the fourth will be cube, as will also all those which leave out two; and the seventh will be at once cube and square, as will also those which leave out five.

Let there be as many numbers as we please, A, B, C, D, E, F, beginning from an unit and in continued proportion; I say that B, the third from the unit, is square, as are also all those which leave out one; C, the fourth, is cube, as are also all those which leave out two; and F, the seventh, is at once cube and square, as are also all those which leave out five.

For since, as the unit is to A, so is A to B, therefore the unit measures the number A the same number of times that A measures B. [:ref:`VII.def.20`]

But the unit measures the number A according to the units in it; therefore A also measures B according to the units in A.

Therefore A by multiplying itself has made B; therefore B is square.

And, since B, C, D are in continued proportion, and B is square, therefore D is also square. [:ref:`VIII.22`]

For the same reason F is also square.

Similarly we can prove that all those which leave out one are square.

I say next that C, the fourth from the unit, is cube, as are also all those which leave out two.

For since, as the unit is to A, so is B to C, therefore the unit measures the number A the same number of times that B measures C.

But the unit measures the number A according to the units in A; therefore B also measures C according to the units in A.

Therefore A by multiplying B has made C.

Since then A by multiplying itself has made B, and by multiplying B has made C, therefore C is cube.

And, since C, D, E, F are in continued proportion, and C is cube, therefore F is also cube. [:ref:`VIII.23`]

But it was also proved square; therefore the seventh from the unit is both cube and square.

Similarly we can prove that all the numbers which leave out five are also both cube and square. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "VIII.21" [URL="/heath/VIII/21/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "IX.8" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/8/", target="_top"];
     "VII.14" [URL="/heath/VII/14/", target="_top"];
     "VII.13" [URL="/heath/VII/13/", target="_top"];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "VII.18" [URL="/heath/VII/18/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "VII.21" [URL="/heath/VII/21/", target="_top"];
     "VIII.20" [URL="/heath/VIII/20/", target="_top"];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "VII.def.12" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.12/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "VII.3" [URL="/heath/VII/3/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "elem.8.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.10" [URL="/heath/VII/10/", target="_top"];
     "VIII.23" [URL="/heath/VIII/23/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "VIII.1" [URL="/heath/VIII/1/", target="_top"];
     "VII.25" [URL="/heath/VII/25/", target="_top"];
     "VII.23" [URL="/heath/VII/23/", target="_top"];
     "VII.27" [URL="/heath/VII/27/", target="_top"];
     "VIII.2" [URL="/heath/VIII/2/", target="_top"];
     "VII.24" [URL="/heath/VII/24/", target="_top"];
     "VIII.3" [URL="/heath/VIII/3/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VII.4" [URL="/heath/VII/4/", target="_top"];
     "elem.7.2.p.1" [style="rounded,filled", fillcolor=orange];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "VII.26" [URL="/heath/VII/26/", target="_top"];
     "VIII.22" [URL="/heath/VIII/22/", target="_top"];
     "VII.1" [URL="/heath/VII/1/", target="_top"];
     "VII.22" [URL="/heath/VII/22/", target="_top"];
     "VII.33" [URL="/heath/VII/33/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "VII.17" [URL="/heath/VII/17/", target="_top"];
     "V.8" -> "V.1";
     "VIII.23" -> "VIII.21";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VIII.1" -> "VII.14";
     "VIII.21" -> "VII.14";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VIII.20" -> "VII.13";
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
     "VIII.21" -> "VII.18";
     "V.9" -> "V.8";
     "VII.24" -> "VII.21";
     "VII.33" -> "VII.21";
     "VIII.1" -> "VII.21";
     "VIII.21" -> "VII.21";
     "VIII.21" -> "VIII.20";
     "VIII.22" -> "VIII.20";
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
     "IX.8" -> "VII.def.20";
     "VII.33" -> "VII.3";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VIII.3" -> "elem.8.2.p.1";
     "VII.13" -> "VII.10";
     "IX.8" -> "VIII.23";
     "V.8" -> "V.def.7";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VIII.1" -> "VII.20";
     "VIII.20" -> "VII.20";
     "VIII.21" -> "VII.20";
     "VII.10" -> "VII.9";
     "VIII.2" -> "VIII.1";
     "VII.27" -> "VII.25";
     "VII.24" -> "VII.23";
     "VIII.2" -> "VII.27";
     "VIII.3" -> "VII.27";
     "VIII.3" -> "VIII.2";
     "VIII.21" -> "VIII.2";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VIII.21" -> "VIII.3";
     "VII.24" -> "VII.19";
     "VII.33" -> "VII.19";
     "VII.20" -> "VII.4";
     "VII.3" -> "elem.7.2.p.1";
     "VII.19" -> "V.9";
     "VII.27" -> "VII.26";
     "IX.8" -> "VIII.22";
     "VII.2" -> "VII.1";
     "VIII.2" -> "VII.22";
     "VIII.3" -> "VII.22";
     "VIII.3" -> "VII.33";
     "VIII.20" -> "VII.33";
     "VIII.21" -> "VII.33";
     "V.7" -> "V.def.5";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VIII.2" -> "VII.17";
     "VIII.20" -> "VII.17";
   }



Required for
------------

:ref:`IX.10`, :ref:`IX.12`, :ref:`IX.13`, :ref:`IX.32`, :ref:`IX.36`, :ref:`IX.9`