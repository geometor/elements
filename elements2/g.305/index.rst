:order: 305
:original_id: IX.18
:type: prop
:dependencies: g.303, g.229

.. _g.305:

G.305
=====

**Heath ID:** :ref:`IX.18`

   Given two numbers, to investigate whether it is possible to find a third proportional to them.

Let A, B be the given two numbers, and let it be required to investigate whether it is possible to find a third proportional to them.

Now A, B are either prime to one another or not.

And, if they are prime to one another, it has been proved that it is impossible to find a third proportional to them. [:ref:`g.303`]

Next, let A, B not be prime to one another, and let B by multiplying itself make C.

Then A either measures C or does not measure it.

First, let it measure it according to D; therefore A by multiplying D has made C.

But, further, B has also by multiplying itself made C; therefore the product of A, D is equal to the square on B.

Therefore, as A is to B, so is B to D; [:ref:`g.229`] therefore a third proportional number D has been found to A, B.

Next, let A not measure C; I say that it is impossible to find a third proportional number to A, B.

For, if possible, let D, such third proportional, have been found.

Therefore the product of A, D is equal to the square on B.

But the square on B is C; therefore the product of A, D is equal to C.

Hence A by multiplying D has made C; therefore A measures C according to D.

But, by hypothesis, it also does not measure it: which is absurd.

Therefore it is not possible to find a third proportional number to A, B when A does not measure C. Q. E. D.


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
     "G.303" [label="G.303", URL="/elements2/g.303/", target="_top"];
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
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.207" [label="G.207", URL="/elements2/g.207/", target="_top"];
     "G.305" [label="G.305", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.305/", target="_top"];
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
     "G.303" -> "G.230";
     "G.218" -> "G.217";
     "G.225" -> "G.222";
     "G.230" -> "G.222";
     "G.305" -> "G.303";
     "G.228" -> "G.226";
     "G.231" -> "G.226";
     "G.147" -> "G.145";
     "G.227" -> "G.223";
     "G.230" -> "G.223";
     "G.207" -> "G.206";
     "G.231" -> "G.206";
     "G.223" -> "G.218";
     "G.226" -> "G.225";
     "G.229" -> "G.148";
     "G.303" -> "G.231";
     "G.230" -> "G.211";
     "G.305" -> "G.229";
     "G.228" -> "G.227";
     "G.229" -> "G.227";
     "G.147" -> "G.146";
     "G.208" -> "G.207";
     "G.222" -> "G.219";
     "G.223" -> "G.219";
     "G.227" -> "G.219";
     "G.230" -> "G.219";
     "G.229" -> "G.228";
     "G.148" -> "G.147";
   }
