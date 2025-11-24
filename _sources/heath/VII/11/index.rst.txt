:order: 11
:number: 282
:type: prop
:dependencies: VII.def.20, elem.7.7 elem.7.8




.. figure:: VII.11.graphic.inverted.png

.. _VII.11:

VII.11
======

   If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.

As the whole AB is to the whole CD, so let AE subtracted be to CF subtracted; I say that the remainder EB is also to the remainder FD as the whole AB to the whole CD.

Since, as AB is to CD, so is AE to CF, whatever part or parts AB is of CD, the same part or the same parts is AE of CF also; [:ref:`VII.def.20`]

Therefore also the remainder EB is the same part or parts of FD that AB is of CD. [:ref:`elem.7.7 elem.7.8`]

Therefore, as EB is to FD, so is AB to CD. [:ref:`VII.def.20`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "elem.7.7 elem.7.8" [style="rounded,filled", fillcolor=orange];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "VII.11" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VII/11/", target="_top"];
     "VII.11" -> "elem.7.7 elem.7.8";
     "VII.11" -> "VII.def.20";
   }
