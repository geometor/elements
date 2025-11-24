:order: 250
:original_id: VII.39
:type: prop
:dependencies: g.247, g.248, g.249

.. _g.250:

G.250
=====

**Heath ID:** :ref:`VII.39`

   To find the number which is the least that will have given parts.

Let A, B, C be the given parts; thus it is required to find the number which is the least that will have the parts A, B, C.

Let D, E, F be numbers called by the same name as the parts A, B, C, and let G, the least number measured by D, E, F, be taken. [:ref:`g.247`]

Therefore G has parts called by the same name as D, E, F. [:ref:`g.248`]

But A, B, C are parts called by the same name as D, E, F; therefore G has the parts A, B, C.

I say next that it is also the least number that has.

For, if not, there will be some number less than G which will have the parts A, B, C.

Let it be H.

Since H has the parts A, B, C, therefore H will be measured by numbers called by the same name as the parts A, B, C. [:ref:`g.249`]

But D, E, F are numbers called by the same name as the parts A, B, C; therefore H is measured by D, E, F.

And it is less than G : which is impossible.

Therefore there will be no number less than G that will have the parts A, B, C. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.248" [label="G.248", URL="/elements2/g.248/", target="_top"];
     "G.140" [label="G.140", style="rounded,filled", fillcolor=orange, URL="/elements2/g.140/", target="_top"];
     "G.250" [label="G.250", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.250/", target="_top"];
     "G.210" [label="G.210", URL="/elements2/g.210/", target="_top"];
     "G.209" [label="G.209", style="rounded,filled", fillcolor=orange, URL="/elements2/g.209/", target="_top"];
     "G.246" [label="G.246", style="rounded,filled", fillcolor=orange, URL="/elements2/g.246/", target="_top"];
     "G.145" [label="G.145", style="rounded,filled", fillcolor=orange, URL="/elements2/g.145/", target="_top"];
     "G.206" [label="G.206", style="rounded,filled", fillcolor=orange, URL="/elements2/g.206/", target="_top"];
     "G.218" [label="G.218", URL="/elements2/g.218/", target="_top"];
     "G.231" [label="G.231", URL="/elements2/g.231/", target="_top"];
     "G.211" [label="G.211", URL="/elements2/g.211/", target="_top"];
     "G.227" [label="G.227", URL="/elements2/g.227/", target="_top"];
     "G.207" [label="G.207", URL="/elements2/g.207/", target="_top"];
     "G.228" [label="G.228", URL="/elements2/g.228/", target="_top"];
     "G.247" [label="G.247", URL="/elements2/g.247/", target="_top"];
     "G.147" [label="G.147", URL="/elements2/g.147/", target="_top"];
     "G.208" [label="G.208", URL="/elements2/g.208/", target="_top"];
     "G.245" [label="G.245", URL="/elements2/g.245/", target="_top"];
     "G.144" [label="G.144", URL="/elements2/g.144/", target="_top"];
     "G.137" [label="G.137", style="rounded,filled", fillcolor=orange, URL="/elements2/g.137/", target="_top"];
     "G.216" [label="G.216", style="rounded,filled", fillcolor=orange, URL="/elements2/g.216/", target="_top"];
     "G.230" [label="G.230", URL="/elements2/g.230/", target="_top"];
     "G.217" [label="G.217", URL="/elements2/g.217/", target="_top"];
     "G.244" [label="G.244", URL="/elements2/g.244/", target="_top"];
     "G.226" [label="G.226", URL="/elements2/g.226/", target="_top"];
     "G.222" [label="G.222", URL="/elements2/g.222/", target="_top"];
     "G.249" [label="G.249", URL="/elements2/g.249/", target="_top"];
     "G.223" [label="G.223", URL="/elements2/g.223/", target="_top"];
     "G.225" [label="G.225", URL="/elements2/g.225/", target="_top"];
     "G.148" [label="G.148", URL="/elements2/g.148/", target="_top"];
     "G.229" [label="G.229", URL="/elements2/g.229/", target="_top"];
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.219" [label="G.219", style="rounded,filled", fillcolor=orange, URL="/elements2/g.219/", target="_top"];
     "G.232" [label="G.232", style="rounded,filled", fillcolor=orange, URL="/elements2/g.232/", target="_top"];
     "G.250" -> "G.248";
     "G.144" -> "G.140";
     "G.244" -> "G.210";
     "G.210" -> "G.209";
     "G.247" -> "G.246";
     "G.147" -> "G.145";
     "G.207" -> "G.206";
     "G.231" -> "G.206";
     "G.223" -> "G.218";
     "G.244" -> "G.231";
     "G.245" -> "G.231";
     "G.230" -> "G.211";
     "G.228" -> "G.227";
     "G.229" -> "G.227";
     "G.245" -> "G.227";
     "G.208" -> "G.207";
     "G.229" -> "G.228";
     "G.250" -> "G.247";
     "G.148" -> "G.147";
     "G.210" -> "G.208";
     "G.211" -> "G.208";
     "G.247" -> "G.245";
     "G.229" -> "G.144";
     "G.147" -> "G.137";
     "G.217" -> "G.216";
     "G.218" -> "G.216";
     "G.222" -> "G.216";
     "G.231" -> "G.230";
     "G.245" -> "G.230";
     "G.218" -> "G.217";
     "G.245" -> "G.244";
     "G.228" -> "G.226";
     "G.231" -> "G.226";
     "G.244" -> "G.226";
     "G.245" -> "G.226";
     "G.225" -> "G.222";
     "G.230" -> "G.222";
     "G.250" -> "G.249";
     "G.227" -> "G.223";
     "G.230" -> "G.223";
     "G.226" -> "G.225";
     "G.248" -> "G.225";
     "G.249" -> "G.225";
     "G.229" -> "G.148";
     "G.244" -> "G.229";
     "G.245" -> "G.229";
     "G.147" -> "G.146";
     "G.222" -> "G.219";
     "G.223" -> "G.219";
     "G.227" -> "G.219";
     "G.230" -> "G.219";
     "G.244" -> "G.219";
     "G.244" -> "G.232";
     "G.245" -> "G.232";
   }
