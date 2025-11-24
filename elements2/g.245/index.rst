:order: 245
:original_id: VII.34
:type: prop
:dependencies: g.226, g.227, g.229, g.230, g.231, g.244, g.232

.. _g.245:

G.245
=====

**Heath ID:** :ref:`VII.34`

   Given two numbers, to find the least number which they measure.

Let A, B be the two given numbers; thus it is required to find the least number which they measure.

Now A, B are either prime to one another or not.

First, let A, B be prime to one another, and let A by multiplying B make C; therefore also B by multiplying A has made C. [:ref:`g.226`]

Therefore A, B measure C

I say next that it is also the least number they measure.

For, if not, A, B will measure some number which is less than C.

Let them measure D.

Then, as many times as A measures D, so many units let there be in E, and, as many times as B measures D, so many units let there be in F; therefore A by multiplying E has made D, and B by multiplying F has made D; [:ref:`g.232`] therefore the product of A, E is equal to the product of B, F.

Therefore, as A is to B, so is F
E. [:ref:`g.229`]

But A, B are prime, primes are also least, [:ref:`g.231`] and the least measure the numbers which have the same ratio the same number of times, the greater the greater and the less the less; [:ref:`g.230`] therefore B measures E, as consequent consequent.

And, since A by multiplying B, E has made C, D, therefore, as B is to E, so is C to D. [:ref:`g.227`]

But B measures E; therefore C also measures D, the greater the less: which is impossible.

Therefore A, B do not measure any number less than C; therefore C is the least that is measured by A, B.

Next, let A, B not be prime to one another, and let F, E, the least numbers of those which have the same ratio with A, B, be taken; [:ref:`g.244`] therefore the product of A, E is equal to the product of B, F. [:ref:`g.229`]

And let A by multiplying E make C; therefore also B by multiplying F has made C; therefore A, B measure C.

I say next that it is also the least number that they measure.

For, if not, A, B will measure some number which is less than C.

Let them measure D.

And, as many times as A measures D, so many units let there be in G, and, as many times as B measures D, so many units let there be in H.

Therefore A by multiplying G has made D, and B by multiplying H has made D.

Therefore the product of A, G is equal to the product of B, H; therefore, as A is to B, so is H to G. [:ref:`g.229`]

But, as A is to B, so is F to E.

Therefore also, as F is to E, so is H to G.

But F, E are least, and the least measure the numbers which have the same ratio the same number of times, the greater the greater and the less the less; [:ref:`g.230`] therefore E measures G.

And, since A by multiplying E, G has made C, D, therefore, as E is to G, so is C to D. [:ref:`g.227`]

But E measures G; therefore C also measures D, the greater the less: which is impossible.

Therefore A, B will not measure any number which is less than C.

Therefore C is the least that is measured by A, B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.208" [label="G.208", URL="/elements2/g.208/", target="_top"];
     "G.245" [label="G.245", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.245/", target="_top"];
     "G.140" [label="G.140", style="rounded,filled", fillcolor=orange, URL="/elements2/g.140/", target="_top"];
     "G.144" [label="G.144", URL="/elements2/g.144/", target="_top"];
     "G.137" [label="G.137", style="rounded,filled", fillcolor=orange, URL="/elements2/g.137/", target="_top"];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.210" [label="G.210", URL="/elements2/g.210/", target="_top"];
     "G.230" [label="G.230", URL="/elements2/g.230/", target="_top"];
     "G.209" [label="G.209", style="rounded,filled", fillcolor=orange, URL="/elements2/g.209/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.244" [label="G.244", URL="/elements2/g.244/", target="_top"];
     "G.226" [label="G.226", URL="/elements2/g.226/", target="_top"];
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
     "G.245" -> "G.230";
     "G.210" -> "G.209";
     "G.218" -> "G.217";
     "G.225" -> "G.222";
     "G.230" -> "G.222";
     "G.245" -> "G.244";
     "G.228" -> "G.226";
     "G.231" -> "G.226";
     "G.244" -> "G.226";
     "G.245" -> "G.226";
     "G.147" -> "G.145";
     "G.227" -> "G.223";
     "G.230" -> "G.223";
     "G.207" -> "G.206";
     "G.231" -> "G.206";
     "G.223" -> "G.218";
     "G.226" -> "G.225";
     "G.229" -> "G.148";
     "G.244" -> "G.231";
     "G.245" -> "G.231";
     "G.230" -> "G.211";
     "G.244" -> "G.229";
     "G.245" -> "G.229";
     "G.228" -> "G.227";
     "G.229" -> "G.227";
     "G.245" -> "G.227";
     "G.244" -> "G.232";
     "G.245" -> "G.232";
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

:ref:`g.247`, :ref:`g.250`, :ref:`g.257`, :ref:`g.258`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.346`, :ref:`g.347`, :ref:`g.351`, :ref:`g.353`, :ref:`g.358`, :ref:`g.361`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.569`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.563`
