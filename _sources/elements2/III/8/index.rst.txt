:order: 8
:number: 116
:type: prop
:tags: line, circle
:dependencies: I.20, I.21, I.24, I.4, III.1




.. figure:: III.8.jpg
   :width: 50%

.. _III.8:

III.8
=====

   If a point be taken outside a circle and from the point straight lines be drawn through to the circle, one of which is through the centre and the others are drawn at random, then, of the straight lines which fall on the concave circumference, that through the centre is greatest, while of the rest
          the nearer to that through the centre is always greater than the more remote, but, of the straight lines falling on the convex circumference, that between the point and the diameter is least, while of the rest the nearer to the least is always less than the more remote, and only two equal straight lines will fall on the circle from the point, one on each side of the least.

Let ``ABC`` be a circle, and let a point ``D`` be taken outside ``ABC``; let there be drawn through from it straight lines ``DA``, ``DE``, ``DF``, ``DC``, and let ``DA`` be through the centre; I say that, of the straight lines falling on the concave circumference ``AEFC``, the straight line ``DA`` through the centre is greatest,

while ``DE`` is greater than ``DF`` and ``DF`` than ``DC``.; but, of the straight lines falling on the convex circumference ``HLKG``, the straight line ``DG`` between the point and the diameter ``AG`` is least; and the nearer to the least ``DG`` is always less than the more remote, namely ``DK`` than ``DL``, and ``DL`` than ``DH``.

For let the centre of the circle ``ABC`` be taken [:ref:`III.1`], and let it be ``M``; let ``ME``, ``MF``, ``MC``, ``MK``, ``ML``, ``MH`` be joined.

Then, since ``AM`` is equal to ``EM``, let ``MD`` be added to each;


.. container:: center

   therefore ``AD`` is equal to ``EM``, ``MD``.


But ``EM``, ``MD`` are greater than ``ED``; [:ref:`I.20`]


.. container:: center

   therefore ``AD`` is also greater than ``ED``.


Again, since ``ME`` is equal to ``MF``,


.. container:: center

   and ``MD`` is common,


therefore ``EM``, ``MD`` are equal to ``FM``, ``MD``;


.. container:: center

   and the angle ``EMD`` is greater than the angle ``FMD``;



.. container:: center

   therefore the base ``ED`` is greater than the base ``FD``. [:ref:`I.24`]


Similarly we can prove that ``FD`` is greater than ``CD``; therefore ``DA`` is greatest, while ``DE`` is greater than ``DF``, and ``DF`` than ``DC``.

Next, since ``MK``, ``KD`` are greater than ``MD``, [:ref:`I.20`] and ``MG`` is equal to ``MK``, therefore the remainder ``KD`` is greater than the remainder ``GD``,


.. container:: center

   so that ``GD`` is less than ``KD``.


And, since on ``MD``, one of the sides of the triangle ``MLD``, two straight lines ``MK``, ``KD`` were constructed meeting within the triangle, therefore ``MK``, ``KD`` are less than ``ML``, ``LD``; [:ref:`I.21`] and ``MK`` is equal to ``ML``;


.. container:: center

   therefore the remainder ``DK`` is less than the remainder ``DL``.


Similarly we can prove that ``DL`` is also less than ``DH``;


.. container:: center

   therefore ``DG`` is least, while ``DK`` is less than ``DL``, and ``DL`` than ``DH``.


I say also that only two equal straight lines will fall from the point ``D`` on the circle, one on each side of the least ``DG``.

On the straight line ``MD``, and at the point ``M`` on it, let the angle ``DMB`` be constructed equal to the angle ``KMD``, and let ``DB`` be joined.

Then, since ``MK`` is equal to ``MB``, and ``MD`` is common,


.. container:: center

   the two sides ``KM``, ``MD`` are equal to the two sides ``BM``, ``MD`` respectively;


and the angle ``KMD`` is equal to the angle ``BMD``;


.. container:: center

   therefore the base ``DK`` is equal to the base ``DB``. [:ref:`I.4`]


I say that no other straight line equal to the straight line ``DK`` will fall on the circle from the point ``D``.

For, if possible, let a straight line so fall, and let it be ``DN``.


.. container:: center

   Then, since ``DK`` is equal to ``DN``,


while ``DK`` is equal to ``DB``,


.. container:: center

   ``DB`` is also equal to ``DN``,


that is, the nearer to the least ``DG`` equal to the more remote: which was proved impossible.

Therefore no more than two equal straight lines will fall on the circle ``ABC`` from the point ``D``, one on each side of ``DG`` the least.

Therefore etc.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.19" [URL="/elements2/I/19/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.18" [URL="/elements2/I/18/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "III.1" [URL="/elements2/III/1/", target="_top"];
     "III.8" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/8/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.21" [URL="/elements2/I/21/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.5/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.24" [URL="/elements2/I/24/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.20" [URL="/elements2/I/20/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.20" -> "I.19";
     "I.24" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
     "I.19" -> "I.18";
     "I.13" -> "I.11";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.1" -> "I.8";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.20" -> "I.5";
     "I.24" -> "I.5";
     "I.16" -> "I.15";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "III.8" -> "III.1";
     "I.16" -> "I.10";
     "III.8" -> "I.21";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.20" -> "I.cn.5";
     "I.15" -> "I.13";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.24" -> "I.4";
     "III.8" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.8" -> "I.7";
     "I.10" -> "I.9";
     "I.24" -> "I.23";
     "I.18" -> "I.16";
     "I.21" -> "I.16";
     "III.8" -> "I.24";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.3" -> "I.2";
     "I.4" -> "I.cn.4";
     "I.15" -> "I.post.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.21" -> "I.20";
     "III.8" -> "I.20";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
   }
