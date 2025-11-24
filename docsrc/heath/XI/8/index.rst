:order: 8
:number: 540
:type: prop
:tags: line
:dependencies: I.29, XI.2, XI.4, XI.7, XI.def.3




.. figure:: XI.8.graphic.inverted.png

.. _XI.8:

XI.8
====

   If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.

Let AB, CD be two parallel straight lines, and let one of them, AB, be at right angles to the plane of reference; I say that the remaining one, CD, will also be at right angles to the same plane.

For let AB, CD meet the plane of reference at the points B, D, and let BD be joined; therefore AB, CD, BD are in one plane. [:ref:`XI.7`]

Let DE be drawn, in the plane of reference, at right angles to BD, let DE be made equal to AB, and let BE, AE, AD be joined.

Now, since AB is at right angles to the plane of reference, therefore AB is also at right angles to all the straight lines which meet it and are in the plane of reference; [:ref:`XI.def.3`] therefore each of the angles ABD, ABE is right.

And, since the straight line BD has fallen on the parallels AB, CD, therefore the angles ABD, CDB are equal to two right angles. [:ref:`I.29`]

But the angle ABD is right; therefore the angle CDB is also right; therefore CD is at right angles to BD.

And, since AB is equal to DE, and BD is common, the two sides AB, BD are equal to the two sides ED, DB; and the angle ABD is equal to the angle EDB, for each is right; therefore the base AD is equal to the base BE.

And, since AB is equal to DE, and BE to AD, the two sides AB, BE are equal to the two sides ED, DA respectively, and AE is their common base; therefore the angle ABE is equal to the angle EDA.

But the angle ABE is right; therefore the angle EDA is also right; therefore ED is at right angles to AD.

But it is also at right angles to DB; therefore ED is also at right angles to the plane through BD, DA. [:ref:`XI.4`]

Therefore ED will also make right angles with all the straight lines which meet it and are in the plane through BD, DA.

But DC is in the plane through BD, DA, inasmuch as AB, BD are in the plane through BD, DA, [:ref:`XI.2`] and DC is also in the plane in which AB, BD are.

Therefore ED is at right angles to DC, so that CD is also at right angles to DE.

But CD is also at right angles to BD.

Therefore CD is set up at right angles to the two straight lines DE, DB which cut one another, from the point of section at D; so that CD is also at right angles to the plane through DE, DB. [:ref:`XI.4`]

But the plane through DE, DB is the plane of reference; therefore CD is at right angles to the plane of reference.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "XI.4" [URL="/heath/XI/4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "XI.8" [style="rounded,filled", fillcolor=lightblue, URL="/heath/XI/8/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "XI.3" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/3/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "XI.def.3" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/def.3/", target="_top"];
     "XI.2" [URL="/heath/XI/2/", target="_top"];
     "XI.7" [URL="/heath/XI/7/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "I.29" [URL="/heath/I/29/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.2/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.5/", target="_top"];
     "XI.1" [style="rounded,filled", fillcolor=orange, URL="/heath/XI/1/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "I.26" [URL="/heath/I/26/", target="_top"];
     "I.10" -> "I.9";
     "XI.8" -> "XI.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "XI.7" -> "XI.3";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "XI.4" -> "XI.def.3";
     "XI.8" -> "XI.def.3";
     "XI.8" -> "XI.2";
     "XI.8" -> "XI.7";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.8" -> "I.7";
     "I.3" -> "I.2";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.15" -> "I.post.4";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "XI.4" -> "I.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.7" -> "I.5";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "XI.4" -> "I.8";
     "XI.8" -> "I.29";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.26" -> "I.16";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "XI.4" -> "I.15";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.29" -> "I.cn.2";
     "I.29" -> "I.post.5";
     "XI.2" -> "XI.1";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "XI.4" -> "I.26";
   }



Required for
------------

:ref:`XI.10`, :ref:`XI.11`, :ref:`XI.12`, :ref:`XI.15`, :ref:`XI.18`, :ref:`XI.23`, :ref:`XI.24`, :ref:`XI.25`, :ref:`XI.26`, :ref:`XI.31`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.35`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.38`, :ref:`XI.39`, :ref:`XI.9`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.17`, :ref:`XIII.18`