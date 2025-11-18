:order: 16
:number: 49
:type: prop
:tags: triangle
:dependencies: I.10, I.15, I.3, I.4, I.post.1, I.post.2




.. figure:: I.16.jpg
   :width: 50%

.. _I.16:

I.16
====

   In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

Let ``ABC`` be a triangle, and let one side of it ``BC`` be produced to ``D``; 

I say that the exterior angle ``ACD`` is greater than either of the interior and opposite angles ``CBA``, ``BAC``.

Let ``AC`` be bisected at ``E`` [:ref:`I.10`], and let ``BE`` be joined and produced in a straight line to ``F``; 

let ``EF`` be made equal to ``BE``[:ref:`I.3`], let ``FC`` be joined [:ref:`I.post.1`], and let ``AC`` be drawn through to ``G`` [:ref:`I.post.2`].

Then, since ``AE`` is equal to ``EC``, and ``BE`` to ``EF``, the two sides ``AE``, ``EB`` are equal to the two sides ``CE``, ``EF`` respectively; and the angle ``AEB`` is equal to the angle ``FEC``, for they are vertical angles. [:ref:`I.15`] Therefore the base ``AB`` is equal to the base ``FC``, and the triangle ``ABE`` is equal to the triangle ``CFE``, and the remaining angles are equal to the remaining angles respectively, namely those which the equal sides subtend; [:ref:`I.4`] therefore the angle ``BAE`` is equal to the angle ``ECF``.
        

But the angle ``ECD`` is greater than the angle ``ECF``; [C. N. 5] therefore the angle ``ACD`` is greater than the angle ``BAE``.

Similarly also, if ``BC`` be bisected, the angle ``BCG``, that is, the angle ``ACD`` [:ref:`I.15`], can be proved greater than the angle ``ABC`` as well.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. the exterior angle,**

   

   literally the outside angle,

    ἡ ἐκτὸς γωνία.


.. note::


   **2. the interior and opposite angles,**

   

   τῶν ἐντὸς καὶ ἀπεναντίον γωνιῶν.


.. note::


   **12. let AC be drawn through to G.**

   

   The word is διήχθω, a variation on the more usual ἐκβεβλήσθω, let it be ``produced``.


.. note::


   **21. CFE,**

   

   in the text ``FEC``.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.16" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/16/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.10" -> "I.9";
     "I.7" -> "I.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.15" -> "I.post.4";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.15" -> "I.13";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.13" -> "I.11";
     "I.16" -> "I.10";
     "I.16" -> "I.15";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
   }



Required for
------------

:ref:`I.17`, :ref:`I.18`, :ref:`I.19`, :ref:`I.20`, :ref:`I.21`, :ref:`I.22`, :ref:`I.24`, :ref:`I.25`, :ref:`I.26`, :ref:`I.27`, :ref:`I.28`, :ref:`I.31`, :ref:`I.32`, :ref:`I.33`, :ref:`I.34`, :ref:`I.35`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.43`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.12`, :ref:`III.13`, :ref:`III.14`, :ref:`III.15`, :ref:`III.16`, :ref:`III.18`, :ref:`III.19`, :ref:`III.2`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.23`, :ref:`III.27`, :ref:`III.29`, :ref:`III.3`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`III.4`, :ref:`III.7`, :ref:`III.8`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.13`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.4`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`