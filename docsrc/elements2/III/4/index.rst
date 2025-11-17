:order: 4
:number: 112
:type: prop
:categories: bisect
:tags: line, circle
:dependencies: III.1, III.3




.. figure:: III.4.jpg
   :width: 50%

.. _III.4:

III.4
=====

   If in a circle two straight lines cut one another which are not through the centre, they do not bisect one another.

Let ``ABCD`` be a circle, and in it let the two straight lines ``AC``, ``BD``, which are not through the centre, cut one another at ``E``;

I say that they do not bisect one another.

For, if possible, let them bisect one another, so that ``AE`` is equal to ``EC``, and ``BE`` to ``ED``; let the centre of the circle ``ABCD`` be taken [:ref:`III.1`], and let it be ``F``; let ``FE`` be joined.

Then, since a straight line ``FE`` through the centre bisects a straight line ``AC`` not through the centre,


.. container:: center

   it also cuts it at right angles; [:ref:`III.3`] therefore the angle ``FEA`` is right.


Again, since a straight line ``FE`` bisects a straight line ``BD``,


.. container:: center

   it also cuts it at right angles; [:ref:`III.3`] therefore the angle ``FEB`` is right.


But the angle ``FEA`` was also proved right;


.. container:: center

   therefore the angle ``FEA`` is equal to the angle ``FEB``, the less to the greater: which is impossible.


Therefore ``AC``, ``BD`` do not bisect one another.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "III.4" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/4/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "III.1" [URL="/elements2/III/1/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "III.3" [URL="/elements2/III/3/", target="_top"];
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
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.26" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
     "III.3" -> "I.def.10";
     "I.10" -> "I.9";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "III.1" -> "I.8";
     "III.3" -> "I.8";
     "I.3" -> "I.2";
     "I.16" -> "I.15";
     "III.3" -> "I.26";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "III.4" -> "III.1";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "III.4" -> "III.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.15" -> "I.13";
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
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.13" -> "I.11";
     "I.7" -> "I.5";
     "III.3" -> "I.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
   }
