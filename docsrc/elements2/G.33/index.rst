:order: 33
:original_id: I.23
:type: prop
:dependencies: G.15

.. _G.33:

G.33
====

**Heath ID:** :ref:`I.23`

   On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

Let ``AB`` be the given straight line, ``A`` the point on it, and the angle ``DCE`` the given rectilineal angle;

thus it is required to construct on the given straight line ``AB``, and at the point ``A`` on it, a rectilineal angle equal to the given rectilineal angle ``DCE``. 

On the straight lines ``CD``, ``CE`` respectively let the points ``D``, ``E`` be taken at random; let ``DE`` be joined, and out of three straight lines which are equal to the three straight lines ``CD``, ``DE``, ``CE`` let the triangle ``AFG`` be constructed in such a way that ``CD`` is equal to ``AF``, ``CE`` to ``AG``, and further ``DE`` to ``FG``.

Then, since the two sides ``DC``, ``CE`` are equal to the two sides ``FA``, ``AG`` respectively, and the base ``DE`` is equal to the base ``FG``, the angle ``DCE`` is equal to the angle ``FAG``. [:ref:`G.15`]

Therefore on the given straight line ``AB``, and at the point ``A`` on it, the rectilineal angle ``FAG`` has been constructed equal to the given rectilineal angle ``DCE``.


**Q. E. D.**


Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.33" [label="G.33", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.33/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.8" -> "G.5";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.12" -> "G.11";
     "G.11" -> "G.10";
     "G.33" -> "G.15";
     "G.8" -> "G.6";
     "G.15" -> "G.14";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.14" -> "G.12";
     "G.12" -> "G.9";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }



Required for
------------

:ref:`G.34`, :ref:`G.35`, :ref:`G.44`, :ref:`G.45`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
