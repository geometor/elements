:order: 109
:original_id: III.28
:type: prop
:dependencies: g.15, g.107

.. _g.109:

G.109
=====

**Heath ID:** :ref:`III.28`

   In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

Let ``ABC``, ``DEF`` be equal circles, and in the circles let ``AB``, ``DE`` be equal straight lines cutting off ``ACB``, ``DFE`` as greater circumferences and ``AGB``, ``DHE`` as lesser; I say that the greater circumference ``ACB`` is equal to the greater circumference ``DFE``, and the less circumference ``AGB`` to ``DHE``.

For let the centres ``K``, ``L`` of the circles be taken, and let ``AK``, ``KB``, ``DL``, ``LE`` be joined.

Now, since the circles are equal,


.. container:: center

   the radii are also equal; therefore the two sides ``AK``, ``KB`` are equal to the two sides ``DL``, ``LE``;


and the base ``AB`` is equal to the base ``DE``;


.. container:: center

   therefore the angle ``AKB`` is equal to the angle ``DLE``. [:ref:`g.15`]


But equal angles stand on equal circumferences, when they are at the centres; [:ref:`g.107`]


.. container:: center

   therefore the circumference ``AGB`` is equal to ``DHE``.


And the whole circle ``ABC`` is also equal to the whole circle ``DEF``; therefore the circumference ``ACB`` which remains is also equal to the circumference ``DFE`` which remains.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.105" [label="G.105", URL="/elements2/g.105/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.109" [label="G.109", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.109/", target="_top"];
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

:ref:`g.111`, :ref:`g.136`, :ref:`g.569`, :ref:`g.574`, :ref:`g.578`, :ref:`g.565`
