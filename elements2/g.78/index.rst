:order: 78
:original_id: III.3
:type: prop
:dependencies: g.36, g.12, g.15, g.18

.. _g.78:

G.78
====

**Heath ID:** :ref:`III.3`

   If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

Let ``ABC`` be a circle, and in it let a straight line ``CD``
through the centre bisect a straight line ``AB`` not through the centre at the point ``F``;

I say that it also cuts it at right angles.

For let the centre of the circle ``ABC``
be taken, and let it be ``E``; let ``EA``, ``EB`` be joined.

Then, since ``AF`` is equal to ``FB``, and ``FE`` is common,


.. container:: center

   two sides are equal to two sides;



.. container:: center

   and the base ``EA`` is equal to the base ``EB``; therefore the angle ``AFE`` is equal to the angle ``BFE``. [:ref:`g.15`]


But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; [:ref:`g.18`]


.. container:: center

   therefore each of the angles ``AFE``, ``BFE`` is right.


Therefore ``CD``, which is through the centre, and bisects ``AB`` which is not through the centre, also cuts it at right angles.

Again, let ``CD`` cut ``AB`` at right angles; I say that it also bisects it. that is, that ``AF`` is equal to ``FB``.

For, with the same construction,


.. container:: center

   since ``EA`` is equal to ``EB``,


the angle ``EAF`` is also equal to the angle ``EBF``. [:ref:`g.12`]

But the right angle ``AFE`` is equal to the right angle ``BFE``, therefore ``EAF``, ``EBF`` are two triangles having two angles equal to two angles and one side equal to one side, namely ``EF``, which is common to them, and subtends one of the equal angles;


.. container:: center

   therefore they will also have the remaining sides equal to the remaining sides; [:ref:`g.36`] therefore ``AF`` is equal to ``FB``.


Therefore etc. Q. E. D.
with the same construction, τῶν αὐτῶν κατασκευασθέντων.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
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
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.78" [label="G.78", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.78/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
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
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.78" -> "G.18";
     "G.24" -> "G.22";
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



Required for
------------

:ref:`g.92`, :ref:`g.94`, :ref:`g.116`, :ref:`g.117`, :ref:`g.118`, :ref:`g.79`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.549`
