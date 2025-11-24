:order: 124
:original_id: IV.4
:type: prop
:dependencies: g.36, g.16, g.95, g.122, g.123

.. _g.124:

G.124
=====

**Heath ID:** :ref:`IV.4`

   In a given triangle to inscribe a circle.

Let ``ABC`` be the given triangle; thus it is required to inscribe a circle in the triangle ``ABC``.

Let the angles ``ABC``, ``ACB``
be bisected by the straight lines ``BD``, ``CD`` [:ref:`g.16`], and let these meet one another at the point ``D``; from ``D`` let ``DE``, ``DF``, ``DG`` be drawn perpendicular to the straight lines ``AB``, ``BC``, ``CA``.

Now, since the angle ``ABD`` is equal to the angle ``CBD``, and the right angle ``BED`` is also equal to the right angle ``BFD``, ``EBD``, ``FBD`` are two triangles having two angles equal to two angles and one side equal to one side, namely that subtending one of the equal angles, which is ``BD`` common to the triangles;


.. container:: center

   therefore they will also have the remaining sides equal to the remaining sides; [:ref:`g.36`]



.. container:: center

   therefore ``DE`` is equal to ``DF``.


For the same reason


.. container:: center

   ``DG`` is also equal to ``DF``.


Therefore the three straight lines ``DE``, ``DF``, ``DG`` are equal to one another;


.. container:: center

   therefore the circle described with centre ``D`` and distance one of the straight lines ``DE``, ``DF``, ``DG`` will pass also through the remaining points, and will touch the straight lines ``AB``, ``BC``, ``CA``, because the angles at the points ``E``, ``F``, ``G``
           are right.


For, if it cuts them, the straight line drawn at right angles to the diameter of the circle from its extremity will be found to fall within the circle : which was proved absurd; [:ref:`g.95`]


.. container:: center

   therefore the circle described with centre ``D`` and distance one of the straight lines ``DE``, ``DF``, ``DG`` will not cut the straight lines ``AB``, ``BC``, ``CA``;



.. container:: center

   therefore it will touch them, and will be the circle inscribed in the triangle ``ABC``. [:ref:`g.123`]


Let it be inscribed, as ``FGE``.

Therefore in the given triangle ``ABC`` the circle ``EFG`` has been inscribed. Q. E. F.
and distance one of the (straight lines D)E, (D)F, (D)G. The words and letters here shown in brackets are put in to fill out the rather careless language of the Greek. Here and in several other places in Book IV. Euclid says literally and with distance one of the (points) ``E``, ``F``, ``G``
(καὶ διαστήματι ὲνὶ τῶν E, Z, H) and the like. In one case (:ref:`g.122`) he actually has with distance one of the ``points G``, ``H``, ``K``, ``L``, ``M``
(διαστήματι ὲνὶ τῶν Η, Θ, Κ, Λ, Μ σημείων). Heiberg notes Graecam locutionem satis miram et negligentem,
but, in view of its frequent occurrence in good MSS., does not venture to correct it.


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
     "G.123" [label="G.123", style="rounded,filled", fillcolor=orange, URL="/elements2/g.123/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.122" [label="G.122", URL="/elements2/g.122/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.124" [label="G.124", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.124/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.124" -> "G.16";
     "G.95" -> "G.26";
     "G.124" -> "G.95";
     "G.122" -> "G.95";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.28" -> "G.27";
     "G.124" -> "G.123";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.24" -> "G.21";
     "G.26" -> "G.21";
     "G.15" -> "G.14";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.124" -> "G.36";
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
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
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
     "G.124" -> "G.122";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.95" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }
