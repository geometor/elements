:order: 304
:original_id: IX.17
:type: prop
:dependencies: g.223, g.230, g.231

.. _g.304:

G.304
=====

**Heath ID:** :ref:`IX.17`

   If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the last will not be to any other number as the first to the second.

For let there be as many numbers as we please, A, B, C, D, in continued proportion, and let the extremes of them, A, D, be prime to one another; I say that D is not to any other number as A is to B.

For, if possible, as A is to B, so let D be to E; therefore, alternately, as A is to D, so is B to E. [:ref:`g.223`]

But A, D are prime, primes are also least, [:ref:`g.231`] and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent. [:ref:`g.230`]

Therefore A measures B.

And, as A is to B, so is B to C.

Therefore B also measures C; so that A also measures C.

And since, as B is to C, so is C to D, and B measures C, therefore C also measures D.

But A measured C; so that A also measures D.

But it also measures itself; therefore A measures A, D which are prime to one another : which is impossible.

Therefore D will not be to any other number as A is to B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.208" [label="G.208", URL="/elements2/g.208/", target="_top"];
     "G.223" [label="G.223", URL="/elements2/g.223/", target="_top"];
     "G.218" [label="G.218", URL="/elements2/g.218/", target="_top"];
     "G.206" [label="G.206", style="rounded,filled", fillcolor=orange, URL="/elements2/g.206/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.231" [label="G.231", URL="/elements2/g.231/", target="_top"];
     "G.211" [label="G.211", URL="/elements2/g.211/", target="_top"];
     "G.226" [label="G.226", URL="/elements2/g.226/", target="_top"];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.207" [label="G.207", URL="/elements2/g.207/", target="_top"];
     "G.230" [label="G.230", URL="/elements2/g.230/", target="_top"];
     "G.304" [label="G.304", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.304/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.211" -> "G.208";
     "G.230" -> "G.223";
     "G.304" -> "G.223";
     "G.223" -> "G.218";
     "G.207" -> "G.206";
     "G.231" -> "G.206";
     "G.226" -> "G.225";
     "G.304" -> "G.231";
     "G.230" -> "G.211";
     "G.231" -> "G.226";
     "G.217" -> "G.216";
     "G.218" -> "G.216";
     "G.222" -> "G.216";
     "G.208" -> "G.207";
     "G.231" -> "G.230";
     "G.304" -> "G.230";
     "G.218" -> "G.217";
     "G.225" -> "G.222";
     "G.230" -> "G.222";
     "G.222" -> "G.219";
     "G.223" -> "G.219";
     "G.230" -> "G.219";
   }



Required for
------------

:ref:`g.306`
