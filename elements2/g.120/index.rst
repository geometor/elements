:order: 120
:original_id: IV.2
:type: prop
:dependencies: g.33, g.45, g.113, g.96

.. _g.120:

G.120
=====

**Heath ID:** :ref:`IV.2`

   In a given circle to inscribe a triangle equiangular with a given triangle.

Let ``ABC`` be the given circle, and ``DEF`` the given triangle; thus it is required to inscribe in the circle ``ABC`` a triangle equiangular with the triangle ``DEF``.

Let ``GH`` be drawn touching the circle ``ABC`` at ``A`` [:ref:`g.96`]; on the straight line ``AH``, and at the point ``A`` on it, let the angle ``HAC`` be constructed equal to the angle ``DEF``, and on the straight line ``AG``, and at the point ``A`` on it, let the angle ``GAB`` be constructed equal to the angle ``DFE``; [:ref:`g.33`] let ``BC`` be joined.

Then, since a straight line ``AH`` touches the circle ``ABC``, and from the point of contact at ``A`` the straight line ``AC`` is drawn across in the circle, therefore the angle ``HAC`` is equal to the angle ``ABC`` in the alternate segment of the circle. [:ref:`g.113`]

But the angle ``HAC`` is equal to the angle ``DEF``; therefore the angle ``ABC`` is also equal to the angle ``DEF``.

For the same reason


.. container:: center

   the angle ``ACB`` is also equal to the angle ``DFE``;


therefore the remaining angle ``BAC`` is also equal to the remaining angle ``EDF``. [:ref:`g.45`]

Therefore in the given circle there has been inscribed a triangle equiangular with the given triangle. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.113" [label="G.113", URL="/elements2/g.113/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.102" [label="G.102", URL="/elements2/g.102/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.101" [label="G.101", URL="/elements2/g.101/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.96" [label="G.96", style="rounded,filled", fillcolor=orange, URL="/elements2/g.96/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.112" [label="G.112", URL="/elements2/g.112/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.45" [label="G.45", URL="/elements2/g.45/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.26" [label="G.26", URL="/elements2/g.26/", target="_top"];
     "G.99" [label="G.99", URL="/elements2/g.99/", target="_top"];
     "G.100" [label="G.100", URL="/elements2/g.100/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.98" [label="G.98", URL="/elements2/g.98/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.120" [label="G.120", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.120/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.120" -> "G.113";
     "G.42" -> "G.41";
     "G.112" -> "G.102";
     "G.113" -> "G.102";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.102" -> "G.101";
     "G.28" -> "G.27";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.120" -> "G.96";
     "G.98" -> "G.28";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.112" -> "G.18";
     "G.24" -> "G.22";
     "G.113" -> "G.112";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.100" -> "G.45";
     "G.102" -> "G.45";
     "G.112" -> "G.45";
     "G.113" -> "G.45";
     "G.120" -> "G.45";
     "G.45" -> "G.44";
     "G.45" -> "G.42";
     "G.42" -> "G.40";
     "G.44" -> "G.38";
     "G.98" -> "G.26";
     "G.112" -> "G.26";
     "G.113" -> "G.99";
     "G.101" -> "G.100";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.26" -> "G.21";
     "G.42" -> "G.21";
     "G.45" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.99" -> "G.98";
     "G.26" -> "G.25";
     "G.27" -> "G.25";
     "G.38" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.8";
     "G.44" -> "G.33";
     "G.120" -> "G.33";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.26" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.100" -> "G.12";
     "G.112" -> "G.12";
   }



Required for
------------

:ref:`g.132`, :ref:`g.133`, :ref:`g.571`, :ref:`g.578`
