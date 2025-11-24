:order: 210
:original_id: VII.3
:type: prop
:dependencies: g.208, g.209

.. _g.210:

G.210
=====

**Heath ID:** :ref:`VII.3`

   Given three numbers not prime to one another, to find their greatest common measure.

Let A, B, C be the three given numbers not prime to one another; thus it is required to find the greatest common measure of A, B, C.

For let the greatest common measure, D, of the two numbers A, B be taken; [:ref:`g.208`] then D either measures, or does not measure, C.

First, let it measure it.

But it measures A, B also; therefore D measures A, B, C; therefore D is a common measure of A, B, C.

I say that it is also the greatest.

For, if D is not the greatest common measure of A, B, C, some number which is greater than D will measure the numbers A, B, C.

Let such a number measure them, and let it be E.

Since then E measures A, B, C, it will also measure A, B; therefore it will also measure the greatest common measure of A, B. [:ref:`g.209`]

But the greatest common measure of A, B is D; therefore E measures D, the greater the less: which is impossible.

Therefore no number which is greater than D will measure the numbers A, B, C;


.. container:: center

   therefore D is the greatest common measure of A, B, C.


Next, let D not measure C; I say first that C, D are not prime to one another.

For, since A, B, C are not prime to one another, some number will measure them.

Now that which measures A, B, C will also measure A, B, and will measure D, the greatest common measure of A, B. [:ref:`g.209`]

But it measures C also; therefore some number will measure the numbers D, C; therefore D, C are not prime to one another.

Let then their greatest common measure E be taken. [:ref:`g.208`]

Then, since E measures D, and D measures A, B, therefore E also measures A, B.

But it measures C also; therefore E measures A, B, C; therefore E is a common measure of A, B, C.

I say next that it is also the greatest.

For, if E is not the greatest common measure of A, B, C, some number which is greater than E will measure the numbers A, B, C.

Let such a number measure them, and let it be F.

Now, since F measures A, B, C, it also measures A, B; therefore it will also measure the greatest common measure of A, B. [:ref:`g.209`]

But the greatest common measure of A, B is D; therefore F measures D.

And it measures C also; therefore F measures D, C; therefore it will also measure the greatest common measure of D, C. [:ref:`g.209`]

But the greatest common measure of D, C is E; therefore F measures E, the greater the less: which is impossible.

Therefore no number which is greater than E will measure the numbers A, B, C; therefore E is the greatest common measure of A, B, C. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.208" [label="G.208", URL="/elements2/g.208/", target="_top"];
     "G.206" [label="G.206", style="rounded,filled", fillcolor=orange, URL="/elements2/g.206/", target="_top"];
     "G.207" [label="G.207", URL="/elements2/g.207/", target="_top"];
     "G.210" [label="G.210", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.210/", target="_top"];
     "G.209" [label="G.209", style="rounded,filled", fillcolor=orange, URL="/elements2/g.209/", target="_top"];
     "G.210" -> "G.208";
     "G.207" -> "G.206";
     "G.208" -> "G.207";
     "G.210" -> "G.209";
   }



Required for
------------

:ref:`g.284`, :ref:`g.294`, :ref:`g.298`, :ref:`g.299`, :ref:`g.285`, :ref:`g.286`, :ref:`g.322`, :ref:`g.329`, :ref:`g.287`, :ref:`g.288`, :ref:`g.289`, :ref:`g.292`, :ref:`g.293`, :ref:`g.244`, :ref:`g.245`, :ref:`g.247`, :ref:`g.250`, :ref:`g.268`, :ref:`g.270`, :ref:`g.271`, :ref:`g.272`, :ref:`g.276`, :ref:`g.277`, :ref:`g.278`, :ref:`g.279`, :ref:`g.280`, :ref:`g.281`, :ref:`g.282`, :ref:`g.283`, :ref:`g.254`, :ref:`g.257`, :ref:`g.258`, :ref:`g.259`, :ref:`g.260`, :ref:`g.261`, :ref:`g.345`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.346`, :ref:`g.347`, :ref:`g.351`, :ref:`g.353`, :ref:`g.358`, :ref:`g.361`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.398`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.342`, :ref:`g.456`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.569`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.563`
