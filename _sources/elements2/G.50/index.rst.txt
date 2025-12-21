:order: 50
:original_id: I.37
:type: prop
:dependencies: G.44, G.47, G.48
:excerpt: Triangles which are on the same base and in the same parallels are equal to one another.

**Heath ID:** `I.37 <https://geometor.github.io/euclid/I/37/>`_

.. picture:: G.50.png

.. _G.50:

G.50
====

    Triangles which are on the same base and in the same parallels are equal to one another.

Let ``ABC``, ``DBC`` be triangles on the same base ``BC`` and in the same parallels ``AD``, ``BC``; I say that the triangle ``ABC`` is equal to the triangle ``DBC``.

Let ``AD`` be produced in both directions to ``E``, ``F``; through ``B`` let ``BE`` be drawn parallel to ``CA``, [:ref:`G.44`] and through ``C`` let ``CF`` be drawn parallel to ``BD``. [:ref:`G.44`] 

Then each of the figures ``EBCA``, ``DBCF`` is a parallelogram; and they are equal, 

for they are on the same base ``BC`` and in the same parallels ``BC``, ``EF``. [:ref:`G.48`]

Moreover the triangle ``ABC`` is half of the parallelogram ``EBCA``; for the diameter ``AB`` bisects it. [:ref:`G.47`]

And the triangle ``DBC`` is half of the parallelogram ``DBCF``; for the diameter ``DC`` bisects it. [:ref:`G.47`]

[But the halves of equal things are equal to one another.]

Therefore the triangle ``ABC`` is equal to the triangle ``DBC``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **21**

   

   Here and in the next proposition Heiberg brackets the words But the halves of equal things are equal to one another

    on the ground that, since the Common Notion which asserted this fact was interpolated at a very early date (before the time of Theon), it is probable that the words here were interpolated at the same time. Cf. note above (p. 224) on the interpolated Common Notion.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.50" [label="G.50", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.50/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.48" [label="G.48", fillcolor="#222244", URL="/elements2/G.48/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.36" [label="G.36", fillcolor="#222244", URL="/elements2/G.36/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.44" [label="G.44", fillcolor="#222244", URL="/elements2/G.44/", target="_top"];
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.47" [label="G.47", fillcolor="#222244", URL="/elements2/G.47/", target="_top"];
     "G.21" -> "G.19";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.11" -> "G.10";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.25" -> "G.17";
     "G.19" -> "G.15";
     "G.16" -> "G.15";
     "G.33" -> "G.15";
     "G.5" -> "G.3";
     "G.25" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.5" -> "G.1";
     "G.24" -> "G.1";
     "G.48" -> "G.1";
     "G.8" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.14" -> "G.12";
     "G.24" -> "G.22";
     "G.9" -> "G.8";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.42" -> "G.40";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.17" -> "G.16";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.8" -> "G.6";
     "G.44" -> "G.38";
     "G.50" -> "G.48";
     "G.25" -> "G.7";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.42" -> "G.41";
     "G.15" -> "G.14";
     "G.47" -> "G.36";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.16" -> "G.9";
     "G.12" -> "G.9";
     "G.38" -> "G.37";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.25" -> "G.11";
     "G.17" -> "G.11";
     "G.12" -> "G.11";
     "G.50" -> "G.44";
     "G.44" -> "G.33";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
   }



Required for
------------

:ref:`G.52`, :ref:`G.54`, :ref:`G.55`, :ref:`G.57`, :ref:`G.58`, :ref:`G.60`, :ref:`G.61`
