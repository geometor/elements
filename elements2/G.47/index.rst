:order: 47
:original_id: I.34
:type: prop
:dependencies: G.36, G.42, G.11, G.40

.. _G.47:

G.47
====

**Heath ID:** :ref:`I.34`

   In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.

Let ``ACDB`` be a parallelogrammic area, and ``BC`` its diameter; I say that the opposite sides and angles of the parallelogram ``ACDB`` are equal to one another, and the diameter ``BC`` bisects it. 

For, since ``AB`` is parallel to ``CD``, and the straight line ``BC`` has fallen  upon them, the alternate angles ``ABC``, ``BCD`` are equal to one another. [:ref:`G.42`]

Again, since ``AC`` is parallel to ``BD``, and ``BC``has fallen upon them, the alternate angles ``ACB``, ``CBD`` are equal to one another. [:ref:`G.42`]

Therefore ``ABC``, ``DCB`` are two triangles having the two angles ``ABC``, ``BCA`` equal to the two angles ``DCB``, ``CBD`` respectively, and one side equal to one side, namely that adjoining the equal angles and common to both of them, ``BC``; therefore they will also have the remaining sides equal to the remaining sides respectively, and the remaining angle to the remaining angle; [:ref:`G.36`] therefore the side ``AB`` is equal to ``CD``, and ``AC`` to ``BD``, and further the angle ``BAC`` is equal to the angle ``CDB``.

And, since the angle ``ABC`` is equal to the angle ``BCD``, and the angle ``CBD`` to the angle ``ACB``, the whole angle ``ABD`` is equal to the whole angle ``ACD``. [:ref:`G.40`]
        And the angle ``BAC`` was also proved equal to the angle ``CDB``.

Therefore in parallelogrammic areas the opposite sides and angles are equal to one another.

I say, next, that the diameter also bisects the areas.

For, since ``AB`` is equal to ``CD``, and ``BC`` is common, the two sides ``AB``, ``BC`` are equal to the two sides ``DC``, ``CB`` respectively; and the angle ``ABC`` is equal to the angle ``BCD``; therefore the base ``AC`` is also equal to ``DB``, and the triangle ``ABC`` is equal to the triangle ``DCB``. [:ref:`G.11`]

Therefore the diameter ``BC`` bisects the parallelogram ``ACDB``.


**Q. E. D.**


Q. E. D.


.. note::


   **1**

   

   It is to be observed that, when parallelograms have to be mentioned for the first time, Euclid calls them parallelogrammic areas

    or, more exactly, parallelogram

    areas (παραλληλόγραμμα χωρία). The meaning is simply areas bounded by parallel straight lines with the further limitation placed upon the term by Euclid that only ``four-sided`` figures are so called, although of course there are certain regular polygons which have opposite sides parallel, and which therefore might be said to be areas bounded by parallel straight lines. We gather from Proclus (p. 393) that the word parallelogram

    was first introduced by Euclid, that its use was suggested by :ref:`G.46`, and that the formation of the word παραλληλόγραμμος (parallel-lined) was analogous to that of εὐθύγραμμος (straight-lined or rectilineal).


.. note::


   **17, 18, 40. DCB**

   

   and 36. DC, CB. The Greek has in these places ``BCD``

    and ``CD``, ``BC``

    respectively. Cf. note on :ref:`G.46`, lines 15, 18.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.36" [label="G.36", fillcolor="#222244", URL="/elements2/G.36/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.47" [label="G.47", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.47/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.21" -> "G.19";
     "G.9" -> "G.8";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.42" -> "G.41";
     "G.25" -> "G.17";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.47" -> "G.42";
     "G.36" -> "G.25";
     "G.17" -> "G.16";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.11" -> "G.10";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.15" -> "G.14";
     "G.47" -> "G.36";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.14" -> "G.12";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
