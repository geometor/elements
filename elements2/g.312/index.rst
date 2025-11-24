:order: 312
:original_id: IX.23
:type: prop
:dependencies: g.309, g.311, g.310

.. _g.312:

G.312
=====

**Heath ID:** :ref:`IX.23`

   If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.

For let as many odd numbers as we please, AB, BC, CD, the multitude of which is odd, be added together; I say that the whole AD is also odd.

Let the unit DE be subtracted from CD; therefore the remainder CE is even. [:ref:`g.310`]

But CA is also even; [:ref:`g.311`] therefore the whole AE is also even. [:ref:`g.309`]

And DE is an unit.

Therefore AD is odd. [:ref:`g.310`] Q. E. D.
3. Literally let there be as many numbers as we please, of which let the multitude be odd.
This form, natural in Greek, is awkward in English.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.308" [label="G.308", style="rounded,filled", fillcolor=orange, URL="/elements2/g.308/", target="_top"];
     "G.311" [label="G.311", URL="/elements2/g.311/", target="_top"];
     "G.309" [label="G.309", URL="/elements2/g.309/", target="_top"];
     "G.310" [label="G.310", style="rounded,filled", fillcolor=orange, URL="/elements2/g.310/", target="_top"];
     "G.312" [label="G.312", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.312/", target="_top"];
     "G.309" -> "G.308";
     "G.312" -> "G.311";
     "G.311" -> "G.309";
     "G.312" -> "G.309";
     "G.311" -> "G.310";
     "G.312" -> "G.310";
   }



Required for
------------

:ref:`g.318`, :ref:`g.319`, :ref:`g.320`
