:order: 30
:number: 138
:type: prop
:categories: bisect
:dependencies: I.4, III.28




.. figure:: III.30.jpg
   :width: 50%

.. _III.30:

III.30
======

   To bisect a given circumference.

Let ``ADB`` be the given circumference; thus it is required to bisect the circumference ``ADB``.

Let ``AB`` be joined and bisected at ``C``; from the point ``C`` let ``CD`` be drawn at right angles to the straight line ``AB``,

and let ``AD``, ``DB`` be joined.

Then, since ``AC`` is equal to ``CB``, and ``CD`` is common,


.. container:: center

   the two sides ``AC``, ``CD`` are equal to the two sides ``BC``, ``CD``;


and the angle ``ACD`` is equal to the angle ``BCD``, for each is right;


.. container:: center

   therefore the base ``AD`` is equal to the base ``DB``. [:ref:`I.4`]


But equal straight lines cut off equal circumferences, the greater equal to the greater, and the less to the less; [:ref:`III.28`]


.. container:: center

   and each of the circumferences ``AD``, ``DB`` is less than a semicircle; therefore the circumference ``AD`` is equal to the circumference ``DB``.


Therefore the given circumference has been bisected at the point ``D``. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "III.5" [URL="/elements2/III/5/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "III.30" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/30/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "III.24" [URL="/elements2/III/24/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "III.28" [URL="/elements2/III/28/", target="_top"];
     "elem.3.1.p.1" [style="rounded,filled", fillcolor=orange];
     "III.26" [URL="/elements2/III/26/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "III.10" [URL="/elements2/III/10/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "III.def.11" [style="rounded,filled", fillcolor=orange, URL="/elements2/III/def.11/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "III.24" -> "I.8";
     "III.28" -> "I.8";
     "III.10" -> "III.5";
     "I.7" -> "I.5";
     "I.5" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "III.26" -> "III.24";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.5" -> "I.4";
     "III.26" -> "I.4";
     "III.30" -> "I.4";
     "I.8" -> "I.7";
     "III.30" -> "III.28";
     "III.10" -> "elem.3.1.p.1";
     "III.28" -> "III.26";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "III.24" -> "III.10";
     "I.3" -> "I.2";
     "III.26" -> "III.def.11";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
   }



Required for
------------

:ref:`IV.16`