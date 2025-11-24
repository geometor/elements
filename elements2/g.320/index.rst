:order: 320
:original_id: IX.31
:type: prop
:dependencies: g.319

.. _g.320:

G.320
=====

**Heath ID:** :ref:`IX.31`

   If an odd number be prime to any number, it will also be prime to the double of it.

For let the odd number A be prime to any number B, and let C be double of B; I say that A is prime to C.

For, if they are not prime to one another, some number will measure them.

Let a number measure them, and let it be D.

Now A is odd; therefore D is also odd.

And since D which is odd measures C, and C is even, therefore [D] will measure the half of C also. [:ref:`g.319`]

But B is half of C; therefore D measures B.

But it also measures A; therefore D measures A, B which are prime to one another: which is impossible.

Therefore A cannot but be prime to C.

Therefore A, C are prime to one another. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.320" [label="G.320", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.320/", target="_top"];
     "G.308" [label="G.308", style="rounded,filled", fillcolor=orange, URL="/elements2/g.308/", target="_top"];
     "G.311" [label="G.311", URL="/elements2/g.311/", target="_top"];
     "G.309" [label="G.309", URL="/elements2/g.309/", target="_top"];
     "G.310" [label="G.310", style="rounded,filled", fillcolor=orange, URL="/elements2/g.310/", target="_top"];
     "G.319" [label="G.319", URL="/elements2/g.319/", target="_top"];
     "G.312" [label="G.312", URL="/elements2/g.312/", target="_top"];
     "G.309" -> "G.308";
     "G.312" -> "G.311";
     "G.311" -> "G.309";
     "G.312" -> "G.309";
     "G.311" -> "G.310";
     "G.312" -> "G.310";
     "G.320" -> "G.319";
     "G.319" -> "G.312";
   }
