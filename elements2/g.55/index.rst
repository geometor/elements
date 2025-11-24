:order: 55
:original_id: I.42
:type: prop
:dependencies: g.33, g.44, g.51, g.54

.. _g.55:

G.55
====

**Heath ID:** :ref:`I.42`

   To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

Let ``ABC`` be the given triangle, and ``D`` the given rectilineal angle; thus it is required to construct in the rectilineal angle ``D`` a parallelogram equal to the triangle ``ABC``. 

Let ``BC`` be bisected at ``E``, and let ``AE`` be joined; on the straight line ``EC``, and at the point ``E`` on it, let the angle ``CEF`` be constructed equal to the angle ``D``; [:ref:`g.33`] through ``A`` let ``AG`` be drawn parallel to ``EC``, and [:ref:`g.44`] through ``C`` let ``CG`` be drawn parallel to ``EF``.

Then ``FECG`` is a parallelogram.

And, since ``BE`` is equal to ``EC``, the triangle ``ABE`` is also equal to the triangle ``AEC``, for they are on equal bases ``BE``, ``EC`` and in the same parallels ``BC``, ``AG``; [:ref:`g.51`] therefore the triangle ``ABC`` is double of the triangle ``AEC``.
        

But the parallelogram ``FECG`` is also double of the triangle ``AEC``, for it has the same base with it and is in the same parallels with it; [:ref:`g.54`] therefore the parallelogram ``FECG`` is equal to the triangle ``ABC``.

And it has the angle ``CEF`` equal to the given angle ``D``.

Therefore the parallelogram ``FECG`` has been constructed equal to the given triangle ``ABC``, in the angle ``CEF`` which is equal to ``D``. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.51" [label="G.51", URL="/elements2/g.51/", target="_top"];
     "G.54" [label="G.54", URL="/elements2/g.54/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.46" [label="G.46", URL="/elements2/g.46/", target="_top"];
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
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.49" [label="G.49", URL="/elements2/g.49/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.50" [label="G.50", URL="/elements2/g.50/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.55" [label="G.55", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.55/", target="_top"];
     "G.55" -> "G.51";
     "G.55" -> "G.54";
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
     "G.50" -> "G.48";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.51" -> "G.49";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.55" -> "G.44";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.44" -> "G.38";
     "G.46" -> "G.38";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.54" -> "G.50";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.47" -> "G.36";
     "G.21" -> "G.19";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.44" -> "G.33";
     "G.55" -> "G.33";
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

:ref:`g.57`, :ref:`g.58`, :ref:`g.75`, :ref:`g.197`, :ref:`g.200`, :ref:`g.201`, :ref:`g.202`, :ref:`g.466`, :ref:`g.467`, :ref:`g.472`, :ref:`g.473`, :ref:`g.475`, :ref:`g.476`, :ref:`g.376`, :ref:`g.377`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.402`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.429`, :ref:`g.430`, :ref:`g.435`, :ref:`g.437`, :ref:`g.442`, :ref:`g.443`, :ref:`g.460`, :ref:`g.461`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.527`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.569`, :ref:`g.574`, :ref:`g.578`
