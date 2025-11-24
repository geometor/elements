:order: 59
:original_id: I.46
:type: prop
:dependencies: g.19, g.42, g.44, g.47

.. _g.59:

G.59
====

**Heath ID:** :ref:`I.46`

   On a given straight line to describe a square.

Let ``AB`` be the given straight line; thus it is required to describe a square on the straight line ``AB``. 
        

Let ``AC`` be drawn at right angles to the straight line ``AB`` from the point ``A`` on it [:ref:`g.19`], and let ``AD`` be made equal to ``AB``; through the point ``D`` let ``DE`` be drawn parallel to ``AB``, and through the point ``B`` let ``BE`` be drawn parallel to ``AD``. [:ref:`g.44`] 

Therefore ``ADEB`` is a parallelogram; therefore ``AB`` is equal to ``DE``, and ``AD`` to ``BE``. [:ref:`g.47`]

But ``AB`` is equal to ``AD``; therefore the four straight lines ``BA``, ``AD``, ``DE``, ``EB`` are equal to one another; therefore the parallelogram ``ADEB`` is equilateral.

I say next that it is also right-angled.

For, since the straight line ``AD`` falls upon the parallels ``AB``, ``DE``, the angles ``BAD``, ``ADE`` are equal to two right angles. [:ref:`g.42`]

But the angle ``BAD`` is right; therefore the angle ``ADE`` is also right.

And in parallelogrammic areas the opposite sides and angles are equal to one another; [:ref:`g.47`] therefore each of the opposite angles ``ABE``, ``BED`` is also right. Therefore ``ADEB`` is right-angled.

And it was also proved equilateral. 

Therefore it is a square; and it is described on the straight line ``AB``.


**Q. E. D.**


Q. E. F.


.. note::


   **1, 3, 30**

   

   Proclus (p. 423, 18 sqq.) notes the difference between the word ``construct`` (συστἡσασθαι) applied by Euclid to the construction of a ``triangle`` (and, he might have added, of an ``angle``) and the words ``describe on`` (ἀναγράφειν ἀπό) used of drawing a square on a given straight line as one side. The ``triangle`` (or ``angle``) is, so to say, pieced together, while the describing of a square on a given straight line is the making of a figure from

    ``one`` side, and corresponds to the multiplication of the number representing the side by itself.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.59" [label="G.59", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.59/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.59" -> "G.44";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.59" -> "G.42";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.44" -> "G.38";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.59" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.47" -> "G.36";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.59" -> "G.47";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.44" -> "G.33";
     "G.9" -> "G.8";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.60`, :ref:`g.61`, :ref:`g.71`, :ref:`g.72`, :ref:`g.73`, :ref:`g.74`, :ref:`g.75`, :ref:`g.63`, :ref:`g.64`, :ref:`g.65`, :ref:`g.66`, :ref:`g.67`, :ref:`g.68`, :ref:`g.70`, :ref:`g.92`, :ref:`g.94`, :ref:`g.116`, :ref:`g.117`, :ref:`g.118`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.302`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.347`, :ref:`g.351`, :ref:`g.353`, :ref:`g.358`, :ref:`g.361`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.432`, :ref:`g.433`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.456`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.509`, :ref:`g.525`, :ref:`g.526`, :ref:`g.553`, :ref:`g.555`, :ref:`g.568`, :ref:`g.569`, :ref:`g.570`, :ref:`g.571`, :ref:`g.572`, :ref:`g.573`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.558`, :ref:`g.563`
