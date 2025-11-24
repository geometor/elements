:order: 166
:original_id: V.25
:type: prop
:dependencies: g.162

.. _g.166:

G.166
=====

**Heath ID:** :ref:`V.25`

   If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

``If four magnitudes be proportional``, ``the greatest and the least are greater than the remaining two``.

Let the four magnitudes ``AB``, ``CD``, ``E``, ``F`` be proportional so that, as ``AB`` is to ``CD``, so is ``E`` to ``F``, and let ``AB`` be the greatest of them and ``F`` the least; I say that ``AB``, ``F`` are greater than ``CD``, ``E``.

For let ``AG`` be made equal to ``E``, and ``CH`` equal to ``F``.

Since, as ``AB`` is to ``CD``, so is ``E`` to ``F``, and ``E`` is equal to ``AG``, and ``F`` to ``CH``,


.. container:: center

   therefore, as ``AB`` is to ``CD``, so is ``AG`` to ``CH``.


And since, as the whole ``AB`` is to the whole ``CD``, so is the part ``AG`` subtracted to the part ``CH`` subtracted,


.. container:: center

   the remainder ``GB`` will also be to the remainder ``HD`` as the whole ``AB`` is to the whole ``CD``. [:ref:`g.162`]


But ``AB`` is greater than ``CD``;


.. container:: center

   therefore ``GB`` is also greater than ``HD``.


And, since ``AG`` is equal to ``E``, and ``CH`` to ``F``, therefore ``AG``, ``F`` are equal to ``CH``, ``E``.

And if, ``GB``, ``HD`` being unequal, and ``GB`` greater, ``AG``, ``F`` be added to ``GB`` and ``CH``, ``E`` be added to ``HD``,


.. container:: center

   it follows that ``AB``, ``F`` are greater than ``CD``, ``E``.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.166" [label="G.166", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.166/", target="_top"];
     "G.159" [label="G.159", URL="/elements2/g.159/", target="_top"];
     "G.151" [label="G.151", URL="/elements2/g.151/", target="_top"];
     "G.157" [label="G.157", style="rounded,filled", fillcolor=orange, URL="/elements2/g.157/", target="_top"];
     "G.156" [label="G.156", URL="/elements2/g.156/", target="_top"];
     "G.140" [label="G.140", style="rounded,filled", fillcolor=orange, URL="/elements2/g.140/", target="_top"];
     "G.137" [label="G.137", style="rounded,filled", fillcolor=orange, URL="/elements2/g.137/", target="_top"];
     "G.149" [label="G.149", URL="/elements2/g.149/", target="_top"];
     "G.144" [label="G.144", URL="/elements2/g.144/", target="_top"];
     "G.160" [label="G.160", URL="/elements2/g.160/", target="_top"];
     "G.155" [label="G.155", URL="/elements2/g.155/", target="_top"];
     "G.145" [label="G.145", style="rounded,filled", fillcolor=orange, URL="/elements2/g.145/", target="_top"];
     "G.150" [label="G.150", style="rounded,filled", fillcolor=orange, URL="/elements2/g.150/", target="_top"];
     "G.138" [label="G.138", style="rounded,filled", fillcolor=orange, URL="/elements2/g.138/", target="_top"];
     "G.154" [label="G.154", URL="/elements2/g.154/", target="_top"];
     "G.152" [label="G.152", URL="/elements2/g.152/", target="_top"];
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.162" [label="G.162", URL="/elements2/g.162/", target="_top"];
     "G.153" [label="G.153", URL="/elements2/g.153/", target="_top"];
     "G.158" [label="G.158", style="rounded,filled", fillcolor=orange, URL="/elements2/g.158/", target="_top"];
     "G.147" [label="G.147", URL="/elements2/g.147/", target="_top"];
     "G.162" -> "G.159";
     "G.154" -> "G.151";
     "G.159" -> "G.157";
     "G.159" -> "G.156";
     "G.144" -> "G.140";
     "G.151" -> "G.140";
     "G.152" -> "G.140";
     "G.159" -> "G.140";
     "G.147" -> "G.137";
     "G.151" -> "G.137";
     "G.160" -> "G.137";
     "G.153" -> "G.149";
     "G.155" -> "G.149";
     "G.156" -> "G.149";
     "G.149" -> "G.144";
     "G.154" -> "G.144";
     "G.162" -> "G.160";
     "G.159" -> "G.155";
     "G.147" -> "G.145";
     "G.159" -> "G.150";
     "G.162" -> "G.150";
     "G.160" -> "G.138";
     "G.159" -> "G.154";
     "G.153" -> "G.152";
     "G.155" -> "G.152";
     "G.156" -> "G.152";
     "G.147" -> "G.146";
     "G.152" -> "G.146";
     "G.166" -> "G.162";
     "G.159" -> "G.153";
     "G.159" -> "G.158";
     "G.149" -> "G.147";
     "G.153" -> "G.147";
     "G.155" -> "G.147";
     "G.156" -> "G.147";
   }
