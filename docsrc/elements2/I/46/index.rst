:order: 46
:number: 79
:type: prop
:categories: describe
:tags: line
:dependencies: I.11, I.29, I.31, I.34




.. figure:: I.46.jpg
   :width: 50%

.. _I.46:

I.46
====

   On a given straight line to describe a square.

Let ``AB`` be the given straight line; thus it is required to describe a square on the straight line ``AB``. 
        

Let ``AC`` be drawn at right angles to the straight line ``AB`` from the point ``A`` on it [:ref:`I.11`], and let ``AD`` be made equal to ``AB``; through the point ``D`` let ``DE`` be drawn parallel to ``AB``, and through the point ``B`` let ``BE`` be drawn parallel to ``AD``. [:ref:`I.31`] 

Therefore ``ADEB`` is a parallelogram; therefore ``AB`` is equal to ``DE``, and ``AD`` to ``BE``. [:ref:`I.34`]

But ``AB`` is equal to ``AD``; therefore the four straight lines ``BA``, ``AD``, ``DE``, ``EB`` are equal to one another; therefore the parallelogram ``ADEB`` is equilateral.

I say next that it is also right-angled.

For, since the straight line ``AD`` falls upon the parallels ``AB``, ``DE``, the angles ``BAD``, ``ADE`` are equal to two right angles. [:ref:`I.29`]

But the angle ``BAD`` is right; therefore the angle ``ADE`` is also right.

And in parallelogrammic areas the opposite sides and angles are equal to one another; [:ref:`I.34`] therefore each of the opposite angles ``ABE``, ``BED`` is also right. Therefore ``ADEB`` is right-angled.

And it was also proved equilateral. 

Therefore it is a square; and it is described on the straight line ``AB``.


**Q. E. D.**


Q. E. F.


.. note::


   **1, 3, 30**

   

   Proclus (p. 423, 18 sqq.) notes the difference between the word ``construct`` (συστἡσασθαι) applied by Euclid to the construction of a ``triangle`` (and, he might have added, of an ``angle``) and the words ``describe on`` (ἀναγράφειν ἀπό) used of drawing a square on a given straight line as one side. The ``triangle`` (or ``angle``) is, so to say, pieced together, while the describing of a square on a given straight line is the making of a figure from

    ``one`` side, and corresponds to the multiplication of the number representing the side by itself.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.46" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/46/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.31" [URL="/elements2/I/31/", target="_top"];
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
     "I.27" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.29" -> "I.post.5";
     "I.31" -> "I.23";
     "I.34" -> "I.26";
     "I.46" -> "I.34";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.31" -> "I.27";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.46" -> "I.31";
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
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.34" -> "I.29";
     "I.46" -> "I.29";
     "I.7" -> "I.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
   }



Required for
------------

:ref:`I.47`, :ref:`I.48`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`