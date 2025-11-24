:order: 506
:original_id: XI.20
:type: prop
:dependencies: g.30, g.35, g.11

.. _g.506:

G.506
=====

**Heath ID:** :ref:`XI.20`

   If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

For let the solid angle at A be contained by the three plane angles BAC, CAD, DAB; I say that any two of the angles BAC, CAD, DAB, taken together in any manner, are greater than the remaining one.

If now the angles BAC, CAD, DAB are equal to one another, it is manifest that any two are greater than the remaining one.

But, if not, let BAC be greater, and on the straight line AB, and at the point A on it, let the angle BAE be constructed, in the plane through BA, AC, equal to the angle DAB; let AE be made equal to AD, and let BEC, drawn across through the point E, cut the straight lines AB, AC at the points B, C; let DB, DC be joined.

Now, since DA is equal to AE, and AB is common, two sides are equal to two sides; and the angle DAB is equal to the angle BAE; therefore the base DB is equal to the base BE. [:ref:`g.11`]

And, since the two sides BD, DC are greater than BC, [:ref:`g.30`] and of these DB was proved equal to BE, therefore the remainder DC is greater than the remainder EC.

Now, since DA is equal to AE, and AC is common, and the base DC is greater than the base EC, therefore the angle DAC is greater than the angle EAC. [:ref:`g.35`]

But the angle DAB was also proved equal to the angle BAE; therefore the angles DAB, DAC are greater than the angle BAC.

Similarly we can prove that the remaining angles also, taken together two and two, are greater than the remaining one.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.506" [label="G.506", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.506/", target="_top"];
     "G.35" [label="G.35", URL="/elements2/g.35/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
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
     "G.30" [label="G.30", URL="/elements2/g.30/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.34" [label="G.34", URL="/elements2/g.34/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.29" [label="G.29", style="rounded,filled", fillcolor=orange, URL="/elements2/g.29/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.506" -> "G.35";
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
     "G.506" -> "G.30";
     "G.30" -> "G.28";
     "G.34" -> "G.28";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.27" -> "G.25";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.34" -> "G.33";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.34" -> "G.11";
     "G.35" -> "G.11";
     "G.506" -> "G.11";
     "G.35" -> "G.34";
     "G.11" -> "G.10";
     "G.30" -> "G.29";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.30" -> "G.12";
     "G.34" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.507`, :ref:`g.578`
