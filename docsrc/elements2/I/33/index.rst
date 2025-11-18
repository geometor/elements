:order: 33
:number: 66
:type: prop
:tags: line
:dependencies: I.27, I.29, I.4




.. figure:: I.33.jpg
   :width: 50%

.. _I.33:

I.33
====

   The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.

Let ``AB``, ``CD`` be equal and parallel, and let the straight  lines ``AC``, ``BD`` join them (at the extremities which are) in the same directions (respectively); I say that ``AC``, ``BD`` are also equal and parallel.

Let ``BC`` be joined. 

Then, since ``AB`` is parallel to ``CD``,  and ``BC`` has fallen upon them, the alternate angles ``ABC``, ``BCD`` are equal to one another. [:ref:`I.29`]

And, since ``AB`` is equal to ``CD``, and ``BC`` is common, the two sides ``AB``, ``BC`` are equal to the two sides ``DC``, ``CB``; and the angle ``ABC`` is equal to the angle ``BCD``; therefore the base ``AC`` is equal to the base ``BD``, and the griangle ``ABC`` is equal to the triangle ``DCB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend; [:ref:`I.4`] therefore the angle ``ACB`` is equal to the angle ``CBD``.

And, since the straight line ``BC`` falling on the two straight lines ``AC``, ``BD`` has made the alternate angles equal to one another, ``AC`` is parallel to ``BD``. [:ref:`I.27`]

And it was also proved equal to it.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. joining...(at the extremities which are) in the same directions (respectively).**

   

   I have for clearness' sake inserted the words in brackets though they are not in the original Greek, which has joining...in the same directions

    or on the same sides,

    ἐπὶ τὰ αυτὰ μέρη ἐπιζευγνύουσαι. The expression tiwards the same parts,

    though usage has sanctioned it, is perhaps not quite satisfactory.


.. note::


   **15. DC, CB**

   

   and 18. DCB. The Greek has  ``BC``, ``CD``

    and ``BCD``

    in these places respectively. Euclid is not always careful to write in corresponding order the letters denoting corresponding points in congruent figures. On the contrary, he evidently prefers the alphabetical order, and seems to disdain to alter it for the sake of beginners or others who might be confused by it. In the case of angles alteration is perhaps unnecessary; but in the case of triangles and pairs of corresponding sides I have ventured to alter the order to that which the mathematician of to-day expects.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.33" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/33/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.10" -> "I.9";
     "I.7" -> "I.5";
     "I.29" -> "I.post.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.33" -> "I.29";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.15" -> "I.post.4";
     "I.27" -> "I.16";
     "I.29" -> "I.cn.2";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.3" -> "I.2";
     "I.33" -> "I.27";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.33" -> "I.4";
     "I.13" -> "I.11";
     "I.16" -> "I.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.27" -> "I.def.23";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
   }



Required for
------------

:ref:`I.36`, :ref:`I.38`, :ref:`I.40`, :ref:`I.42`, :ref:`I.44`, :ref:`I.45`, :ref:`II.11`, :ref:`II.14`, :ref:`II.5`, :ref:`II.6`, :ref:`II.8`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`