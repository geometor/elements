:order: 497
:original_id: XI.13
:type: prop
:dependencies: g.486, g.487

.. _g.497:

G.497
=====

**Heath ID:** :ref:`XI.13`

   From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

For, if possible, from the same point A let the two straight lines AB, AC be set up at right angles to the plane of reference and on the same side, and let a plane be drawn through BA, AC; it will then make, as section through A in the plane of reference, a straight line. [:ref:`g.486`]

Let it make DAE; therefore the straight lines AB, AC, DAE are in one plane.

And, since CA is at right angles to the plane of reference, it will also make right angles with all the straight lines which meet it and are in the plane of reference. [:ref:`g.487`]

But DAE meets it and is in the plane of reference; therefore the angle CAE is right.

For the same reason the angle BAE is also right; therefore the angle CAE is equal to the angle BAE.

And they are in one plane: which is impossible.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.497" [label="G.497", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.497/", target="_top"];
     "G.487" [label="G.487", style="rounded,filled", fillcolor=orange, URL="/elements2/g.487/", target="_top"];
     "G.486" [label="G.486", style="rounded,filled", fillcolor=orange, URL="/elements2/g.486/", target="_top"];
     "G.497" -> "G.487";
     "G.497" -> "G.486";
   }



Required for
------------

:ref:`g.505`
