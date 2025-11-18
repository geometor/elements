:order: 23
:number: 131
:type: prop
:categories: construct
:tags: line, circle
:dependencies: I.16, III.def.11




.. figure:: III.23.jpg
   :width: 50%

.. _III.23:

III.23
======

   On the same straight line there cannot be constructed two similar and unequal segments of circles on the same side.

For, if possible, on the same straight line ``AB`` let two similar and unequal segments of circles ``ACB``, ``ADB`` be constructed on the same side;

let ``ACD`` be drawn through, and let ``CB``, ``DB`` be joined.

Then, since the segment ``ACB`` is similar to the segment ``ADB``, and similar segments of circles are those which admit equal angles, [:ref:`III.def.11`]


.. container:: center

   the angle ``ACB`` is equal to the angle ``ADB``, the exterior to the interior: which is impossible. [:ref:`I.16`]


Therefore etc. Q. E. D.
cannot be constructed, οὐ συσταθήσεται, the same phrase as in 1. 7.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "III.def.11" [style="rounded,filled", fillcolor=orange, URL="/elements2/III/def.11/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "III.23" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/23/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.10" -> "I.9";
     "I.7" -> "I.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.15" -> "I.post.4";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.23" -> "I.16";
     "I.15" -> "I.13";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.13" -> "I.11";
     "III.23" -> "III.def.11";
     "I.16" -> "I.10";
     "I.16" -> "I.15";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
   }
