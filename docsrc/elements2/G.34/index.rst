:order: 34
:original_id: I.24
:type: prop
:dependencies: G.28, G.33, G.11, G.12
:excerpt: If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.

**Heath ID:** `I.24 <https://geometor.github.io/euclid/I/24/>`_

.. picture:: G.34.png

.. _G.34:

G.34
====

    If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.

Let ``ABC``, ``DEF`` be two triangles having the two sides ``AB``, ``AC`` equal to the two sides ``DE``, ``DF`` respectively, namely ``AB`` to ``DE``, and ``AC`` to ``DF``, and let the angle at ``A`` be greater than the angle at ``D``;

I say that the base ``BC`` is also greater than the base ``EF``. 

For, since the angle ``BAC`` is greater than the angle ``EDF``, let there be constructed, on the straight line ``DE``, and at the point ``D`` on it, the angle ``EDG``
        equal to the angle ``BAC``; [:ref:`G.33`] let ``DG`` be made equal to either of the two straight lines ``AC``, ``DF``, and let ``EG``, ``FG`` be joined. 
        

Then, since ``AB`` is equal to ``DE``, and ``AC`` to ``DG``, the two sides ``BA``, ``AC`` are equal to the two sides ``ED``, ``DG``, respectively; and the angle ``BAC`` is equal to the angle ``EDG``; therefore the base ``BC`` is equal to the base ``EG``. [:ref:`G.11`]

Again, since ``DF`` is equal to ``DG``, the angle ``DGF`` is also equal to the angle ``DFG``; [:ref:`G.12`] therefore the angle ``DFG`` is greater than the angle ``EGF``.

Therefore the angle ``EFG`` is much greater than the angle ``EGF``.

And, since ``EFG`` is a triangle having the angle ``EFG``
        greater than the angle ``EGF``, and the greater angle is subtended by the greater side, [:ref:`G.28`] the side ``EG`` is also greater than ``EF``.

But ``EG`` is equal to ``BC``. Therefore ``BC`` is also greater than ``EF``.
        

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **10**

   

   I have naturally left out the well-known words added by Simson in order to avoid the necessity of considering three cases: Of the two sides ``DE``, ``DF`` let ``DE`` be the side which is not greater than the other.

    I doubt whether Euclid could have been induced to insert the words himself, even if it had been represented to him that their omission meant leaving two possible cases out of consideration. His habit and that of the great Greek geometers was, not to set out all possible cases, but to give as a rule one case, generally the most difficult, as here, and to leave the others to the reader to work out for himself. We have already seen one instance in :ref:`G.14`.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.27" [label="G.27", fillcolor="#222244", URL="/elements2/G.27/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.34" [label="G.34", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.34/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.28" [label="G.28", fillcolor="#222244", URL="/elements2/G.28/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.28" -> "G.27";
     "G.24" -> "G.6";
     "G.8" -> "G.6";
     "G.21" -> "G.19";
     "G.25" -> "G.24";
     "G.24" -> "G.21";
     "G.11" -> "G.10";
     "G.25" -> "G.7";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.5" -> "G.3";
     "G.25" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.17";
     "G.19" -> "G.15";
     "G.16" -> "G.15";
     "G.33" -> "G.15";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.5" -> "G.1";
     "G.24" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.34" -> "G.12";
     "G.28" -> "G.12";
     "G.14" -> "G.12";
     "G.24" -> "G.22";
     "G.15" -> "G.14";
     "G.34" -> "G.28";
     "G.9" -> "G.8";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.16" -> "G.9";
     "G.27" -> "G.9";
     "G.12" -> "G.9";
     "G.27" -> "G.25";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.25" -> "G.11";
     "G.17" -> "G.11";
     "G.34" -> "G.11";
     "G.12" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.34" -> "G.33";
     "G.17" -> "G.16";
   }



Required for
------------

:ref:`G.35`
