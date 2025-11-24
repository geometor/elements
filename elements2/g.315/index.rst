:order: 315
:original_id: IX.26
:type: prop
:dependencies: g.313, g.310

.. _g.315:

G.315
=====

**Heath ID:** :ref:`IX.26`

   If from an odd number an odd number be subtracted, the remainder will be even.

For from the odd number AB let the odd number BC be subtracted; I say that the remainder CA is even.

For, since AB is odd, let the unit BD be subtracted; therefore the remainder AD is even. [:ref:`g.310`]

For the same reason CD is also even; [:ref:`g.310`] so that the remainder CA is also even. [:ref:`g.313`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.310" [label="G.310", style="rounded,filled", fillcolor=orange, URL="/elements2/g.310/", target="_top"];
     "G.315" [label="G.315", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.315/", target="_top"];
     "G.313" [label="G.313", URL="/elements2/g.313/", target="_top"];
     "G.308" [label="G.308", style="rounded,filled", fillcolor=orange, URL="/elements2/g.308/", target="_top"];
     "G.315" -> "G.310";
     "G.315" -> "G.313";
     "G.313" -> "G.308";
   }
