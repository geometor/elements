:order: 564
:original_id: XIII.7
:type: prop
:dependencies: g.11, g.12, g.13, g.15

.. _g.564:

G.564
=====

**Heath ID:** :ref:`XIII.7`

   If three angles of an equilateral pentagon, taken either in order or not in order, be equal, the pentagon will be equiangular.

For in the equilateral pentagon ABCDE let, first, three angles taken in order, those at A, B, C, be equal to one another; I say that the pentagon ABCDE is equiangular.

For let AC, BE, FD be joined.

Now, since the two sides CB, BA are equal to the two sides BA, AE respectively, and the angle CBA is equal to the angle BAE, therefore the base AC is equal to the base BE, the triangle ABC is equal to the triangle ABE, and the remaining angles will be equal to the remaining angles, namely those which the equal sides subtend, [:ref:`g.11`] that is, the angle BCA to the angle BEA, and the angle ABE to the angle CAB; hence the side AF is also equal to the side BF. [:ref:`g.13`]

But the whole AC was also proved equal to the whole BE; therefore the remainder FC is also equal to the remainder FE.

But CD is also equal to DE.

Therefore the two sides FC, CD are equal to the two sides FE, ED; and the base FD is common to them; therefore the angle FCD is equal to the angle FED. [:ref:`g.15`]

But the angle BCA was also proved equal to the angle AEB; therefore the whole angle BCD is also equal to the whole angle AED.

But, by hypothesis, the angle BCD is equal to the angles at A, B; therefore the angle AED is also equal to the angles at A, B.

Similarly we can prove that the angle CDE is also equal to the angles at A, B, C; therefore the pentagon ABCDE is equiangular.

Next, let the given equal angles not be angles taken in order, but let the angles at the points A, C, D be equal; I say that in this case too the pentagon ABCDE is equiangular.

For let BD be joined.

Then, since the two sides BA, AE are equal to the two sides BC, CD, and they contain equal angles, therefore the base BE is equal to the base BD, the triangle ABE is equal to the triangle BCD, and the remaining angles will be equal to the remaining angles, namely those which the equal sides subtend; [:ref:`g.11`] therefore the angle AEB is equal to the angle CDB.

But the angle BED is also equal to the angle BDE, since the side BE is also equal to the side BD. [:ref:`g.12`]

Therefore the whole angle AED is equal to the whole angle CDE.

But the angle CDE is, by hypothesis, equal to the angles at A, C; therefore the angle AED is also equal to the angles at A, C.

For the same reason the angle ABC is also equal to the angles at A, C, D.

Therefore the pentagon ABCDE is equiangular. Q. E. D.


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
     "G.13" [label="G.13", style="rounded,filled", fillcolor=orange, URL="/elements2/g.13/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.564" [label="G.564", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.564/", target="_top"];
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.564" -> "G.15";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.5";
     "G.564" -> "G.13";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.12" -> "G.11";
     "G.564" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.564" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }



Required for
------------

:ref:`g.575`, :ref:`g.578`
