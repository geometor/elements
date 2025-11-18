:order: 9
:number: 42
:type: prop
:categories: bisect
:tags: line
:dependencies: I.3, I.8




.. figure:: I.9.jpg
   :width: 50%

.. _I.9:

I.9
===

   To bisect a given rectilineal angle.

Let the angle ``BAC`` be the given rectilineal angle.

Thus it is required to bisect it.

Let a point ``D`` be taken at random on ``AB``; let ``AE`` be cut off from ``AC`` equal to ``AD``; [:ref:`I.3`] let ``DE`` be joined, and on ``DE`` let the equilateral triangle ``DEF`` be constructed; let ``AF`` be joined. 

I say that the angle ``BAC`` has been bisected by the straight line ``AF``.

For, since ``AD`` is equal to ``AE``, and ``AF`` is common, the two sides ``DA``, ``AF`` are equal to the two sides ``EA``, ``AF`` respectively.

And the base ``DF`` is equal to the base ``EF``; therefore the angle ``DAF`` is equal to the angle ``EAF``. [:ref:`I.8`]

Therefore the given rectilineal angle ``BAC`` has been bisected by the straight line ``AF``.


**Q. E. D.**


Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.9" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/9/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" -> "I.8";
     "I.3" -> "I.2";
     "I.2" -> "I.1";
     "I.2" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.5" -> "I.4";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.7" -> "I.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
   }



Required for
------------

:ref:`I.10`, :ref:`I.12`, :ref:`I.16`, :ref:`I.17`, :ref:`I.18`, :ref:`I.19`, :ref:`I.20`, :ref:`I.21`, :ref:`I.22`, :ref:`I.24`, :ref:`I.25`, :ref:`I.26`, :ref:`I.27`, :ref:`I.28`, :ref:`I.31`, :ref:`I.32`, :ref:`I.33`, :ref:`I.34`, :ref:`I.35`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.43`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.12`, :ref:`III.13`, :ref:`III.14`, :ref:`III.15`, :ref:`III.16`, :ref:`III.18`, :ref:`III.19`, :ref:`III.2`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.23`, :ref:`III.27`, :ref:`III.29`, :ref:`III.3`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`III.4`, :ref:`III.7`, :ref:`III.8`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.13`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.4`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`