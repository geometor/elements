:order: 314
:original_id: IX.25
:type: prop
:dependencies: g.313, g.310

.. _g.314:

G.314
=====

**Heath ID:** :ref:`IX.25`

   If from an even number an odd number be subtracted, the remainder will be odd.

For from the even number AB let the odd number BC be subtracted; I say that the remainder CA is odd.

For let the unit CD be subtracted from BC; therefore DB is even. [:ref:`g.310`]

But AB is also even; therefore the remainder AD is also even. [:ref:`g.313`]

And CD is an unit; therefore CA is odd. [:ref:`g.310`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.310" [label="G.310", style="rounded,filled", fillcolor=orange, URL="/elements2/g.310/", target="_top"];
     "G.314" [label="G.314", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.314/", target="_top"];
     "G.313" [label="G.313", URL="/elements2/g.313/", target="_top"];
     "G.308" [label="G.308", style="rounded,filled", fillcolor=orange, URL="/elements2/g.308/", target="_top"];
     "G.314" -> "G.310";
     "G.314" -> "G.313";
     "G.313" -> "G.308";
   }
