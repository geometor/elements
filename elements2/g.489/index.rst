:order: 489
:original_id: XI.5
:type: prop
:dependencies: g.486, g.488, g.487

.. _g.489:

G.489
=====

**Heath ID:** :ref:`XI.5`

   If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.

For let a straight line AB be set up at right angles to the three straight lines BC, BD, BE, at their point of meeting at B; I say that BC, BD, BE are in one plane.

For suppose they are not, but, if possible, let BD, BE be in the plane of reference and BC in one more elevated; let the plane through AB, BC be produced; it will thus make, as common section in the plane of reference, a straight line. [:ref:`g.486`]

Let it make BF.

Therefore the three straight lines AB, BC, BF are in one plane, namely that drawn through AB, BC.

Now, since AB is at right angles to each of the straight lines BD, BE, therefore AB is also at right angles to the plane through BD, BE. [:ref:`g.488`]

But the plane through BD, BE is the plane of reference; therefore AB is at right angles to the plane of reference.

Thus AB will also make right angles with all the straight lines which meet it and are in the plane of reference. [:ref:`g.487`]

But BF which is in the plane of reference meets it; therefore the angle ABF is right.

But, by hypothesis, the angle ABC is also right; therefore the angle ABF is equal to the angle ABC.

And they are in one plane: which is impossible.

Therefore the straight line BC is not in a more elevated plane; therefore the three straight lines BC, BD, BE are in one plane.

Therefore, if a straight line be set up at right angles to three straight lines, at their point of meeting, the three straight lines are in one plane. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.489" [label="G.489", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.489/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.488" [label="G.488", URL="/elements2/g.488/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.487" [label="G.487", style="rounded,filled", fillcolor=orange, URL="/elements2/g.487/", target="_top"];
     "G.486" [label="G.486", style="rounded,filled", fillcolor=orange, URL="/elements2/g.486/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.489" -> "G.488";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.488" -> "G.24";
     "G.24" -> "G.21";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.488" -> "G.487";
     "G.489" -> "G.487";
     "G.489" -> "G.486";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.488" -> "G.36";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.488" -> "G.15";
     "G.21" -> "G.19";
     "G.36" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.488" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.494`, :ref:`g.500`, :ref:`g.510`, :ref:`g.511`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.526`, :ref:`g.527`, :ref:`g.528`, :ref:`g.529`, :ref:`g.490`, :ref:`g.493`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`
