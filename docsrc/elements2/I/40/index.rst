:order: 40
:number: 73
:type: prop
:tags: triangle
:dependencies: I.31, I.38, I.cn.1




.. figure:: I.40.jpg
   :width: 50%

.. _I.40:

I.40
====

   Equal triangles which are on equal bases and on the same side are also in the same parallels.

Let ``ABC``, ``CDE`` be equal triangles on equal bases ``BC``, ``CE`` and on the same side.

I say that they are also in the same parallels.

For let ``AD`` be joined; I say that ``AD`` is parallel to ``BE``.

For, if not, let ``AF`` be drawn through ``A`` parallel to ``BE`` [:ref:`I.31`], and let ``FE`` be joined.

Therefore the triangle ``ABC`` is equal to the triangle ``FCE``; for they are on equal bases ``BC``, ``CE`` and in the same parallels ``BE``, ``AF``. [:ref:`I.38`]

But the triangle ``ABC`` is equal to the triangle ``DCE``;


.. container:: center

   therefore the triangle ``DCE`` is also equal to the triangle ``FCE``, [:ref:`I.cn.1`] the greater to the less: which is impossible. Therefore ``AF`` is not parallel to ``BE``.


Similarly we can prove that neither is any other straight line except ``AD``;


.. container:: center

   therefore ``AD`` is parallel to ``BE``.


Therefore etc. Q. E. D.]


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.36" [URL="/elements2/I/36/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.40" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/40/", target="_top"];
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
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.38" -> "I.34";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
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
     "I.40" -> "I.38";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.31" -> "I.23";
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
     "I.36" -> "I.33";
     "I.38" -> "I.31";
     "I.40" -> "I.31";
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.40" -> "I.cn.1";
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
