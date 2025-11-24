:order: 12
:number: 601
:type: prop
:tags: circle, triangle
:dependencies: I.47, III.31, IV.15.p.1




.. figure:: XIII.12.graphic.inverted.png

.. _XIII.12:

XIII.12
=======

   If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.

Let ABC be a circle, and let the equilateral triangle ABC be inscribed in it; I say that the square on one side of the triangle ABC is triple of the square on the radius of the circle.

For let the centre D of the circle ABC be taken, let AD be joined and carried through to E, and let BE be joined.

Then, since the triangle ABC is equilateral, therefore the circumference BEC is a third part of the circumference of the circle ABC.

Therefore the circumference BE is a sixth part of the circumference of the circle; therefore the straight line BE belongs to a hexagon; therefore it is equal to the radius DE. [:ref:`IV.15.p.1`]

And, since AE is double of DE, the square on AE is quadruple of the square on ED, that is, of the square on BE.

But the square on AE is equal to the squares on AB, BE; [:ref:`III.31`, :ref:`I.47`] therefore the squares on AB, BE are quadruple of the square on BE.

Therefore, separando, the square on AB is triple of the square on BE.

But BE is equal to DE; therefore the square on AB is triple of the square on DE.

Therefore the square on the side of the triangle is triple of the square on the radius. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.23" [URL="/heath/I/23/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "I.32" [URL="/heath/I/32/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "IV.15.p.1" [style="rounded,filled", fillcolor=orange];
     "I.47" [URL="/heath/I/47/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "III.20" [URL="/heath/III/20/", target="_top"];
     "I.31" [URL="/heath/I/31/", target="_top"];
     "III.22" [URL="/heath/III/22/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "XIII.12" [style="rounded,filled", fillcolor=lightblue, URL="/heath/XIII/12/", target="_top"];
     "I.27" [URL="/heath/I/27/", target="_top"];
     "I.14" [URL="/heath/I/14/", target="_top"];
     "I.34" [URL="/heath/I/34/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.35" [URL="/heath/I/35/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.17" [URL="/heath/I/17/", target="_top"];
     "I.37" [URL="/heath/I/37/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "I.29" [URL="/heath/I/29/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "III.31" [URL="/heath/III/31/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.23/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.2/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.5/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "III.21" [URL="/heath/III/21/", target="_top"];
     "I.41" [URL="/heath/I/41/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.46" [URL="/heath/I/46/", target="_top"];
     "I.26" [URL="/heath/I/26/", target="_top"];
     "I.31" -> "I.23";
     "I.10" -> "I.9";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "XIII.12" -> "IV.15.p.1";
     "XIII.12" -> "I.47";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "III.21" -> "III.20";
     "I.32" -> "I.31";
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "III.31" -> "III.22";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.31" -> "I.def.10";
     "I.31" -> "I.27";
     "I.47" -> "I.14";
     "I.35" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.46" -> "I.34";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.37" -> "I.35";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.8" -> "I.7";
     "I.3" -> "I.2";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.7" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
     "III.31" -> "I.17";
     "I.41" -> "I.37";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.32" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "I.17" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "XIII.12" -> "III.31";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.27" -> "I.def.23";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.29" -> "I.post.5";
     "I.4" -> "I.cn.4";
     "III.22" -> "III.21";
     "I.47" -> "I.41";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.47" -> "I.46";
     "I.34" -> "I.26";
   }



Required for
------------

:ref:`XIII.13`, :ref:`XIII.18`