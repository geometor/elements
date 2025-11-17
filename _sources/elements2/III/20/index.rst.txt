:order: 20
:number: 128
:type: prop
:tags: circle
:dependencies: I.32, I.5




.. figure:: III.20.jpg
   :width: 50%

.. _III.20:

III.20
======

   In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.

Let ``ABC`` be a circle, let the angle ``BEC`` be an angle at its centre, and the angle ``BAC`` an angle at the circumference, and let them have the same circumference ``BC`` as base; I say that the angle ``BEC`` is double of the angle ``BAC``.

For let ``AE`` be joined and drawn through to ``F``.

Then, since ``EA`` is equal to ``EB``,


.. container:: center

   the angle ``EAB`` is also equal to the angle ``EBA``; [:ref:`I.5`]


therefore the angles ``EAB``, ``EBA`` are double of the angle ``EAB``.

But the angle ``BEF`` is equal to the angles ``EAB``, ``EBA``; [:ref:`I.32`] therefore the angle ``BEF`` is also double of the angle ``EAB``.

For the same reason


.. container:: center

   the angle ``FEC`` is also double of the angle ``EAC``.


Therefore the whole angle ``BEC`` is double of the whole angle ``BAC``.

Again let another straight line be inflected, and let there be another angle ``BDC``; let ``DE`` be joined and produced to ``G``.

Similarly then we can prove that the angle ``GEC`` is double of the angle ``EDC``,


.. container:: center

   of which the angle ``GEB`` is double of the angle ``EDB``; therefore the angle ``BEC`` which remains is double of the angle ``BDC``.


Therefore etc. Q. E. D.
let another straight line be inflected, κεκλάσθω δὴ πάλιν (without εὐθεῖα). The verb κλάω (to ``break off``) was the regular technical term for drawing from a point a (broken) straight line which first meets another straight line or curve and is then ``bent back`` from it to another point, or (in other words) for drawing straight lines from two points meeting at a point on a curve or another straight line. κεκλάσθαι is one of the geometrical terms the definition of which must according to Aristotle be assumed (Anal. Post. I. 10, 76 b 9).


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
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.32" [URL="/elements2/I/32/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "III.20" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/20/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
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
     "I.27" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.3" -> "I.2";
     "III.20" -> "I.32";
     "I.29" -> "I.cn.2";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.29" -> "I.post.5";
     "I.31" -> "I.23";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
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
     "I.32" -> "I.13";
     "I.32" -> "I.31";
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
     "I.32" -> "I.29";
     "I.7" -> "I.5";
     "III.20" -> "I.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
   }



Required for
------------

:ref:`III.21`, :ref:`III.22`, :ref:`III.27`, :ref:`III.29`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.5`, :ref:`IV.6`, :ref:`VI.13`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`, :ref:`VI.33`