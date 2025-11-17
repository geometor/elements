:order: 31
:number: 139
:type: prop
:tags: circle
:dependencies: I.17, I.32, I.5, I.def.10, III.22




.. figure:: III.31.jpg
   :width: 50%

.. _III.31:

III.31
======

   In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of the greater segment is greater than a right angle, and the angle of the less segment less than a right angle.

Let ``ABCD`` be a circle, let ``BC`` be its diameter, and ``E`` its centre, and let ``BA``, ``AC``, ``AD``, ``DC`` be joined; I say that the angle ``BAC`` in the semicircle ``BAC`` is right, the angle ``ABC`` in the segment ``ABC`` greater than the semicircle is less

than a right angle, and the angle ``ADC`` in the segment ``ADC`` less than the semicircle is greater than a right angle.

Let ``AE`` be joined, and let ``BA`` be carried through to ``F``.

Then, since ``BE`` is equal to ``EA``,


.. container:: center

   the angle ``ABE`` is also equal to the angle ``BAE``. [:ref:`I.5`]


Again, since ``CE`` is equal to ``EA``,


.. container:: center

   the angle ``ACE`` is also equal to the angle ``CAE``. [:ref:`I.5`]


Therefore the whole angle ``BAC`` is equal to the two angles ``ABC``, ``ACB``.

But the angle ``FAC`` exterior to the triangle ``ABC`` is also equal to the two angles ``ABC``, ``ACB``; [:ref:`I.32`]


.. container:: center

   therefore the angle ``BAC`` is also equal to the angle ``FAC``; therefore each is right; [:ref:`I.def.10`] therefore the angle ``BAC`` in the semicircle ``BAC`` is right.


Next, since in the triangle ``ABC`` the two angles ``ABC``, ``BAC`` are less than two right angles, [:ref:`I.17`] and the angle ``BAC`` is a right angle,


.. container:: center

   the angle ``ABC`` is less than a right angle;


and it is the angle in the segment ``ABC`` greater than the semicircle.

Next, since ``ABCD`` is a quadrilateral in a circle, and the opposite angles of quadrilaterals in circles are equal to two right angles, [:ref:`III.22`] while the angle ``ABC`` is less than a right angle, therefore the angle ``ADC`` which remains is greater than a right angle; and it is the angle in the segment ``ADC`` less than the semicircle.

I say further that the angle of the greater segment, namely that contained by the circumference ``ABC`` and the straight line ``AC``, is greater than a right angle; and the angle of the less segment, namely that contained by the circumference ``ADC`` and the straight line ``AC``, is less than a right angle.

This is at once manifest. For, since the angle contained by the straight lines ``BA``, ``AC`` is right,


.. container:: center

   the angle contained by the circumference ``ABC`` and the straight line ``AC`` is greater than a right angle.


Again, since the angle contained by the straight lines ``AC``, ``AF`` is right,


.. container:: center

   the angle contained by the straight line ``CA`` and the circumference ``ADC`` is less than a right angle.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "III.22" [URL="/elements2/III/22/", target="_top"];
     "I.32" [URL="/elements2/I/32/", target="_top"];
     "III.31" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/31/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "III.21" [URL="/elements2/III/21/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "III.20" [URL="/elements2/III/20/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.31" [URL="/elements2/I/31/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.17" [URL="/elements2/I/17/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.31" -> "I.def.10";
     "III.31" -> "III.22";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.31" -> "I.27";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.8" -> "I.7";
     "I.13" -> "I.11";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.17" -> "I.16";
     "I.27" -> "I.16";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.3" -> "I.2";
     "I.29" -> "I.cn.2";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.29" -> "I.post.5";
     "III.22" -> "III.21";
     "I.31" -> "I.23";
     "III.21" -> "III.20";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.32" -> "I.31";
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
     "III.31" -> "I.17";
     "I.32" -> "I.29";
     "I.7" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
   }



Required for
------------

:ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.2`, :ref:`IV.5`, :ref:`IV.6`, :ref:`VI.13`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`