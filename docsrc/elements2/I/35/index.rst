:order: 35
:number: 68
:type: prop
:dependencies: I.29, I.34, I.4, I.cn.1, I.cn.2, I.cn.3




.. figure:: I.35.jpg
   :width: 50%



.. figure:: I.35-b.jpg
   :width: 50%

.. _I.35:

I.35
====

   Parallelograms which are on the same base and in the same parallels are equal to one another.

Let ``ABCD``, ``EBCF`` be parallelograms on the same base ``BC`` and in the same parallels ``AF``, ``BC``; I say that ``ABCD`` is equal to the parallelogram ``EBCF``.

For, since ``ABCD`` is a parallelogram, ``AD`` is equal to ``BC``. [:ref:`I.34`]
        

For the same reason also ``EF`` is equal to ``BC``, so that ``AD`` is also equal to ``EF``; [:ref:`I.cn.1`] and ``DE`` is common; therefore the whole ``AE`` is equal to the whole ``DF``. [:ref:`I.cn.2`]

But ``AB`` is also equal to ``DC``; [:ref:`I.34`] therefore the two sides ``EA``, ``AB`` are equal to the two sides ``FD``, ``DC`` respectively, 
        and the angle ``FDC`` is equal to the angle ``EAB``, the exterior to the interior; [:ref:`I.29`] therefore the base ``EB`` is equal to the base ``FC``, and the triangle ``EAB`` will be equal to the triangle ``FDC``. [:ref:`I.4`]

Let ``DGE`` be subtracted from each; therefore the trapezium ``ABGD`` which remains is equal to the trapezium ``EGCF`` which remains. [:ref:`I.cn.3`] 

Let the triangle ``GBC`` be added to each; therefore the whole parallelogram ``ABCD`` is equal to the whole parallelogram ``EBCF``. [:ref:`I.cn.2`]

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **21. FDC.**

   

   The text has ``DFC``.


.. note::


   **22. Let DGE be subtracted.**

   

   Euclid speaks of the triangle ``DGE`` without any explanation that, in the case which he takes (where ``AD``, ``EF`` have no point in common), ``BE``, ``CD`` must meet at a point ``G`` between the two parallels. He allows this to appear from the figure simply.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.35" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/35/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.26" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.10" -> "I.9";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.29" -> "I.post.5";
     "I.34" -> "I.26";
     "I.3" -> "I.2";
     "I.35" -> "I.34";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
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
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.13" -> "I.11";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.7" -> "I.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
   }



Required for
------------

:ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.44`, :ref:`I.45`, :ref:`I.47`, :ref:`I.48`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.5`, :ref:`II.6`, :ref:`II.8`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`