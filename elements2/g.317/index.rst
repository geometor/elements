:order: 317
:original_id: IX.28
:type: prop
:dependencies: g.309, g.232

.. _g.317:

G.317
=====

**Heath ID:** :ref:`IX.28`

   If an odd number by multiplying an even number make some number, the product will be even.

For let the odd number A by multiplying the even number B make C; I say that C is even.

For, since A by multiplying B has made C, therefore C is made up of as many numbers equal to B as there are units in A. [:ref:`g.232`]

And B is even; therefore C is made up of even numbers.

But, if as many even numbers as we please be added together, the whole is even. [:ref:`g.309`]

Therefore C is even. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.317" [label="G.317", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.317/", target="_top"];
     "G.308" [label="G.308", style="rounded,filled", fillcolor=orange, URL="/elements2/g.308/", target="_top"];
     "G.232" [label="G.232", style="rounded,filled", fillcolor=orange, URL="/elements2/g.232/", target="_top"];
     "G.309" [label="G.309", URL="/elements2/g.309/", target="_top"];
     "G.309" -> "G.308";
     "G.317" -> "G.232";
     "G.317" -> "G.309";
   }
