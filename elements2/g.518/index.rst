:order: 518
:original_id: XI.29
:type: prop
:dependencies: g.47, g.49, g.517

.. _g.518:

G.518
=====

**Heath ID:** :ref:`XI.29`

   Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

Let CM, CN be parallelepipedal solids on the same base AB and of the same height, and let the extremities of their sides which stand up, namely AG, AF, LM, LN, CD, CE, BH, BK, be on the same straight lines FN, DK; I say that the solid CM is equal to the solid CN.

For, since each of the figures CH, CK is a parallelogram, CB is equal to each of the straight lines DH, EK, [:ref:`g.47`] hence DH is also equal to EK.

Let EH be subtracted from each; therefore the remainder DE is equal to the remainder HK.

Hence the triangle DCE is also equal to the triangle HBK, [:ref:`g.517`] and the parallelogram DG to the parallelogram HN. [:ref:`g.49`]

For the same reason the triangle AFG is also equal to the triangle MLN.

But the parallelogram CF is equal to the parallelogram BM, and CG to BN, for they are opposite; therefore the prism contained by the two triangles AFG, DCE and the three parallelograms AD, DG, CG is equal to the prism contained by the two triangles MLN, HBK and the three parallelograms BM, HN, BN.

Let there be added to each the solid of which the parallelogram AB is the base and GEHM its opposite; therefore the whole parallelepipedal solid CM is equal to the whole parallelepipedal solid CN.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.518" [label="G.518", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.518/", target="_top"];
     "G.46" [label="G.46", URL="/elements2/g.46/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.48" [label="G.48", URL="/elements2/g.48/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.49" [label="G.49", URL="/elements2/g.49/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.517" [label="G.517", style="rounded,filled", fillcolor=orange, URL="/elements2/g.517/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.49" -> "G.46";
     "G.42" -> "G.41";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.49" -> "G.48";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.518" -> "G.49";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.46" -> "G.38";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.47" -> "G.36";
     "G.21" -> "G.19";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.518" -> "G.517";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.518" -> "G.47";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
   }



Required for
------------

:ref:`g.519`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.526`, :ref:`g.527`, :ref:`g.529`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`
