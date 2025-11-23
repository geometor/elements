:order: 18
:number: 355
:type: prop
:dependencies: IX.16, VII.19




.. figure:: IX.18.graphic.inverted.png

.. _IX.18:

IX.18
=====

   Given two numbers, to investigate whether it is possible to find a third proportional to them.

Let A, B be the given two numbers, and let it be required to investigate whether it is possible to find a third proportional to them.

Now A, B are either prime to one another or not.

And, if they are prime to one another, it has been proved that it is impossible to find a third proportional to them. [:ref:`IX.16`]

Next, let A, B not be prime to one another, and let B by multiplying itself make C.

Then A either measures C or does not measure it.

First, let it measure it according to D; therefore A by multiplying D has made C.

But, further, B has also by multiplying itself made C; therefore the product of A, D is equal to the square on B.

Therefore, as A is to B, so is B to D; [:ref:`VII.19`] therefore a third proportional number D has been found to A, B.

Next, let A not measure C; I say that it is impossible to find a third proportional number to A, B.

For, if possible, let D, such third proportional, have been found.

Therefore the product of A, D is equal to the square on B.

But the square on B is C; therefore the product of A, D is equal to C.

Hence A by multiplying D has made C; therefore A measures C according to D.

But, by hypothesis, it also does not measure it: which is absurd.

Therefore it is not possible to find a third proportional number to A, B when A does not measure C. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "IX.16" [URL="/heath/IX/16/", target="_top"];
     "IX.18" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/18/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "VII.13" [URL="/heath/VII/13/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "VII.18" [URL="/heath/VII/18/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "VII.21" [URL="/heath/VII/21/", target="_top"];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VII.def.12" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.12/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.4" [URL="/heath/VII/4/", target="_top"];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "VII.1" [URL="/heath/VII/1/", target="_top"];
     "VII.10" [URL="/heath/VII/10/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "VII.17" [URL="/heath/VII/17/", target="_top"];
     "V.8" -> "V.1";
     "VII.21" -> "VII.20";
     "IX.16" -> "VII.20";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "IX.18" -> "IX.16";
     "VII.10" -> "VII.9";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "V.8" -> "V.def.4";
     "VII.19" -> "VII.18";
     "V.9" -> "V.8";
     "IX.16" -> "VII.21";
     "VII.19" -> "V.7";
     "IX.18" -> "VII.19";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.16" -> "VII.15";
     "VII.20" -> "VII.4";
     "VII.19" -> "V.9";
     "VII.4" -> "VII.2";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VII.2" -> "VII.1";
     "VII.13" -> "VII.10";
     "V.8" -> "V.def.7";
     "V.7" -> "V.def.5";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
   }
