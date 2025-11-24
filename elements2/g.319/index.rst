:order: 319
:original_id: IX.30
:type: prop
:dependencies: g.312

.. _g.319:

G.319
=====

**Heath ID:** :ref:`IX.30`

   If an odd number measure an even number, it will also measure the half of it.

For let the odd number A measure the even number B; I say that it will also measure the half of it.

For, since A measures B, let it measure it according to C; I say that C is not odd.

For, if possible, let it be so.

Then, since A measures B according to C, therefore A by multiplying C has made B.

Therefore B is made up of odd numbers the multitude of which is odd.

Therefore B is odd: [:ref:`g.312`] which is absurd, for by hypothesis it is even.

Therefore C is not odd; therefore C is even.

Thus A measures B an even number of times.

For this reason then it also measures the half of it. Q. E. D.


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
     "G.319" [label="G.319", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.319/", target="_top"];
     "G.312" [label="G.312", URL="/elements2/g.312/", target="_top"];
     "G.309" -> "G.308";
     "G.312" -> "G.311";
     "G.311" -> "G.309";
     "G.312" -> "G.309";
     "G.311" -> "G.310";
     "G.312" -> "G.310";
     "G.319" -> "G.312";
   }



Required for
------------

:ref:`g.320`
