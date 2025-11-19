:order: 10
:number: 43
:type: prop
:categories: bisect
:tags: line
:dependencies: I.1, I.4, I.9




.. figure:: I.10.jpg
   :width: 50%

.. _I.10:

I.10
====

   To bisect a given finite straight line.

Let ``AB`` be the given finite straight line.

Thus it is required to bisect the finite straight line ``AB``.

Let the equilateral triangle ``ABC`` be constructed on it, [:ref:`I.1`] and let the angle ``ACB`` be bisected by the straight line ``CD``; [:ref:`I.9`]

I say that the straight line ``AB`` has been bisected at the point ``D``.

For, since ``AC`` is equal to ``CB``, and ``CD`` is common, 
        the two sides ``AC``, ``CD`` are equal to the two sides ``BC``, ``CD`` respectively; and the angle ``ACD`` is equal to the angle ``BCD``; therefore the base ``AD`` is equal to the base ``BD``. [:ref:`I.4`]

Therefore the given finite straight line ``AB`` has been bisected at ``D``.


**Q. E. D.**


Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.10" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/10/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.10" -> "I.9";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.9" -> "I.8";
     "I.3" -> "I.2";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.7" -> "I.5";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.2" -> "I.cn.3";
     "I.8" -> "I.7";
   }



Required for
------------

:ref:`I.12`, :ref:`I.16`, :ref:`I.17`, :ref:`I.18`, :ref:`I.19`, :ref:`I.20`, :ref:`I.21`, :ref:`I.22`, :ref:`I.24`, :ref:`I.25`, :ref:`I.26`, :ref:`I.27`, :ref:`I.28`, :ref:`I.31`, :ref:`I.32`, :ref:`I.33`, :ref:`I.34`, :ref:`I.35`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.43`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.12`, :ref:`III.13`, :ref:`III.14`, :ref:`III.15`, :ref:`III.16`, :ref:`III.18`, :ref:`III.19`, :ref:`III.2`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.23`, :ref:`III.27`, :ref:`III.29`, :ref:`III.3`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`III.4`, :ref:`III.7`, :ref:`III.8`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.13`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.4`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`