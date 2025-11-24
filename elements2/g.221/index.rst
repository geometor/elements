:order: 221
:original_id: VII.11
:type: prop
:dependencies: g.219, g.220

.. _g.221:

G.221
=====

**Heath ID:** :ref:`VII.11`

   If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.

As the whole AB is to the whole CD, so let AE subtracted be to CF subtracted; I say that the remainder EB is also to the remainder FD as the whole AB to the whole CD.

Since, as AB is to CD, so is AE to CF, whatever part or parts AB is of CD, the same part or the same parts is AE of CF also; [:ref:`g.219`]

Therefore also the remainder EB is the same part or parts of FD that AB is of CD. [:ref:`g.220`]

Therefore, as EB is to FD, so is AB to CD. [:ref:`g.219`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.220" [label="G.220", style="rounded,filled", fillcolor=orange, URL="/elements2/g.220/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.221" [label="G.221", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.221/", target="_top"];
     "G.221" -> "G.220";
     "G.221" -> "G.219";
   }
