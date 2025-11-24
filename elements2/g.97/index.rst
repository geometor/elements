:order: 97
:original_id: III.17
:type: prop
:dependencies: g.11, g.76, g.96

.. _g.97:

G.97
====

**Heath ID:** :ref:`III.17`

   From a given point to draw a straight line touching a given circle.

Let ``A`` be the given point, and ``BCD`` the given circle; thus it is required to draw from the point ``A`` a straight line touching the circle ``BCD``.

For let the centre ``E`` of the circle be taken; [:ref:`g.76`] let ``AE`` be joined, and with centre ``E`` and distance ``EA`` let the circle ``AFG`` be described;

from ``D`` let ``DF`` be drawn at right angles to ``EA``, and let ``EF``, ``AB`` be joined; I say that ``AB`` has been drawn from the point ``A`` touching the circle ``BCD``.

For, since ``E`` is the centre of the circles ``BCD``, ``AFG``,


.. container:: center

   ``EA`` is equal to ``EF``, and ``ED`` to ``EB``;


therefore the two sides ``AE``, ``EB`` are equal to the two sides ``FE``, ``ED``: and they contain a common angle, the angle at ``E``;


.. container:: center

   therefore the base ``DF`` is equal to the base ``AB``, and the triangle ``DEF`` is equal to the triangle ``BEA``, and the remaining angles to the remaining angles; [:ref:`g.11`] therefore the angle ``EDF`` is equal to the angle ``EBA``.


But the angle ``EDF`` is right;


.. container:: center

   therefore the angle ``EBA`` is also right.


Now ``EB`` is a radius; and the straight line drawn at right angles to the diameter of a circle, from its extremity, touches the circle; [:ref:`g.96`]


.. container:: center

   therefore ``AB`` touches the circle ``BCD``.


Therefore from the given point ``A`` the straight line ``AB`` has been drawn touching the circle ``BCD``.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.76" [label="G.76", URL="/elements2/g.76/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.96" [label="G.96", style="rounded,filled", fillcolor=orange, URL="/elements2/g.96/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.97" [label="G.97", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.97/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.97" -> "G.76";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.76" -> "G.15";
     "G.97" -> "G.96";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.5";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.76" -> "G.18";
     "G.12" -> "G.11";
     "G.97" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }
