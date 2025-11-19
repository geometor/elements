:order: 34
:number: 67
:type: prop
:categories: bisect
:dependencies: I.26, I.29, I.4, I.cn.2




.. figure:: I.34.jpg
   :width: 50%

.. _I.34:

I.34
====

   In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.

Let ``ACDB`` be a parallelogrammic area, and ``BC`` its diameter; I say that the opposite sides and angles of the parallelogram ``ACDB`` are equal to one another, and the diameter ``BC`` bisects it. 

For, since ``AB`` is parallel to ``CD``, and the straight line ``BC`` has fallen  upon them, the alternate angles ``ABC``, ``BCD`` are equal to one another. [:ref:`I.29`]

Again, since ``AC`` is parallel to ``BD``, and ``BC``has fallen upon them, the alternate angles ``ACB``, ``CBD`` are equal to one another. [:ref:`I.29`]

Therefore ``ABC``, ``DCB`` are two triangles having the two angles ``ABC``, ``BCA`` equal to the two angles ``DCB``, ``CBD`` respectively, and one side equal to one side, namely that adjoining the equal angles and common to both of them, ``BC``; therefore they will also have the remaining sides equal to the remaining sides respectively, and the remaining angle to the remaining angle; [:ref:`I.26`] therefore the side ``AB`` is equal to ``CD``, and ``AC`` to ``BD``, and further the angle ``BAC`` is equal to the angle ``CDB``.

And, since the angle ``ABC`` is equal to the angle ``BCD``, and the angle ``CBD`` to the angle ``ACB``, the whole angle ``ABD`` is equal to the whole angle ``ACD``. [:ref:`I.cn.2`]
        And the angle ``BAC`` was also proved equal to the angle ``CDB``.

Therefore in parallelogrammic areas the opposite sides and angles are equal to one another.

I say, next, that the diameter also bisects the areas.

For, since ``AB`` is equal to ``CD``, and ``BC`` is common, the two sides ``AB``, ``BC`` are equal to the two sides ``DC``, ``CB`` respectively; and the angle ``ABC`` is equal to the angle ``BCD``; therefore the base ``AC`` is also equal to ``DB``, and the triangle ``ABC`` is equal to the triangle ``DCB``. [:ref:`I.4`]

Therefore the diameter ``BC`` bisects the parallelogram ``ACDB``.


**Q. E. D.**


Q. E. D.


.. note::


   **1**

   

   It is to be observed that, when parallelograms have to be mentioned for the first time, Euclid calls them parallelogrammic areas

    or, more exactly, parallelogram

    areas (παραλληλόγραμμα χωρία). The meaning is simply areas bounded by parallel straight lines with the further limitation placed upon the term by Euclid that only ``four-sided`` figures are so called, although of course there are certain regular polygons which have opposite sides parallel, and which therefore might be said to be areas bounded by parallel straight lines. We gather from Proclus (p. 393) that the word parallelogram

    was first introduced by Euclid, that its use was suggested by :ref:`I.33`, and that the formation of the word παραλληλόγραμμος (parallel-lined) was analogous to that of εὐθύγραμμος (straight-lined or rectilineal).


.. note::


   **17, 18, 40. DCB**

   

   and 36. DC, CB. The Greek has in these places ``BCD``

    and ``CD``, ``BC``

    respectively. Cf. note on :ref:`I.33`, lines 15, 18.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.34" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/34/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.15" -> "I.post.4";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.7" -> "I.5";
     "I.29" -> "I.post.5";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.16" -> "I.10";
     "I.34" -> "I.26";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.8" -> "I.7";
     "I.10" -> "I.9";
     "I.34" -> "I.29";
     "I.26" -> "I.16";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.3" -> "I.2";
     "I.4" -> "I.cn.4";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
   }



Required for
------------

:ref:`I.35`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.43`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.7`, :ref:`IV.8`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`