:order: 29
:number: 366
:type: prop
:dependencies: IX.23, VII.def.15




.. figure:: IX.29.graphic.inverted.png

.. _IX.29:

IX.29
=====

   If an odd number by multiplying an odd number make some number, the product will be odd.

For let the odd number A by multiplying the odd number B make C; I say that C is odd.

For, since A by multiplying B has made C, therefore C is made up of as many numbers equal to B as there are units in A. [:ref:`VII.def.15`]

And each of the numbers A, B is odd; therefore C is made up of odd numbers the multitude of which is odd.

Thus C is odd. [:ref:`IX.23`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "VII.def.6" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.6/", target="_top"];
     "IX.22" [URL="/heath/IX/22/", target="_top"];
     "IX.29" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/29/", target="_top"];
     "IX.23" [URL="/heath/IX/23/", target="_top"];
     "VII.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.7/", target="_top"];
     "IX.21" [URL="/heath/IX/21/", target="_top"];
     "IX.29" -> "VII.def.15";
     "IX.21" -> "VII.def.6";
     "IX.23" -> "IX.22";
     "IX.29" -> "IX.23";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
   }
