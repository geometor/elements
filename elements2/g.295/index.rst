:order: 295
:original_id: IX.11
:type: prop
:dependencies: g.225

.. _g.295:

G.295
=====

**Heath ID:** :ref:`IX.11`

   If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

Let there be as many numbers as we please, B, C, D, E, beginning from the unit A and in continued proportion; I say that B, the least of the numbers B, C, D, E, measures E according to some one of the numbers C, D.

For since, as the unit A is to B, so is D to E, therefore the unit A measures the number B the same number of times as D measures E; therefore, alternately, the unit A measures D the same number of times as B measures E. [:ref:`g.225`]

But the unit A measures D according to the units in it; therefore B also measures E according to the units in D; so that B the less measures E the greater according to some number of those which have place among the proportional numbers.—


.. _elem.9.11.p.1:


**IX.11.p.1**


And it is manifest that, whatever place the measuring number has, reckoned from the unit, the same place also has the number according to which it measures, reckoned from the number measured, in the direction of the number before it.—

Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.295" [label="G.295", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.295/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.222" -> "G.216";
     "G.295" -> "G.225";
     "G.225" -> "G.222";
     "G.222" -> "G.219";
   }



Required for
------------

:ref:`g.299`, :ref:`g.322`, :ref:`g.329`
