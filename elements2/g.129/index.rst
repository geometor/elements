:order: 129
:original_id: IV.8
:type: prop
:dependencies: g.17, g.44, g.47, g.95

.. _g.129:

G.129
=====

**Heath ID:** :ref:`IV.8`

   In a given square to inscribe a circle.

``In a given square to inscribe a circle``.

Let ``ABCD`` be the given square; thus it is required to inscribe a circle in the given square ``ABCD``.

Let the straight lines ``AD``, ``AB`` be bisected at the points ``E``, ``F`` respectively [:ref:`g.17`], through ``E`` let ``EH`` be drawn parallel to either ``AB`` or ``CD``, and through ``F`` let ``FK`` be drawn parallel to either ``AD`` or ``BC``; [:ref:`g.44`] therefore each of the figures ``AK``, ``KB``, ``AH``, ``HD``, ``AG``, ``GC``, ``BG``, ``GD`` is a parallelogram, and their opposite sides are evidently equal. [:ref:`g.47`]

Now, since ``AD`` is equal to ``AB``, and ``AE`` is half of ``AD``, and ``AF`` half of ``AB``,


.. container:: center

   therefore ``AE`` is equal to ``AF``, so that the opposite sides are also equal;



.. container:: center

   therefore ``FG`` is equal to ``GE``.


Similarly we can prove that each of the straight lines ``GH``, ``GK`` is equal to each of the straight lines ``FG``, ``GE``;


.. container:: center

   therefore the four straight lines ``GE``, ``GF``, ``GH``, ``GK`` are equal to one another.


Therefore the circle described with centre ``G`` and distance one of the straight lines ``GE``, ``GF``, ``GH``, ``GK`` will pass also through the remaining points.

And it will touch the straight lines ``AB``, ``BC``, ``CD``, ``DA``, because the angles at ``E``, ``F``, ``H``, ``K`` are right.

For, if the circle cuts ``AB``, ``BC``, ``CD``, ``DA``, the straight line drawn at right angles to the diameter of the circle from its extremity will fall within the circle : which was proved absurd; [:ref:`g.95`] therefore the circle described with centre ``G`` and distance one of the straight lines ``GE``, ``GF``, ``GH``, ``GK`` will not cut the straight lines ``AB``, ``BC``, ``CD``, ``DA``.

Therefore it will touch them, and will have been inscribed in the square ``ABCD``.

Therefore in the given square a circle has been inscribed. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.95" [label="G.95", URL="/elements2/g.95/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.129" [label="G.129", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.129/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.26" [label="G.26", URL="/elements2/g.26/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.129" -> "G.95";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.28" -> "G.27";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.95" -> "G.28";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.129" -> "G.44";
     "G.47" -> "G.42";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.44" -> "G.38";
     "G.95" -> "G.26";
     "G.25" -> "G.17";
     "G.129" -> "G.17";
     "G.24" -> "G.21";
     "G.26" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.47" -> "G.36";
     "G.21" -> "G.19";
     "G.26" -> "G.25";
     "G.27" -> "G.25";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.129" -> "G.47";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.44" -> "G.33";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.26" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.95" -> "G.12";
   }
