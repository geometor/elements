:order: 2
:number: 85
:type: prop
:tags: line
:dependencies: I.31, I.46




.. figure:: II.2.jpg
   :width: 50%

.. _II.2:

II.2
====

   If a straight line be cut at random, the rectangle contained by the whole and both of the segments is equal to the square on the whole.

For let the straight line ``AB`` be cut at random at the point ``C``; I say that the rectangle contained by ``AB``, ``BC`` together with the rectangle contained by ``BA``, ``AC`` is equal to the square on ``AB``.

For let the square ``ADEB`` be described on ``AB`` [:ref:`I.46`], and let ``CF`` be drawn through ``C`` parallel to either ``AD`` or ``BE``. [:ref:`I.31`]

Then ``AE`` is equal to ``AF``, ``CE``.

Now ``AE`` is the square on ``AB``;

``AF`` is the rectangle contained by ``BA``, ``AC``, for it is contained by ``DA``, ``AC``, and ``AD`` is equal to ``AB``;


.. container:: center

   and ``CE`` is the rectangle ``AB``, ``BC``, for ``BE`` is equal to ``AB``.


Therefore the rectangle ``BA``, ``AC`` together with the rectangle ``AB``, ``BC`` is equal to the square on ``AB``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.46" [URL="/elements2/I/46/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.31" [URL="/elements2/I/31/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "II.2" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/II/2/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "II.2" -> "I.46";
     "I.46" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.31" -> "I.27";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.8" -> "I.7";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.31" -> "I.23";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.29" -> "I.post.5";
     "I.34" -> "I.26";
     "I.3" -> "I.2";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.46" -> "I.31";
     "II.2" -> "I.31";
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.34" -> "I.29";
     "I.46" -> "I.29";
     "I.7" -> "I.5";
   }
