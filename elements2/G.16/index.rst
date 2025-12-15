:order: 16
:original_id: I.9
:type: prop
:dependencies: G.9, G.15

.. _G.16:

G.16
====

**Heath ID:** :ref:`I.9`

   To bisect a given rectilineal angle.

Let the angle ``BAC`` be the given rectilineal angle.

Thus it is required to bisect it.

Let a point ``D`` be taken at random on ``AB``; let ``AE`` be cut off from ``AC`` equal to ``AD``; [:ref:`G.9`] let ``DE`` be joined, and on ``DE`` let the equilateral triangle ``DEF`` be constructed; let ``AF`` be joined. 

I say that the angle ``BAC`` has been bisected by the straight line ``AF``.

For, since ``AD`` is equal to ``AE``, and ``AF`` is common, the two sides ``DA``, ``AF`` are equal to the two sides ``EA``, ``AF`` respectively.

And the base ``DF`` is equal to the base ``EF``; therefore the angle ``DAF`` is equal to the angle ``EAF``. [:ref:`G.15`]

Therefore the given rectilineal angle ``BAC`` has been bisected by the straight line ``AF``.


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
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.16" [label="G.16", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.16/", target="_top"];
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
     "G.16" -> "G.15";
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
     "G.16" -> "G.9";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }



Required for
------------

:ref:`G.17`, :ref:`G.20`, :ref:`G.25`, :ref:`G.26`, :ref:`G.27`, :ref:`G.28`, :ref:`G.30`, :ref:`G.31`, :ref:`G.32`, :ref:`G.34`, :ref:`G.35`, :ref:`G.36`, :ref:`G.38`, :ref:`G.39`, :ref:`G.44`, :ref:`G.45`, :ref:`G.46`, :ref:`G.47`, :ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
