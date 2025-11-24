:order: 111
:original_id: III.30
:type: prop
:dependencies: g.11, g.109

.. _g.111:

G.111
=====

**Heath ID:** :ref:`III.30`

   To bisect a given circumference.

Let ``ADB`` be the given circumference; thus it is required to bisect the circumference ``ADB``.

Let ``AB`` be joined and bisected at ``C``; from the point ``C`` let ``CD`` be drawn at right angles to the straight line ``AB``,

and let ``AD``, ``DB`` be joined.

Then, since ``AC`` is equal to ``CB``, and ``CD`` is common,


.. container:: center

   the two sides ``AC``, ``CD`` are equal to the two sides ``BC``, ``CD``;


and the angle ``ACD`` is equal to the angle ``BCD``, for each is right;


.. container:: center

   therefore the base ``AD`` is equal to the base ``DB``. [:ref:`g.11`]


But equal straight lines cut off equal circumferences, the greater equal to the greater, and the less to the less; [:ref:`g.109`]


.. container:: center

   and each of the circumferences ``AD``, ``DB`` is less than a semicircle; therefore the circumference ``AD`` is equal to the circumference ``DB``.


Therefore the given circumference has been bisected at the point ``D``. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.111" [label="G.111", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.111/", target="_top"];
     "G.105" [label="G.105", URL="/elements2/g.105/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.109" [label="G.109", URL="/elements2/g.109/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.86" [label="G.86", URL="/elements2/g.86/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.103" [label="G.103", style="rounded,filled", fillcolor=orange, URL="/elements2/g.103/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.107" [label="G.107", URL="/elements2/g.107/", target="_top"];
     "G.84" [label="G.84", style="rounded,filled", fillcolor=orange, URL="/elements2/g.84/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.80" [label="G.80", URL="/elements2/g.80/", target="_top"];
     "G.107" -> "G.105";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.111" -> "G.109";
     "G.15" -> "G.14";
     "G.105" -> "G.86";
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.80" -> "G.2";
     "G.86" -> "G.2";
     "G.8" -> "G.6";
     "G.105" -> "G.15";
     "G.109" -> "G.15";
     "G.8" -> "G.5";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.107" -> "G.103";
     "G.12" -> "G.11";
     "G.107" -> "G.11";
     "G.111" -> "G.11";
     "G.11" -> "G.10";
     "G.109" -> "G.107";
     "G.86" -> "G.84";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.86" -> "G.80";
   }



Required for
------------

:ref:`g.136`
