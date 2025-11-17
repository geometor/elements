:order: 25
:number: 133
:type: prop
:categories: describe
:tags: circle
:dependencies: I.6, III.9




.. figure:: III.25.jpg
   :width: 50%

.. _III.25:

III.25
======

   Given a segment of a circle, to describe the complete circle of which it is a segment.

Let ``ABC`` be the given segment of a circle; thus it is required to describe the complete circle belonging to the segment ``ABC``, that is, of which it is a segment.

For let ``AC`` be bisected at ``D``, let ``DB`` be drawn from the point ``D`` at right angles to ``AC``, and let ``AB``. be joined;


.. container:: center

   the angle ``ABD`` is then greater than, equal to, or less than the angle ``BAD``.


First let it be greater; and on the straight line ``BA``, and at the point ``A`` on it, let the angle ``BAE`` be constructed equal to the angle ``ABD``; let ``DB`` be drawn through to ``E``, and let ``EC`` be joined.

Then, since the angle ``ABE`` is equal to the angle ``BAE``,


.. container:: center

   the straight line ``EB`` is also equal to ``EA``. [:ref:`I.6`]


And, since ``AD`` is equal to ``DC``, and ``DE`` is common,


.. container:: center

   the two sides ``AD``, ``DE`` are equal to the two sides ``CD``, ``DE`` respectively;


and the angle ``ADE`` is equal to the angle ``CDE``, for each is right;


.. container:: center

   therefore the base ``AE`` is equal to the base ``CE``.


But ``AE`` was proved equal to ``BE``;


.. container:: center

   therefore ``BE`` is also equal to ``CE``;


therefore the three straight lines ``AE``, ``EB``, ``EC`` are equal to one another.

Therefore the circle drawn with centre ``E`` and distance one of the straight lines ``AE``, ``EB``, ``EC`` will also pass through the remaining points and will have been completed. [:ref:`III.9`]

Therefore, given a segment of a circle, the complete circle has been described.

And it is manifest that the segment ``ABC`` is less than a semicircle, because the centre ``E`` happens to be outside it.

Similarly, even if the angle ``ABD`` be equal to the angle ``BAD``, ``AD`` being equal to each of the two ``BD``, ``DC``,


.. container:: center

   the three straight lines ``DA``, ``DB``, ``DC`` will be equal to one another, 
           ``D`` will be the centre of the completed circle, and ``ABC`` will clearly be a semicircle.


But, if the angle ``ABD`` be less than the angle ``BAD``, and if we construct, on the straight line ``BA`` and at the point ``A`` on it, an angle equal to the angle ``ABD``, the centre will fall on ``DB`` within the segment ``ABC``, and the segment

``ABC`` will clearly be greater than a semicircle.

Therefore, given a segment of a circle, the complete circle has been described. Q. E. F.
to describe the complete circle, προσαναγράψαι τὸν κύκλον, literally “to describe the circle ``on to it``.’


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "III.9" [URL="/elements2/III/9/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "III.25" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/25/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "elem.3.1.p.1" [style="rounded,filled", fillcolor=orange];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.6" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/6/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "III.25" -> "III.9";
     "III.9" -> "I.def.10";
     "III.9" -> "I.8";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "III.9" -> "elem.3.1.p.1";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.8" -> "I.7";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.5" -> "I.3";
     "III.25" -> "I.6";
     "I.2" -> "I.cn.3";
     "I.7" -> "I.5";
     "I.5" -> "I.4";
   }
