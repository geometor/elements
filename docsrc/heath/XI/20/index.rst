:order: 20
:number: 552
:type: prop
:dependencies: I.20, I.25, I.4




.. figure:: XI.20.graphic.inverted.png

.. _XI.20:

XI.20
=====

   If a solid angle be contained by three plane angles, any two, taken together in any manner, are greater than the remaining one.

For let the solid angle at A be contained by the three plane angles BAC, CAD, DAB; I say that any two of the angles BAC, CAD, DAB, taken together in any manner, are greater than the remaining one.

If now the angles BAC, CAD, DAB are equal to one another, it is manifest that any two are greater than the remaining one.

But, if not, let BAC be greater, and on the straight line AB, and at the point A on it, let the angle BAE be constructed, in the plane through BA, AC, equal to the angle DAB; let AE be made equal to AD, and let BEC, drawn across through the point E, cut the straight lines AB, AC at the points B, C; let DB, DC be joined.

Now, since DA is equal to AE, and AB is common, two sides are equal to two sides; and the angle DAB is equal to the angle BAE; therefore the base DB is equal to the base BE. [:ref:`I.4`]

And, since the two sides BD, DC are greater than BC, [:ref:`I.20`] and of these DB was proved equal to BE, therefore the remainder DC is greater than the remainder EC.

Now, since DA is equal to AE, and AC is common, and the base DC is greater than the base EC, therefore the angle DAC is greater than the angle EAC. [:ref:`I.25`]

But the angle DAB was also proved equal to the angle BAE; therefore the angles DAB, DAC are greater than the angle BAC.

Similarly we can prove that the remaining angles also, taken together two and two, are greater than the remaining one.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "I.cn.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.5/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.20" [URL="/heath/I/20/", target="_top"];
     "I.24" [URL="/heath/I/24/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "XI.20" [style="rounded,filled", fillcolor=lightblue, URL="/heath/XI/20/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.18" [URL="/heath/I/18/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "I.19" [URL="/heath/I/19/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.25" [URL="/heath/I/25/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.23" [URL="/heath/I/23/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.20" -> "I.cn.5";
     "I.15" -> "I.post.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.13" -> "I.11";
     "I.8" -> "I.7";
     "XI.20" -> "I.20";
     "I.25" -> "I.24";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.3" -> "I.2";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.24" -> "I.4";
     "I.25" -> "I.4";
     "XI.20" -> "I.4";
     "I.15" -> "I.13";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.19" -> "I.18";
     "I.18" -> "I.16";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.20" -> "I.19";
     "I.24" -> "I.19";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.10" -> "I.9";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "XI.20" -> "I.25";
     "I.4" -> "I.cn.4";
     "I.24" -> "I.23";
     "I.16" -> "I.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.16" -> "I.10";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.20" -> "I.5";
     "I.24" -> "I.5";
   }



Required for
------------

:ref:`XI.21`, :ref:`XIII.18`