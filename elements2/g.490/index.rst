:order: 490
:original_id: XI.6
:type: prop
:dependencies: g.39, g.11, g.15, g.485, g.489, g.487

.. _g.490:

G.490
=====

**Heath ID:** :ref:`XI.6`

   If two straight lines be at right angles to the same plane, the straight lines will be parallel.

For let the two straight lines AB, CD be at right angles to the plane of reference; I say that AB is parallel to CD.

For let them meet the plane of reference at the points B, D, let the straight line BD be joined, let DE be drawn, in the plane of reference, at right angles to BD, let DE be made equal to AB, and let BE, AE, AD be joined.

Now, since AB is at right angles to the plane of reference, it will also make right angles with all the straight lines which meet it and are in the plane of reference. [:ref:`g.487`]

But each of the straight lines BD, BE is in the plane of reference and meets AB; therefore each of the angles ABD, ABE is right.

For the same reason each of the angles CDB, CDE is also right.

And, since AB is equal to DE, and BD is common, the two sides AB, BD are equal to the two sides ED, DB; and they include right angles; therefore the base AD is equal to the base BE. [:ref:`g.11`]

And, since AB is equal to DE, while AD is also equal to BE, the two sides AB, BE are equal to the two sides ED, DA; and AE is their common base; therefore the angle ABE is equal to the angle EDA. [:ref:`g.15`]

But the angle ABE is right; therefore the angle EDA is also right; therefore ED is at right angles to DA.

But it is also at right angles to each of the straight lines BD, DC; therefore ED is set up at right angles to the three straight lines BD, DA, DC at their point of meeting; therefore the three straight lines BD, DA, DC are in one plane. [:ref:`g.489`]

But, in whatever plane DB, DA are, in that plane is AB also, for every triangle is in one plane; [:ref:`g.485`] therefore the straight lines AB, BD, DC are in one plane.

And each of the angles ABD, BDC is right; therefore AB is parallel to CD. [:ref:`g.39`]

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.490" [label="G.490", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.490/", target="_top"];
     "G.489" [label="G.489", URL="/elements2/g.489/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.39" [label="G.39", URL="/elements2/g.39/", target="_top"];
     "G.488" [label="G.488", URL="/elements2/g.488/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.487" [label="G.487", style="rounded,filled", fillcolor=orange, URL="/elements2/g.487/", target="_top"];
     "G.486" [label="G.486", style="rounded,filled", fillcolor=orange, URL="/elements2/g.486/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.484" [label="G.484", style="rounded,filled", fillcolor=orange, URL="/elements2/g.484/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.485" [label="G.485", URL="/elements2/g.485/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.24";
     "G.39" -> "G.24";
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
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.490" -> "G.489";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.39" -> "G.38";
     "G.490" -> "G.39";
     "G.489" -> "G.488";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.39" -> "G.21";
     "G.15" -> "G.14";
     "G.488" -> "G.487";
     "G.489" -> "G.487";
     "G.490" -> "G.487";
     "G.489" -> "G.486";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.488" -> "G.36";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.9" -> "G.8";
     "G.485" -> "G.484";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.488" -> "G.11";
     "G.490" -> "G.11";
     "G.11" -> "G.10";
     "G.490" -> "G.485";
     "G.14" -> "G.12";
   }



Required for
------------

:ref:`g.494`, :ref:`g.500`, :ref:`g.510`, :ref:`g.511`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.526`, :ref:`g.527`, :ref:`g.528`, :ref:`g.529`, :ref:`g.493`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`
