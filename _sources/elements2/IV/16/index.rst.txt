:order: 16
:number: 168
:type: prop
:tags: circle
:dependencies: III.30




.. figure:: IV.16.jpg
   :width: 50%

.. _IV.16:

IV.16
=====

   In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular.

``In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular``.

Let ``ABCD`` be the given circle; thus it is required to inscribe in the circle ``ABCD`` a fifteenangled figure which shall be both equilateral and equiangular.

In the circle ``ABCD`` let there be inscribed a side ``AC`` of the equilateral triangle inscribed in it, and a side ``AB`` of an equilateral pentagon; therefore, of the equal segments of which there are fifteen in the circle ``ABCD``, there will be five in the circumference ``ABC`` which is one-third of the circle, and there will be three in the circumference ``AB`` which is one-fifth of the circle;


.. container:: center

   therefore in the remainder ``BC`` there will be two of the equal segments.


Let ``BC`` be bisected at ``E``; [:ref:`III.30`] therefore each of the circumferences ``BE``, ``EC`` is a fifteenth of the circle ``ABCD``.

If therefore we join ``BE``, ``EC`` and fit into the circle ``ABCD`` straight lines equal to them and in contiguity, a fifteen-angled figure which is both equilateral and equiangular will have been inscribed in it. Q. E. F.

And, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents to the circle, there will be circumscribed about the circle a fifteen-angled figure which is equilateral and equiangular.

And further, by proofs similar to those in the case of the pentagon, we can both inscribe a circle in the given fifteenangled figure and circumscribe one about it. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "III.24" [URL="/elements2/III/24/", target="_top"];
     "III.30" [URL="/elements2/III/30/", target="_top"];
     "III.def.11" [style="rounded,filled", fillcolor=orange, URL="/elements2/III/def.11/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "III.28" [URL="/elements2/III/28/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "III.10" [URL="/elements2/III/10/", target="_top"];
     "IV.16" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/IV/16/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "elem.3.1.p.1" [style="rounded,filled", fillcolor=orange];
     "III.5" [URL="/elements2/III/5/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "III.26" [URL="/elements2/III/26/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "III.26" -> "III.24";
     "IV.16" -> "III.30";
     "III.26" -> "III.def.11";
     "III.24" -> "I.8";
     "III.28" -> "I.8";
     "I.3" -> "I.2";
     "III.30" -> "III.28";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "III.24" -> "III.10";
     "I.2" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "III.10" -> "elem.3.1.p.1";
     "III.10" -> "III.5";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.8" -> "I.7";
     "III.28" -> "III.26";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.5" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.7" -> "I.5";
     "I.5" -> "I.4";
     "III.26" -> "I.4";
     "III.30" -> "I.4";
   }
