:order: 25
:original_id: I.16
:type: prop
:dependencies: G.17, G.24, G.9, G.11, G.3, G.7
:excerpt: In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

**Heath ID:** `I.16 <https://geometor.github.io/euclid/I/16/>`_

.. picture:: G.25.png

.. _G.25:

G.25
====

    In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

Let ``ABC`` be a triangle, and let one side of it ``BC`` be produced to ``D``; 

I say that the exterior angle ``ACD`` is greater than either of the interior and opposite angles ``CBA``, ``BAC``.

Let ``AC`` be bisected at ``E`` [:ref:`G.17`], and let ``BE`` be joined and produced in a straight line to ``F``; 

let ``EF`` be made equal to ``BE``[:ref:`G.9`], let ``FC`` be joined [:ref:`G.3`], and let ``AC`` be drawn through to ``G`` [:ref:`G.7`].

Then, since ``AE`` is equal to ``EC``, and ``BE`` to ``EF``, the two sides ``AE``, ``EB`` are equal to the two sides ``CE``, ``EF`` respectively; and the angle ``AEB`` is equal to the angle ``FEC``, for they are vertical angles. [:ref:`G.24`] Therefore the base ``AB`` is equal to the base ``FC``, and the triangle ``ABE`` is equal to the triangle ``CFE``, and the remaining angles are equal to the remaining angles respectively, namely those which the equal sides subtend; [:ref:`G.11`] therefore the angle ``BAE`` is equal to the angle ``ECF``.
        

But the angle ``ECD`` is greater than the angle ``ECF``; [C. N. 5] therefore the angle ``ACD`` is greater than the angle ``BAE``.

Similarly also, if ``BC`` be bisected, the angle ``BCG``, that is, the angle ``ACD`` [:ref:`G.24`], can be proved greater than the angle ``ABC`` as well.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. the exterior angle,**

   

   literally the outside angle,

    ἡ ἐκτὸς γωνία.


.. note::


   **2. the interior and opposite angles,**

   

   τῶν ἐντὸς καὶ ἀπεναντίον γωνιῶν.


.. note::


   **12. let AC be drawn through to G.**

   

   The word is διήχθω, a variation on the more usual ἐκβεβλήσθω, let it be ``produced``.


.. note::


   **21. CFE,**

   

   in the text ``FEC``.


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
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.25" [label="G.25", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.25/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.24" -> "G.6";
     "G.8" -> "G.6";
     "G.21" -> "G.19";
     "G.25" -> "G.24";
     "G.24" -> "G.21";
     "G.11" -> "G.10";
     "G.25" -> "G.7";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.17";
     "G.5" -> "G.3";
     "G.25" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.15";
     "G.16" -> "G.15";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.5" -> "G.1";
     "G.24" -> "G.1";
     "G.8" -> "G.1";
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
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.25" -> "G.11";
     "G.17" -> "G.11";
     "G.12" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.17" -> "G.16";
   }



Required for
------------

:ref:`G.26`, :ref:`G.27`, :ref:`G.28`, :ref:`G.30`, :ref:`G.31`, :ref:`G.32`, :ref:`G.34`, :ref:`G.35`, :ref:`G.36`, :ref:`G.38`, :ref:`G.39`, :ref:`G.44`, :ref:`G.45`, :ref:`G.46`, :ref:`G.47`, :ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
