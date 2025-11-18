:order: 12
:number: 120
:type: prop
:tags: line, circle
:dependencies: I.20




.. figure:: III.12.jpg
   :width: 50%

.. _III.12:

III.12
======

   If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.

For let the two circles ``ABC``, ``ADE`` touch one another externally at the point ``A``, and let the centre ``F`` of ``ABC``, and the centre ``G`` of ``ADE``, be taken; I say that the straight line joined from ``F`` to ``G`` will pass through the point of contact at ``A``.

For suppose it does not, but, if possible, let it pass as ``FCDG``, and let ``AF``, ``AG`` be joined.

Then, since the point ``F`` is the centre of the circle ``ABC``,


.. container:: center

   ``FA`` is equal to ``FC``.


Again, since the point ``G`` is the centre of the circle ``ADE``,


.. container:: center

   ``GA`` is equal to ``GD``.


But ``FA`` was also proved equal to ``FC``;


.. container:: center

   therefore ``FA``, ``AG`` are equal to ``FC``, ``GD``, so that the whole ``FG`` is greater than ``FA``, ``AG``;


but it is also less [:ref:`I.20`]: which is impossible.

Therefore the straight line joined from ``F`` to ``G`` will not fail to pass through the point of contact at ``A``;


.. container:: center

   therefore it will pass through it.


Therefore etc. Q. E. D.]
will not fail to pass. The Greek has the double negative, οὐκ ἄρα ἡ...εὐθεῖα... οὐκ ἐλεύσεται, literally the straight line...will not ``not``-pass....


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.19" [URL="/elements2/I/19/", target="_top"];
     "III.12" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/12/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.18" [URL="/elements2/I/18/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.20" [URL="/elements2/I/20/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.20" -> "I.19";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.10" -> "I.9";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.20" -> "I.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.18" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.19" -> "I.18";
     "I.15" -> "I.13";
     "I.15" -> "I.post.4";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.20" -> "I.cn.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.13" -> "I.11";
     "I.16" -> "I.10";
     "I.16" -> "I.15";
     "III.12" -> "I.20";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
   }
