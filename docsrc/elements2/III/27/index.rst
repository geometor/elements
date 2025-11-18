:order: 27
:number: 135
:type: prop
:tags: circle
:dependencies: I.23, III.20, III.26




.. figure:: III.27.jpg
   :width: 50%

.. _III.27:

III.27
======

   In equal circles angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences.

For in equal circles ``ABC``, ``DEF``, on equal circumferences ``BC``, ``EF``, let the angles ``BGC``, ``EHF`` stand at the centres ``G``, ``H``, and the angles ``BAC``, ``EDF`` at the circumferences; I say that the angle ``BGC`` is equal to the angle ``EHF``, and the angle ``BAC`` is equal to the angle ``EDF``.

For, if the angle ``BGC`` is unequal to the angle ``EHF``,


.. container:: center

   one of them is greater.


Let the angle ``BGC`` be greater : and on the straight line ``BG``, and at the point ``G`` on it, let the angle ``BGK`` be constructed equal to the angle ``EHF``. [:ref:`I.23`]

Now equal angles stand on equal circumferences, when they are at the centres; [:ref:`III.26`]


.. container:: center

   therefore the circumference ``BK`` is equal to the circumference ``EF``.


But ``EF`` is equal to ``BC``;


.. container:: center

   therefore ``BK`` is also equal to ``BC``, the less to the greater : which is impossible.


Therefore the angle ``BGC`` is not unequal to the angle ``EHF``;


.. container:: center

   therefore it is equal to it.


And the angle at ``A`` is half of the angle ``BGC``,


.. container:: center

   and the angle at ``D`` half of the angle ``EHF``; [:ref:`III.20`]


therefore the angle at ``A`` is also equal to the angle at ``D``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.31" [URL="/elements2/I/31/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.32" [URL="/elements2/I/32/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "elem.3.1.p.1" [style="rounded,filled", fillcolor=orange];
     "III.26" [URL="/elements2/III/26/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "III.20" [URL="/elements2/III/20/", target="_top"];
     "III.27" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/27/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "III.5" [URL="/elements2/III/5/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "III.24" [URL="/elements2/III/24/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "III.10" [URL="/elements2/III/10/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "III.def.11" [style="rounded,filled", fillcolor=orange, URL="/elements2/III/def.11/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.32" -> "I.31";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.24" -> "I.8";
     "I.7" -> "I.5";
     "III.20" -> "I.5";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "III.20" -> "I.32";
     "I.8" -> "I.7";
     "I.31" -> "I.23";
     "III.27" -> "I.23";
     "III.10" -> "elem.3.1.p.1";
     "III.27" -> "III.26";
     "I.27" -> "I.16";
     "III.27" -> "III.20";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.15" -> "I.post.4";
     "III.10" -> "III.5";
     "I.27" -> "I.def.23";
     "I.29" -> "I.post.5";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.16" -> "I.10";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "III.26" -> "III.24";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "III.26" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.10" -> "I.9";
     "I.32" -> "I.29";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "III.24" -> "III.10";
     "I.3" -> "I.2";
     "I.31" -> "I.27";
     "III.26" -> "III.def.11";
     "I.4" -> "I.cn.4";
     "I.29" -> "I.cn.2";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
   }



Required for
------------

:ref:`III.29`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`VI.33`