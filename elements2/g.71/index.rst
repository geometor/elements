:order: 71
:original_id: II.10
:type: prop
:dependencies: g.19, g.24, g.42, g.9, g.44, g.45, g.47, g.60, g.12, g.13, g.1, g.41

.. _g.71:

G.71
====

**Heath ID:** :ref:`II.10`

   If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

For let a straight line ``AB`` be bisected at ``C``, and let a straight line ``BD`` be added to it in a straight line;

I say that the squares on ``AD``, ``DB`` are double of the squares on ``AC``, ``CD``.

For let ``CE`` be drawn from the point ``C`` at right angles to ``AB`` [:ref:`g.19`], and let it be made equal to either ``AC`` or ``CB`` [:ref:`g.9`]; let ``EA``, ``EB`` be joined; through ``E`` let ``EF`` be drawn parallel to ``AD``, and through ``D`` let ``FD`` be drawn parallel to ``CE``. [:ref:`g.44`]

Then, since a straight line ``EF`` falls on the parallel straight lines ``EC``, ``FD``,


.. container:: center

   the angles ``CEF``, ``EFD`` are equal to two right angles; [:ref:`g.42`] therefore the angles ``FEB``, ``EFD`` are less than two right angles.


But straight lines produced from angles less than two right angles meet; [:ref:`g.41`]


.. container:: center

   therefore ``EB``, ``FD``, if produced in the direction ``B``, ``D``, will meet.


Let them be produced and meet at ``G``, and let ``AG`` be joined.

Then, since ``AC`` is equal to ``CE``, the angle ``EAC`` is also equal to the angle ``AEC``; [:ref:`g.12`] and the angle at ``C`` is right;


.. container:: center

   therefore each of the angles ``EAC``, ``AEC`` is half a right angle. [:ref:`g.45`]


For the same reason


.. container:: center

   each of the angles ``CEB``, ``EBC`` is also half a right angle; therefore the angle ``AEB`` is right.


And, since the angle ``EBC`` is half a right angle, the angle ``DBG`` is also half a right angle. [:ref:`g.24`]


.. container:: center

   But the angle ``BDG`` is also right,


for it is equal to the angle ``DCE``, they being alternate; [:ref:`g.42`]


.. container:: center

   therefore the remaining angle ``DGB`` is half a right angle; [:ref:`g.45`]


therefore the angle ``DGB`` is equal to the angle ``DBG``,


.. container:: center

   so that the side ``BD`` is also equal to the side ``GD``. [:ref:`g.13`]


Again, since the angle ``EGF`` is half a right angle, and the angle at ``F`` is right, for it is equal to the opposite angle, the angle at ``C``, [:ref:`g.47`]


.. container:: center

   the remaining angle ``FEG`` is half a right angle; [:ref:`g.45`] therefore the angle ``EGF`` is equal to the angle ``FEG``, so that the side ``GF`` is also equal to the side ``EF``. [:ref:`g.13`]


Now, since the square on ``EC`` is equal to the square on ``CA``, the squares on ``EC``, ``CA`` are double of the square on ``CA``.

But the square on ``EA`` is equal to the squares on ``EC``, ``CA``; [:ref:`g.60`] therefore the square on ``EA`` is double of the square on ``AC``. [:ref:`g.1`]

Again, since ``FG`` is equal to ``EF``, the square on ``FG`` is also equal to the square on ``FE``; therefore the squares on ``GF``, ``FE`` are double of the square on ``EF``.

But the square on ``EG`` is equal to the squares on ``GF``, ``FE``; [:ref:`g.60`] therefore the square on ``EG`` is double of the square on ``EF``.

And ``EF`` is equal to ``CD``; [:ref:`g.47`]


.. container:: center

   therefore the square on ``EG`` is double of the square on ``CD``.


But the square on ``EA`` was also proved double of the square on ``AC``; therefore the squares on ``AE``, ``EG`` are double of the squares on ``AC``, ``CD``.

And the square on ``AG`` is equal to the squares on ``AE``, ``EG``; [:ref:`g.60`] therefore the square on ``AG`` is double of the squares on ``AC``, ``CD``. But the squares on ``AD``, ``DG`` are equal to the square on ``AG``; [:ref:`g.60`] therefore the squares on ``AD``, ``DG`` are double of the squares on ``AC``, ``CD``.

And ``DG`` is equal to ``DB``; therefore the squares on ``AD``, ``DB`` are double of the squares on ``AC``, ``CD``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.54" [label="G.54", URL="/elements2/g.54/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.71" [label="G.71", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.71/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.48" [label="G.48", URL="/elements2/g.48/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.23" [label="G.23", URL="/elements2/g.23/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.60" [label="G.60", URL="/elements2/g.60/", target="_top"];
     "G.45" [label="G.45", URL="/elements2/g.45/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.59" [label="G.59", URL="/elements2/g.59/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.50" [label="G.50", URL="/elements2/g.50/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.13" [label="G.13", style="rounded,filled", fillcolor=orange, URL="/elements2/g.13/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.60" -> "G.54";
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.71" -> "G.41";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.71" -> "G.24";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.71" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.50" -> "G.48";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.23" -> "G.22";
     "G.24" -> "G.22";
     "G.60" -> "G.23";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.71" -> "G.60";
     "G.71" -> "G.45";
     "G.45" -> "G.44";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.71" -> "G.44";
     "G.60" -> "G.59";
     "G.45" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.71" -> "G.42";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.60" -> "G.40";
     "G.44" -> "G.38";
     "G.25" -> "G.17";
     "G.23" -> "G.21";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.45" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.54" -> "G.50";
     "G.8" -> "G.6";
     "G.23" -> "G.6";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.21" -> "G.19";
     "G.59" -> "G.19";
     "G.71" -> "G.19";
     "G.47" -> "G.36";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.71" -> "G.47";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.23" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.71" -> "G.1";
     "G.9" -> "G.8";
     "G.44" -> "G.33";
     "G.71" -> "G.13";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.71" -> "G.12";
   }
