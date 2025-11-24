:order: 233
:original_id: VII.22
:type: prop
:dependencies: g.227, g.232

.. _g.233:

G.233
=====

**Heath ID:** :ref:`VII.22`

   The least numbers of those which have the same ratio with them are prime to one another.

Let A, B be the least numbers of those which have the same ratio with them; I say that A, B are prime to one another.

For, if they are not prime to one another, some number will measure them.

Let some number measure them, and let it be C.

And, as many times as C measures A, so many units let there be in D, and, as many times as C measures B, so many units let there be in E

Since C measures A according to the units in D, therefore C by multiplying D has made A. [:ref:`g.232`]

For the same reason also C by multiplying E has made B.

Thus the number C by multiplying the two numbers D, E has made A, B; therefore, as D is to E, so is A to B; [:ref:`g.227`] therefore D, E are in the same ratio with A, B, being less than they: which is impossible.

Therefore no number will measure the numbers A, B.

Therefore A, B are prime to one another. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.223" [label="G.223", URL="/elements2/g.223/", target="_top"];
     "G.218" [label="G.218", URL="/elements2/g.218/", target="_top"];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.232" [label="G.232", style="rounded,filled", fillcolor=orange, URL="/elements2/g.232/", target="_top"];
     "G.227" [label="G.227", URL="/elements2/g.227/", target="_top"];
     "G.233" [label="G.233", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.233/", target="_top"];
     "G.227" -> "G.223";
     "G.223" -> "G.218";
     "G.217" -> "G.216";
     "G.218" -> "G.216";
     "G.218" -> "G.217";
     "G.223" -> "G.219";
     "G.227" -> "G.219";
     "G.233" -> "G.232";
     "G.233" -> "G.227";
   }



Required for
------------

:ref:`g.284`, :ref:`g.294`, :ref:`g.298`, :ref:`g.299`, :ref:`g.302`, :ref:`g.286`, :ref:`g.322`, :ref:`g.329`, :ref:`g.287`, :ref:`g.288`, :ref:`g.289`, :ref:`g.292`, :ref:`g.293`, :ref:`g.268`, :ref:`g.270`, :ref:`g.271`, :ref:`g.272`, :ref:`g.252`, :ref:`g.277`, :ref:`g.279`, :ref:`g.280`, :ref:`g.281`, :ref:`g.282`, :ref:`g.283`, :ref:`g.254`, :ref:`g.259`, :ref:`g.260`, :ref:`g.261`, :ref:`g.262`, :ref:`g.345`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.392`, :ref:`g.393`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.398`, :ref:`g.399`, :ref:`g.400`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.342`, :ref:`g.456`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.465`, :ref:`g.569`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.563`
