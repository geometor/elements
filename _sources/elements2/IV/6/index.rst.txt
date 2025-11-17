:order: 6
:number: 158
:type: prop
:tags: circle
:dependencies: I.4, I.def.22, III.31




.. figure:: IV.6.jpg
   :width: 50%

.. _IV.6:

IV.6
====

   In a given circle to inscribe a square.

``In a given circle to inscribe a square``.

Let ``ABCD`` be the given circle; thus it is required to inscribe a square in the circle ``ABCD``.

Let two diameters ``AC``, ``BD`` of the circle ``ABCD`` be drawn at right angles to one another, and let ``AB``, ``BC``, ``CD``, ``DA`` be joined.

Then, since ``BE`` is equal to ``ED``, for ``E`` is the centre, and ``EA`` is common and at right angles, therefore the base ``AB`` is equal to the base ``AD``. [:ref:`I.4`]

For the same reason each of the straight lines ``BC``, ``CD`` is also equal to each of the straight lines ``AB``, ``AD``;


.. container:: center

   therefore the quadrilateral ``ABCD`` is equilateral.


I say next that it is also right-angled.

For, since the straight line ``BD`` is a diameter of the circle ``ABCD``, therefore ``BAD`` is a semicircle;


.. container:: center

   therefore the angle ``BAD`` is right. [:ref:`III.31`]


For the same reason each of the angles ``ABC``, ``BCD``, ``CDA`` is also right;


.. container:: center

   therefore the quadrilateral ``ABCD`` is right-angled.


But it was also proved equilateral; therefore it is a square; [:ref:`I.def.22`] and it has been inscribed in the circle ``ABCD``.

Therefore in the given circle the square ``ABCD`` has been inscribed. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "III.22" [URL="/elements2/III/22/", target="_top"];
     "I.32" [URL="/elements2/I/32/", target="_top"];
     "III.31" [URL="/elements2/III/31/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.22" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.22/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "IV.6" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/IV/6/", target="_top"];
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
     "IV.6" -> "III.31";
     "I.4" -> "I.cn.4";
     "IV.6" -> "I.def.22";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
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
     "IV.6" -> "I.4";
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
