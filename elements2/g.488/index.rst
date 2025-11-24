:order: 488
:original_id: XI.4
:type: prop
:dependencies: g.24, g.36, g.11, g.15, g.487

.. _g.488:

G.488
=====

**Heath ID:** :ref:`XI.4`

   If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

For let a straight line EF be set up at right angles to the two straight lines AB, CD, which cut one another at the point E, from E; I say that EF is also at right angles to the plane through AB, CD.

For let AE, EB, CE, ED be cut off equal to one another, and let any straight line GEH be drawn across through E, at random; let AD, CB be joined, and further let FA, FG, FD, FC, FH, FB be joined from the point F taken at random <on EF>.

Now, since the two straight lines AE, ED are equal to the two straight lines CE, EB, and contain equal angles, [:ref:`g.24`] therefore the base AD is equal to the base CB, and the triangle AED will be equal to the triangle CEB; [:ref:`g.11`] so that the angle DAE is also equal to the angle EBC.

But the angle AEG is also equal to the angle BEH; [:ref:`g.24`] therefore AGE, BEH are two triangles which have two angles equal to two angles respectively, and one side equal to one side, namely that adjacent to the equal angles, that is to say, AE to EB; therefore they will also have the remaining sides equal to the remaining sides. [:ref:`g.36`]

Therefore GE is equal to EH, and AG to BH.

And, since AE is equal to EB, while FE is common and at right angles, therefore the base FA is equal to the base FB. [:ref:`g.11`]

For the same reason FC is also equal to FD.

And, since AD is equal to CB, and FA is also equal to FB, the two sides FA, AD are equal to the two sides FB, BC respectively; and the base FD was proved equal to the base FC; therefore the angle FAD is also equal to the angle FBC. [:ref:`g.15`]

And since, again, AG was proved equal to BH, and further FA also equal to FB, the two sides FA, AG are equal to the two sides FB, BH.

And the angle FAG was proved equal to the angle FBH; therefore the base FG is equal to the base FH. [:ref:`g.11`]

Now since, again, GE was proved equal to EH, and EF is common, the two sides GE, EF are equal to the two sides HE, EF; and the base FG is equal to the base FH; therefore the angle GEF is equal to the angle HEF. [:ref:`g.15`]

Therefore each of the angles GEF, HEF is right.

Therefore FE is at right angles to GH drawn at random through E.

Similarly we can prove that FE will also make right angles with all the straight lines which meet it and are in the plane of reference.

But a straight line is at right angles to a plane when it makes right angles with all the straight lines which meet it and are in that same plane; [:ref:`g.487`] therefore FE is at right angles to the plane of reference.

But the plane of reference is the plane through the straight lines AB, CD.

Therefore FE is at right angles to the plane through AB, CD.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.488" [label="G.488", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.488/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.487" [label="G.487", style="rounded,filled", fillcolor=orange, URL="/elements2/g.487/", target="_top"];
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

:ref:`g.494`, :ref:`g.495`, :ref:`g.496`, :ref:`g.500`, :ref:`g.504`, :ref:`g.509`, :ref:`g.510`, :ref:`g.511`, :ref:`g.512`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.525`, :ref:`g.526`, :ref:`g.527`, :ref:`g.528`, :ref:`g.529`, :ref:`g.489`, :ref:`g.490`, :ref:`g.492`, :ref:`g.493`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.571`, :ref:`g.572`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`
