:order: 15
:number: 231
:type: prop
:tags: triangle
:dependencies: I.14, V.11, V.7, V.9, VI.1




.. figure:: VI.15.graphic.inverted.png

.. _VI.15:

VI.15
=====

   In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one angle, and in which the sides about the equal angles are reciprocally proportional, are equal.

Let ``ABC``, ``ADE`` be equal triangles having one angle equal to one angle, namely the angle ``BAC`` to the angle ``DAE``; I say that in the triangles ``ABC``, ``ADE`` the sides about the equal angles are reciprocally proportional, that is to say, that,


.. container:: center

   as ``CA`` is to ``AD``, so is ``EA`` to ``AB``.


For let them be placed so that ``CA`` is in a straight line with ``AD``; therefore ``EA`` is also in a straight line with ``AB``. [:ref:`I.14`]

Let ``BD`` be joined.

Since then the triangle ``ABC`` is equal to the triangle ``ADE``, and ``BAD`` is another area, therefore, as the triangle ``CAB`` is to the triangle ``BAD``, so is the triangle ``EAD`` to the triangle ``BAD``. [:ref:`V.7`]

But, as ``CAB`` is to ``BAD``, so is ``CA`` to ``AD``, [:ref:`VI.1`] and, as ``EAD`` is to ``BAD``, so is ``EA`` to ``AB``. [``id``.]

Therefore also, as ``CA`` is to ``AD``, so is ``EA`` to ``AB``. [:ref:`V.11`]

Therefore in the triangles ``ABC``, ``ADE`` the sides about the equal angles are reciprocally proportional.

Next, let the sides of the triangles ``ABC``, ``ADE`` be reciprocally proportional, that is to say, let ``EA`` be to ``AB`` as ``CA`` to ``AD``; I say that the triangle ``ABC`` is equal to the triangle ``ADE``.

For, if ``BD`` be again joined, since, as ``CA`` is to ``AD``, so is ``EA`` to ``AB``, while, as ``CA`` is to ``AD``, so is the triangle ``ABC`` to the triangle ``BAD``, and, as ``EA`` is to ``AB``, so is the triangle ``EAD`` to the triangle ``BAD``, [:ref:`VI.1`] therefore, as the triangle ``ABC`` is to the triangle ``BAD``, so is the triangle ``EAD`` to the triangle ``BAD``. [:ref:`V.11`]

Therefore each of the triangles ``ABC``, ``EAD`` has the same ratio to ``BAD``.

Therefore the triangle ``ABC`` is equal to the triangle ``EAD``. [:ref:`V.9`]

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
     "V.14" [URL="/heath/V/14/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "I.29" [URL="/heath/I/29/", target="_top"];
     "V.12" [URL="/heath/V/12/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.2/", target="_top"];
     "V.20" [URL="/heath/V/20/", target="_top"];
     "V.10" [URL="/heath/V/10/", target="_top"];
     "V.11" [style="rounded,filled", fillcolor=orange, URL="/heath/V/11/", target="_top"];
     "V.13" [URL="/heath/V/13/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "V.15" [URL="/heath/V/15/", target="_top"];
     "VI.1" [URL="/heath/VI/1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "I.14" [URL="/heath/I/14/", target="_top"];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "V.16" [URL="/heath/V/16/", target="_top"];
     "I.23" [URL="/heath/I/23/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.35" [URL="/heath/I/35/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "I.41" [URL="/heath/I/41/", target="_top"];
     "I.36" [URL="/heath/I/36/", target="_top"];
     "I.27" [URL="/heath/I/27/", target="_top"];
     "I.37" [URL="/heath/I/37/", target="_top"];
     "I.34" [URL="/heath/I/34/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.23/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.33" [URL="/heath/I/33/", target="_top"];
     "I.31" [URL="/heath/I/31/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "elem.5.20 elem.5.21 elem.5.22 elem.5.23" [style="rounded,filled", fillcolor=orange];
     "elem.5.17 elem.5.18" [style="rounded,filled", fillcolor=orange];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "VI.15" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VI/15/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.5/", target="_top"];
     "I.38" [URL="/heath/I/38/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "V.21" [URL="/heath/V/21/", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.34" -> "I.26";
     "V.16" -> "V.14";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "VI.1" -> "V.def.5";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "V.15" -> "V.12";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "V.16" -> "V.20";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
     "V.16" -> "V.11";
     "VI.1" -> "V.11";
     "VI.15" -> "V.11";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "V.16" -> "V.15";
     "VI.1" -> "V.15";
     "VI.15" -> "VI.1";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "VI.15" -> "V.7";
     "VI.15" -> "I.14";
     "VI.15" -> "V.9";
     "VI.1" -> "V.16";
     "I.31" -> "I.23";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "V.9" -> "V.8";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "VI.1" -> "I.41";
     "I.38" -> "I.36";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "I.41" -> "I.37";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.38" -> "I.34";
     "I.41" -> "I.34";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.8" -> "I.7";
     "I.3" -> "I.2";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.27" -> "I.def.23";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.36" -> "I.33";
     "I.37" -> "I.31";
     "I.38" -> "I.31";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "V.16" -> "elem.5.20 elem.5.21 elem.5.22 elem.5.23";
     "V.16" -> "elem.5.17 elem.5.18";
     "I.10" -> "I.9";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "V.8" -> "V.def.4";
     "I.4" -> "I.cn.4";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.29" -> "I.post.5";
     "VI.1" -> "I.38";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "I.16" -> "I.10";
     "I.7" -> "I.5";
     "V.16" -> "V.21";
   }



Required for
------------

:ref:`VI.19`, :ref:`VI.20`, :ref:`X.68`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.2`, :ref:`XII.8`