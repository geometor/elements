:order: 29
:number: 561
:type: prop
:tags: line
:dependencies: I.34, I.36, elem.1.8 elem.1.4




.. figure:: XI.29.graphic.inverted.png

.. _XI.29:

XI.29
=====

   Parallelepipedal solids which are on the same base and of the same height, and in which the extremities of the sides which stand up are on the same straight lines, are equal to one another.

Let CM, CN be parallelepipedal solids on the same base AB and of the same height, and let the extremities of their sides which stand up, namely AG, AF, LM, LN, CD, CE, BH, BK, be on the same straight lines FN, DK; I say that the solid CM is equal to the solid CN.

For, since each of the figures CH, CK is a parallelogram, CB is equal to each of the straight lines DH, EK, [:ref:`I.34`] hence DH is also equal to EK.

Let EH be subtracted from each; therefore the remainder DE is equal to the remainder HK.

Hence the triangle DCE is also equal to the triangle HBK, [:ref:`elem.1.8 elem.1.4`] and the parallelogram DG to the parallelogram HN. [:ref:`I.36`]

For the same reason the triangle AFG is also equal to the triangle MLN.

But the parallelogram CF is equal to the parallelogram BM, and CG to BN, for they are opposite; therefore the prism contained by the two triangles AFG, DCE and the three parallelograms AD, DG, CG is equal to the prism contained by the two triangles MLN, HBK and the three parallelograms BM, HN, BN.

Let there be added to each the solid of which the parallelogram AB is the base and GEHM its opposite; therefore the whole parallelepipedal solid CM is equal to the whole parallelepipedal solid CN.

Therefore etc. Q. E. D.


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
     "I.26" [URL="/heath/I/26/", target="_top"];
     "I.29" [URL="/heath/I/29/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "XI.29" [style="rounded,filled", fillcolor=lightblue, URL="/heath/XI/29/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.35" [URL="/heath/I/35/", target="_top"];
     "I.36" [URL="/heath/I/36/", target="_top"];
     "I.27" [URL="/heath/I/27/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.34" [URL="/heath/I/34/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.23/", target="_top"];
     "elem.1.8 elem.1.4" [style="rounded,filled", fillcolor=orange];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.33" [URL="/heath/I/33/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.5/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.15" -> "I.post.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.34" -> "I.26";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.36" -> "I.35";
     "XI.29" -> "I.36";
     "I.33" -> "I.27";
     "I.8" -> "I.7";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "XI.29" -> "I.34";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.3" -> "I.2";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.27" -> "I.def.23";
     "XI.29" -> "elem.1.8 elem.1.4";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.36" -> "I.33";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.10" -> "I.9";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.4" -> "I.cn.4";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.29" -> "I.post.5";
     "I.16" -> "I.10";
     "I.7" -> "I.5";
   }



Required for
------------

:ref:`XI.30`, :ref:`XI.31`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.39`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`