:order: 508
:original_id: XI.22
:type: prop
:dependencies: g.34, g.11

.. _g.508:

G.508
=====

**Heath ID:** :ref:`XI.22`

   If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

Let there be three plane angles ABC, DEF, GHK, of which two, taken together in any manner, are greater than the remaining one, namely


.. container:: center

   the angles ABC, DEF greater than the angle GHK, the angles DEF, GHK greater than the angle ABC,


and, further, the angles GHK, ABC greater than the angle DEF; let the straight lines AB, BC, DE, EF, GH, HK be equal, and let AC, DF, GK be joined; I say that it is possible to construct a triangle out of straight lines equal to AC, DF, GK, that is, that any two of the straight lines AC, DF, GK are greater than the remaining one.

Now, if the angles ABC, DEF, GHK are equal to one another, it is manifest that, AC, DF, GK being equal also, it is possible to construct a triangle out of straight lines equal to AC, DF, GK.

But, if not, let them be unequal, and on the straight line HK, and at the point H on it, let the angle KHL be constructed equal to the angle ABC; let HL be made equal to one of the straight lines AB, BC, DE, EF, GH, HK, and let KL, GL be joined.

Now, since the two sides AB, BC are equal to the two sides KH, HL, and the angle at B is equal to the angle KHL, therefore the base AC is equal to the base KL. [:ref:`g.11`]

And, since the angles ABC, GHK are greater than the angle DEF, while the angle ABC is equal to the angle KHL, therefore the angle GHL is greater than the angle DEF.

And, since the two sides GH, HL are equal to the two sides DE, EF, and the angle GHL is greater than the angle DEF, therefore the base GL is greater than the base DF. [:ref:`g.34`]

But GK, KL are greater than GL.

Therefore GK, KL are much greater than DF.

But KL is equal to AC; therefore AC, GK are greater than the remaining straight line DF.

Similarly we can prove that AC, DF are greater than GK, and further DF, GK are greater than AC.

Therefore it is possible to construct a triangle out of straight lines equal to AC, DF, GK. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.508" [label="G.508", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.508/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.34" [label="G.34", URL="/elements2/g.34/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.28" -> "G.27";
     "G.24" -> "G.21";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.15" -> "G.14";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.34" -> "G.28";
     "G.27" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.34" -> "G.33";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.34" -> "G.11";
     "G.508" -> "G.11";
     "G.508" -> "G.34";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.34" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.509`
