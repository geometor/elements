:order: 30
:number: 367
:type: prop
:dependencies: IX.23




.. figure:: IX.30.graphic.inverted.png

.. _IX.30:

IX.30
=====

   If an odd number measure an even number, it will also measure the half of it.

For let the odd number A measure the even number B; I say that it will also measure the half of it.

For, since A measures B, let it measure it according to C; I say that C is not odd.

For, if possible, let it be so.

Then, since A measures B according to C, therefore A by multiplying C has made B.

Therefore B is made up of odd numbers the multitude of which is odd.

Therefore B is odd: [:ref:`IX.23`] which is absurd, for by hypothesis it is even.

Therefore C is not odd; therefore C is even.

Thus A measures B an even number of times.

For this reason then it also measures the half of it. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.def.6" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.6/", target="_top"];
     "IX.30" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/30/", target="_top"];
     "IX.22" [URL="/heath/IX/22/", target="_top"];
     "IX.23" [URL="/heath/IX/23/", target="_top"];
     "VII.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.7/", target="_top"];
     "IX.21" [URL="/heath/IX/21/", target="_top"];
     "IX.21" -> "VII.def.6";
     "IX.23" -> "IX.22";
     "IX.30" -> "IX.23";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
   }



Required for
------------

:ref:`IX.31`