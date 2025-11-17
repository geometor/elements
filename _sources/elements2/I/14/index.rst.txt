:order: 14
:number: 47
:type: prop
:tags: line
:dependencies: I.13, I.cn.1, I.cn.3, I.post.4




.. figure:: I.14.jpg
   :width: 50%

.. _I.14:

I.14
====

   If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

For with any straight line ``AB``, and at the point ``B`` on it, let the two straight lines ``BC``, ``BD`` not lying on the same side make the adjacent angles ``ABC``, ``ABD`` equal to two right angles;

I say that ``BD`` is in a straight line with ``CB``. 

For, if ``BD`` is not in a straight line with ``BC``, let ``BE`` be in a straight line with ``CB``.

Then, since the straight line ``AB`` stands on the straight line ``CBE``, 
        the angles ``ABC``, ``ABE`` are equal to two right angles. [:ref:`I.13`] But the angles ``ABC``, ``ABD`` are also equal to two right angles; therefore the angles ``CBA``, ``ABE`` are equal to the angles ``CBA``, ``ABD``. [:ref:`I.post.4` and :ref:`I.cn.1`]

Let the angle ``CBA`` be subtracted from each; therefore the remaining angle ``ABE`` is equal to the remaining angle ``ABD``, [:ref:`I.cn.3`] the less to the greater: which is impossible. Therefore ``BE`` is not in a straight line with ``CB``.

Similarly we can prove that neither is any other straight line except ``BD``. Therefore ``CB`` is in a straight line with ``BD``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. If with any straight line....**

   

   There is no greater difficulty in translating the works of the Greek geometers than that of accurately giving the force of prepositions. πρός, for instance, is used in all sorts of expressions with various shades of meaning. The present enunciation begins ἐὰν πρός τινι εὐθείᾳ καὶ τῷ πρὸς αὐτῆ σημείῳ, and it is really necessary in this one sentence to translate πρός by three different words, ``with``, ``at``, and ``on``. The first πρός must be translated by ``with`` because two straight lines make

    an angle ``with`` one another. On the other hand, where the similar expression πρὸς τῇ δοθείση εὐθείᾳ occurs in :ref:`I.23`, but it is a question of constructing

    an angle (συστἡσασθαι), we have to say to construct ``on`` a given straight line.

    Against would perhaps be the English word coming nearest to expressing all these meanings of πρός, but it would be intolerable as a translation.


.. note::


   **17**

   

   Todhunter points out that for the inference in this line :ref:`I.post.4`, that all right angles are equal, is necessary as well as the Common Notion that things which are equal to the same thing (or rather, here, to ``equal things``) are equal. A similar remark applies to steps in the proofs of :ref:`I.15` and :ref:`I.28`.


.. note::


   **24. we can prove.**

   

   The Greek expresses this by the future of the verb, δείξομεν, we shall prove,

    which however would perhaps be misleading in English.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.14" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/14/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.11" -> "I.8";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.14" -> "I.13";
     "I.14" -> "I.post.4";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.8" -> "I.7";
     "I.5" -> "I.3";
     "I.11" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.13" -> "I.11";
     "I.7" -> "I.5";
     "I.5" -> "I.4";
   }



Required for
------------

:ref:`I.45`, :ref:`I.47`, :ref:`I.48`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.19`, :ref:`VI.20`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`, :ref:`VI.32`