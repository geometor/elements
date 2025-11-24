:order: 208
:original_id: VII.2
:type: prop
:dependencies: g.207

.. _g.208:

G.208
=====

**Heath ID:** :ref:`VII.2`

   Given two numbers not prime to one another, to find their greatest common measure.

Let AB, CD be the two given numbers not prime to one another.

Thus it is required to find the greatest common measure of AB, CD.

If now CD measures AB—and it also measures itself—CD is a common measure of CD, AB.

And it is manifest that it is also the greatest; for no greater number than CD will measure CD.

But, if CD does not measure AB, then, the less of the numbers AB, CD being continually subtracted from the greater, some number will be left which will measure the one before it.

For an unit will not be left; otherwise AB, CD will be prime to one another [:ref:`g.207`], which is contrary to the hypothesis.

Therefore some number will be left which will measure the one before it.

Now let CD, measuring BE, leave EA less than itself, let EA, measuring DF, leave FC less than itself, and let CF measure AE.

Since then, CF measures AE, and AE measures DF, therefore CF will also measure DF.

But it also measures itself; therefore it will also measure the whole CD.

But CD measures BE; therefore CF also measures BE.

But it also measures EA; therefore it will also measure the whole BA.

But it also measures CD; therefore CF measures AB, CD.

Therefore CF is a common measure of AB, CD.

I say next that it is also the greatest.

For, if CF is not the greatest common measure of AB, CD, some number which is greater than CF will measure the numbers AB, CD.

Let such a number measure them, and let it be G.

Now, since G measures CD, while CD measures BE, G also measures BE.

But it also measures the whole BA; therefore it will also measure the remainder AE.

But AE measures DF; therefore G will also measure DF.

But it also measures the whole DC; therefore it will also measure the remainder CF, that is, the greater will measure the less: which is impossible.

Therefore no number which is greater than CF will measure the numbers AB, CD;


.. container:: center

   therefore CF is the greatest common measure of AB, CD.



.. _elem.7.2.p.1:


**VII.2.p.1**


From this it is manifest that, if a number measure two numbers, it will also measure their greatest common measure.

Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.208" [label="G.208", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.208/", target="_top"];
     "G.206" [label="G.206", style="rounded,filled", fillcolor=orange, URL="/elements2/g.206/", target="_top"];
     "G.207" [label="G.207", URL="/elements2/g.207/", target="_top"];
     "G.207" -> "G.206";
     "G.208" -> "G.207";
   }



Required for
------------

:ref:`g.284`, :ref:`g.294`, :ref:`g.298`, :ref:`g.299`, :ref:`g.300`, :ref:`g.302`, :ref:`g.303`, :ref:`g.304`, :ref:`g.305`, :ref:`g.306`, :ref:`g.285`, :ref:`g.286`, :ref:`g.322`, :ref:`g.329`, :ref:`g.287`, :ref:`g.288`, :ref:`g.289`, :ref:`g.292`, :ref:`g.293`, :ref:`g.230`, :ref:`g.231`, :ref:`g.235`, :ref:`g.236`, :ref:`g.237`, :ref:`g.238`, :ref:`g.210`, :ref:`g.241`, :ref:`g.244`, :ref:`g.245`, :ref:`g.247`, :ref:`g.250`, :ref:`g.211`, :ref:`g.251`, :ref:`g.268`, :ref:`g.270`, :ref:`g.271`, :ref:`g.272`, :ref:`g.252`, :ref:`g.276`, :ref:`g.277`, :ref:`g.278`, :ref:`g.279`, :ref:`g.280`, :ref:`g.281`, :ref:`g.282`, :ref:`g.283`, :ref:`g.254`, :ref:`g.257`, :ref:`g.258`, :ref:`g.259`, :ref:`g.260`, :ref:`g.261`, :ref:`g.262`, :ref:`g.345`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.346`, :ref:`g.347`, :ref:`g.351`, :ref:`g.353`, :ref:`g.358`, :ref:`g.361`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.398`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.342`, :ref:`g.456`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.569`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.563`
