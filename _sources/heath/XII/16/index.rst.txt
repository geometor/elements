:order: 16
:number: 587
:type: prop
:tags: circle
:dependencies: I.4, III.3, X.1, elem.3.16.p.1




.. figure:: XII.16.graphic.inverted.png

.. _XII.16:

XII.16
======

   Given two circles about the same centre, to inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle.

Let ABCD, EFGH be the two given circles about the same centre K; thus it is required to inscribe in the greater circle ABCD an equilateral polygon with an even number of sides which does not touch the circle EFGH.

For let the straight line BKD be drawn through the centre K, and from the point G let GA be drawn at right angles to the straight line BD and carried through to C; therefore AC touches the circle EFGH. [:ref:`elem.3.16.p.1`]

Then, bisecting the circumference BAD, bisecting the half of it, and doing this continually, we shall leave a circumference less than AD. [:ref:`X.1`]

Let such be left, and let it be LD; from L let LM be drawn perpendicular to BD and carried through to N, and let LD, DN be joined; therefore LD is equal to DN. [:ref:`III.3`, :ref:`I.4`]

Now, since LN is parallel to AC, and AC touches the circle EFGH, therefore LN does not touch the circle EFGH; therefore LD, DN are far from touching the circle EFGH.

If then we fit into the circle ABCD straight lines equal to the straight line LD and placed continuously, there will be inscribed in the circle ABCD an equilateral polygon with an even number of sides which does not touch the lesser circle EFGH. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "X.1" [URL="/heath/X/1/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "III.3" [URL="/heath/III/3/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.26" [URL="/heath/I/26/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "XII.16" [style="rounded,filled", fillcolor=lightblue, URL="/heath/XII/16/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "elem.3.16.p.1" [style="rounded,filled", fillcolor=orange];
     "I.15" -> "I.13";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.7" -> "I.5";
     "III.3" -> "I.5";
     "I.13" -> "I.11";
     "I.8" -> "I.7";
     "I.16" -> "I.10";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "XII.16" -> "I.4";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.26" -> "I.16";
     "XII.16" -> "X.1";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "III.3" -> "I.8";
     "I.10" -> "I.9";
     "X.1" -> "V.def.4";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.3" -> "I.def.10";
     "XII.16" -> "III.3";
     "I.15" -> "I.post.4";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.3" -> "I.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.4" -> "I.cn.4";
     "III.3" -> "I.26";
     "I.16" -> "I.15";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "XII.16" -> "elem.3.16.p.1";
   }
