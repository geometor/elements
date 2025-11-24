:order: 291
:original_id: IX.7
:type: prop
:dependencies: g.290, g.232

.. _g.291:

G.291
=====

**Heath ID:** :ref:`IX.7`

   If a composite number by multiplying any number make some number, the product will be solid.

For let the composite number A by multiplying any number B make C; I say that C is solid.

For, since A is composite, it will be measured by some number. [:ref:`g.290`]

Let it be measured by D; and, as many times as D measures A, so many units let there be in E.

Since then D measures A according to the units in E, therefore E by multiplying D has made A. [:ref:`g.232`]

And, since A by multiplying B has made C, and A is the product of D, E, therefore the product of D, E by multiplying B has made C.

Therefore C is solid, and D, E, B are its sides. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.291" [label="G.291", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.291/", target="_top"];
     "G.290" [label="G.290", style="rounded,filled", fillcolor=orange, URL="/elements2/g.290/", target="_top"];
     "G.232" [label="G.232", style="rounded,filled", fillcolor=orange, URL="/elements2/g.232/", target="_top"];
     "G.291" -> "G.290";
     "G.291" -> "G.232";
   }
