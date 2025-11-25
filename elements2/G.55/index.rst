:order: 55
:original_id: I.42
:type: prop
:dependencies: G.33, G.44, G.51, G.54

.. _G.55:

G.55
====

**Heath ID:** :ref:`I.42`

   To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

Let ``ABC`` be the given triangle, and ``D`` the given rectilineal angle; thus it is required to construct in the rectilineal angle ``D`` a parallelogram equal to the triangle ``ABC``. 

Let ``BC`` be bisected at ``E``, and let ``AE`` be joined; on the straight line ``EC``, and at the point ``E`` on it, let the angle ``CEF`` be constructed equal to the angle ``D``; [:ref:`G.33`] through ``A`` let ``AG`` be drawn parallel to ``EC``, and [:ref:`G.44`] through ``C`` let ``CG`` be drawn parallel to ``EF``.

Then ``FECG`` is a parallelogram.

And, since ``BE`` is equal to ``EC``, the triangle ``ABE`` is also equal to the triangle ``AEC``, for they are on equal bases ``BE``, ``EC`` and in the same parallels ``BC``, ``AG``; [:ref:`G.51`] therefore the triangle ``ABC`` is double of the triangle ``AEC``.
        

But the parallelogram ``FECG`` is also double of the triangle ``AEC``, for it has the same base with it and is in the same parallels with it; [:ref:`G.54`] therefore the parallelogram ``FECG`` is equal to the triangle ``ABC``.

And it has the angle ``CEF`` equal to the given angle ``D``.

Therefore the parallelogram ``FECG`` has been constructed equal to the given triangle ``ABC``, in the angle ``CEF`` which is equal to ``D``. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.54" [label="G.54", fillcolor="#222244", URL="/elements2/G.54/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.36" [label="G.36", fillcolor="#222244", URL="/elements2/G.36/", target="_top"];
     "G.47" [label="G.47", fillcolor="#222244", URL="/elements2/G.47/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.49" [label="G.49", fillcolor="#222244", URL="/elements2/G.49/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.44" [label="G.44", fillcolor="#222244", URL="/elements2/G.44/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.51" [label="G.51", fillcolor="#222244", URL="/elements2/G.51/", target="_top"];
     "G.50" [label="G.50", fillcolor="#222244", URL="/elements2/G.50/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.46" [label="G.46", fillcolor="#222244", URL="/elements2/G.46/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.55" [label="G.55", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.55/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.48" [label="G.48", fillcolor="#222244", URL="/elements2/G.48/", target="_top"];
     "G.44" -> "G.33";
     "G.55" -> "G.33";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.21" -> "G.19";
     "G.24" -> "G.22";
     "G.42" -> "G.41";
     "G.38" -> "G.37";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.55" -> "G.54";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.15" -> "G.14";
     "G.47" -> "G.36";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.51" -> "G.49";
     "G.14" -> "G.12";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.55" -> "G.44";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.55" -> "G.51";
     "G.54" -> "G.50";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.44" -> "G.38";
     "G.46" -> "G.38";
     "G.49" -> "G.46";
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
     "G.25" -> "G.17";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.17" -> "G.16";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.11" -> "G.10";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
   }



Required for
------------

:ref:`G.57`, :ref:`G.58`
