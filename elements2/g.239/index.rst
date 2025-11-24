:order: 239
:original_id: VII.28
:type: prop
:dependencies: g.206

.. _g.239:

G.239
=====

**Heath ID:** :ref:`VII.28`

   If two numbers be prime to one another, the sum will also be prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers will also be prime to one another.

For let two numbers AB, BC prime to one another be added; I say that the sum AC is also prime to each of the numbers AB, BC.

For, if CA, AB are not prime to one another, some number will measure CA, AB.

Let a number measure them, and let it be D.

Since then D measures CA, AB, therefore it will also measure the remainder BC.

But it also measures BA; therefore D measures AB, BC which are prime to one another: which is impossible. [:ref:`g.206`]

Therefore no number will measure the numbers CA, AB; therefore CA, AB are prime to one another.

For the same reason AC, CB are also prime to one another.

Therefore CA is prime to each of the numbers AB, BC.

Again, let CA, AB be prime to one another; I say that AB, BC are also prime to one another.

For, if AB, BC are not prime to one another, some number will measure AB, BC.

Let a number measure them, and let it be D.

Now, since D measures each of the numbers AB, BC, it will also measure the whole CA.

But it also measures AB; therefore D measures CA, AB which are prime to one another: which is impossible. [:ref:`g.206`]

Therefore no number will measure the numbers AB, BC.

Therefore AB, BC are prime to one another. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.206" [label="G.206", style="rounded,filled", fillcolor=orange, URL="/elements2/g.206/", target="_top"];
     "G.239" [label="G.239", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.239/", target="_top"];
     "G.239" -> "G.206";
   }



Required for
------------

:ref:`g.302`
