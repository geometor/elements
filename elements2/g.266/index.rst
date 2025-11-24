:order: 266
:original_id: VIII.12
:type: prop
:dependencies: g.265, g.227, g.228

.. _g.266:

G.266
=====

**Heath ID:** :ref:`VIII.12`

   Between two cube numbers there are two mean proportional numbers, and the cube has to the cube the ratio triplicate of that which the side has to the side.

Let A, B be cube numbers, and let C be the side of A, and D of B; I say that between A, B there are two mean proportional numbers, and A has to B the ratio triplicate of that which C has to D.

For let C by multiplying itself make E, and by multiplying D let it make F; let D by multiplying itself make G, and let the numbers C, D by multiplying F make H, K respectively.

Now, since A is a cube, and C its side, and C by multiplying itself has made E, therefore C by multiplying itself has made E and by multiplying E has made A.

For the same reason also D by multiplying itself has made G and by multiplying G has made B.

And, since C by multiplying the numbers C, D has made E, F respectively, therefore, as C is to D, so is E to F. [:ref:`g.227`]

For the same reason also,


.. container:: center

   as C is to D, so is F to G. [:ref:`g.228`]


Again, since C by multiplying the numbers E, F has made A, H respectively, therefore, as E is to F, so is A to H. [:ref:`g.227`]

But, as E is to F, so is C to D.

Therefore also, as C is to D, so is A to H.

Again, since the numbers C, D by multiplying F have made H, K respectively, therefore, as C is to D, so is H to K. [:ref:`g.228`]

Again, since D by multiplying each of the numbers F, G has made K, B respectively, therefore, as F is to G, so is K to B. [:ref:`g.227`]

But, as F is to G, so is C to D; therefore also, as C is to D, so is A to H, H to K, and K to B.

Therefore H, K are two mean proportionals between A, B.

I say next that A also has to B the ratio triplicate of that which C has to D.

For, since A, H, K, B are four numbers in proportion, therefore A has to B the ratio triplicate of that which A has to H. [:ref:`g.265`]

But, as A is to H, so is C to D; therefore A also has to B the ratio triplicate of that which C has to D. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.223" [label="G.223", URL="/elements2/g.223/", target="_top"];
     "G.218" [label="G.218", URL="/elements2/g.218/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.266" [label="G.266", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.266/", target="_top"];
     "G.226" [label="G.226", URL="/elements2/g.226/", target="_top"];
     "G.227" [label="G.227", URL="/elements2/g.227/", target="_top"];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.265" [label="G.265", style="rounded,filled", fillcolor=orange, URL="/elements2/g.265/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.228" [label="G.228", URL="/elements2/g.228/", target="_top"];
     "G.227" -> "G.223";
     "G.223" -> "G.218";
     "G.226" -> "G.225";
     "G.228" -> "G.226";
     "G.228" -> "G.227";
     "G.266" -> "G.227";
     "G.217" -> "G.216";
     "G.218" -> "G.216";
     "G.222" -> "G.216";
     "G.266" -> "G.265";
     "G.218" -> "G.217";
     "G.225" -> "G.222";
     "G.222" -> "G.219";
     "G.223" -> "G.219";
     "G.227" -> "G.219";
     "G.266" -> "G.228";
   }
