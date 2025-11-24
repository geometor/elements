:order: 85
:original_id: III.9
:type: prop
:dependencies: g.15, g.18, g.84

.. _g.85:

G.85
====

**Heath ID:** :ref:`III.9`

   If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

Let ``ABC`` be a circle and ``D`` a point within it, and from ``D`` let more than two equal straight lines, namely ``DA``, ``DB``, ``DC``, fall on the circle ``ABC``; I say that the point ``D`` is the centre of the circle ``ABC``.

For let ``AB``, ``BC`` be joined and bisected at the points ``E``, ``F``, and let ``ED``, ``FD`` be joined and drawn through to the points ``G``, ``K``, ``H``, ``L``.

Then, since ``AE`` is equal to ``EB``, and ``ED`` is common,


.. container:: center

   the two sides ``AE``, ``ED`` are equal to the two sides ``BE``, ``ED``;


and the base ``DA`` is equal to the base ``DB``;


.. container:: center

   therefore the angle ``AED`` is equal to the angle ``BED``. [:ref:`g.15`]


Therefore each of the angles ``AED``, ``BED`` is right; [:ref:`g.18`] therefore ``GK`` cuts ``AB`` into two equal parts and at right angles.

And since, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line, [:ref:`g.84`]


.. container:: center

   the centre of the circle is on ``GK``.


For the same reason


.. container:: center

   the centre of the circle ``ABC`` is also on ``HL``.


And the straight lines ``GK``, ``HL`` have no other point common but the point ``D``;


.. container:: center

   therefore the point ``D`` is the centre of the circle ``ABC``.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.85" [label="G.85", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.85/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.84" [label="G.84", style="rounded,filled", fillcolor=orange, URL="/elements2/g.84/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.85" -> "G.15";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.5";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.85" -> "G.18";
     "G.12" -> "G.11";
     "G.11" -> "G.10";
     "G.85" -> "G.84";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }



Required for
------------

:ref:`g.106`
