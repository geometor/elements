:order: 76
:original_id: III.1
:type: prop
:dependencies: g.15, g.18

.. _g.76:

G.76
====

**Heath ID:** :ref:`III.1`

   To find the centre of a given circle.

Let ``ABC`` be the given circle; thus it is required to find the centre of the circle ``ABC``.

Let a straight line ``AB`` be drawn through it at random, and let it be bisected at the point ``D``; from ``D`` let ``DC`` be drawn at right angles to ``AB`` and let it be drawn through to ``E``; let ``CE`` be bisected at ``F``; I say that ``F`` is the centre of the circle ``ABC``.

For suppose it is not, but, if possible, let ``G`` be the centre, and let ``GA``, ``GD``, ``GB`` be joined.

Then, since ``AD`` is equal to ``DB``, and ``DG`` is common,


.. container:: center

   the two sides ``AD``, ``DG`` are equal to the two sides ``BD``, ``DG`` respectively;


and the base ``GA`` is equal to the base ``GB``, for they are radii;


.. container:: center

   therefore the angle ``ADG`` is equal to the angle ``GDB``. [:ref:`g.15`]


But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; [:ref:`g.18`]


.. container:: center

   therefore the angle ``GDB`` is right.


But the angle ``FDB`` is also right; therefore the angle ``FDB`` is equal to the angle ``GDB``, the greater to the less: which is impossible.


.. container:: center

   Therefore ``G`` is not the centre of the circle ``ABC``.


Similarly we can prove that neither is any other point except ``F``.


.. container:: center

   Therefore the point ``F`` is the centre of the circle ``ABC``.



.. _elem.3.1.p.1:


**III.1.p.1**


From this it is manifest that, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line. Q. E. F.


.. note::


   **12**

   

   12. For suppose it is not. This is expressed in the Greek by the two words Μὴ γάρ, but such an elliptical phrase is impossible in English.


.. note::


   **17**

   

   the two sides AD, DG are equal to the two sides BD, DG respectively. As before observed, Euclid is not always careful to put the equals in corresponding order. The text here has ``GD``, ``DB``.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.76" [label="G.76", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.76/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.76" -> "G.15";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.5";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.76" -> "G.18";
     "G.12" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }



Required for
------------

:ref:`g.90`, :ref:`g.92`, :ref:`g.94`, :ref:`g.97`, :ref:`g.77`, :ref:`g.79`, :ref:`g.83`, :ref:`g.133`, :ref:`g.121`, :ref:`g.571`, :ref:`g.578`
