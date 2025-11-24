:order: 79
:original_id: III.4
:type: prop
:dependencies: g.76, g.78

.. _g.79:

G.79
====

**Heath ID:** :ref:`III.4`

   If in a circle two straight lines cut one another which are not through the centre, they do not bisect one another.

Let ``ABCD`` be a circle, and in it let the two straight lines ``AC``, ``BD``, which are not through the centre, cut one another at ``E``;

I say that they do not bisect one another.

For, if possible, let them bisect one another, so that ``AE`` is equal to ``EC``, and ``BE`` to ``ED``; let the centre of the circle ``ABCD`` be taken [:ref:`g.76`], and let it be ``F``; let ``FE`` be joined.

Then, since a straight line ``FE`` through the centre bisects a straight line ``AC`` not through the centre,


.. container:: center

   it also cuts it at right angles; [:ref:`g.78`] therefore the angle ``FEA`` is right.


Again, since a straight line ``FE`` bisects a straight line ``BD``,


.. container:: center

   it also cuts it at right angles; [:ref:`g.78`] therefore the angle ``FEB`` is right.


But the angle ``FEA`` was also proved right;


.. container:: center

   therefore the angle ``FEA`` is equal to the angle ``FEB``, the less to the greater: which is impossible.


Therefore ``AC``, ``BD`` do not bisect one another.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.76" [label="G.76", URL="/elements2/g.76/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
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
     "G.79" [label="G.79", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.79/", target="_top"];
     "G.79" -> "G.76";
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
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
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.76" -> "G.15";
     "G.78" -> "G.15";
     "G.21" -> "G.19";
     "G.36" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.79" -> "G.78";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.76" -> "G.18";
     "G.78" -> "G.18";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.78" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }
