:order: 303
:original_id: IX.16
:type: prop
:dependencies: g.230, g.231

.. _g.303:

G.303
=====

**Heath ID:** :ref:`IX.16`

   If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

For let the two numbers A, B be prime to one another; I say that B is not to any other number as A is to B.

For, if possible, as A is to B, so let B be to C.

Now A, B are prime, primes are also least, [:ref:`g.231`] and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent; [:ref:`g.230`] therefore A measures B as antecedent antecedent.

But it also measures itself; therefore A measures A, B which are prime to one another: which is absurd.

Therefore B will not be to C, as A is to B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.208" [label="G.208", URL="/elements2/g.208/", target="_top"];
     "G.223" [label="G.223", URL="/elements2/g.223/", target="_top"];
     "G.206" [label="G.206", style="rounded,filled", fillcolor=orange, URL="/elements2/g.206/", target="_top"];
     "G.218" [label="G.218", URL="/elements2/g.218/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.211" [label="G.211", URL="/elements2/g.211/", target="_top"];
     "G.231" [label="G.231", URL="/elements2/g.231/", target="_top"];
     "G.226" [label="G.226", URL="/elements2/g.226/", target="_top"];
     "G.303" [label="G.303", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.303/", target="_top"];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.207" [label="G.207", URL="/elements2/g.207/", target="_top"];
     "G.230" [label="G.230", URL="/elements2/g.230/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.211" -> "G.208";
     "G.230" -> "G.223";
     "G.207" -> "G.206";
     "G.231" -> "G.206";
     "G.223" -> "G.218";
     "G.226" -> "G.225";
     "G.230" -> "G.211";
     "G.303" -> "G.231";
     "G.231" -> "G.226";
     "G.217" -> "G.216";
     "G.218" -> "G.216";
     "G.222" -> "G.216";
     "G.208" -> "G.207";
     "G.231" -> "G.230";
     "G.303" -> "G.230";
     "G.218" -> "G.217";
     "G.225" -> "G.222";
     "G.230" -> "G.222";
     "G.222" -> "G.219";
     "G.223" -> "G.219";
     "G.230" -> "G.219";
   }



Required for
------------

:ref:`g.305`
