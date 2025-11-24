:order: 136
:original_id: IV.16
:type: prop
:dependencies: g.111

.. _g.136:

G.136
=====

**Heath ID:** :ref:`IV.16`

   In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular.

``In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular``.

Let ``ABCD`` be the given circle; thus it is required to inscribe in the circle ``ABCD`` a fifteenangled figure which shall be both equilateral and equiangular.

In the circle ``ABCD`` let there be inscribed a side ``AC`` of the equilateral triangle inscribed in it, and a side ``AB`` of an equilateral pentagon; therefore, of the equal segments of which there are fifteen in the circle ``ABCD``, there will be five in the circumference ``ABC`` which is one-third of the circle, and there will be three in the circumference ``AB`` which is one-fifth of the circle;


.. container:: center

   therefore in the remainder ``BC`` there will be two of the equal segments.


Let ``BC`` be bisected at ``E``; [:ref:`g.111`] therefore each of the circumferences ``BE``, ``EC`` is a fifteenth of the circle ``ABCD``.

If therefore we join ``BE``, ``EC`` and fit into the circle ``ABCD`` straight lines equal to them and in contiguity, a fifteen-angled figure which is both equilateral and equiangular will have been inscribed in it. Q. E. F.

And, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents to the circle, there will be circumscribed about the circle a fifteen-angled figure which is equilateral and equiangular.

And further, by proofs similar to those in the case of the pentagon, we can both inscribe a circle in the given fifteenangled figure and circumscribe one about it. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.111" [label="G.111", URL="/elements2/g.111/", target="_top"];
     "G.105" [label="G.105", URL="/elements2/g.105/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.109" [label="G.109", URL="/elements2/g.109/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.86" [label="G.86", URL="/elements2/g.86/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.136" [label="G.136", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.136/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.103" [label="G.103", style="rounded,filled", fillcolor=orange, URL="/elements2/g.103/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.107" [label="G.107", URL="/elements2/g.107/", target="_top"];
     "G.84" [label="G.84", style="rounded,filled", fillcolor=orange, URL="/elements2/g.84/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.80" [label="G.80", URL="/elements2/g.80/", target="_top"];
     "G.136" -> "G.111";
     "G.107" -> "G.105";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.111" -> "G.109";
     "G.15" -> "G.14";
     "G.105" -> "G.86";
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.80" -> "G.2";
     "G.86" -> "G.2";
     "G.8" -> "G.6";
     "G.105" -> "G.15";
     "G.109" -> "G.15";
     "G.8" -> "G.5";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.107" -> "G.103";
     "G.12" -> "G.11";
     "G.107" -> "G.11";
     "G.111" -> "G.11";
     "G.11" -> "G.10";
     "G.109" -> "G.107";
     "G.86" -> "G.84";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.86" -> "G.80";
   }
