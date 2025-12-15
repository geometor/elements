:order: 59
:original_id: I.46
:type: prop
:dependencies: G.19, G.42, G.44, G.47

.. _G.59:

G.59
====

**Heath ID:** :ref:`I.46`

   On a given straight line to describe a square.

Let ``AB`` be the given straight line; thus it is required to describe a square on the straight line ``AB``. 
        

Let ``AC`` be drawn at right angles to the straight line ``AB`` from the point ``A`` on it [:ref:`G.19`], and let ``AD`` be made equal to ``AB``; through the point ``D`` let ``DE`` be drawn parallel to ``AB``, and through the point ``B`` let ``BE`` be drawn parallel to ``AD``. [:ref:`G.44`] 

Therefore ``ADEB`` is a parallelogram; therefore ``AB`` is equal to ``DE``, and ``AD`` to ``BE``. [:ref:`G.47`]

But ``AB`` is equal to ``AD``; therefore the four straight lines ``BA``, ``AD``, ``DE``, ``EB`` are equal to one another; therefore the parallelogram ``ADEB`` is equilateral.

I say next that it is also right-angled.

For, since the straight line ``AD`` falls upon the parallels ``AB``, ``DE``, the angles ``BAD``, ``ADE`` are equal to two right angles. [:ref:`G.42`]

But the angle ``BAD`` is right; therefore the angle ``ADE`` is also right.

And in parallelogrammic areas the opposite sides and angles are equal to one another; [:ref:`G.47`] therefore each of the opposite angles ``ABE``, ``BED`` is also right. Therefore ``ADEB`` is right-angled.

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
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.59" [label="G.59", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.59/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
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
     "G.47" [label="G.47", fillcolor="#222244", URL="/elements2/G.47/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.44" [label="G.44", fillcolor="#222244", URL="/elements2/G.44/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.44" -> "G.33";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.44" -> "G.38";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.21" -> "G.19";
     "G.59" -> "G.19";
     "G.9" -> "G.8";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.42" -> "G.41";
     "G.38" -> "G.37";
     "G.25" -> "G.17";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.47" -> "G.42";
     "G.59" -> "G.42";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
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
     "G.33" -> "G.15";
     "G.15" -> "G.14";
     "G.47" -> "G.36";
     "G.59" -> "G.47";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.14" -> "G.12";
     "G.59" -> "G.44";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
   }



Required for
------------

:ref:`G.60`, :ref:`G.61`
