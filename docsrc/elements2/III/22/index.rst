:order: 22
:number: 130
:type: prop
:tags: circle
:dependencies: I.32, III.21




.. figure:: III.22.jpg
   :width: 50%

.. _III.22:

III.22
======

   The opposite angles of quadrilaterals in circles are equal to two right angles.

Let ``ABCD`` be a circle, and let ``ABCD`` be a quadrilateral in it; I say that the opposite angles are equal to two right angles.

Let ``AC``, ``BD`` be joined.

Then, since in any triangle the three angles are equal to two right angles, [:ref:`I.32`]


.. container:: center

   the three angles ``CAB``, ``ABC``, ``BCA`` of the triangle ``ABC`` are equal to two right angles.


But the angle ``CAB`` is equal to the angle ``BDC``, for they are in the same segment ``BADC``; [:ref:`III.21`] and the angle ``ACB`` is equal to the angle

``ADB``, for they are in the same segment ``ADCB``; therefore the whole angle ``ADC`` is equal to the angles ``BAC``, ``ACB``.

Let the angle ``ABC`` be added to each; therefore the angles ``ABC``, ``BAC``, ``ACB`` are equal to the angles ``ABC``, ``ADC``. But the angles ``ABC``, ``BAC``, ``ACB`` are equal to two right angles; therefore the angles ``ABC``, ``ADC`` are also equal to two right angles.

Similarly we can prove that the angles ``BAD``, ``DCB`` are also equal to two right angles.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.32" [URL="/elements2/I/32/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "III.22" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/22/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.31" [URL="/elements2/I/31/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "III.21" [URL="/elements2/III/21/", target="_top"];
     "III.20" [URL="/elements2/III/20/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.7" -> "I.5";
     "III.20" -> "I.5";
     "I.29" -> "I.post.5";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.29" -> "I.cn.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.32" -> "I.31";
     "I.13" -> "I.11";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.27" -> "I.def.23";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "III.22" -> "III.21";
     "III.21" -> "III.20";
     "I.8" -> "I.7";
     "I.10" -> "I.9";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.32" -> "I.29";
     "I.15" -> "I.post.4";
     "I.27" -> "I.16";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.3" -> "I.2";
     "I.31" -> "I.27";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.16" -> "I.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.31" -> "I.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
   }



Required for
------------

:ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.2`, :ref:`IV.5`, :ref:`IV.6`, :ref:`VI.13`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`