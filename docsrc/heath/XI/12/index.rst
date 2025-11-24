:order: 12
:number: 544
:type: prop
:tags: line
:dependencies: I.31, XI.11, XI.8




.. figure:: XI.12.graphic.inverted.png

.. _XI.12:

XI.12
=====

   To set up a straight line at right angles to a given plane from a given point in it.

Let the plane of reference be the given plane, and A the point in it; thus it is required to set up from the point A a straight line at right angles to the plane of reference.

Let any elevated point B be conceived, from B let BC be drawn perpendicular to the plane of reference, [:ref:`XI.11`] and through the point A let AD be drawn parallel to BC. [:ref:`I.31`]

Then, since AD, CB are two parallel straight lines, while one of them, BC, is at right angles to the plane of reference, therefore the remaining one, AD, is also at right angles to the plane of reference. [:ref:`XI.8`]

Therefore AD has been set up at right angles to the given plane from the point A in it.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "XI.def.3" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/def.3/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.26" [URL="/heath/I/26/", target="_top"];
     "XI.12" [style="rounded,filled", fillcolor=lightblue, URL="/heath/XI/12/", target="_top"];
     "XI.7" [URL="/heath/XI/7/", target="_top"];
     "I.29" [URL="/heath/I/29/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.2/", target="_top"];
     "XI.8" [URL="/heath/XI/8/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "XI.11" [URL="/heath/XI/11/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "XI.1" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/1/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "XI.2" [URL="/heath/XI/2/", target="_top"];
     "I.23" [URL="/heath/I/23/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.27" [URL="/heath/I/27/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.23/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.12" [URL="/heath/I/12/", target="_top"];
     "I.31" [URL="/heath/I/31/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "XI.4" [URL="/heath/XI/4/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.5/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "XI.3" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/3/", target="_top"];
     "I.11" -> "I.def.10";
     "I.12" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "XI.11" -> "I.11";
     "XI.4" -> "XI.def.3";
     "XI.8" -> "XI.def.3";
     "XI.11" -> "XI.def.3";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.15" -> "I.post.4";
     "XI.4" -> "I.26";
     "XI.8" -> "XI.7";
     "XI.8" -> "I.29";
     "I.29" -> "I.cn.2";
     "XI.11" -> "XI.8";
     "XI.12" -> "XI.8";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "XI.12" -> "XI.11";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.12" -> "I.post.3";
     "XI.2" -> "XI.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "XI.8" -> "XI.2";
     "I.31" -> "I.23";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.12" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.31" -> "I.27";
     "I.8" -> "I.7";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.3" -> "I.2";
     "I.27" -> "I.def.23";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "XI.4" -> "I.4";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "XI.11" -> "I.12";
     "XI.11" -> "I.31";
     "XI.12" -> "I.31";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.10" -> "I.9";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.12" -> "I.8";
     "I.23" -> "I.8";
     "XI.4" -> "I.8";
     "I.4" -> "I.cn.4";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "XI.4" -> "I.15";
     "XI.8" -> "XI.4";
     "XI.11" -> "XI.4";
     "I.29" -> "I.post.5";
     "I.12" -> "I.10";
     "I.16" -> "I.10";
     "I.7" -> "I.5";
     "XI.7" -> "XI.3";
   }



Required for
------------

:ref:`XI.23`, :ref:`XI.26`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.18`