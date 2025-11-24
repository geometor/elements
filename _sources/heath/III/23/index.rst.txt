:order: 23
:number: 131
:type: prop
:categories: construct
:tags: line, circle
:dependencies: I.16, III.def.11




.. figure:: III.23.graphic.inverted.png

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
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "III.def.11" [style="rounded,filled", fillcolor=orange, URL="/heath/III/def.11/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "III.23" [style="rounded,filled", fillcolor=lightblue, URL="/heath/III/23/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.15" -> "I.post.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.8" -> "I.7";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.3" -> "I.2";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.15" -> "I.13";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "III.23" -> "III.def.11";
     "III.23" -> "I.16";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.10" -> "I.9";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.4" -> "I.cn.4";
     "I.16" -> "I.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.16" -> "I.10";
     "I.7" -> "I.5";
   }
