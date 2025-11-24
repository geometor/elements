:order: 306
:original_id: IX.19
:type: prop
:dependencies: g.304, g.224, g.229, g.230, g.231

.. _g.306:

G.306
=====

**Heath ID:** :ref:`IX.19`

   Given three numbers, to investigate when it is possible to find a fourth proportional to them.

Let A, B, C be the given three numbers, and let it be required to investigate when it is possible to find a fourth proportional to them.

Now either they are not in continued proportion, and the extremes of them are prime to one another; or they are in continued proportion, and the extremes of them are not prime to one another; or they are not in continued proportion, nor are the extremes of them prime to one another; or they are in continued proportion, and the extremes of them are prime to one another.

If then A, B, C are in continued proportion, and the extremes of them A, C are prime to one another, it has been proved that it is impossible to find a fourth proportional number to them. [:ref:`g.304`]

<*>Next, let A, B, C not be in continued proportion, the extremes being again prime to one another; I say that in this case also it is impossible to find a fourth proportional to them.

For, if possible, let D have been found, so that,


.. container:: center

   as A is to B, so is C to D,


and let it be contrived that, as B is to C, so is D to E.

Now, since, as A is to B, so is C to D, and, as B is to C, so is D to E, therefore, ex aequali, as A is to C, so is C to E. [:ref:`g.224`]

But A, C are prime, primes are also least, [:ref:`g.231`] and the least numbers measure those which have the same ratio, the antecedent the antecedent and the consequent the consequent. [:ref:`g.230`]

Therefore A measures C as antecedent antecedent.

But it also measures itself; therefore A measures A, C which are prime to one another: which is impossible.

Therefore it is not possible to find a fourth proportional to A, B, C.<*>

Next, let A, B, C be again in continued proportion, but let A, C not be prime to one another.

I say that it is possible to find a fourth proportional to them.

For let B by multiplying C make D; therefore A either measures D or does not measure it.

First, let it measure it according to E; therefore A by multiplying E has made D.

But, further, B has also by multiplying C made D; therefore the product of A, E is equal to the product of B, C; therefore, proportionally, as A is to B, so is C to E; [:ref:`g.229`] therefore E has been found a fourth proportional to A, B, C.

Next, let A not measure D; I say that it is impossible to find a fourth proportional number to A, B, C.

For, if possible, let E have been found; therefore the product of A, E is equal to the product of B, C. [:ref:`g.229`]

But the product of B, C is D; therefore the product of A, E is also equal to D.

Therefore A by multiplying E has made D; therefore A measures D according to E, so that A measures D.

But it also does not measure it: which is absurd.

Therefore it is not possible to find a fourth proportional number to A, B, C when A does not measure D.

Next, let A, B, C not be in continued proportion, nor the extremes prime to one another.

And let B by multiplying C make D.

Similarly then it can be proved that, if A measures D, it is possible to find a fourth proportional to them, but, if it does not measure it, impossible. Q. E. D.


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
     "G.230" [label="G.230", URL="/elements2/g.230/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.226" [label="G.226", URL="/elements2/g.226/", target="_top"];
     "G.306" [label="G.306", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.306/", target="_top"];
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
     "G.224" [label="G.224", URL="/elements2/g.224/", target="_top"];
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.207" [label="G.207", URL="/elements2/g.207/", target="_top"];
     "G.304" [label="G.304", URL="/elements2/g.304/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.228" [label="G.228", URL="/elements2/g.228/", target="_top"];
     "G.147" [label="G.147", URL="/elements2/g.147/", target="_top"];
     "G.211" -> "G.208";
     "G.144" -> "G.140";
     "G.229" -> "G.144";
     "G.147" -> "G.137";
     "G.217" -> "G.216";
     "G.218" -> "G.216";
     "G.222" -> "G.216";
     "G.231" -> "G.230";
     "G.304" -> "G.230";
     "G.306" -> "G.230";
     "G.218" -> "G.217";
     "G.225" -> "G.222";
     "G.230" -> "G.222";
     "G.228" -> "G.226";
     "G.231" -> "G.226";
     "G.147" -> "G.145";
     "G.224" -> "G.223";
     "G.227" -> "G.223";
     "G.230" -> "G.223";
     "G.304" -> "G.223";
     "G.207" -> "G.206";
     "G.231" -> "G.206";
     "G.223" -> "G.218";
     "G.226" -> "G.225";
     "G.229" -> "G.148";
     "G.304" -> "G.231";
     "G.306" -> "G.231";
     "G.230" -> "G.211";
     "G.306" -> "G.229";
     "G.228" -> "G.227";
     "G.229" -> "G.227";
     "G.306" -> "G.224";
     "G.147" -> "G.146";
     "G.208" -> "G.207";
     "G.306" -> "G.304";
     "G.222" -> "G.219";
     "G.223" -> "G.219";
     "G.227" -> "G.219";
     "G.230" -> "G.219";
     "G.229" -> "G.228";
     "G.148" -> "G.147";
   }
