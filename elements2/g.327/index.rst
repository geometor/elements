:order: 327
:original_id: IX.35
:type: prop
:dependencies: g.222, g.326

.. _g.327:

G.327
=====

**Heath ID:** :ref:`IX.35`

   If as many numbers as we please be in continued proportion, and there be subtracted from the second and the last numbers equal to the first, then, as the excess of the second is to the first, so will the excess of the last be to all those before it.

Let there be as many numbers as we please in continued proportion, A, BC, D, EF, beginning from A as least, and let there be subtracted from BC and EF the numbers BG, FH, each equal to A; I say that, as GC is to A, so is EH to A, BC, D.

For let FK be made equal to BC, and FL equal to D.

Then, since FK is equal to BC, and of these the part FH is equal to the part BG, therefore the remainder HK is equal to the remainder GC.

And since, as EF is to D, so is D to BC, and BC to A, while D is equal to FL, BC to FK, and A to FH, therefore, as EF is to FL, so is LF to FK, and FK to FH.

Separando, as EL is to LF, so is LK to FK, and KH to FH. [:ref:`g.326`]

Therefore also, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents; [:ref:`g.222`] therefore, as KH is to FH, so are EL, LK. KH to LF, FK, HF.

But KH is equal to CG, FH to A, and LF, FK, HF to D, BC, A; therefore, as CG is to A, so is EH to D, BC, A.

Therefore, as the excess of the second is to the first, so is the excess of the last to all those before it. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.326" [label="G.326", style="rounded,filled", fillcolor=orange, URL="/elements2/g.326/", target="_top"];
     "G.327" [label="G.327", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.327/", target="_top"];
     "G.222" -> "G.216";
     "G.327" -> "G.222";
     "G.222" -> "G.219";
     "G.327" -> "G.326";
   }



Required for
------------

:ref:`g.329`
