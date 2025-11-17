:order: 16
:number: 124
:type: prop
:tags: line, circle
:dependencies: I.17, I.19, I.5




.. figure:: III.16.jpg
   :width: 50%

.. _III.16:

III.16
======

   The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.

Let ``ABC`` be a circle about ``D`` as centre and ``AB`` as diameter; I say that the straight line drawn from ``A`` at right angles to ``AB`` from its extremity will fall outside the circle.

For suppose it does not, but, if possible, let it fall within as ``CA``, and let ``DC`` be joined.

Since ``DA`` is equal to ``DC``,


.. container:: center

   the angle ``DAC`` is also equal to the angle ``ACD``. [:ref:`I.5`]


But the angle ``DAC`` is right;


.. container:: center

   therefore the angle ``ACD`` is also right:


thus, in the triangle ``ACD``, the two angles ``DAC``, ``ACD`` are equal to two right angles: which is impossible. [:ref:`I.17`]

Therefore the straight line drawn from the point ``A`` at right angles to ``BA`` will not fall within the circle.

Similarly we can prove that neither will it fall on the circumference;


.. container:: center

   therefore it will fall outside.


Let it fall as ``AE``; I say next that into the space between the straight line ``AE`` and the circumference ``CHA`` another straight line cannot be interposed.

For, if possible, let another straight line be so interposed, as ``FA``, and let ``DG`` be drawn from the point ``D`` perpendicular to ``FA``.

Then, since the angle ``AGD`` is right,


.. container:: center

   and the angle ``DAG`` is less than a right angle, ``AD`` is greater than ``DG``. [:ref:`I.19`]


But ``DA`` is equal to ``DH``;


.. container:: center

   therefore ``DH`` is greater than ``DG``, the less than the greater: which is impossible.


Therefore another straight line cannot be interposed into the space between the straight line and the circumference.

I say further that the angle of the semicircle contained by the straight line ``BA`` and the circumference ``CHA`` is greater than any acute rectilineal angle, and the remaining angle contained by the circumference ``CHA`` and the straight line ``AE`` is less than any acute rectilineal angle.

For, if there is any rectilineal angle greater than the angle contained by the straight line ``BA`` and the circumference ``CHA``, and any rectilineal angle less than the angle contained by the circumference ``CHA`` and the straight line ``AE``, then into the space between the circumference and the straight line ``AE`` a straight line will be interposed such as will make an angle contained by straight lines which is greater than the angle contained by the straight line ``BA`` and the circumference ``CHA``, and another angle contained by straight lines which is less than the angle contained by the circumference ``CHA`` and the straight line ``AE``.

But such a straight line cannot be interposed;

therefore there will not be any acute angle contained by straight lines which is greater than the angle contained by the straight line ``BA`` and the circumference ``CHA``, nor yet any acute angle contained by straight lines which is less than the angle contained by the circumference ``CHA`` and the straight line ``AE``.—


.. _elem.3.16.p.1:


**III.16.p.1**


From this it is manifest that the straight line drawn at right angles to the diameter of a circle from its extremity touches the circle. Q. E. D.


.. note::


   **4**

   

   cannot be interposed, literally will not fall in between

    (οὐ παρεμπεσεῖται).


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.18" [URL="/elements2/I/18/", target="_top"];
     "III.16" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/16/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
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
     "I.17" [URL="/elements2/I/17/", target="_top"];
     "I.19" [URL="/elements2/I/19/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.10" -> "I.9";
     "I.19" -> "I.18";
     "I.3" -> "I.2";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.16" -> "I.15";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
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
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.13" -> "I.11";
     "III.16" -> "I.17";
     "III.16" -> "I.19";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.16" -> "I.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
   }



Required for
------------

:ref:`IV.13`, :ref:`IV.4`, :ref:`IV.8`