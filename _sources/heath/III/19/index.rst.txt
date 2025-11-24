:order: 19
:number: 127
:type: prop
:tags: line, circle
:dependencies: III.18




.. figure:: III.19.graphic.inverted.png

.. _III.19:

III.19
======

   If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle will be on the straight line so drawn.

For let a straight line ``DE`` touch the circle ``ABC`` at the point ``C``, and from ``C`` let ``CA`` be drawn at right angles to ``DE``; I say that the centre of the circle is on ``AC``.

For suppose it is not, but, if

possible, let ``F`` be the centre, and let ``CF`` be joined.

Since a straight line ``DE`` touches the circle ``ABC``, and ``FC`` has been joined from the centre to the point of contact,


.. container:: center

   ``FC`` is perpendicular to ``DE``; [:ref:`III.18`] therefore the angle ``FCE`` is right.


But the angle ``ACE`` is also right;


.. container:: center

   therefore the angle ``FCE`` is equal to the angle ``ACE``, the less to the greater: which is impossible.


Therefore ``F`` is not the centre of the circle ``ABC``.

Similarly we can prove that neither is any other point except a point on ``AC``.

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
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.17" [URL="/heath/I/17/", target="_top"];
     "III.19" [style="rounded,filled", fillcolor=lightblue, URL="/heath/III/19/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.18" [URL="/heath/I/18/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "I.19" [URL="/heath/I/19/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "III.18" [URL="/heath/III/18/", target="_top"];
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
     "I.18" -> "I.3";
     "I.3" -> "I.2";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "III.18" -> "I.17";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.19" -> "I.18";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.18" -> "I.19";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.10" -> "I.9";
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
     "III.19" -> "III.18";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
   }



Required for
------------

:ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.2`, :ref:`XIII.13`, :ref:`XIII.18`