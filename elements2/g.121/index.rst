:order: 121
:original_id: IV.3
:type: prop
:dependencies: g.21, g.33, g.45, g.76, g.98, g.96

.. _g.121:

G.121
=====

**Heath ID:** :ref:`IV.3`

   About a given circle to circumscribe a triangle equiangular with a given triangle.

Let ``ABC`` be the given circle, and ``DEF`` the given triangle; thus it is required to circumscribe about the circle ``ABC`` a triangle equiangular with the triangle ``DEF``.

Let ``EF`` be produced in both directions to the points ``G``, ``H``, let the centre ``K`` of the circle ``ABC`` be taken [:ref:`g.76`], and let the straight line ``KB`` be drawn across at random; on the straight line ``KB``, and at the point ``K`` on it, let the angle ``BKA`` be constructed equal to the angle ``DEG``, and the angle ``BKC`` equal to the angle ``DFH``; [:ref:`g.33`] and through the points ``A``, ``B``, ``C`` let ``LAM``, ``MBN``, ``NCL`` be drawn touching the circle ``ABC``. [:ref:`g.96`]

Now, since ``LM``, ``MN``, ``NL`` touch the circle ``ABC`` at the points ``A``, ``B``, ``C``, and ``KA``, ``KB``, ``KC`` have been joined from the centre ``K`` to the points ``A``, ``B``, ``C``, therefore the angles at the points ``A``, ``B``, ``C`` are right. [:ref:`g.98`]

And, since the four angles of the quadrilateral ``AMBK`` are equal to four right angles, inasmuch as ``AMBK`` is in fact divisible into two triangles,


.. container:: center

   and the angles ``KAM``, ``KBM`` are right,


therefore the remaining angles ``AKB``, ``AMB`` are equal to two right angles.

But the angles ``DEG``, ``DEF`` are also equal to two right angles; [:ref:`g.21`] therefore the angles ``AKB``, ``AMB`` are equal to the angles ``DEG``, ``DEF``, of which the angle ``AKB`` is equal to the angle ``DEG``;


.. container:: center

   therefore the angle ``AMB`` which remains is equal to the angle ``DEF`` which remains.


Similarly it can be proved that the angle ``LNB`` is also equal to the angle ``DFE``;


.. container:: center

   therefore the remaining angle ``MLN`` is equal to the angle ``EDF``. [:ref:`g.45`]


Therefore the triangle ``LMN`` is equiangular with the triangle ``DEF``; and it has been circumscribed about the circle ``ABC``.

Therefore about a given circle there has been circumscribed a triangle equiangular with the given triangle. Q. E. F.
at random, literally as it may chance,
ὡς ἕτυχεν. The same expression is used in :ref:`g.76` and commonly.
is in fact divisible, καὶ διαιρεῖται, literally is actually divided.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.96" [label="G.96", style="rounded,filled", fillcolor=orange, URL="/elements2/g.96/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.76" [label="G.76", URL="/elements2/g.76/", target="_top"];
     "G.45" [label="G.45", URL="/elements2/g.45/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.26" [label="G.26", URL="/elements2/g.26/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.121" [label="G.121", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.121/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.98" [label="G.98", URL="/elements2/g.98/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.28" -> "G.27";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.121" -> "G.96";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.76" -> "G.15";
     "G.98" -> "G.28";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.76" -> "G.18";
     "G.24" -> "G.22";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.121" -> "G.76";
     "G.121" -> "G.45";
     "G.45" -> "G.44";
     "G.45" -> "G.42";
     "G.42" -> "G.40";
     "G.98" -> "G.26";
     "G.44" -> "G.38";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.26" -> "G.21";
     "G.42" -> "G.21";
     "G.45" -> "G.21";
     "G.121" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.121" -> "G.98";
     "G.26" -> "G.25";
     "G.27" -> "G.25";
     "G.38" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.8";
     "G.44" -> "G.33";
     "G.121" -> "G.33";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.26" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
   }
