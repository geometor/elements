:order: 549
:original_id: XII.16
:type: prop
:dependencies: g.11, g.78, g.330, g.96

.. _g.549:

G.549
=====

**Heath ID:** :ref:`XII.16`

   Given two circles about the same centre, to inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle.

Let ABCD, EFGH be the two given circles about the same centre K; thus it is required to inscribe in the greater circle ABCD an equilateral polygon with an even number of sides which does not touch the circle EFGH.

For let the straight line BKD be drawn through the centre K, and from the point G let GA be drawn at right angles to the straight line BD and carried through to C; therefore AC touches the circle EFGH. [:ref:`g.96`]

Then, bisecting the circumference BAD, bisecting the half of it, and doing this continually, we shall leave a circumference less than AD. [:ref:`g.330`]

Let such be left, and let it be LD; from L let LM be drawn perpendicular to BD and carried through to N, and let LD, DN be joined; therefore LD is equal to DN. [:ref:`g.78`, :ref:`g.11`]

Now, since LN is parallel to AC, and AC touches the circle EFGH, therefore LN does not touch the circle EFGH; therefore LD, DN are far from touching the circle EFGH.

If then we fit into the circle ABCD straight lines equal to the straight line LD and placed continuously, there will be inscribed in the circle ABCD an equilateral polygon with an even number of sides which does not touch the lesser circle EFGH. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.330" [label="G.330", URL="/elements2/g.330/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.549" [label="G.549", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.549/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.145" [label="G.145", style="rounded,filled", fillcolor=orange, URL="/elements2/g.145/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.96" [label="G.96", style="rounded,filled", fillcolor=orange, URL="/elements2/g.96/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.78" [label="G.78", URL="/elements2/g.78/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.549" -> "G.330";
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.330" -> "G.145";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.24" -> "G.21";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.78" -> "G.36";
     "G.549" -> "G.96";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.78" -> "G.15";
     "G.21" -> "G.19";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.36" -> "G.25";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.549" -> "G.78";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.78" -> "G.18";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.549" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.78" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }
