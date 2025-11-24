:order: 122
:original_id: IV.13
:type: prop
:dependencies: g.36, g.11, g.95

.. _g.122:

G.122
=====

**Heath ID:** :ref:`IV.13`

   In a given pentagon, which is equilateral and equiangular, to inscribe a circle.

Let ``ABCDE`` be the given equilateral and equiangular pentagon; thus it is required to inscribe a circle in the pentagon ``ABCDE``.

For let the angles ``BCD``, ``CDE`` be bisected by the straight lines ``CF``, ``DF`` respectively; and from the point ``F``, at which the straight lines ``CF``, ``DF`` meet one another, let the straight lines ``FB``, ``FA``, ``FE`` be joined.

Then, since ``BC`` is equal to ``CD``, and ``CF`` common, the two sides ``BC``, ``CF`` are equal to the two sides ``DC``, ``CF``;

and the angle ``BCF`` is equal to the angle ``DCF``;


.. container:: center

   therefore the base ``BF`` is equal to the base ``DF``,


and the triangle ``BCF`` is equal to the triangle ``DCF``, and the remaining angles will be equal to the remaining angles, namely those which the equal sides subtend. [:ref:`g.11`]

Therefore the angle ``CBF`` is equal to the angle ``CDF``.

And, since the angle ``CDE`` is double of the angle ``CDF``, and the angle ``CDE`` is equal to the angle ``ABC``, while the angle ``CDF`` is equal to the angle ``CBF``; therefore the angle ``CBA`` is also double of the angle ``CBF``;


.. container:: center

   therefore the angle ``ABF`` is equal to the angle ``FBC``;


therefore the angle ``ABC`` has been bisected by the straight line ``BF``.

Similarly it can be proved that the angles ``BAE``, ``AED`` have also been bisected by the straight lines ``FA``, ``FE`` respectively.

Now let ``FG``, ``FH``, ``FK``, ``FL``, ``FM`` be drawn from the point ``F`` perpendicular to the straight lines ``AB``, ``BC``, ``CD``, ``DE``, ``EA``.

Then, since the angle ``HCF`` is equal to the angle ``KCF``, and the right angle ``FHC`` is also equal to the angle ``FKC``, ``FHC``, ``FKC`` are two triangles having two angles equal to two angles and one side equal to one side, namely ``FC`` which is common to them and subtends one of the equal angles; therefore they will also have the remaining sides equal to the remaining sides; [:ref:`g.36`] therefore the perpendicular ``FH`` is equal to the perpendicular ``FK``.

Similarly it can be proved that each of the straight lines ``FL``, ``FM``, ``FG`` is also equal to each of the straight lines ``FH``, ``FK``; therefore the five straight lines ``FG``, ``FH``, ``FK``, ``FL``, ``FM`` are equal to one another.

Therefore the circle described with centre ``F`` and distance one of the straight lines ``FG``, ``FH``, ``FK``, ``FL``, ``FM`` will pass also through the remaining points; and it will touch the straight lines ``AB``, ``BC``, ``CD``, ``DE``, ``EA``, because the angles at the points ``G``, ``H``, ``K``, ``L``, ``M`` are right.

For, if it does not touch them. but cuts them, it will result that the straight line drawn at right angles to the diameter of the circle from its extremity falls within the circle: which was proved absurd. [:ref:`g.95`]

Therefore the circle described with centre ``F`` and distance one of the straight lines ``FG``, ``FH``, ``FK``, ``FL``, ``FM`` will not cut the straight lines ``AB``, ``BC``, ``CD``, ``DE``, ``EA``;


.. container:: center

   therefore it will touch them.


Let it be described, as ``GHKLM``.

Therefore in the given pentagon, which is equilateral and equiangular, a circle has been inscribed. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.26" [label="G.26", URL="/elements2/g.26/", target="_top"];
     "G.95" [label="G.95", URL="/elements2/g.95/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.122" [label="G.122", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.122/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.95" -> "G.26";
     "G.122" -> "G.95";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.28" -> "G.27";
     "G.24" -> "G.21";
     "G.26" -> "G.21";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.15" -> "G.14";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.122" -> "G.36";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.95" -> "G.28";
     "G.21" -> "G.19";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.26" -> "G.25";
     "G.27" -> "G.25";
     "G.36" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.26" -> "G.7";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.122" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.95" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.124`
