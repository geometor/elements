:order: 10
:number: 542
:type: prop
:tags: line
:dependencies: I.33, I.8, XI.9




.. figure:: XI.10.graphic.inverted.png

.. _XI.10:

XI.10
=====

   If two straight lines meeting one another be parallel to two straight lines meeting one another not in the same plane, they will contain equal angles.

For let the two straight lines AB, BC meeting one another be parallel to the two straight lines DE, EF meeting one another, not in the same plane; I say that the angle ABC is equal to the angle DEF.

For let BA, BC, ED, EF be cut off equal to one another, and let AD, CF, BE, AC, DF be joined.

Now, since BA is equal and parallel to ED, therefore AD is also equal and parallel to BE. [:ref:`I.33`]

For the same reason CF is also equal and parallel to BE.

Therefore each of the straight lines AD, CF is equal and parallel to BE.

But straight lines which are parallel to the same straight line and are not in the same plane with it are parallel to one another; [:ref:`XI.9`] therefore AD is parallel and equal to CF.

And AC, DF join them; therefore AC is also equal and parallel to DF. [:ref:`I.33`]

Now, since the two sides AB, BC are equal to the two sides DE, EF, and the base AC is equal to the base DF, therefore the angle ABC is equal to the angle DEF. [:ref:`I.8`]

Therefore etc.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "I.29" [URL="/heath/I/29/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.27" [URL="/heath/I/27/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.23/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "XI.4" [URL="/heath/XI/4/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.28" [URL="/heath/I/28/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "XI.1" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/1/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "XI.10" [style="rounded,filled", fillcolor=lightblue, URL="/heath/XI/10/", target="_top"];
     "I.26" [URL="/heath/I/26/", target="_top"];
     "I.33" [URL="/heath/I/33/", target="_top"];
     "XI.9" [URL="/heath/XI/9/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.2/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "XI.5" [URL="/heath/XI/5/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "XI.def.3" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/def.3/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.5/", target="_top"];
     "XI.3" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/3/", target="_top"];
     "XI.6" [URL="/heath/XI/6/", target="_top"];
     "XI.7" [URL="/heath/XI/7/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "XI.2" [URL="/heath/XI/2/", target="_top"];
     "XI.8" [URL="/heath/XI/8/", target="_top"];
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.33" -> "I.29";
     "XI.8" -> "I.29";
     "I.8" -> "I.7";
     "I.28" -> "I.27";
     "I.33" -> "I.27";
     "I.27" -> "I.def.23";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "XI.4" -> "I.8";
     "XI.6" -> "I.8";
     "XI.10" -> "I.8";
     "I.10" -> "I.9";
     "XI.5" -> "XI.4";
     "XI.8" -> "XI.4";
     "XI.9" -> "XI.4";
     "I.15" -> "I.post.4";
     "I.3" -> "I.2";
     "XI.6" -> "I.28";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "XI.2" -> "XI.1";
     "I.4" -> "I.cn.4";
     "XI.4" -> "I.26";
     "XI.10" -> "I.33";
     "XI.10" -> "XI.9";
     "I.15" -> "I.13";
     "I.28" -> "I.13";
     "I.29" -> "I.13";
     "I.29" -> "I.cn.2";
     "I.7" -> "I.5";
     "I.13" -> "I.11";
     "I.16" -> "I.10";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "XI.4" -> "I.4";
     "XI.6" -> "I.4";
     "XI.6" -> "XI.5";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "XI.4" -> "XI.def.3";
     "XI.5" -> "XI.def.3";
     "XI.6" -> "XI.def.3";
     "XI.8" -> "XI.def.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.29" -> "I.post.5";
     "XI.5" -> "XI.3";
     "XI.7" -> "XI.3";
     "XI.9" -> "XI.6";
     "XI.8" -> "XI.7";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "I.29" -> "I.15";
     "XI.4" -> "I.15";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "XI.6" -> "XI.2";
     "XI.8" -> "XI.2";
     "XI.9" -> "XI.8";
   }



Required for
------------

:ref:`XI.24`, :ref:`XI.25`, :ref:`XI.31`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.39`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`