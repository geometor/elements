:order: 505
:original_id: XI.19
:type: prop
:dependencies: g.497, g.503

.. _g.505:

G.505
=====

**Heath ID:** :ref:`XI.19`

   If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

For let the two planes AB, BC be at right angles to the plane of reference, and let BD be their common section; I say that BD is at right angles to the plane of reference.

For suppose it is not, and from the point D let DE be drawn in the plane AB at right angles to the straight line AD, and DF in the plane BC at right angles to CD.

Now, since the plane AB is at right angles to the plane of reference, and DE has been drawn in the plane AB at right angles to AD, their common section, therefore DE is at right angles to the plane of reference. [:ref:`g.503`]

Similarly we can prove that DF is also at right angles to the plane of reference.

Therefore from the same point D two straight lines have been set up at right angles to the plane of reference on the same side: which is impossible. [:ref:`g.497`]

Therefore no straight line except the common section DB of the planes AB, BC can be set up from the point D at right angles to the plane of reference.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.487" [label="G.487", style="rounded,filled", fillcolor=orange, URL="/elements2/g.487/", target="_top"];
     "G.486" [label="G.486", style="rounded,filled", fillcolor=orange, URL="/elements2/g.486/", target="_top"];
     "G.497" [label="G.497", URL="/elements2/g.497/", target="_top"];
     "G.503" [label="G.503", style="rounded,filled", fillcolor=orange, URL="/elements2/g.503/", target="_top"];
     "G.505" [label="G.505", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.505/", target="_top"];
     "G.497" -> "G.487";
     "G.497" -> "G.486";
     "G.505" -> "G.497";
     "G.505" -> "G.503";
   }
