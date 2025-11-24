:order: 14
:number: 546
:type: prop
:tags: line
:dependencies: I.17, XI.3, XI.def.3, XI.def.8




.. figure:: XI.14.graphic.inverted.png

.. _XI.14:

XI.14
=====

   Planes to which the same straight line is at right angles will be parallel.

For let any straight line AB be at right angles to each of the planes CD, EF; I say that the planes are parallel.

For, if not, they will meet when produced.

Let them meet; they will then make, as common section, a straight line. [:ref:`XI.3`]

Let them make GH; let a point K be taken at random on GH, and let AK, BK be joined.

Now, since AB is at right angles to the plane EF, therefore AB is also at right angles to BK which is a straight line in the plane EF produced; [:ref:`XI.def.3`] therefore the angle ABK is right.

For the same reason the angle BAK is also right.

Thus, in the triangle ABK, the two angles ABK, BAK are equal to two right angles: which is impossible. [:ref:`I.17`]

Therefore the planes CD, EF will not meet when produced; therefore the planes CD, EF are parallel. [:ref:`XI.def.8`]

Therefore planes to which the same straight line is at right angles are parallel. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "XI.def.8" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/def.8/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.17" [URL="/heath/I/17/", target="_top"];
     "XI.3" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "XI.14" [style="rounded,filled", fillcolor=lightblue, URL="/heath/XI/14/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "XI.def.3" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/def.3/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.10" -> "I.9";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.8" -> "I.7";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "XI.14" -> "XI.def.8";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.15" -> "I.post.4";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.7" -> "I.5";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "XI.14" -> "I.17";
     "XI.14" -> "XI.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.17" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "XI.14" -> "XI.def.3";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
   }



Required for
------------

:ref:`XI.15`