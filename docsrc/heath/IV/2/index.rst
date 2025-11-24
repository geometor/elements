:order: 2
:number: 154
:type: prop
:tags: circle, triangle
:dependencies: I.23, I.32, III.16.p.1, III.32




.. figure:: IV.2.graphic.inverted.png

.. _IV.2:

IV.2
====

   In a given circle to inscribe a triangle equiangular with a given triangle.

Let ``ABC`` be the given circle, and ``DEF`` the given triangle; thus it is required to inscribe in the circle ``ABC`` a triangle equiangular with the triangle ``DEF``.

Let ``GH`` be drawn touching the circle ``ABC`` at ``A`` [:ref:`III.16.p.1`]; on the straight line ``AH``, and at the point ``A`` on it, let the angle ``HAC`` be constructed equal to the angle ``DEF``, and on the straight line ``AG``, and at the point ``A`` on it, let the angle ``GAB`` be constructed equal to the angle ``DFE``; [:ref:`I.23`] let ``BC`` be joined.

Then, since a straight line ``AH`` touches the circle ``ABC``, and from the point of contact at ``A`` the straight line ``AC`` is drawn across in the circle, therefore the angle ``HAC`` is equal to the angle ``ABC`` in the alternate segment of the circle. [:ref:`III.32`]

But the angle ``HAC`` is equal to the angle ``DEF``; therefore the angle ``ABC`` is also equal to the angle ``DEF``.

For the same reason


.. container:: center

   the angle ``ACB`` is also equal to the angle ``DFE``;


therefore the remaining angle ``BAC`` is also equal to the remaining angle ``EDF``. [:ref:`I.32`]

Therefore in the given circle there has been inscribed a triangle equiangular with the given triangle. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.23" [URL="/heath/I/23/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "I.32" [URL="/heath/I/32/", target="_top"];
     "III.16.p.1" [style="rounded,filled", fillcolor=orange];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.19" [URL="/heath/I/19/", target="_top"];
     "III.20" [URL="/heath/III/20/", target="_top"];
     "III.19" [URL="/heath/III/19/", target="_top"];
     "I.31" [URL="/heath/I/31/", target="_top"];
     "III.22" [URL="/heath/III/22/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "I.18" [URL="/heath/I/18/", target="_top"];
     "I.27" [URL="/heath/I/27/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "III.18" [URL="/heath/III/18/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "III.32" [URL="/heath/III/32/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.17" [URL="/heath/I/17/", target="_top"];
     "I.29" [URL="/heath/I/29/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "III.31" [URL="/heath/III/31/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.23/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.2/", target="_top"];
     "IV.2" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IV/2/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.5/", target="_top"];
     "III.21" [URL="/heath/III/21/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.31" -> "I.23";
     "IV.2" -> "I.23";
     "I.10" -> "I.9";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "III.32" -> "I.32";
     "IV.2" -> "I.32";
     "IV.2" -> "III.16.p.1";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "III.18" -> "I.19";
     "III.21" -> "III.20";
     "III.32" -> "III.19";
     "I.32" -> "I.31";
     "III.31" -> "III.22";
     "III.32" -> "III.22";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.31" -> "I.def.10";
     "I.19" -> "I.18";
     "I.31" -> "I.27";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "III.19" -> "III.18";
     "I.8" -> "I.7";
     "IV.2" -> "III.32";
     "I.3" -> "I.2";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.15" -> "I.post.4";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.18" -> "I.17";
     "III.31" -> "I.17";
     "I.32" -> "I.29";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.27" -> "I.16";
     "III.32" -> "III.31";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.27" -> "I.def.23";
     "I.29" -> "I.cn.2";
     "I.29" -> "I.post.5";
     "III.22" -> "III.21";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
   }



Required for
------------

:ref:`IV.11`, :ref:`IV.12`, :ref:`XIII.13`, :ref:`XIII.18`