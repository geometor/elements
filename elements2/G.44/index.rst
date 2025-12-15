:order: 44
:original_id: I.31
:type: prop
:dependencies: G.33, G.38

.. _G.44:

G.44
====

**Heath ID:** :ref:`I.31`

   Through a given point to draw a straight line parallel to a given straight line.

Let ``A`` be the given point, and ``BC`` the given straight line; thus it is required to draw through the point ``A`` a straight line parallel to the straight line ``BC``. 

Let a point ``D`` be taken at random on ``BC``, and let ``AD`` be joined; on the straight line ``DA``, and at the point ``A`` on it, let the angle ``DAE`` be constructed equal to the angle ``ADC`` [:ref:`G.33`]; and let the straight line ``AF`` be produced in a straight line with ``EA``. 

Then, since the straight line ``AD`` falling on the two straight lines ``BC``, ``EF`` has made the alternate angles ``EAD``, ``ADC`` equal to one another, therefore ``EAF`` is parallel to ``BC``. [:ref:`G.38`]

Therefore through the given point ``A`` the straight line ``EAF`` has been drawn parallel to the given straight line ``BC``.


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
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.44" [label="G.44", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.44/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.44" -> "G.33";
     "G.25" -> "G.24";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.44" -> "G.38";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.21" -> "G.19";
     "G.9" -> "G.8";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.38" -> "G.37";
     "G.25" -> "G.17";
     "G.38" -> "G.25";
     "G.17" -> "G.16";
     "G.24" -> "G.21";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.15" -> "G.14";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.14" -> "G.12";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`G.45`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
