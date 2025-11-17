:order: 48
:number: 81
:type: prop
:tags: triangle
:dependencies: I.47, I.8




.. figure:: I.48.jpg
   :width: 50%



.. figure:: I.48-b.jpg
   :width: 50%

.. _I.48:

I.48
====

   If in a triangle the square on one of the sides be equal to the squares on the remaining two sides of the triangle, the angle contained by the remaining two sides of the triangle is right.

For in the triangle ``ABC`` let the square on one side ``BC`` be equal to the squares on the sides ``BA``, ``AC``;

I say that the angle ``BAC`` is right.

For let ``AD`` be drawn from the point ``A`` at right angles to the straight line ``AC``, let ``AD`` be made equal to ``BA``, and let ``DC`` be joined.

Since ``DA`` is equal to ``AB``, the square on ``DA`` is also equal to the square on ``AB``. 

Let the square on ``AC`` be added to each; therefore the squares on ``DA``, ``AC`` are equal to the squares on ``BA``, ``AC``.

But the square on ``DC`` is equal to the squares on ``DA``, ``AC``, for the angle ``DAC`` is right; [:ref:`I.47`] and the square on ``BC`` is equal to the squares on ``BA``, ``AC``, for this is the hypothesis; therefore the square on ``DC`` is equal to the square on ``BC``, so that the side ``DC`` is also equal to ``BC``.

And, since ``DA`` is equal to ``AB``, and ``AC`` is common, the two sides ``DA``, ``AC`` are equal to the two sides ``BA``, ``AC``; and the base ``DC`` is equal to the base ``BC``; therefore the angle ``DAC`` is equal to the angle ``BAC``. [:ref:`I.8`] But the angle ``DAC`` is right; therefore the angle ``BAC`` is also right.

Therefore etc.


**Q. E. D.**


Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.37" [URL="/elements2/I/37/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.46" [URL="/elements2/I/46/", target="_top"];
     "I.47" [URL="/elements2/I/47/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.41" [URL="/elements2/I/41/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.14" [URL="/elements2/I/14/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.35" [URL="/elements2/I/35/", target="_top"];
     "I.48" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/48/", target="_top"];
     "I.31" [URL="/elements2/I/31/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.41" -> "I.37";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.47" -> "I.46";
     "I.48" -> "I.47";
     "I.35" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.46" -> "I.34";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.47" -> "I.41";
     "I.31" -> "I.27";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.8" -> "I.7";
     "I.47" -> "I.14";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.48" -> "I.8";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.34" -> "I.26";
     "I.29" -> "I.post.5";
     "I.31" -> "I.23";
     "I.3" -> "I.2";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.37" -> "I.35";
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "I.7" -> "I.5";
   }
