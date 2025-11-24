:order: 22
:number: 359
:type: prop
:dependencies: IX.21, VII.def.7




.. figure:: IX.22.graphic.inverted.png

.. _IX.22:

IX.22
=====

   If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.

For let as many odd numbers as we please, AB, BC, CD, DE, even in multitude, be added together; I say that the whole AE is even.

For, since each of the numbers AB, BC, CD, DE is odd, if an unit be subtracted from each, each of the remainders will be even; [:ref:`VII.def.7`] so that the sum of them will be even. [:ref:`IX.21`]

But the multitude of the units is also even.

Therefore the whole AE is also even. [:ref:`IX.21`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.def.6" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.6/", target="_top"];
     "VII.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.7/", target="_top"];
     "IX.21" [URL="/heath/IX/21/", target="_top"];
     "IX.22" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/22/", target="_top"];
     "IX.21" -> "VII.def.6";
     "IX.22" -> "VII.def.7";
     "IX.22" -> "IX.21";
   }



Required for
------------

:ref:`IX.23`, :ref:`IX.29`, :ref:`IX.30`, :ref:`IX.31`