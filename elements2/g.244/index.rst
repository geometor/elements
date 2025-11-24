:order: 244
:original_id: VII.33
:type: prop
:dependencies: g.226, g.229, g.231, g.210, g.232, g.219

.. _g.244:

G.244
=====

**Heath ID:** :ref:`VII.33`

   Given as many numbers as we please, to find the least of those which have the same ratio with them.

Let A, B, C be the given numbers, as many as we please; thus it is required to find the least of those which have the same ratio with A, B, C.

A, B, C are either prime to one another or not.

Now, if A, B, C are prime to one another, they are the least of those which have the same ratio with them. [:ref:`g.231`]

But, if not, let D the greatest common measure of A, B, C be taken, [:ref:`g.210`] and, as many times as D measures the numbers A, B, C
respectively, so many units let there be in the numbers E, F, G respectively.

Therefore the numbers E, F, G measure the numbers A, B, C respectively according to the units in D. [:ref:`g.226`]

Therefore E, F, G measure A, B, C the same number of times; therefore E, F, G are in the same ratio with A, B, C. [:ref:`g.219`]

I say next that they are the least that are in that ratio.

For, if E, F, G are not the least of those which have the same ratio with A, B, C, there will be numbers less than E, F, G which are in the same ratio with A, B, C.

Let them be H, K, L; therefore H measures A the same number of times that the numbers K, L measure the numbers B, C respectively.

Now, as many times as H measures A, so many units let there be in M; therefore the numbers K, L also measure the numbers B, C respectively according to the units in M.

And, since H measures A according to the units in M, therefore M also measures A according to the units in H. [:ref:`g.226`]

For the same reason M also measures the numbers B, C according to the units in the numbers K, L respectively;

Therefore M measures A, B, C.

Now, since H measures A according to the units in M, therefore H by multiplying M has made A. [:ref:`g.232`]

For the same reason also E by multiplying D has made A.

Therefore the product of E, D is equal to the product of H, M.

Therefore, as E is to H, so is M to D. [:ref:`g.229`]

But E is greater than H; therefore M is also greater than D.

And it measures A, B, C: which is impossible, for by hypothesis D is the greatest common measure of A, B, C.

Therefore there cannot be any numbers less than E, F, G which are in the same ratio with A, B, C.

Therefore E, F, G are the least of those which have the same ratio with A, B, C. Q. E. D.
literally (as usual) each of the numbers E, F, G measures each of the numbers A, B, C.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.208" [label="G.208", URL="/elements2/g.208/", target="_top"];
     "G.140" [label="G.140", style="rounded,filled", fillcolor=orange, URL="/elements2/g.140/", target="_top"];
     "G.144" [label="G.144", URL="/elements2/g.144/", target="_top"];
     "G.137" [label="G.137", style="rounded,filled", fillcolor=orange, URL="/elements2/g.137/", target="_top"];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.210" [label="G.210", URL="/elements2/g.210/", target="_top"];
     "G.230" [label="G.230", URL="/elements2/g.230/", target="_top"];
     "G.209" [label="G.209", style="rounded,filled", fillcolor=orange, URL="/elements2/g.209/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.226" [label="G.226", URL="/elements2/g.226/", target="_top"];
     "G.244" [label="G.244", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.244/", target="_top"];
     "G.145" [label="G.145", style="rounded,filled", fillcolor=orange, URL="/elements2/g.145/", target="_top"];
     "G.223" [label="G.223", URL="/elements2/g.223/", target="_top"];
     "G.206" [label="G.206", style="rounded,filled", fillcolor=orange, URL="/elements2/g.206/", target="_top"];
     "G.218" [label="G.218", URL="/elements2/g.218/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.148" [label="G.148", URL="/elements2/g.148/", target="_top"];
     "G.231" [label="G.231", URL="/elements2/g.231/", target="_top"];
     "G.211" [label="G.211", URL="/elements2/g.211/", target="_top"];
     "G.229" [label="G.229", URL="/elements2/g.229/", target="_top"];
     "G.227" [label="G.227", URL="/elements2/g.227/", target="_top"];
     "G.232" [label="G.232", style="rounded,filled", fillcolor=orange, URL="/elements2/g.232/", target="_top"];
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.207" [label="G.207", URL="/elements2/g.207/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.228" [label="G.228", URL="/elements2/g.228/", target="_top"];
     "G.147" [label="G.147", URL="/elements2/g.147/", target="_top"];
     "G.210" -> "G.208";
     "G.211" -> "G.208";
     "G.144" -> "G.140";
     "G.229" -> "G.144";
     "G.147" -> "G.137";
     "G.217" -> "G.216";
     "G.218" -> "G.216";
     "G.222" -> "G.216";
     "G.244" -> "G.210";
     "G.231" -> "G.230";
     "G.210" -> "G.209";
     "G.218" -> "G.217";
     "G.225" -> "G.222";
     "G.230" -> "G.222";
     "G.228" -> "G.226";
     "G.231" -> "G.226";
     "G.244" -> "G.226";
     "G.147" -> "G.145";
     "G.227" -> "G.223";
     "G.230" -> "G.223";
     "G.207" -> "G.206";
     "G.231" -> "G.206";
     "G.223" -> "G.218";
     "G.226" -> "G.225";
     "G.229" -> "G.148";
     "G.244" -> "G.231";
     "G.230" -> "G.211";
     "G.244" -> "G.229";
     "G.228" -> "G.227";
     "G.229" -> "G.227";
     "G.244" -> "G.232";
     "G.147" -> "G.146";
     "G.208" -> "G.207";
     "G.222" -> "G.219";
     "G.223" -> "G.219";
     "G.227" -> "G.219";
     "G.230" -> "G.219";
     "G.244" -> "G.219";
     "G.229" -> "G.228";
     "G.148" -> "G.147";
   }



Required for
------------

:ref:`g.284`, :ref:`g.294`, :ref:`g.298`, :ref:`g.299`, :ref:`g.285`, :ref:`g.286`, :ref:`g.322`, :ref:`g.329`, :ref:`g.287`, :ref:`g.288`, :ref:`g.289`, :ref:`g.292`, :ref:`g.293`, :ref:`g.245`, :ref:`g.247`, :ref:`g.250`, :ref:`g.268`, :ref:`g.270`, :ref:`g.271`, :ref:`g.272`, :ref:`g.276`, :ref:`g.277`, :ref:`g.278`, :ref:`g.279`, :ref:`g.280`, :ref:`g.281`, :ref:`g.282`, :ref:`g.283`, :ref:`g.254`, :ref:`g.257`, :ref:`g.258`, :ref:`g.259`, :ref:`g.260`, :ref:`g.261`, :ref:`g.345`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.346`, :ref:`g.347`, :ref:`g.351`, :ref:`g.353`, :ref:`g.358`, :ref:`g.361`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.398`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.342`, :ref:`g.456`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.569`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.563`
