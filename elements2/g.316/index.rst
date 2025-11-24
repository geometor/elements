:order: 316
:original_id: IX.27
:type: prop
:dependencies: g.313, g.310

.. _g.316:

G.316
=====

**Heath ID:** :ref:`IX.27`

   If from an odd number an even number be subtracted, the remainder will be odd.

For from the odd number AB let the even number BC be subtracted; I say that the remainder CA is odd.

Let the unit AD be subtracted; therefore DB is even. [:ref:`g.310`]

But BC is also even; therefore the remainder CD is even. [:ref:`g.313`]

Therefore CA is odd. [:ref:`g.310`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.310" [label="G.310", style="rounded,filled", fillcolor=orange, URL="/elements2/g.310/", target="_top"];
     "G.316" [label="G.316", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.316/", target="_top"];
     "G.313" [label="G.313", URL="/elements2/g.313/", target="_top"];
     "G.308" [label="G.308", style="rounded,filled", fillcolor=orange, URL="/elements2/g.308/", target="_top"];
     "G.316" -> "G.310";
     "G.316" -> "G.313";
     "G.313" -> "G.308";
   }
