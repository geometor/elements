:order: 335
:original_id: X.4
:type: prop
:dependencies: g.333, g.334

.. _g.335:

G.335
=====

**Heath ID:** :ref:`X.4`

   Given three commensurable magnitudes, to find their greatest common measure.

Let A, B, C be the three given commensurable magnitudes; thus it is required to find the greatest common measure of A, B, C.

Let the greatest common measure of the two magnitudes A, B be taken, and let it be D; [:ref:`g.333`] then D either measures C, or does not measure it.

First, let it measure it.

Since then D measures C, while it also measures A, B, therefore D is a common measure of A, B, C.

And it is manifest that it is also the greatest; for a greater magnitude than the magnitude D does not measure A, B.

Next, let D not measure C.

I say first that C, D are commensurable.

For, since A, B, C are commensurable, some magnitude will measure them, and this will of course measure A, B also; so that it will also measure the greatest common measure of A, B, namely D. [:ref:`g.334`]

But it also measures C; so that the said magnitude will measure C, D; therefore C, D are commensurable.

Now let their greatest common measure be taken, and let it be E. [:ref:`g.333`]

Since then E measures D, while D measures A, B, therefore E will also measure A, B.

But it measures C also; therefore E measures A, B, C; therefore E is a common measure of A, B, C.

I say next that it is also the greatest.

For, if possible, let there be some magnitude F greater than E, and let it measure A, B, C.

Now, since F measures A, B, C, it will also measure A, B, and will measure the greatest common measure of A, B. [:ref:`g.334`]

But the greatest common measure of A, B is D; therefore F measures D.

But it measures C also; therefore F measures C, D; therefore F will also measure the greatest common measure of C, D. [:ref:`g.334`]

But that is E; therefore F will measure E, the greater the less: which is impossible.

Therefore no magnitude greater than the magnitude E will measure A, B, C; therefore E is the greatest common measure of A, B, C if D do not measure C, and, if it measure it, D is itself the greatest common measure.

Therefore the greatest common measure of the three given commensurable magnitudes has been found.


.. _elem.10.4.p.1:


**X.4.p.1**


From this it is manifest that, if a magnitude measure three magnitudes, it will also measure their greatest common measure. 
Similarly too, with more magnitudes, the greatest common measure can be found, and the porism can be extended. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.335" [label="G.335", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.335/", target="_top"];
     "G.334" [label="G.334", style="rounded,filled", fillcolor=orange, URL="/elements2/g.334/", target="_top"];
     "G.331" [label="G.331", style="rounded,filled", fillcolor=orange, URL="/elements2/g.331/", target="_top"];
     "G.332" [label="G.332", URL="/elements2/g.332/", target="_top"];
     "G.333" [label="G.333", URL="/elements2/g.333/", target="_top"];
     "G.335" -> "G.334";
     "G.332" -> "G.331";
     "G.333" -> "G.332";
     "G.335" -> "G.333";
   }
