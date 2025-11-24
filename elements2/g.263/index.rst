:order: 263
:original_id: VIII.10
:type: prop
:dependencies: g.227, g.228, g.219

.. _g.263:

G.263
=====

**Heath ID:** :ref:`VIII.10`

   If numbers fall between each of two numbers and an unit in continued proportion, however many numbers fall between each of them and an unit in continued proportion, so many also will fall between the numbers themselves in continued proportion.

For let the numbers D, E and F, G respectively fall between the two numbers A, B and the unit C in continued proportion; I say that, as many numbers as have fallen between each of the numbers A, B and the unit C in continued proportion, so many numbers will also fall between A, B in continued proportion.

For let D by multiplying F make H, and let the numbers D, F by multiplying H make K, L respectively.

Now, since, as the unit C is to the number D, so is D to E, therefore the unit C measures the number D the same number of times as D measures E. [:ref:`g.219`]

But the unit C measures the number D according to the units in D; therefore the number D also measures E according to the units in D; therefore D by multiplying itself has made E.

Again, since, as C is to the number D, so is E to A, therefore the unit C measures the number D the same number of times as E measures A.

But the unit C measures the number D according to the units in D; therefore E also measures A according to the units in D; therefore D by multiplying E has made A.

For the same reason also F by multiplying itself has made G, and by multiplying G has made B.

And, since D by multiplying itself has made E and by multiplying F has made H, therefore, as D is to F, so is E to H. [:ref:`g.227`]

For the same reason also,


.. container:: center

   as D is to F, so is H to G. [:ref:`g.228`]


Therefore also, as E is to H, so is H to G.

Again, since D by multiplying the numbers E, H has made A, K respectively, therefore, as E is to H, so is A to K. [:ref:`g.227`]

But, as E is to H, so is D to F; therefore also, as D is to F, so is A to K.

Again, since the numbers D, F by multiplying H have made K, L respectively, therefore, as D is to F, so is K to L. [:ref:`g.228`]

But, as D is to F, so is A to K; therefore also, as A is to K, so is K to L.

Further, since F by multiplying the numbers H, G has made L, B respectively, therefore, as H is to G, so is L to B. [:ref:`g.227`]

But, as H is to G, so is D to F; therefore also, as D is to F, so is L to B.

But it was also proved that,


.. container:: center

   as D is to F, so is A to K and K to L;


therefore also, as A is to K, so is K to L and L to B.

Therefore A, K, L, B are in continued proportion.

Therefore, as many numbers as fall between each of the numbers A, B and the unit C in continued proportion, so many also will fall between A, B in continued proportion. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.223" [label="G.223", URL="/elements2/g.223/", target="_top"];
     "G.218" [label="G.218", URL="/elements2/g.218/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.226" [label="G.226", URL="/elements2/g.226/", target="_top"];
     "G.263" [label="G.263", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.263/", target="_top"];
     "G.227" [label="G.227", URL="/elements2/g.227/", target="_top"];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.228" [label="G.228", URL="/elements2/g.228/", target="_top"];
     "G.227" -> "G.223";
     "G.223" -> "G.218";
     "G.226" -> "G.225";
     "G.228" -> "G.226";
     "G.228" -> "G.227";
     "G.263" -> "G.227";
     "G.217" -> "G.216";
     "G.218" -> "G.216";
     "G.222" -> "G.216";
     "G.218" -> "G.217";
     "G.225" -> "G.222";
     "G.222" -> "G.219";
     "G.223" -> "G.219";
     "G.227" -> "G.219";
     "G.263" -> "G.219";
     "G.263" -> "G.228";
   }
