:order: 48
:original_id: I.35
:type: prop
:dependencies: G.42, G.47, G.11, G.1, G.40, G.6
:excerpt: Parallelograms which are on the same base and in the same parallels are equal to one another.

**Heath ID:** `I.35 <https://geometor.github.io/euclid/I/35/>`_

.. picture:: G.48.png

.. _G.48:

G.48
====

    Parallelograms which are on the same base and in the same parallels are equal to one another.

Let ``ABCD``, ``EBCF`` be parallelograms on the same base ``BC`` and in the same parallels ``AF``, ``BC``; I say that ``ABCD`` is equal to the parallelogram ``EBCF``.

For, since ``ABCD`` is a parallelogram, ``AD`` is equal to ``BC``. [:ref:`G.47`]
        

For the same reason also ``EF`` is equal to ``BC``, so that ``AD`` is also equal to ``EF``; [:ref:`G.1`] and ``DE`` is common; therefore the whole ``AE`` is equal to the whole ``DF``. [:ref:`G.40`]

But ``AB`` is also equal to ``DC``; [:ref:`G.47`] therefore the two sides ``EA``, ``AB`` are equal to the two sides ``FD``, ``DC`` respectively, 
        and the angle ``FDC`` is equal to the angle ``EAB``, the exterior to the interior; [:ref:`G.42`] therefore the base ``EB`` is equal to the base ``FC``, and the triangle ``EAB`` will be equal to the triangle ``FDC``. [:ref:`G.11`]

Let ``DGE`` be subtracted from each; therefore the trapezium ``ABGD`` which remains is equal to the trapezium ``EGCF`` which remains. [:ref:`G.6`] 

Let the triangle ``GBC`` be added to each; therefore the whole parallelogram ``ABCD`` is equal to the whole parallelogram ``EBCF``. [:ref:`G.40`]

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **21. FDC.**

   

   The text has ``DFC``.


.. note::


   **22. Let DGE be subtracted.**

   

   Euclid speaks of the triangle ``DGE`` without any explanation that, in the case which he takes (where ``AD``, ``EF`` have no point in common), ``BE``, ``CD`` must meet at a point ``G`` between the two parallels. He allows this to appear from the figure simply.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.48" [label="G.48", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.48/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.36" [label="G.36", fillcolor="#222244", URL="/elements2/G.36/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.47" [label="G.47", fillcolor="#222244", URL="/elements2/G.47/", target="_top"];
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.8" -> "G.6";
     "G.21" -> "G.19";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.11" -> "G.10";
     "G.25" -> "G.7";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.25" -> "G.17";
     "G.19" -> "G.15";
     "G.16" -> "G.15";
     "G.5" -> "G.3";
     "G.25" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.42" -> "G.41";
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
     "G.15" -> "G.14";
     "G.9" -> "G.8";
     "G.47" -> "G.36";
     "G.36" -> "G.25";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.16" -> "G.9";
     "G.12" -> "G.9";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.25" -> "G.11";
     "G.17" -> "G.11";
     "G.12" -> "G.11";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.42" -> "G.40";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.17" -> "G.16";
     "G.48" -> "G.47";
   }



Required for
------------

:ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.57`, :ref:`G.58`, :ref:`G.60`, :ref:`G.61`
