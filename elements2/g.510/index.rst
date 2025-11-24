:order: 510
:original_id: XI.24
:type: prop
:dependencies: g.47, g.11, g.494, g.501

.. _g.510:

G.510
=====

**Heath ID:** :ref:`XI.24`

   If a solid be contained by parallel planes, the opposite planes in it are equal and parallelogrammic.

For let the solid CDHG be contained by the parallel planes AC, GF, AH, DF, BF, AE; I say that the opposite planes in it are equal and parallelogrammic.

For, since the two parallel planes BG, CE are cut by the plane AC, their common sections are parallel. [:ref:`g.501`]

Therefore AB is parallel to DC.

Again, since the two parallel planes BF, AE are cut by the plane AC, their common sections are parallel. [:ref:`g.501`]

Therefore BC is parallel to AD.

But AB was also proved parallel to DC; therefore AC is a parallelogram.

Similarly we can prove that each of the planes DF, FG, GB, BF, AE is a parallelogram.

Let AH, DF be joined.

Then, since AB is parallel to DC, and BH to CF, the two straight lines AB, BH which meet one another are parallel to the two straight lines DC, CF which meet one another, not in the same plane; therefore they will contain equal angles; [:ref:`g.494`] therefore the angle ABH is equal to the angle DCF.

And, since the two sides AB, BH are equal to the two sides DC, CF, [:ref:`g.47`] and the angle ABH is equal to the angle DCF, therefore the base AH is equal to the base DF, and the triangle ABH is equal to the triangle DCF. [:ref:`g.11`]

And the parallelogram BG is double of the triangle ABH, and the parallelogram CE double of the triangle DCF; [:ref:`g.47`] therefore the parallelogram BG is equal to the parallelogram CE.

Similarly we can prove that AC is also equal to GF, and AE to BF.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.494" [label="G.494", URL="/elements2/g.494/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.46" [label="G.46", URL="/elements2/g.46/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.510" [label="G.510", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.510/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.492" [label="G.492", URL="/elements2/g.492/", target="_top"];
     "G.490" [label="G.490", URL="/elements2/g.490/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.501" [label="G.501", URL="/elements2/g.501/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.489" [label="G.489", URL="/elements2/g.489/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.39" [label="G.39", URL="/elements2/g.39/", target="_top"];
     "G.488" [label="G.488", URL="/elements2/g.488/", target="_top"];
     "G.491" [label="G.491", URL="/elements2/g.491/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.493" [label="G.493", URL="/elements2/g.493/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.487" [label="G.487", style="rounded,filled", fillcolor=orange, URL="/elements2/g.487/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.486" [label="G.486", style="rounded,filled", fillcolor=orange, URL="/elements2/g.486/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.484" [label="G.484", style="rounded,filled", fillcolor=orange, URL="/elements2/g.484/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.485" [label="G.485", URL="/elements2/g.485/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.510" -> "G.494";
     "G.17" -> "G.16";
     "G.494" -> "G.46";
     "G.42" -> "G.41";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.24";
     "G.39" -> "G.24";
     "G.42" -> "G.24";
     "G.488" -> "G.24";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.488" -> "G.15";
     "G.490" -> "G.15";
     "G.494" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.493" -> "G.492";
     "G.493" -> "G.490";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.510" -> "G.501";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.490" -> "G.489";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.492" -> "G.42";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.39" -> "G.38";
     "G.46" -> "G.38";
     "G.490" -> "G.39";
     "G.489" -> "G.488";
     "G.492" -> "G.488";
     "G.493" -> "G.488";
     "G.492" -> "G.491";
     "G.25" -> "G.17";
     "G.494" -> "G.493";
     "G.24" -> "G.21";
     "G.39" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.488" -> "G.487";
     "G.489" -> "G.487";
     "G.490" -> "G.487";
     "G.492" -> "G.487";
     "G.38" -> "G.37";
     "G.501" -> "G.37";
     "G.489" -> "G.486";
     "G.491" -> "G.486";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.47" -> "G.36";
     "G.488" -> "G.36";
     "G.21" -> "G.19";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.510" -> "G.47";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.8";
     "G.485" -> "G.484";
     "G.501" -> "G.484";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.488" -> "G.11";
     "G.490" -> "G.11";
     "G.510" -> "G.11";
     "G.11" -> "G.10";
     "G.490" -> "G.485";
     "G.492" -> "G.485";
     "G.14" -> "G.12";
   }



Required for
------------

:ref:`g.511`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.526`, :ref:`g.527`, :ref:`g.529`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`
