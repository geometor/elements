:order: 61
:original_id: I.48
:type: prop
:dependencies: G.60, G.15

.. _G.61:

G.61
====

**Heath ID:** :ref:`I.48`

   If in a triangle the square on one of the sides be equal to the squares on the remaining two sides of the triangle, the angle contained by the remaining two sides of the triangle is right.

For in the triangle ``ABC`` let the square on one side ``BC`` be equal to the squares on the sides ``BA``, ``AC``;

I say that the angle ``BAC`` is right.

For let ``AD`` be drawn from the point ``A`` at right angles to the straight line ``AC``, let ``AD`` be made equal to ``BA``, and let ``DC`` be joined.

Since ``DA`` is equal to ``AB``, the square on ``DA`` is also equal to the square on ``AB``. 

Let the square on ``AC`` be added to each; therefore the squares on ``DA``, ``AC`` are equal to the squares on ``BA``, ``AC``.

But the square on ``DC`` is equal to the squares on ``DA``, ``AC``, for the angle ``DAC`` is right; [:ref:`G.60`] and the square on ``BC`` is equal to the squares on ``BA``, ``AC``, for this is the hypothesis; therefore the square on ``DC`` is equal to the square on ``BC``, so that the side ``DC`` is also equal to ``BC``.

And, since ``DA`` is equal to ``AB``, and ``AC`` is common, the two sides ``DA``, ``AC`` are equal to the two sides ``BA``, ``AC``; and the base ``DC`` is equal to the base ``BC``; therefore the angle ``DAC`` is equal to the angle ``BAC``. [:ref:`G.15`] But the angle ``DAC`` is right; therefore the angle ``BAC`` is also right.

Therefore etc.


**Q. E. D.**


Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.59" [label="G.59", fillcolor="#222244", URL="/elements2/G.59/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.60" [label="G.60", fillcolor="#222244", URL="/elements2/G.60/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.61" [label="G.61", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.61/", target="_top"];
     "G.54" [label="G.54", fillcolor="#222244", URL="/elements2/G.54/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.36" [label="G.36", fillcolor="#222244", URL="/elements2/G.36/", target="_top"];
     "G.47" [label="G.47", fillcolor="#222244", URL="/elements2/G.47/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.44" [label="G.44", fillcolor="#222244", URL="/elements2/G.44/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.50" [label="G.50", fillcolor="#222244", URL="/elements2/G.50/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.23" [label="G.23", fillcolor="#222244", URL="/elements2/G.23/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.48" [label="G.48", fillcolor="#222244", URL="/elements2/G.48/", target="_top"];
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.44" -> "G.33";
     "G.60" -> "G.59";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.21" -> "G.19";
     "G.59" -> "G.19";
     "G.23" -> "G.22";
     "G.24" -> "G.22";
     "G.61" -> "G.60";
     "G.42" -> "G.41";
     "G.38" -> "G.37";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.60" -> "G.40";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.23" -> "G.21";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.60" -> "G.54";
     "G.8" -> "G.6";
     "G.23" -> "G.6";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.15" -> "G.14";
     "G.47" -> "G.36";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.14" -> "G.12";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.54" -> "G.50";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.44" -> "G.38";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.23" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.60" -> "G.23";
     "G.25" -> "G.17";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.17" -> "G.16";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.11" -> "G.10";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.61" -> "G.15";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.50" -> "G.48";
   }
