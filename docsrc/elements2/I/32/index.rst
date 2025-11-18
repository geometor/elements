:order: 32
:number: 65
:type: prop
:tags: triangle
:dependencies: I.13, I.29, I.31




.. figure:: I.32.jpg
   :width: 50%

.. _I.32:

I.32
====

   In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

Let ``ABC`` be a triangle, and let one side of it ``BC`` be produced to ``D``;

I say that the exterior angle ``ACD`` is equal to the two interior and opposite angles ``CAB``, ``ABC``, and the three interior angles of the triangle ``ABC``, ``BCA``, ``CAB`` are equal to two right angles. 

For let ``CE`` be drawn through the point ``C`` parallel to the straight line ``AB``. [:ref:`I.31`]

Then, since ``AB`` is parallel to ``CE``, and ``AC`` has fallen upon them, the alternate angles ``BAC``, ``ACE`` are equal to one another. [:ref:`I.29`]
        

Again, since ``AB`` is parallel to ``CE``, and the straight line ``BD`` has fallen upon them, the exterior angle ``ECD`` is equal to the interior and opposite angle ``ABC``. [:ref:`I.29`]

But the angle ``ACE`` was also proved equal to the angle ``BAC``; therefore the whole angle ``ACD`` is equal to the two interior and opposite angles ``BAC``, ``ABC``.

Let the angle ``ACB`` be added to each; therefore the angles ``ACD``, ``ACB`` are equal to the three angles ``ABC``, ``BCA``, ``CAB``.

But the angles ``ACD``, ``ACB`` are equal to two right angles; [:ref:`I.13`] therefore the angles ``ABC``, ``BCA``, ``CAB`` are also equal to two right angles.

Therefore etc.


**Q. E. D.**


Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.31" [URL="/elements2/I/31/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.32" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/32/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.32" -> "I.31";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.27" -> "I.def.23";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.7" -> "I.5";
     "I.29" -> "I.post.5";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.15" -> "I.post.4";
     "I.16" -> "I.10";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.8" -> "I.7";
     "I.10" -> "I.9";
     "I.32" -> "I.29";
     "I.31" -> "I.23";
     "I.27" -> "I.16";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.3" -> "I.2";
     "I.31" -> "I.27";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.cn.2";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
   }



Required for
------------

:ref:`II.10`, :ref:`II.9`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.27`, :ref:`III.29`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.5`, :ref:`IV.6`, :ref:`VI.13`, :ref:`VI.18`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`