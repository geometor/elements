:order: 33
:number: 370
:type: prop
:dependencies: VII.def.8, VII.def.9




.. figure:: IX.33.graphic.inverted.png

.. _IX.33:

IX.33
=====

   If a number have its half odd, it is even-times odd only.

For let the number A have its half odd; I say that A is even-times odd only.

Now that it is even-times odd is manifest; for the half of it, being odd, measures it an even number of times. [:ref:`VII.def.9`]

I say next that it is also even-times odd only.

For, if A is even-times even also, it will be measured by an even number according to an even number; [:ref:`VII.def.8`] so that the half of it will also be measured by an even number though it is odd: which is absurd.

Therefore A is even-times odd only. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.def.8" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.8/", target="_top"];
     "IX.33" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/33/", target="_top"];
     "VII.def.9" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.9/", target="_top"];
     "IX.33" -> "VII.def.8";
     "IX.33" -> "VII.def.9";
   }
