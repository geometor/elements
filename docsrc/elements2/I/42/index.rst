:order: 42
:number: 75
:type: prop
:categories: construct
:tags: line, triangle
:dependencies: I.23, I.31, I.38, I.41




.. figure:: I.42.jpg
   :width: 50%

.. _I.42:

I.42
====

   To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

Let ``ABC`` be the given triangle, and ``D`` the given rectilineal angle; thus it is required to construct in the rectilineal angle ``D`` a parallelogram equal to the triangle ``ABC``. 

Let ``BC`` be bisected at ``E``, and let ``AE`` be joined; on the straight line ``EC``, and at the point ``E`` on it, let the angle ``CEF`` be constructed equal to the angle ``D``; [:ref:`I.23`] through ``A`` let ``AG`` be drawn parallel to ``EC``, and [:ref:`I.31`] through ``C`` let ``CG`` be drawn parallel to ``EF``.

Then ``FECG`` is a parallelogram.

And, since ``BE`` is equal to ``EC``, the triangle ``ABE`` is also equal to the triangle ``AEC``, for they are on equal bases ``BE``, ``EC`` and in the same parallels ``BC``, ``AG``; [:ref:`I.38`] therefore the triangle ``ABC`` is double of the triangle ``AEC``.
        

But the parallelogram ``FECG`` is also double of the triangle ``AEC``, for it has the same base with it and is in the same parallels with it; [:ref:`I.41`] therefore the parallelogram ``FECG`` is equal to the triangle ``ABC``.

And it has the angle ``CEF`` equal to the given angle ``D``.

Therefore the parallelogram ``FECG`` has been constructed equal to the given triangle ``ABC``, in the angle ``CEF`` which is equal to ``D``. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.37" [URL="/elements2/I/37/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.41" [URL="/elements2/I/41/", target="_top"];
     "I.36" [URL="/elements2/I/36/", target="_top"];
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
     "I.38" [URL="/elements2/I/38/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.42" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/42/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.35" [URL="/elements2/I/35/", target="_top"];
     "I.33" [URL="/elements2/I/33/", target="_top"];
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
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.38" -> "I.34";
     "I.41" -> "I.34";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.42" -> "I.41";
     "I.38" -> "I.36";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
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
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.42" -> "I.38";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.31" -> "I.23";
     "I.42" -> "I.23";
     "I.34" -> "I.26";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.29" -> "I.post.5";
     "I.3" -> "I.2";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "I.36" -> "I.33";
     "I.37" -> "I.31";
     "I.38" -> "I.31";
     "I.42" -> "I.31";
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.7" -> "I.5";
   }



Required for
------------

:ref:`I.44`, :ref:`I.45`, :ref:`II.14`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`