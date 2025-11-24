:order: 504
:original_id: XI.18
:type: prop
:dependencies: g.19, g.39, g.492, g.487, g.503

.. _g.504:

G.504
=====

**Heath ID:** :ref:`XI.18`

   If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

For let any straight line AB be at right angles to the plane of reference; I say that all the planes through AB are also at right angles to the plane of reference.

For let the plane DE be drawn through AB, let CE be the common section of the plane DE and the plane of reference, let a point F be taken at random on CE, and from F let FG be drawn in the plane DE at right angles to CE. [:ref:`g.19`]

Now, since AB is at right angles to the plane of reference, AB is also at right angles to all the straight lines which meet it and are in the plane of reference; [:ref:`g.487`] so that it is also at right angles to CE; therefore the angle ABF is right.

But the angle GFB is also right; therefore AB is parallel to FG. [:ref:`g.39`]

But AB is at right angles to the plane of reference; therefore FG is also at right angles to the plane of reference. [:ref:`g.492`]

Now a plane is at right angles to a plane, when the straight lines drawn, in one of the planes, at right angles to the common section of the planes are at right angles to the remaining plane. [:ref:`g.503`]

And FG, drawn in one of the planes DE at right angles to CE, the common section of the planes, was proved to be at right angles to the plane of reference; therefore the plane DE is at right angles to the plane of reference.

Similarly also it can be proved that all the planes through AB are at right angles to the plane of reference.

Therefore etc. Q. E. D.


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
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.503" [label="G.503", style="rounded,filled", fillcolor=orange, URL="/elements2/g.503/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.492" [label="G.492", URL="/elements2/g.492/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.39" [label="G.39", URL="/elements2/g.39/", target="_top"];
     "G.491" [label="G.491", URL="/elements2/g.491/", target="_top"];
     "G.488" [label="G.488", URL="/elements2/g.488/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.504" [label="G.504", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.504/", target="_top"];
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
     "G.25" -> "G.24";
     "G.39" -> "G.24";
     "G.42" -> "G.24";
     "G.488" -> "G.24";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.488" -> "G.15";
     "G.504" -> "G.503";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.504" -> "G.492";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.492" -> "G.42";
     "G.42" -> "G.40";
     "G.39" -> "G.38";
     "G.504" -> "G.39";
     "G.492" -> "G.491";
     "G.492" -> "G.488";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.39" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.488" -> "G.487";
     "G.492" -> "G.487";
     "G.504" -> "G.487";
     "G.38" -> "G.37";
     "G.491" -> "G.486";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.504" -> "G.19";
     "G.488" -> "G.36";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.8";
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

:ref:`g.553`, :ref:`g.555`
