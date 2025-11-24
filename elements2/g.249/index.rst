:order: 249
:original_id: VII.38
:type: prop
:dependencies: g.225

.. _g.249:

G.249
=====

**Heath ID:** :ref:`VII.38`

   If a number have any part whatever, it will be measured by a number called by the same name as the part.

For let the number A have any part whatever, B, and let C be a number called by the same name as the part B; I say that C measures A.

For, since B is a part of A called by the same name as C, and the unit D is also a part of C called by the same name as it, therefore, whatever part the unit D is of the number C, the same part is B of A also; therefore the unit D measures the number C the same number of times that B measures A.

Therefore, alternately, the unit D measures the number B the same number of times that C measures A. [:ref:`g.225`]

Therefore C measures A. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.249" [label="G.249", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.249/", target="_top"];
     "G.222" -> "G.216";
     "G.249" -> "G.225";
     "G.225" -> "G.222";
     "G.222" -> "G.219";
   }



Required for
------------

:ref:`g.250`
