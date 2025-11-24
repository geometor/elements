:order: 26
:number: 363
:type: prop
:dependencies: IX.24, VII.def.7




.. figure:: IX.26.graphic.inverted.png

.. _IX.26:

IX.26
=====

   If from an odd number an odd number be subtracted, the remainder will be even.

For from the odd number AB let the odd number BC be subtracted; I say that the remainder CA is even.

For, since AB is odd, let the unit BD be subtracted; therefore the remainder AD is even. [:ref:`VII.def.7`]

For the same reason CD is also even; [:ref:`VII.def.7`] so that the remainder CA is also even. [:ref:`IX.24`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.7/", target="_top"];
     "VII.def.6" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.6/", target="_top"];
     "IX.24" [URL="/heath/IX/24/", target="_top"];
     "IX.26" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/26/", target="_top"];
     "IX.26" -> "VII.def.7";
     "IX.24" -> "VII.def.6";
     "IX.26" -> "IX.24";
   }
