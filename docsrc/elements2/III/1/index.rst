:order: 1
:number: 109
:type: prop
:tags: circle
:dependencies: I.8, I.def.10




.. figure:: III.1.jpg
   :width: 50%

.. _III.1:

III.1
=====

   To find the centre of a given circle.

Let ``ABC`` be the given circle; thus it is required to find the centre of the circle ``ABC``.

Let a straight line ``AB`` be drawn through it at random, and let it be bisected at the point ``D``; from ``D`` let ``DC`` be drawn at right angles to ``AB`` and let it be drawn through to ``E``; let ``CE`` be bisected at ``F``; I say that ``F`` is the centre of the circle ``ABC``.

For suppose it is not, but, if possible, let ``G`` be the centre, and let ``GA``, ``GD``, ``GB`` be joined.

Then, since ``AD`` is equal to ``DB``, and ``DG`` is common,


.. container:: center

   the two sides ``AD``, ``DG`` are equal to the two sides ``BD``, ``DG`` respectively;


and the base ``GA`` is equal to the base ``GB``, for they are radii;


.. container:: center

   therefore the angle ``ADG`` is equal to the angle ``GDB``. [:ref:`I.8`]


But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; [:ref:`I.def.10`]


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
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "III.1" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/1/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "III.1" -> "I.def.10";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.2" -> "I.1";
     "III.1" -> "I.8";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.3" -> "I.2";
     "I.5" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.7" -> "I.5";
     "I.5" -> "I.4";
   }



Required for
------------

:ref:`III.13`, :ref:`III.14`, :ref:`III.15`, :ref:`III.17`, :ref:`III.2`, :ref:`III.4`, :ref:`III.8`, :ref:`IV.12`, :ref:`IV.3`