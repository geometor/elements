:order: 30
:number: 63
:type: prop
:tags: line
:dependencies: I.29, I.cn.1




.. figure:: I.30.jpg
   :width: 50%

.. _I.30:

I.30
====

   Straight lines parallel to the same straight line are also parallel to one another.

Let each of the straight lines ``AB``, ``CD`` be parallel to ``EF``; I say that ``AB`` is also parallel to ``CD``. 

For let the straight line ``GK`` fall upon them; 

Then, since the straight line ``GK`` has fallen on the parallel straight lines ``AB``, ``EF``, the angle ``AGK`` is equal to the angle ``GHF``. [:ref:`I.29`]

Again, since the straight line ``GK`` has fallen on the parallel straight lines ``EF``, ``CD``, the angle ``GHF`` is equal to the angle ``GKD``. [:ref:`I.29`]
        

But the angle ``AGK`` was also proved equal to the angle ``GHF``; therefore the angle ``AGK`` is also equal to the angle ``GKD``; [:ref:`I.cn.1`] and they are alternate. 

Therefore ``AB`` is parallel to ``CD``.


**Q. E. D.**


Q. E. D.


.. note::


   **20**

   

   The usual ``conclusion`` in general terms (Therefore etc.

   ) repeating the enunciation is, curiously enough, wanting at the end of this proposition.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.30" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/30/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.11" -> "I.8";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.2" -> "I.1";
     "I.11" -> "I.1";
     "I.4" -> "I.cn.4";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.7" -> "I.5";
     "I.29" -> "I.post.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.30" -> "I.cn.1";
     "I.30" -> "I.29";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.15" -> "I.post.4";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.29" -> "I.cn.2";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.5" -> "I.4";
     "I.13" -> "I.11";
     "I.29" -> "I.15";
     "I.5" -> "I.3";
     "I.11" -> "I.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
   }



Required for
------------

:ref:`I.45`, :ref:`II.14`, :ref:`IV.7`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`