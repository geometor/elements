:order: 31
:original_id: I.21
:type: prop
:dependencies: g.25, g.30

.. _g.31:

G.31
====

**Heath ID:** :ref:`I.21`

   If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greater angle.

On ``BC``, one of the sides of the triangle ``ABC``, from its extremities ``B``, ``C``, let the two straight lines ``BD``, ``DC`` be constructed meeting within the triangle;

I say that ``BD``, ``DC`` are less than the remaining two sides of the triangle ``BA``, ``AC``, but contain an angle ``BDC`` greater than the angle ``BAC``. 

For let ``BD`` be drawn through to ``E``.

Then, since in any triangle two sides are greater than the remaining one, [:ref:`g.30`] therefore, in the triangle ``ABE``, the two sides ``AB``, ``AE`` are greater than ``BE``.

Let ``EC`` be added to each; therefore ``BA``, ``AC`` are greater than ``BE``, ``EC``.
        

Again, since, in the triangle ``CED``, the two sides ``CE``, ``ED`` are greater than ``CD``, let ``DB`` be added to each; therefore ``CE``, ``EB`` are greater than ``CD``, ``DB``.

But ``BA``, ``AC`` were proved greater than ``BE``, ``EC``; therefore ``BA``, ``AC`` are much greater than ``BD``, ``DC``.

Again, since in any triangle the exterior angle is greater than the interior and opposite angle, [:ref:`g.25`] therefore, in the triangle ``CDE``, the exterior angle ``BDC`` is greater than the angle ``CED``.
        

For the same reason, moreover, in the triangle ``ABE`` also, the exterior angle ``CEB`` is greater than the angle ``BAC``. But the angle ``BDC`` was proved greater than the angle ``CEB``; therefore the angle ``BDC`` is much greater than the angle ``BAC``.
        

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **2. be constructed...meeting within the triangle.**

   

   The word meeting

    is not in the Greek, where the words are ἐντὸς συσταθῶσιν. συνίστασθαι is the word used of constructing two straight lines ``to a point`` (cf. :ref:`g.14`) or so as to form a triangle; but it is necessary in English to indicate that they ``meet``.


.. note::


   **3. the straight lines so constructed.**

   

   Observe the elegant brevity of the Greek αἱ συσταθεῖσαι.


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
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.30" [label="G.30", URL="/elements2/g.30/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.31" [label="G.31", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.31/", target="_top"];
     "G.29" [label="G.29", style="rounded,filled", fillcolor=orange, URL="/elements2/g.29/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.28" -> "G.27";
     "G.24" -> "G.21";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.15" -> "G.14";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.31" -> "G.30";
     "G.30" -> "G.28";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.27" -> "G.25";
     "G.31" -> "G.25";
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
     "G.30" -> "G.29";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.30" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.83`
