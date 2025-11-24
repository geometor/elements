:order: 318
:original_id: IX.29
:type: prop
:dependencies: g.312, g.232

.. _g.318:

G.318
=====

**Heath ID:** :ref:`IX.29`

   If an odd number by multiplying an odd number make some number, the product will be odd.

For let the odd number A by multiplying the odd number B make C; I say that C is odd.

For, since A by multiplying B has made C, therefore C is made up of as many numbers equal to B as there are units in A. [:ref:`g.232`]

And each of the numbers A, B is odd; therefore C is made up of odd numbers the multitude of which is odd.

Thus C is odd. [:ref:`g.312`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.308" [label="G.308", style="rounded,filled", fillcolor=orange, URL="/elements2/g.308/", target="_top"];
     "G.311" [label="G.311", URL="/elements2/g.311/", target="_top"];
     "G.309" [label="G.309", URL="/elements2/g.309/", target="_top"];
     "G.310" [label="G.310", style="rounded,filled", fillcolor=orange, URL="/elements2/g.310/", target="_top"];
     "G.232" [label="G.232", style="rounded,filled", fillcolor=orange, URL="/elements2/g.232/", target="_top"];
     "G.318" [label="G.318", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.318/", target="_top"];
     "G.312" [label="G.312", URL="/elements2/g.312/", target="_top"];
     "G.309" -> "G.308";
     "G.312" -> "G.311";
     "G.311" -> "G.309";
     "G.312" -> "G.309";
     "G.311" -> "G.310";
     "G.312" -> "G.310";
     "G.318" -> "G.232";
     "G.318" -> "G.312";
   }
