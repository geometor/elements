:order: 248
:original_id: VII.37
:type: prop
:dependencies: g.225

.. _g.248:

G.248
=====

**Heath ID:** :ref:`VII.37`

   If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

For let the number A be measured by any number B; I say that A has a part called by the same name as B.

For, as many times as B measures A, so many units let there be in C.

Since B measures A according to the units in C, and the unit D also measures the number C according to the units in it, therefore the unit D measures the number C the same number of times as B measures A.

Therefore, alternately, the unit D measures the number B the same number of times as C measures A; [:ref:`g.225`] therefore, whatever part the unit D is of the number B, the same part is C of A also.

But the unit D is a part of the number B called by the same name as it; therefore C is also a part of A called by the same name as B, so that A has a part C which is called by the same name as B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.248" [label="G.248", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.248/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.222" -> "G.216";
     "G.248" -> "G.225";
     "G.225" -> "G.222";
     "G.222" -> "G.219";
   }



Required for
------------

:ref:`g.250`
