:order: 130
:original_id: IV.9
:type: prop
:dependencies: g.13, g.15

.. _g.130:

G.130
=====

**Heath ID:** :ref:`IV.9`

   About a given square to circumscribe a circle.

Let ``ABCD`` be the given square; thus it is required to circumscribe a circle about the square ``ABCD``.

For let ``AC``, ``BD`` be joined, and let them cut one another at ``E``.

Then, since ``DA`` is equal to ``AB``, and ``AC`` is common, therefore the two sides ``DA``, ``AC`` are equal to the two sides ``BA``, ``AC``; and the base ``DC`` is equal to the base ``BC``;


.. container:: center

   therefore the angle ``DAC`` is equal to the angle ``BAC``. [:ref:`g.15`]


Therefore the angle ``DAB`` is bisected by ``AC``.

Similarly we can prove that each of the angles ``ABC``, ``BCD``, ``CDA`` is bisected by the straight lines ``AC``, ``DB``.

Now, since the angle ``DAB`` is equal to the angle ``ABC``, and the angle ``EAB`` is half the angle ``DAB``, and the angle ``EBA`` half the angle ``ABC``, therefore the angle ``EAB`` is also equal to the angle ``EBA``; so that the side ``EA`` is also equal to ``EB``. [:ref:`g.13`]

Similarly we can prove that each of the straight lines ``EA``, ``EB`` is equal to each of the straight lines ``EC``, ``ED``.

Therefore the four straight lines ``EA``, ``EB``, ``EC``, ``ED`` are equal to one another.

Therefore the circle described with centre ``E`` and distance one of the straight lines ``EA``, ``EB``, ``EC``, ``ED`` will pass also through the remaining points; and it will have been circumscribed about the square ``ABCD``.

Let it be circumscribed, as ``ABCD``.

Therefore about the given square a circle has been circumscribed. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.130" [label="G.130", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.130/", target="_top"];
     "G.13" [label="G.13", style="rounded,filled", fillcolor=orange, URL="/elements2/g.13/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.130" -> "G.15";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.5";
     "G.130" -> "G.13";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.12" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }
