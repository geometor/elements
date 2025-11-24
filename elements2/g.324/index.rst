:order: 324
:original_id: IX.33
:type: prop
:dependencies: g.321, g.323

.. _g.324:

G.324
=====

**Heath ID:** :ref:`IX.33`

   If a number have its half odd, it is even-times odd only.

For let the number A have its half odd; I say that A is even-times odd only.

Now that it is even-times odd is manifest; for the half of it, being odd, measures it an even number of times. [:ref:`g.323`]

I say next that it is also even-times odd only.

For, if A is even-times even also, it will be measured by an even number according to an even number; [:ref:`g.321`] so that the half of it will also be measured by an even number though it is odd: which is absurd.

Therefore A is even-times odd only. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.321" [label="G.321", style="rounded,filled", fillcolor=orange, URL="/elements2/g.321/", target="_top"];
     "G.323" [label="G.323", style="rounded,filled", fillcolor=orange, URL="/elements2/g.323/", target="_top"];
     "G.324" [label="G.324", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.324/", target="_top"];
     "G.324" -> "G.321";
     "G.324" -> "G.323";
   }
