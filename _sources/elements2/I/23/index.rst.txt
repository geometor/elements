:order: 23
:number: 56
:type: prop
:categories: construct
:tags: line
:dependencies: I.8




.. figure:: I.23.jpg
   :width: 50%

.. _I.23:

I.23
====

   On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

Let ``AB`` be the given straight line, ``A`` the point on it, and the angle ``DCE`` the given rectilineal angle;

thus it is required to construct on the given straight line ``AB``, and at the point ``A`` on it, a rectilineal angle equal to the given rectilineal angle ``DCE``. 

On the straight lines ``CD``, ``CE`` respectively let the points ``D``, ``E`` be taken at random; let ``DE`` be joined, and out of three straight lines which are equal to the three straight lines ``CD``, ``DE``, ``CE`` let the triangle ``AFG`` be constructed in such a way that ``CD`` is equal to ``AF``, ``CE`` to ``AG``, and further ``DE`` to ``FG``.

Then, since the two sides ``DC``, ``CE`` are equal to the two sides ``FA``, ``AG`` respectively, and the base ``DE`` is equal to the base ``FG``, the angle ``DCE`` is equal to the angle ``FAG``. [:ref:`I.8`]

Therefore on the given straight line ``AB``, and at the point ``A`` on it, the rectilineal angle ``FAG`` has been constructed equal to the given rectilineal angle ``DCE``.


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
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.23" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/23/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.23" -> "I.8";
     "I.3" -> "I.2";
     "I.2" -> "I.1";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.cn.3";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.5" -> "I.4";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.5" -> "I.3";
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

:ref:`I.24`, :ref:`I.25`, :ref:`I.31`, :ref:`I.32`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.27`, :ref:`III.29`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`III.7`, :ref:`III.8`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.8`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`