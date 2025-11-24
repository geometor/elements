:order: 25
:original_id: I.16
:type: prop
:dependencies: g.17, g.24, g.9, g.11, g.3, g.7

.. _g.25:

G.25
====

**Heath ID:** :ref:`I.16`

   In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

Let ``ABC`` be a triangle, and let one side of it ``BC`` be produced to ``D``; 

I say that the exterior angle ``ACD`` is greater than either of the interior and opposite angles ``CBA``, ``BAC``.

Let ``AC`` be bisected at ``E`` [:ref:`g.17`], and let ``BE`` be joined and produced in a straight line to ``F``; 

let ``EF`` be made equal to ``BE``[:ref:`g.9`], let ``FC`` be joined [:ref:`g.3`], and let ``AC`` be drawn through to ``G`` [:ref:`g.7`].

Then, since ``AE`` is equal to ``EC``, and ``BE`` to ``EF``, the two sides ``AE``, ``EB`` are equal to the two sides ``CE``, ``EF`` respectively; and the angle ``AEB`` is equal to the angle ``FEC``, for they are vertical angles. [:ref:`g.24`] Therefore the base ``AB`` is equal to the base ``FC``, and the triangle ``ABE`` is equal to the triangle ``CFE``, and the remaining angles are equal to the remaining angles respectively, namely those which the equal sides subtend; [:ref:`g.11`] therefore the angle ``BAE`` is equal to the angle ``ECF``.
        

But the angle ``ECD`` is greater than the angle ``ECF``; [C. N. 5] therefore the angle ``ACD`` is greater than the angle ``BAE``.

Similarly also, if ``BC`` be bisected, the angle ``BCG``, that is, the angle ``ACD`` [:ref:`g.24`], can be proved greater than the angle ``ABC`` as well.

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
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.25" [label="G.25", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.24" -> "G.21";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.26`, :ref:`g.27`, :ref:`g.28`, :ref:`g.30`, :ref:`g.31`, :ref:`g.32`, :ref:`g.34`, :ref:`g.35`, :ref:`g.36`, :ref:`g.38`, :ref:`g.39`, :ref:`g.44`, :ref:`g.45`, :ref:`g.46`, :ref:`g.47`, :ref:`g.48`, :ref:`g.49`, :ref:`g.50`, :ref:`g.51`, :ref:`g.52`, :ref:`g.53`, :ref:`g.54`, :ref:`g.55`, :ref:`g.56`, :ref:`g.57`, :ref:`g.58`, :ref:`g.59`, :ref:`g.60`, :ref:`g.61`, :ref:`g.62`, :ref:`g.71`, :ref:`g.72`, :ref:`g.73`, :ref:`g.74`, :ref:`g.75`, :ref:`g.63`, :ref:`g.64`, :ref:`g.65`, :ref:`g.66`, :ref:`g.67`, :ref:`g.68`, :ref:`g.69`, :ref:`g.70`, :ref:`g.88`, :ref:`g.90`, :ref:`g.92`, :ref:`g.94`, :ref:`g.95`, :ref:`g.98`, :ref:`g.99`, :ref:`g.77`, :ref:`g.100`, :ref:`g.101`, :ref:`g.102`, :ref:`g.104`, :ref:`g.108`, :ref:`g.110`, :ref:`g.78`, :ref:`g.112`, :ref:`g.113`, :ref:`g.114`, :ref:`g.115`, :ref:`g.116`, :ref:`g.117`, :ref:`g.118`, :ref:`g.79`, :ref:`g.82`, :ref:`g.83`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.122`, :ref:`g.135`, :ref:`g.120`, :ref:`g.121`, :ref:`g.124`, :ref:`g.125`, :ref:`g.127`, :ref:`g.128`, :ref:`g.129`, :ref:`g.302`, :ref:`g.167`, :ref:`g.177`, :ref:`g.178`, :ref:`g.179`, :ref:`g.181`, :ref:`g.182`, :ref:`g.183`, :ref:`g.184`, :ref:`g.185`, :ref:`g.186`, :ref:`g.189`, :ref:`g.168`, :ref:`g.191`, :ref:`g.194`, :ref:`g.195`, :ref:`g.196`, :ref:`g.197`, :ref:`g.198`, :ref:`g.199`, :ref:`g.200`, :ref:`g.201`, :ref:`g.169`, :ref:`g.202`, :ref:`g.203`, :ref:`g.204`, :ref:`g.205`, :ref:`g.170`, :ref:`g.171`, :ref:`g.172`, :ref:`g.173`, :ref:`g.175`, :ref:`g.176`, :ref:`g.258`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.483`, :ref:`g.347`, :ref:`g.348`, :ref:`g.351`, :ref:`g.353`, :ref:`g.355`, :ref:`g.356`, :ref:`g.357`, :ref:`g.358`, :ref:`g.361`, :ref:`g.363`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.432`, :ref:`g.433`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.456`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.494`, :ref:`g.495`, :ref:`g.496`, :ref:`g.499`, :ref:`g.500`, :ref:`g.502`, :ref:`g.504`, :ref:`g.506`, :ref:`g.507`, :ref:`g.508`, :ref:`g.509`, :ref:`g.510`, :ref:`g.511`, :ref:`g.512`, :ref:`g.514`, :ref:`g.516`, :ref:`g.518`, :ref:`g.519`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.525`, :ref:`g.526`, :ref:`g.527`, :ref:`g.528`, :ref:`g.529`, :ref:`g.488`, :ref:`g.489`, :ref:`g.490`, :ref:`g.492`, :ref:`g.493`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.549`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.557`, :ref:`g.568`, :ref:`g.569`, :ref:`g.570`, :ref:`g.571`, :ref:`g.572`, :ref:`g.573`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.558`, :ref:`g.560`, :ref:`g.562`, :ref:`g.563`, :ref:`g.565`, :ref:`g.567`
