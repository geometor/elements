:order: 495
:original_id: XI.11
:type: prop
:dependencies: g.19, g.20, g.44, g.488, g.492, g.487

.. _g.495:

G.495
=====

**Heath ID:** :ref:`XI.11`

   From a given elevated point to draw a straight line perpendicular to a given plane.

Let A be the given elevated point, and the plane of reference the given plane; thus it is required to draw from the point A a straight line perpendicular to the plane of reference.

Let any straight line BC be drawn, at random, in the plane of reference, and let AD be drawn from the point A perpendicular to BC. [:ref:`g.20`]

If then AD is also perpendicular to the plane of reference, that which was enjoined will have been done.

But, if not, let DE be drawn from the point D at right angles to BC and in the plane of reference, [:ref:`g.19`] let AF be drawn from A perpendicular to DE, [:ref:`g.20`] and let GH be drawn through the point F parallel to BC. [:ref:`g.44`]

Now, since BC is at right angles to each of the straight lines DA, DE, therefore BC is also at right angles to the plane through ED, DA. [:ref:`g.488`]

And GH is parallel to it; but, if two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane; [:ref:`g.492`] therefore GH is also at right angles to the plane through ED, DA.

Therefore GH is also at right angles to all the straight lines which meet it and are in the plane through ED, DA. [:ref:`g.487`]

But AF meets it and is in the plane through ED, DA; therefore GH is at right angles to FA, so that FA is also at right angles to GH.

But AF is also at right angles to DE; therefore AF is at right angles to each of the straight lines GH, DE.

But, if a straight line be set up at right angles to two straight lines which cut one another, at the point of section, it will also be at right angles to the plane through them; [:ref:`g.488`] therefore FA is at right angles to the plane through ED, GH.

But the plane through ED, GH is the plane of reference; therefore AF is at right angles to the plane of reference.

Therefore from the given elevated point A the straight line AF has been drawn perpendicular to the plane of reference. Q. E. F.


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
     "G.20" [label="G.20", URL="/elements2/g.20/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.492" [label="G.492", URL="/elements2/g.492/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.495" [label="G.495", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.495/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.488" [label="G.488", URL="/elements2/g.488/", target="_top"];
     "G.491" [label="G.491", URL="/elements2/g.491/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.487" [label="G.487", style="rounded,filled", fillcolor=orange, URL="/elements2/g.487/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.486" [label="G.486", style="rounded,filled", fillcolor=orange, URL="/elements2/g.486/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.484" [label="G.484", style="rounded,filled", fillcolor=orange, URL="/elements2/g.484/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.485" [label="G.485", URL="/elements2/g.485/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.20" -> "G.4";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.488" -> "G.24";
     "G.495" -> "G.20";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.20" -> "G.15";
     "G.33" -> "G.15";
     "G.488" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.495" -> "G.492";
     "G.19" -> "G.18";
     "G.20" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.20" -> "G.3";
     "G.25" -> "G.3";
     "G.495" -> "G.44";
     "G.492" -> "G.42";
     "G.42" -> "G.40";
     "G.44" -> "G.38";
     "G.492" -> "G.488";
     "G.495" -> "G.488";
     "G.492" -> "G.491";
     "G.20" -> "G.17";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.488" -> "G.487";
     "G.492" -> "G.487";
     "G.495" -> "G.487";
     "G.38" -> "G.37";
     "G.491" -> "G.486";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.495" -> "G.19";
     "G.488" -> "G.36";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.8";
     "G.44" -> "G.33";
     "G.485" -> "G.484";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.488" -> "G.11";
     "G.11" -> "G.10";
     "G.492" -> "G.485";
     "G.14" -> "G.12";
   }



Required for
------------

:ref:`g.496`, :ref:`g.500`, :ref:`g.509`, :ref:`g.512`, :ref:`g.553`, :ref:`g.555`, :ref:`g.571`, :ref:`g.572`, :ref:`g.578`
