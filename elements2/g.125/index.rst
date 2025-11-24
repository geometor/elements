:order: 125
:original_id: IV.5
:type: prop
:dependencies: g.17, g.11, g.112

.. _g.125:

G.125
=====

**Heath ID:** :ref:`IV.5`

   About a given triangle to circumscribe a circle.

Let ``ABC`` be the given triangle; thus it is required to circumscribe a circle about the given triangle ``ABC``.

Let the straight lines ``AB``, ``AC`` be bisected at the points ``D``, ``E`` [:ref:`g.17`], and from the points ``D``, ``E`` let ``DF``, ``EF`` be drawn at right angles to ``AB``, ``AC``; they will then meet within the triangle ``ABC``, or on the straight line ``BC``, or outside ``BC``.

First let them meet within at ``F``, and let ``FB``, ``FC``, ``FA`` be joined.

Then, since ``AD`` is equal to ``DB``, and ``DF`` is common and at right angles, therefore the base ``AF`` is equal to the base ``FB``. [:ref:`g.11`]

Similarly we can prove that


.. container:: center

   ``CF`` is also equal to ``AF``;


so that ``FB`` is also equal to ``FC``;


.. container:: center

   therefore the three straight lines ``FA``, ``FB``, ``FC`` are equal to one another.


Therefore the circle described with centre ``F`` and distance one of the straight lines ``FA``, ``FB``, ``FC`` will pass also through the remaining points, and the circle will have been circumscribed about the triangle ``ABC``.

Let it be circumscribed, as ``ABC``.

Next, let ``DF``, ``EF`` meet on the straight line ``BC`` at ``F``, as is the case in the second figure; and let ``AF`` be joined.

Then, similarly, we shall prove that the point ``F`` is the centre of the circle circumscribed about the triangle ``ABC``.

Again, let ``DF``, ``EF`` meet outside the triangle ``ABC`` at ``F``, as is the case in the third figure, and let ``AF``, ``BF``, ``CF`` be joined.

Then again, since ``AD`` is equal to ``DB``, and ``DF`` is common and at right angles, therefore the base ``AF`` is equal to the base ``BF``. [:ref:`g.11`]

Similarly we can prove that


.. container:: center

   ``CF`` is also equal to ``AF``;


so that ``BF`` is also equal to ``FC``; therefore the circle described with centre ``F`` and distance one of the straight lines ``FA``, ``FB``, ``FC`` will pass also through the remaining points, and will have been circumscribed about the triangle ``ABC``.

Therefore about the given triangle a circle has been circumscribed. Q. E. F.

And it is manifest that, when the centre of the circle falls within the triangle, the angle ``BAC``, being in a segment greater than the semicircle, is less than a right angle; when the centre falls on the straight line ``BC``, the angle ``BAC``, being in a semicircle, is right; and when the centre of the circle falls outside the triangle, the angle ``BAC``, being in a segment less than the semicircle, is greater than a right angle. [:ref:`g.112`]


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.102" [label="G.102", URL="/elements2/g.102/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.101" [label="G.101", URL="/elements2/g.101/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.125" [label="G.125", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.125/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.112" [label="G.112", URL="/elements2/g.112/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.45" [label="G.45", URL="/elements2/g.45/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.26" [label="G.26", URL="/elements2/g.26/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.100" [label="G.100", URL="/elements2/g.100/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.112" -> "G.102";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.102" -> "G.101";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.112" -> "G.18";
     "G.24" -> "G.22";
     "G.125" -> "G.112";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.100" -> "G.45";
     "G.102" -> "G.45";
     "G.112" -> "G.45";
     "G.45" -> "G.44";
     "G.45" -> "G.42";
     "G.42" -> "G.40";
     "G.112" -> "G.26";
     "G.44" -> "G.38";
     "G.101" -> "G.100";
     "G.25" -> "G.17";
     "G.125" -> "G.17";
     "G.24" -> "G.21";
     "G.26" -> "G.21";
     "G.42" -> "G.21";
     "G.45" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.26" -> "G.25";
     "G.38" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.8";
     "G.44" -> "G.33";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.26" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.125" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.100" -> "G.12";
     "G.112" -> "G.12";
   }



Required for
------------

:ref:`g.131`, :ref:`g.132`, :ref:`g.133`
