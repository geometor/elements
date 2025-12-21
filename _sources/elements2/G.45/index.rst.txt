:order: 45
:original_id: I.32
:type: prop
:dependencies: G.21, G.42, G.44
:excerpt: In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

**Heath ID:** `I.32 <https://geometor.github.io/euclid/I/32/>`_

.. picture:: G.45.png

.. _G.45:

G.45
====

    In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

Let ``ABC`` be a triangle, and let one side of it ``BC`` be produced to ``D``;

I say that the exterior angle ``ACD`` is equal to the two interior and opposite angles ``CAB``, ``ABC``, and the three interior angles of the triangle ``ABC``, ``BCA``, ``CAB`` are equal to two right angles. 

For let ``CE`` be drawn through the point ``C`` parallel to the straight line ``AB``. [:ref:`G.44`]

Then, since ``AB`` is parallel to ``CE``, and ``AC`` has fallen upon them, the alternate angles ``BAC``, ``ACE`` are equal to one another. [:ref:`G.42`]
        

Again, since ``AB`` is parallel to ``CE``, and the straight line ``BD`` has fallen upon them, the exterior angle ``ECD`` is equal to the interior and opposite angle ``ABC``. [:ref:`G.42`]

But the angle ``ACE`` was also proved equal to the angle ``BAC``; therefore the whole angle ``ACD`` is equal to the two interior and opposite angles ``BAC``, ``ABC``.

Let the angle ``ACB`` be added to each; therefore the angles ``ACD``, ``ACB`` are equal to the three angles ``ABC``, ``BCA``, ``CAB``.

But the angles ``ACD``, ``ACB`` are equal to two right angles; [:ref:`G.21`] therefore the angles ``ABC``, ``BCA``, ``CAB`` are also equal to two right angles.

Therefore etc.


**Q. E. D.**


Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.44" [label="G.44", fillcolor="#222244", URL="/elements2/G.44/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.45" [label="G.45", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.45/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.45" -> "G.44";
     "G.24" -> "G.6";
     "G.8" -> "G.6";
     "G.21" -> "G.19";
     "G.44" -> "G.38";
     "G.24" -> "G.21";
     "G.45" -> "G.21";
     "G.42" -> "G.21";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.11" -> "G.10";
     "G.25" -> "G.7";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.45" -> "G.42";
     "G.5" -> "G.3";
     "G.25" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.15";
     "G.16" -> "G.15";
     "G.33" -> "G.15";
     "G.25" -> "G.17";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.42" -> "G.41";
     "G.5" -> "G.1";
     "G.24" -> "G.1";
     "G.8" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.14" -> "G.12";
     "G.24" -> "G.22";
     "G.15" -> "G.14";
     "G.9" -> "G.8";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.16" -> "G.9";
     "G.12" -> "G.9";
     "G.38" -> "G.25";
     "G.38" -> "G.37";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.25" -> "G.11";
     "G.17" -> "G.11";
     "G.12" -> "G.11";
     "G.42" -> "G.40";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.44" -> "G.33";
     "G.17" -> "G.16";
   }
