:order: 61
:original_id: I.48
:type: prop
:dependencies: g.60, g.15

.. _g.61:

G.61
====

**Heath ID:** :ref:`I.48`

   If in a triangle the square on one of the sides be equal to the squares on the remaining two sides of the triangle, the angle contained by the remaining two sides of the triangle is right.

For in the triangle ``ABC`` let the square on one side ``BC`` be equal to the squares on the sides ``BA``, ``AC``;

I say that the angle ``BAC`` is right.

For let ``AD`` be drawn from the point ``A`` at right angles to the straight line ``AC``, let ``AD`` be made equal to ``BA``, and let ``DC`` be joined.

Since ``DA`` is equal to ``AB``, the square on ``DA`` is also equal to the square on ``AB``. 

Let the square on ``AC`` be added to each; therefore the squares on ``DA``, ``AC`` are equal to the squares on ``BA``, ``AC``.

But the square on ``DC`` is equal to the squares on ``DA``, ``AC``, for the angle ``DAC`` is right; [:ref:`g.60`] and the square on ``BC`` is equal to the squares on ``BA``, ``AC``, for this is the hypothesis; therefore the square on ``DC`` is equal to the square on ``BC``, so that the side ``DC`` is also equal to ``BC``.

And, since ``DA`` is equal to ``AB``, and ``AC`` is common, the two sides ``DA``, ``AC`` are equal to the two sides ``BA``, ``AC``; and the base ``DC`` is equal to the base ``BC``; therefore the angle ``DAC`` is equal to the angle ``BAC``. [:ref:`g.15`] But the angle ``DAC`` is right; therefore the angle ``BAC`` is also right.

Therefore etc.


**Q. E. D.**


Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.54" [label="G.54", URL="/elements2/g.54/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.48" [label="G.48", URL="/elements2/g.48/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.23" [label="G.23", URL="/elements2/g.23/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.61" [label="G.61", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.61/", target="_top"];
     "G.60" [label="G.60", URL="/elements2/g.60/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.59" [label="G.59", URL="/elements2/g.59/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.50" [label="G.50", URL="/elements2/g.50/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.60" -> "G.54";
     "G.17" -> "G.16";
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
     "G.50" -> "G.48";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.61" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.23" -> "G.22";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.60" -> "G.23";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.61" -> "G.60";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.60" -> "G.59";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.60" -> "G.40";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.44" -> "G.38";
     "G.25" -> "G.17";
     "G.23" -> "G.21";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.54" -> "G.50";
     "G.8" -> "G.6";
     "G.23" -> "G.6";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.21" -> "G.19";
     "G.59" -> "G.19";
     "G.47" -> "G.36";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.23" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.44" -> "G.33";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
   }



Required for
------------

:ref:`g.525`, :ref:`g.526`
