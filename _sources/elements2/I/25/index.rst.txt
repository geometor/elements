:order: 25
:number: 58
:type: prop
:tags: line, triangle
:dependencies: I.24, I.4




.. figure:: I.25.jpg
   :width: 50%



.. figure:: I.25-b.jpg
   :width: 50%

.. _I.25:

I.25
====

   If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other.

Let ``ABC``, ``DEF`` be two triangles having the two sides ``AB``, ``AC`` equal to the two sides ``DE``, ``DF`` respectively, namely ``AB`` to ``DE``, and ``AC`` to ``DF``; and let the base ``BC`` be greater than the base ``EF``;

I say that the angle ``BAC`` is also greater than the angle ``EDF``. 

For, if not, it is either equal to it or less.

Now the angle ``BAC`` is not equal to the angle ``EDF``; for then the base ``BC`` would also have been equal to the base ``EF``, [:ref:`I.4`] but it is not; therefore the angle ``BAC`` is not equal to the angle ``EDF``.

Neither again is the angle ``BAC`` less than the angle ``EDF``; for then the base ``BC`` would also have been less than the base ``EF``, [:ref:`I.24`] but it is not; therefore the angle ``BAC`` is not less than the angle ``EDF``.

But it was proved that it is not equal either; therefore the angle ``BAC`` is greater than the angle ``EDF``.

Therefore etc.


**Q. E. D.**


Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.18" [URL="/elements2/I/18/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.25" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/25/", target="_top"];
     "I.24" [URL="/elements2/I/24/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.19" [URL="/elements2/I/19/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.18" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.10" -> "I.9";
     "I.19" -> "I.18";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.3" -> "I.2";
     "I.24" -> "I.23";
     "I.16" -> "I.15";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.15" -> "I.13";
     "I.25" -> "I.24";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.8" -> "I.7";
     "I.16" -> "I.10";
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.13" -> "I.11";
     "I.24" -> "I.19";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.24" -> "I.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.24" -> "I.4";
     "I.25" -> "I.4";
   }
